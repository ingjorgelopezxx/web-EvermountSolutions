import flet as ft
import requests
import base64

def get_menu_view(page: ft.Page):
    contenedor_menu = ft.Row(scroll="always", spacing=10, height=130)
    texto_seleccion = ft.Text("Selecciona una imagen", size=18)
    selected_image = {"nombre": None}
    spinner_gif = ft.Image(
    src="https://i.gifer.com/ZZ5H.gif",  # un spinner animado ejemplo
    width=80,
    height=80,
    )
    spinner_text = ft.Text("Cargando...", color="white", size=16)
    interaccion_habilitada = {"valor": True}
    spinner_modal = ft.Container(
        visible=False,
        expand=True,
        bgcolor=ft.Colors.BLACK54,
        alignment=ft.alignment.center,
        content=ft.Column(
            [
                spinner_gif,
                spinner_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
        )
    # SnackBar para notificaciones
    snack_bar = ft.SnackBar(content=ft.Text(""), open=False)
    page.snack_bar = snack_bar

    # FilePicker oculto correctamente
    file_picker = ft.FilePicker()
    file_picker_container = ft.Container(
        content=file_picker,
        opacity=0,
        height=0,
        width=0,
        visible=True
    )

    # Diálogo de confirmación para eliminar
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmación de eliminación"),
        content=ft.Text("¿Quieres eliminar esta imagen?"),
        actions=[ft.TextButton("Sí", on_click=lambda e: eliminar_imagen()),
            ft.TextButton("No", on_click=lambda e: page.close(dlg_modal)),],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    def mostrar_spinner(mensaje="Cargando..."):
        boton_logout.disabled = True
        boton_cargar.disabled = True
        spinner_text.value = mensaje
        spinner_modal.visible = True
        page.update()
    def ocultar_spinner():
        boton_logout.disabled = False
        boton_cargar.disabled = False
        spinner_modal.visible = False
        page.update()

    def eliminar_imagen():
        nombre = selected_image["nombre"]
        mostrar_spinner("Eliminando imagen...")
        if nombre:
            try:
                response = requests.delete(f"http://localhost:5000/imagen/{nombre}")
                response.raise_for_status()
            except Exception as e:
                page.snack_bar.content.value = f"❌ Error al eliminar imagen: {e}"
            else:
                page.snack_bar.content.value = f"🗑️ Imagen '{nombre}' eliminada correctamente"
                cargar_menu()
        ocultar_spinner()
        page.snack_bar.open = True
        page.update()
        page.close(dlg_modal)

    def on_click(e, nombre):
        if not interaccion_habilitada["valor"]:
            return  # ⛔ Ignorar clic si la interacción está deshabilitada
        selected_image["nombre"] = nombre
        texto_seleccion.value = f"Seleccionaste: {nombre}"
        texto_seleccion.update()
        imagen_ampliada.src = f"http://localhost:5000/imagen/{nombre}"
        imagen_ampliada.visible = True
        fondo_expandido.bgcolor = ft.Colors.WHITE
        imagen_ampliada.update()
        fondo_expandido.update()

        dlg_modal.content.value = f"¿Quieres eliminar la imagen '{nombre}'?"
        dlg_modal.actions = [
            ft.TextButton(on_click=lambda e: eliminar_imagen()),
            ft.TextButton(on_click=lambda e: page.close(dlg_modal)),
        ]
        page.open(dlg_modal)

    def on_hover(e):
        e.control.scale = 1.2 if e.data == "true" else 1.0
        e.control.update()

    def cargar_menu():
        contenedor_menu.controls.clear()
        texto_seleccion.value = "Selecciona una imagen"
        texto_seleccion.update()

        try:
            response = requests.get("http://localhost:5000/imagenes")
            response.raise_for_status()
            nombres_imagenes = response.json()
        except Exception as e:
            page.snack_bar.content.value = f"⚠️ Error al obtener imágenes: {e}"
            page.snack_bar.open = True
            page.update()
            return

        for nombre in nombres_imagenes:
            url = f"http://localhost:5000/imagen/{nombre}"
            imagen = ft.Image(
                src=url,
                width=100,
                height=100,
                fit=ft.ImageFit.COVER
            )

            contenedor_imagen = ft.Container(
                content=imagen,
                width=100,
                height=100,
                border_radius=10,
                border=ft.border.all(1, "gray"),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                scale=1.0,
                animate_scale=300,
                data=nombre,
                on_hover=on_hover
            )
            nombre_sin_extension = nombre.rsplit(".", 1)[0].upper()
            texto_nombre = ft.Text(
                nombre_sin_extension,
                size=11,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
                text_align=ft.TextAlign.CENTER,
                max_lines=1,
                overflow="ellipsis",
                width=100
            )

            hover_detector = ft.Column(
                controls=[
                    ft.GestureDetector(
                        content=contenedor_imagen,
                        data=nombre,
                        on_tap=lambda e, n=nombre: on_click(e, n),
                        mouse_cursor="pointer"
                    ),
                    texto_nombre
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
                width=100
            )

            contenedor_menu.controls.append(hover_detector)

        contenedor_menu.update()
        page.update()

    def subir_imagen(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        interaccion_habilitada["valor"] = False
        mostrar_spinner("Subiendo imagen...")
        archivo = e.files[0]
        nombre = archivo.name

        try:
            with open(archivo.path, "rb") as f:
                contenido = f.read()
            base64_str = "data:image/jpeg;base64," + base64.b64encode(contenido).decode()

            resp = requests.post(
                "http://localhost:5000/upload_image",
                json={"name": nombre, "image_base64": base64_str}
            )

            if resp.status_code == 200:
                cargar_menu()
                page.snack_bar.content.value = "✅ Imagen subida correctamente"
            else:
                page.snack_bar.content.value = f"❌ Error al subir imagen: {resp.text}"

        except Exception as ex:
            page.snack_bar.content.value = f"⚠️ Error: {ex}"
        ocultar_spinner()
        interaccion_habilitada["valor"] = True
        page.snack_bar.open = True
        page.update()

    file_picker.on_result = subir_imagen

    # Botones
    boton_cargar = ft.ElevatedButton(
        "Subir imagen",
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["jpg", "jpeg", "png"]
        )
    )

    boton_logout = ft.ElevatedButton(
        "Cerrar sesión",
        on_click=lambda e: page.go("/")
    )

    barra_superior = ft.Container(
        content=ft.Row(
            controls=[boton_cargar, boton_logout],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    imagen_ampliada = ft.Image(
        src="",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
        visible=False
    )

    fondo_expandido = ft.Container(
        expand=True,
        bgcolor=ft.Colors.TRANSPARENT,
        alignment=ft.alignment.center,
        content=imagen_ampliada
    )




    view = ft.View(
        route="/home",
        controls=[
            ft.Column(
                controls=[
                    barra_superior,
                    contenedor_menu,
                    texto_seleccion,
                    fondo_expandido,  # << ESTE CAMBIA DE COLOR
                    snack_bar,
                    dlg_modal,
                    file_picker_container
                ],
                expand=True  # << NECESARIO PARA QUE el fondo ocupe espacio
            ),
            spinner_modal
        ],
        scroll=ft.ScrollMode.AUTO,
    )



    return view, cargar_menu
