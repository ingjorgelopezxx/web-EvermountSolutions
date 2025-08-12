import flet as ft
import os
import asyncio

async def main(page: ft.Page):
    page.title = "Botón WhatsApp + Menú Empresa"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.window_resizable = True

    imagenes_visibles = [ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8)
                         for _ in range(3)]
    fila_carrusel = ft.Row(controls=imagenes_visibles, scroll="always", spacing=10)
    contenido = ft.Column([], expand=True, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
   
    # --- WhatsApp ---
    url_whatsapp = f"https://wa.me/{"+56937539304"}?text=Hola"
    # --- Tercer botón: Facebook ---
    url_facebook = "https://facebook.com/evermountsolutions"
    imagen_facebook = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/b/b9/2023_Facebook_icon.svg",
        width=60, height=60, fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Síguenos en Facebook"
    )
    boton_facebook = ft.Container(
        content=imagen_facebook,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=None,  # sin fondo
        shadow=None,   # sin sombra
        on_click=lambda _: page.launch_url(url_facebook),
        ink=False,     # sin efecto de tinta
        margin=ft.margin.only(left=16, bottom=16),
    )
    
    # --- Segundo botón (ejemplo: Instagram) ---
    url_izquierdo = "https://instagram.com/evermountsolutions"  # Puedes cambiarlo
    imagen_izquierda = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg",
        fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Síguenos en Instagram"
    )
    
    boton_izquierdo = ft.Container(
        content=imagen_izquierda,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        on_click=lambda _: page.launch_url(url_izquierdo),
        ink=True,
        margin=ft.margin.only(bottom=16),
    )

    # -- Botón WhatsApp --
    imagen_logo = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
        fit=ft.ImageFit.COVER,
        scale=1.0, animate_scale=200, tooltip="Contáctanos por WhatsApp"
    )
    def animar_logo(e):
        imagen_logo.scale = 1.1 if e.data=="true" else 1.0
        imagen_logo.update()
   
    boton_whatsapp = ft.Container(
        content=imagen_logo,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        on_click=lambda _: page.launch_url(url_whatsapp),
        on_hover=animar_logo,
        ink=True,
        margin=ft.margin.only(right=16, bottom=16),
    )

    # --- Botón Empresa + Dropdown ---
    logo_empresa_url = "https://i.postimg.cc/rFxRRS5D/logo-72x72.png"
    logo_empresa_ulr_mensaje = "https://i.postimg.cc/8PvSgg5x/logo-mobile-dark.png"
    imagen_empresa = ft.Image(
        src=logo_empresa_url, fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Menú Empresa"
    )
    def animar_empresa(e):
        imagen_empresa.scale = 1.1 if e.data=="true" else 1.0
        imagen_empresa.update()

    

    # === Aquí agregamos iconos a cada item ===
    menu_data = [
        ("Contactos", ft.Icons.CONTACT_PHONE),
        ("Ubicación",  ft.Icons.PLACE),
        ("Misión",     ft.Icons.FLAG),
        ("Visión",     ft.Icons.VISIBILITY),
    ]
    menu_items = []
    for text, icon in menu_data:
        def _on_click(e, t=text):
            show_info(t)
        item = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, size=20, color=ft.Colors.BLACK54),
                    ft.Text(text, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(vertical=6, horizontal=12),
            bgcolor=ft.Colors.WHITE,
            border_radius=4,
            on_click=_on_click,
            ink=True,
        )
        item.on_hover = (lambda c: lambda e: (
            setattr(c, "bgcolor", ft.Colors.BLACK12 if e.data=="true" else ft.Colors.WHITE),
            c.update()
        ))(item)
        menu_items.append(item)

    menu_column = ft.Column(controls=menu_items, spacing=0)
    dropdown = ft.Container(
        content=ft.Container(
            content=menu_column,
            bgcolor=ft.Colors.WHITE,
            border_radius=6,
            shadow=ft.BoxShadow(1,4,ft.Colors.BLACK26, offset=ft.Offset(0,2)),
            width=150,
            height=150
        ),
        visible=False,
        alignment=ft.alignment.top_right,
        margin=ft.margin.only(top=70, right=10),
    )
    def toggle_menu(e):
        dropdown.visible = not dropdown.visible
        cerrar_menu_overlay.visible = dropdown.visible
        page.update()
    cerrar_menu_overlay = ft.Container(
        expand=True,
        bgcolor=ft.Colors.TRANSPARENT,
        visible=False,
        on_click=lambda e: (
            setattr(dropdown, "visible", False),
            setattr(cerrar_menu_overlay, "visible", False),
            page.update()
        )
    )

    boton_empresa = ft.Container(
    content=ft.Container(
        content=imagen_empresa,
        width=50,
        height=50,
        border_radius=25,
        bgcolor=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#ffffff", "#dcdcdc"]
        ),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.Colors.BLACK38,
            offset=ft.Offset(3, 3)
        ),
        on_hover=animar_empresa,
        on_click=toggle_menu,
        ink=True,
        alignment=ft.alignment.center
    ),
    width=64,
    height=64,
    bgcolor=ft.Colors.BLACK12,  # Fondo circular más visible
    border_radius=32,
    padding=7,  # Espaciado interno
    )



    # --- Barra superior con botón Empresa ---
    texto_titulo = ft.Stack([
        ft.Text("EvermountSolutions – Pest Defense",
                size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK45, top=1, left=1),
        ft.Text("EvermountSolutions – Pest Defense",
                size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
    ])
    barra_superior = ft.Container(
        padding=ft.padding.symmetric(horizontal=10, vertical=8),
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left, end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"],
        ),
        content=ft.Row([
            ft.Container(content=texto_titulo, expand=True, alignment=ft.alignment.center_left),
            boton_empresa
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # --- Carrusel (igual) ---
    sets_imagenes = [
        ["https://irp.cdn-website.com/fe74ab3f/dms3rep/multi/3-c76791a1.jpg", "https://www.multianau.com/wp-content/uploads/2023/11/img-MULTIANAU-BLOG-Claves-para-el-control-de-plagas-en-la-industria-alimentaria.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXeZ7ElGw51_JF6TZuylsCHQcXd-e_GyV7mA&s"],
        ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxriBp7gAvC3DeO0ZsaDqinL-7dZCJ_ulUmx_B3ad-QOo911PD0nwmsyZFBF3dK_bTzsw&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTimFMgOc-bNR1xeYjxD__RbzP0LApis-ovRuggm-TM0CPZl6OBeSj8TCc3Ph1sYVIjhcg&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAF2blxqmgt_0N7htQAMCDfn8thMHzWPy0z9a7_tdSsSgxDzYD9GiinavAWy8CpM7Ndl0&usqp=CAU"],
    ]
 
    async def rotar_sets():
        idx = 0
        while True:
            for i, img in enumerate(imagenes_visibles):
                img.src = sets_imagenes[idx][i]; img.update()
            await asyncio.sleep(3); idx = (idx+1) % len(sets_imagenes)

    async def animacion_alternada():
     while True:
        for img in [imagen_logo, imagen_izquierda, imagen_facebook,imagen_empresa]:
            img.scale = 1.2
            img.update()
            await asyncio.sleep(0.4)
            img.scale = 1.0
            img.update()
            await asyncio.sleep(0.4)

    

    # --- Responsive: texto + ancho automático para WhatsApp ---
    def ajustar_tamanos(e=None):
        a = page.width
        # título
        s = 14 if a<450 else 18 if a<600 else 26
        texto_titulo.controls[0].size = s
        texto_titulo.controls[1].size = s
        texto_titulo.update()
        page.update()

    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data=="shown" else None

    # --- Modal de bienvenida ---
    def close_intro(e):
        intro_modal.visible = False
        page.update()

    # Contenedor circular para el logo
    # Contenedor circular para el logo (ajustado a arriba)
    logo_circular = ft.Container(
        content=ft.Image(src="https://i.postimg.cc/8PvSgg5x/logo-mobile-dark.png", fit=ft.ImageFit.COVER),
        width=256,
        height=128,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.top_center,   # ⬅️ Esto lo alinea arriba
    )


    intro_modal = ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLACK54,  # fondo semitransparente
        alignment=ft.alignment.center,
        content=ft.Container(
            width=350,
            height=430,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            padding=20,
            content=ft.Column([
                # Botón de cierre (X)
                ft.Row([
                    ft.Text("", expand=True),  # empuja la X a la derecha
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        on_click=close_intro,
                        icon_color=ft.Colors.BLACK
                    )
                ]),
                # Logo en la parte superior
                logo_circular,
                # Título en negro y negrita
                ft.Text(
                    "¡Bienvenidos!",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),
                ft.Text(
                    "Aquí encontrarás todo lo referente al control de plagas profesional "
                    "navega por la página y usa los botones para contactarte.",
                    color=ft.Colors.BLACK
                ),
                # Descripción en negro y negrita
                ft.Text(
                    "Si deseas obtener mas información referente a la empresa "
                    "has clic sobre el boton ubicado en la esquina superior derecha.",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )
    )
    #  Esta parte es la que añade el on_connect para reiniciar TODO al recargar:
    def on_connect(e):
        intro_modal.visible = True
        dropdown.visible = False
        for i, img in enumerate(imagenes_visibles):
            img.src = sets_imagenes[0][i]
            img.update()
        page.update()

    page.on_connect = on_connect
    # --- Montaje final + overlays ---
    page.add(
        ft.Column([
            barra_superior,
            contenido,
            ft.Row(
            [boton_facebook, boton_izquierdo, boton_whatsapp],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END,
            spacing=10,
            ),
        ], expand=True,  horizontal_alignment=ft.CrossAxisAlignment.CENTER )
    )
    def show_info(opt):
        contenido.controls.clear()
        if opt == "Ubicación":
            contenido.controls.append(
                ft.Text("dirección de empresa", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
            )
        contenido.update()
        dropdown.visible = False
        cerrar_menu_overlay.visible = False
        page.update()

    contenido.controls.clear()
    contenido.controls.extend([
        ft.Text("Bienvenido a EvermountSolutions"),
        ft.Text("Control de plagas profesional. Haz clic en los botones."),
        fila_carrusel
    ])
    contenido.update()

    # overlay: dropdown y modal inicial
    page.overlay.clear()
    page.overlay.extend([dropdown, cerrar_menu_overlay, intro_modal])

    # Inicia carrusel y primer resize
    asyncio.create_task(rotar_sets())
    ajustar_tamanos()
    asyncio.create_task(animacion_alternada())
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))
