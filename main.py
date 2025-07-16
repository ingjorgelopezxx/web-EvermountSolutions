import flet as ft
import os
import asyncio

async def main(page: ft.Page):
    page.title = "Botón WhatsApp + Menú Empresa"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.window_resizable = True

    # --- WhatsApp ---
    numero_whatsapp = "+56937539304"
    mensaje = "Hola, deseo recibir mas informacion de los servicios que ofrecen"
    url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje.replace(' ', '%20')}"

    # --- Botón WhatsApp ---
    imagen_logo = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
        width=60, height=60, fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200,
        tooltip="Contáctanos por WhatsApp",
    )
    def animar_logo(e):
        imagen_logo.scale = 1.1 if e.data == "true" else 1.0
        imagen_logo.update()

    texto_whatsapp = ft.Text("Whatsapp", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87)
    boton_whatsapp = ft.Container(
        content=ft.Row([imagen_logo, texto_whatsapp],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=8),
        width=170, height=65,
        border_radius=100, bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=8,
                            color=ft.Colors.BLACK26, offset=ft.Offset(2,2)),
        on_click=lambda _: page.launch_url(url_whatsapp),
        on_hover=animar_logo,
        ink=True,
    )

    # --- Botón + Menú Empresa ---
    logo_empresa_url = "https://i.postimg.cc/SKgGrpQ8/logo-512x512.png"
    imagen_empresa = ft.Image(
        src=logo_empresa_url, width=60, height=60,
        fit=ft.ImageFit.CONTAIN, scale=1.0, animate_scale=200,
        tooltip="Menú Empresa",
    )
    def animar_empresa(e):
        imagen_empresa.scale = 1.1 if e.data == "true" else 1.0
        imagen_empresa.update()

    texto_Empresa = ft.Column([
        ft.Text("Evermount", size=14, weight=ft.FontWeight.BOLD, no_wrap=True),
        ft.Text("Solution", size=14, weight=ft.FontWeight.BOLD, no_wrap=True),
    ], spacing=0)

    show_menu = False
    def toggle_menu(e):
        nonlocal show_menu
        show_menu = not show_menu
        menu_container.visible = show_menu
        page.update()

    def show_info(opt):
        dlg = ft.AlertDialog(
            title=ft.Text(opt),
            content=ft.Text(f"Aquí va la información para «{opt}»."),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: dlg.dismiss())]
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Construir ítems del menú con on_hover manual
    menu_items = []
    for opt in ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]:
        # Creamos contenedor primero
        item = ft.Container(
            content=ft.Text(opt, selectable=False),
            padding=ft.padding.symmetric(vertical=6, horizontal=12),
            bgcolor=ft.Colors.WHITE,
            border_radius=4,
            on_click=lambda e, o=opt: (show_info(o), toggle_menu(e)),
            ink=True,
        )
        # Añadimos hover que cambia el fondo
        def make_hover(c):
            return lambda e: (
                setattr(c, "bgcolor", ft.Colors.BLACK12 if e.data=="true" else ft.Colors.WHITE),
                c.update()
            )
        item.on_hover = make_hover(item)
        menu_items.append(item)

    menu_container = ft.Container(
    content=ft.Column(
        controls=menu_items,
        spacing=0,
    ),
    visible=False,
    bgcolor=ft.Colors.WHITE,
    border_radius=6,
    shadow=ft.BoxShadow(spread_radius=1, blur_radius=4, color=ft.Colors.BLACK26, offset=ft.Offset(0,2)),
    width=150,
)


    boton_empresa = ft.Container(
        content=ft.Row([imagen_empresa, texto_Empresa],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=4),
        height=50,
        padding=ft.padding.symmetric(horizontal=10),
        border_radius=100,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=8,
                            color=ft.Colors.BLACK26, offset=ft.Offset(2,2)),
        on_hover=animar_empresa,
        on_click=toggle_menu,
        ink=True,
    )

    # --- Barra superior con botón+menú ---
    texto_titulo = ft.Stack([
        ft.Text("EvermountSolutions – Pest Defense",
                size=26, weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK45, top=1, left=1),
        ft.Text("EvermountSolutions – Pest Defense",
                size=26, weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE),
    ])
    barra_superior = ft.Container(
        padding=ft.padding.symmetric(horizontal=10, vertical=8),
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left, end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"],
        ),
        content=ft.Row([
            ft.Container(content=texto_titulo, expand=True,
                         alignment=ft.alignment.center_left),
            ft.Column([boton_empresa, menu_container], spacing=0)
        ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )

    # --- Carrusel (igual que antes) ---
    sets_imagenes = [
        ["https://irp.cdn-website.com/fe74ab3f/dms3rep/multi/3-c76791a1.jpg",
         "https://www.multianau.com/wp-content/uploads/2023/11/img-MULTIANAU-BLOG-Claves-para-el-control-de-plagas-en-la-industria-alimentaria.jpg",
         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXeZ7ElGw51_JF6TZuylsCHQcXd-e_GyV7mA&s"],
        ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxriBp7gAvC3DeO0ZsaDqinL-7dZCJ_ulUmx_B3ad-QOo911PD0nwmsyZFBF3dK_bTzsw&usqp=CAU",
         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTimFMgOc-bNR1xeYjxD__RbzP0LApis-ovRuggm-TM0CPZl6OBeSj8TCc3Ph1sYVIjhcg&usqp=CAU",
         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAF2blxqmgt_0N7htQAMCDfn8thMHzWPy0z9a7_tdSsSgxDzYD9GiinavAWy8CpM7Ndl0&usqp=CAU"]
    ]
    imagenes_visibles = [ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8)
                         for _ in range(3)]
    fila_carrusel = ft.Row(controls=imagenes_visibles,
                           scroll="always", spacing=10,
                           alignment=ft.MainAxisAlignment.START)

    async def rotar_sets():
        idx = 0
        while True:
            for i, img in enumerate(imagenes_visibles):
                img.src = sets_imagenes[idx][i]
                img.update()
            await asyncio.sleep(3)
            idx = (idx + 1) % len(sets_imagenes)

    contenido = ft.Column([
        ft.Text("Bienvenido a EvermountSolutions"),
        ft.Text("Control de plagas profesional. Haz clic en los botones."),
        fila_carrusel
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    # --- Responsive ---
    def ajustar_tamanos(e=None):
        ancho = page.width
        size = 14 if ancho < 450 else 18 if ancho < 600 else 26
        texto_titulo.controls[0].size = size
        texto_titulo.controls[1].size = size
        texto_titulo.update()

        if ancho < 500:
            boton_whatsapp.width, boton_whatsapp.height = 130, 45
        elif ancho < 800:
            boton_whatsapp.width, boton_whatsapp.height = 145, 50
        else:
            boton_whatsapp.width, boton_whatsapp.height = 170, 65
        boton_whatsapp.update()
        page.update()

    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data == "shown" else None

    # --- Montaje final ---
    page.add(
        ft.Column([
            barra_superior,
            contenido,
            ft.Row([boton_whatsapp], alignment=ft.MainAxisAlignment.END),
        ], expand=True)
    )

    asyncio.create_task(rotar_sets())
    ajustar_tamanos()

ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))
