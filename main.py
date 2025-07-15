import flet as ft
import os
import asyncio
async def main(page: ft.Page):
    page.title = "Botón WhatsApp Flotante"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.window_resizable = True

    # Número de WhatsApp y mensaje
    numero_whatsapp = "+56937539304"
    mensaje = "Hola, deseo recibir mas informacion de los servicios que ofrecen"
    mensaje_encoded = mensaje.replace(" ", "%20")
    url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje_encoded}"

    # URL del logo (formato PNG o SVG público)
    logo_url = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"

    # Imagen como botón con efectos
    imagen_logo = ft.Image(
        src=logo_url,
        width=60,
        height=60,
        fit=ft.ImageFit.CONTAIN,
        tooltip="Contáctanos por WhatsApp",
    )

    texto_whatsapp = ft.Text(
    "Whatsapp",
    size=18,
    weight=ft.FontWeight.BOLD,
    color=ft.Colors.BLACK87,
    selectable=False,
    style=ft.TextThemeStyle.BODY_MEDIUM,
    # Puedes ajustar el padding o margen si quieres separación
)
    # Contenedor con estilo y efecto hover
    boton_contenedor = ft.Container(
           content=ft.Row(
        [
            imagen_logo,
            texto_whatsapp
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8
    ),
    alignment=ft.alignment.center,
    width=200,  # más ancho para que quepa el texto
    height=65,
    border_radius=100,
    bgcolor=ft.Colors.WHITE,
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=8,
        color=ft.Colors.BLACK26,
        offset=ft.Offset(2, 2),
        blur_style=ft.ShadowBlurStyle.NORMAL,
    ),
        on_click=lambda _: page.launch_url(url_whatsapp),
        on_hover=lambda e: imagen_logo.scale.update(1.1 if e.data == "true" else 1.0),
        ink=True,
    )

    # Activar escala animada al pasar el mouse
    imagen_logo.scale = 1.0
    imagen_logo.animate_scale = 200

    # Botón flotante alineado abajo a la derecha
    boton_flotante = ft.Container(
        content=boton_contenedor,
        alignment=ft.alignment.bottom_right,
        padding=20,
        expand=True
    )

    # Agrega el botón como superposición
    page.overlay.append(boton_flotante)

  # Título con sombra 3D simulada
    texto_sombra = ft.Stack([
        ft.Text(
            "EvermountSolutions - Pest Defense",
            size=26,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK45,
            top=2,
            left=2,
        ),
        ft.Text(
            "EvermountSolutions - Pest Defense",
            size=26,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
        ),
    ])

    # Imágenes por grupo (3 por set)
    sets_imagenes = [
        [
            "https://bearclaw.cl/wp-content/uploads/2020/08/procedimiento-de-control-de-plagas.jpg",
            "https://www.multianau.com/wp-content/uploads/2023/11/img-MULTIANAU-BLOG-Claves-para-el-control-de-plagas-en-la-industria-alimentaria.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXeZ7ElGw51_JF6TZuylsCHQcXd-e_GyV7mA&s"
        ],
        [
            "https://cursosudgassesorar.com/wp-content/uploads/2022/02/Libros-de-Control-de-Plagas.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTimFMgOc-bNR1xeYjxD__RbzP0LApis-ovRuggm-TM0CPZl6OBeSj8TCc3Ph1sYVIjhcg&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAF2blxqmgt_0N7htQAMCDfn8thMHzWPy0z9a7_tdSsSgxDzYD9GiinavAWy8CpM7Ndl0&usqp=CAU"
        ]
    ]

    # Controles de las 3 imágenes visibles
    imagenes_visibles = [
        ft.Image(width=150, height=100, fit=ft.ImageFit.COVER, border_radius=8),
        ft.Image(width=150, height=100, fit=ft.ImageFit.COVER, border_radius=8),
        ft.Image(width=150, height=100, fit=ft.ImageFit.COVER, border_radius=8),
    ]

    fila_carrusel = ft.Row(
        controls=imagenes_visibles,
        spacing=10,
        alignment=ft.MainAxisAlignment.START,
        scroll="auto",  # visible solo cuando sea necesario
        wrap=False,  # <--- evita que las imágenes bajen en lugar de hacer scroll
        expand=False
    )

    carrusel_section = ft.Container(
        content=ft.Column([
            fila_carrusel
        ]),
        padding=ft.padding.symmetric(horizontal=10, vertical=10),
        alignment=ft.alignment.center_left,
        expand=True  # <--- Importante
    )

    async def rotar_sets():
        index = 0
        while True:
            set_actual = sets_imagenes[index]
            for i in range(3):
                imagenes_visibles[i].src = set_actual[i]
                imagenes_visibles[i].update()
            await asyncio.sleep(3)
            index = (index + 1) % len(sets_imagenes)

   
    asyncio.create_task(rotar_sets())
    # Barra personalizada con fondo degradado
        # Barra personalizada responsive con fondo degradado


    barra_superior = ft.Container(
        height=100,
        padding=ft.padding.symmetric(horizontal=10),
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"],
        ),
        content=ft.Row(
            controls=[
                ft.Container(content=texto_sombra, expand=True, alignment=ft.alignment.center_left),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


    # Contenido principal
    contenido = ft.Column([
        ft.Text("Bienvenido a EvermountSolutions", size=22),
        ft.Text("Control de plagas profesional. Haz clic en el botón para contactarnos."),
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
        # Sección del carrusel debajo del contenido principal

    async def ajustar_tamanos(e=None):
        ancho = page.window_width

        # Tamaño de texto
        if ancho < 500:
            texto_sombra.controls[0].size = 16
            texto_sombra.controls[1].size = 16
        elif ancho < 800:
            texto_sombra.controls[0].size = 20
            texto_sombra.controls[1].size = 20
        else:
            texto_sombra.controls[0].size = 26
            texto_sombra.controls[1].size = 26

        # Ajuste dinámico del tamaño de las imágenes
        for img in imagenes_visibles:
            if ancho < 500:
                img.width = 100
                img.height = 70
            elif ancho < 800:
                img.width = 130
                img.height = 90
            else:
                img.width = 180
                img.height = 120

        page.update()

    # Llamar al inicio y cuando se cambie el tamaño
    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data == "shown" else None

    # Agregar todo a la página
    page.add(barra_superior, contenido,carrusel_section)

# Ejecutar en navegador
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))

