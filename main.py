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
    url_whatsapp = f"https://wa.me/{numero_whatsapp}?text=Hola"

    # -- Botón WhatsApp --
    imagen_logo = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
        width=60, height=60, fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Contáctanos por WhatsApp"
    )
    def animar_logo(e):
        imagen_logo.scale = 1.1 if e.data == "true" else 1.0
        imagen_logo.update()

    texto_whatsapp = ft.Text("Whatsapp", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87)
    boton_whatsapp = ft.Container(
        content=ft.Row([imagen_logo, texto_whatsapp], alignment=ft.MainAxisAlignment.CENTER, spacing=4),
        width=170, height=65, border_radius=100, bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1,8,ft.Colors.BLACK26,offset=ft.Offset(2,2)),
        on_click=lambda _: page.launch_url(url_whatsapp),
        on_hover=animar_logo,
        ink=True,
        margin=ft.margin.only(right=16, bottom=16),  # <-- aquí
    )

    # --- Botón Empresa y Dropdown ---
    logo_empresa_url = "https://i.postimg.cc/SKgGrpQ8/logo-512x512.png"
    imagen_empresa = ft.Image(
        src=logo_empresa_url, width=60, height=60,
        fit=ft.ImageFit.CONTAIN, scale=1.0, animate_scale=200,
        tooltip="Menú Empresa"
    )
    def animar_empresa(e):
        imagen_empresa.scale = 1.1 if e.data == "true" else 1.0
        imagen_empresa.update()


    # Items del menú
    def show_info(opt):
        dlg = ft.AlertDialog(
            title=ft.Text(opt),
            content=ft.Text(f"Aquí va la información para «{opt}»."),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: dlg.dismiss())]
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    menu_items = []
    for opt in ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]:
        item = ft.Container(
            content=ft.Text(opt),
            padding=ft.padding.symmetric(vertical=6, horizontal=12),
            bgcolor=ft.Colors.WHITE,
            border_radius=4,
            on_click=lambda e, o=opt: show_info(o),
            ink=True,
        )
        # hover manual
        item.on_hover = (lambda c: lambda e: (
            setattr(c, "bgcolor", ft.Colors.BLACK12 if e.data=="true" else ft.Colors.WHITE),
            c.update()
        ))(item)
        menu_items.append(item)

    # Este es el Column que agrupa las opciones
    menu_column = ft.Column(controls=menu_items, spacing=0)

    # Este es el wrapper que vamos a mostrar/ocultar
    dropdown = ft.Container(
        content=ft.Container(
            content=menu_column,
            bgcolor=ft.Colors.WHITE,
            border_radius=6,
            shadow=ft.BoxShadow(1,4,ft.Colors.BLACK26,offset=ft.Offset(0,2)),
            width=150,
            height=130
            
        ),
        visible=False,
        alignment=ft.alignment.top_right,
        margin=ft.margin.only(top=70, right=10),  # justo debajo de la barra
    )

    def toggle_menu(e):
        dropdown.visible = not dropdown.visible
        page.update()

    boton_empresa = ft.Container(
        content=imagen_empresa,
        width=50,
        height=50,
        border_radius=25,             # radio = mitad del ancho/alto
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLACK26,
            offset=ft.Offset(2, 2)
        ),
        on_hover=animar_empresa,
        on_click=toggle_menu,
        ink=True,
    )

    # --- Barra superior con botón Empresa dentro ---
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
    imagenes_visibles = [ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8)
                         for _ in range(3)]
    fila_carrusel = ft.Row(controls=imagenes_visibles, scroll="always", spacing=10)
    async def rotar_sets():
        idx = 0
        while True:
            for i, img in enumerate(imagenes_visibles):
                img.src = sets_imagenes[idx][i]; img.update()
            await asyncio.sleep(3); idx = (idx+1) % len(sets_imagenes)

    contenido = ft.Column([
        ft.Text("Bienvenido a EvermountSolutions"),
        ft.Text("Control de plagas profesional. Haz clic en los botones."),
        fila_carrusel
    ], expand=True, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # --- Responsive ---
    def ajustar_tamanos(e=None):
        a = page.width

        # --- Título ---
        s = 14 if a < 450 else 18 if a < 600 else 26
        texto_titulo.controls[0].size = s
        texto_titulo.controls[1].size = s
        texto_titulo.update()

        # --- Botón WhatsApp responsive ---
        if a < 400:
            # Móvil muy estrecho: texto pequeño, ancho automático
            texto_whatsapp.size = 12
            boton_whatsapp.width = None
            boton_whatsapp.padding = ft.padding.symmetric(horizontal=8, vertical=8)
        elif a < 600:
            # Tablet / móvil medio: texto algo más pequeño, ancho reducido
            texto_whatsapp.size = 14
            boton_whatsapp.width = 140
            boton_whatsapp.padding = ft.padding.symmetric(horizontal=10, vertical=8)
        else:
            # Escritorio: valores originales
            texto_whatsapp.size = 18
            boton_whatsapp.width = 170
            boton_whatsapp.padding = ft.padding.symmetric(horizontal=16, vertical=8)

        texto_whatsapp.update()
        boton_whatsapp.update()

        page.update()


    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data=="shown" else None

    # --- Montaje final con Stack para el dropdown ---
    page.add(
        ft.Stack(
            controls=[
                ft.Column([
                    barra_superior,
                    contenido,
                    ft.Row([boton_whatsapp], alignment=ft.MainAxisAlignment.END),
                ], expand=True),
                dropdown  # flota sobre todo sin alterar la barra
            ],
            expand=True
        )
    )

    asyncio.create_task(rotar_sets())
    ajustar_tamanos()

ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))
