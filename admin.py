import flet as ft
import requests
import base64

def main(page: ft.Page):
    page.title = "Menú con zoom, subir y eliminar imagen"
    page.scroll = "auto"

    contenedor_menu = ft.Row(scroll="always", spacing=10, height=130)
    texto_seleccion = ft.Text("Selecciona una imagen", size=18)
    selected_image = {"nombre": None}

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    # Diálogo de confirmación
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmación de eliminación"),
        content=ft.Text("¿Quieres eliminar esta imagen?"),
        actions=[
            ft.TextButton("Sí", on_click=lambda e: eliminar_imagen()),
            ft.TextButton("No", on_click=lambda e: page.close(dlg_modal)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def eliminar_imagen():
        nombre = selected_image["nombre"]
        if nombre:
            try:
                response = requests.delete(f"http://localhost:5000/imagen/{nombre}")
                response.raise_for_status()
            except Exception as e:
                texto_seleccion.value = f"Error al eliminar imagen: {e}"
                texto_seleccion.update()
            else:
                texto_seleccion.value = f"Imagen '{nombre}' eliminada"
                texto_seleccion.update()
                cargar_menu()
        page.close(dlg_modal)

    def on_click(e, nombre):
        selected_image["nombre"] = nombre
        texto_seleccion.value = f"Seleccionaste: {nombre}"
        texto_seleccion.update()
        dlg_modal.content.value = f"¿Quieres eliminar la imagen '{nombre}'?"
        dlg_modal.content.update()
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
            page.snack_bar = ft.SnackBar(ft.Text(f"Error al obtener imágenes: {e}"))
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

            hover_detector = ft.GestureDetector(
                content=contenedor_imagen,
                data=nombre,
                on_tap=lambda e, n=nombre: on_click(e, n),
                mouse_cursor="pointer"
            )

            contenedor_menu.controls.append(hover_detector)

        contenedor_menu.update()

    def subir_imagen(e: ft.FilePickerResultEvent):
        if not e.files:
            return

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
                page.snack_bar = ft.SnackBar(ft.Text("Imagen subida correctamente"))
            else:
                page.snack_bar = ft.SnackBar(ft.Text(f"Error al subir imagen: {resp.text}"))

        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {ex}"))

        page.snack_bar.open = True
        page.update()

    file_picker.on_result = subir_imagen

    boton_cargar = ft.ElevatedButton("Subir imagen", on_click=lambda _: file_picker.pick_files(
        allow_multiple=False,
        allowed_extensions=["jpg", "jpeg", "png"]
    ))

    # Inicializar página
    page.add(
        boton_cargar,
        contenedor_menu,
        texto_seleccion,
        dlg_modal
    )
    cargar_menu()

ft.app(target=main)
