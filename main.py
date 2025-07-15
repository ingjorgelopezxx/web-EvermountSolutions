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
    texto_empresa = ft.Stack([
    ft.Text(
        "EvermountSolutions - Pest Defense",
        size=26,  # valor inicial que cambiaremos luego
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK45,
        no_wrap=True,
        overflow=ft.TextOverflow.CLIP,
        max_lines=1,
        top=1,
        left=1
    ),
    ft.Text(
        "EvermountSolutions - Pest Defense",
        size=26,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        no_wrap=True,
        overflow=ft.TextOverflow.CLIP,
        max_lines=1,
    )
])



    # Imágenes por grupo (3 por set)
    sets_imagenes = [
        [
            "https://irp.cdn-website.com/fe74ab3f/dms3rep/multi/3-c76791a1.jpg",
            "https://www.multianau.com/wp-content/uploads/2023/11/img-MULTIANAU-BLOG-Claves-para-el-control-de-plagas-en-la-industria-alimentaria.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXeZ7ElGw51_JF6TZuylsCHQcXd-e_GyV7mA&s"
        ],
        [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxriBp7gAvC3DeO0ZsaDqinL-7dZCJ_ulUmx_B3ad-QOo911PD0nwmsyZFBF3dK_bTzsw&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTimFMgOc-bNR1xeYjxD__RbzP0LApis-ovRuggm-TM0CPZl6OBeSj8TCc3Ph1sYVIjhcg&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAF2blxqmgt_0N7htQAMCDfn8thMHzWPy0z9a7_tdSsSgxDzYD9GiinavAWy8CpM7Ndl0&usqp=CAU"
        ]
    ]

    # Controles de las 3 imágenes visibles
    imagenes_visibles = [
    ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8),
    ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8),
    ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8),
    ]
    fila_carrusel = ft.Row(
    controls=imagenes_visibles,
    scroll="always",  # fuerza scroll visible para que se note
    spacing=10,
    alignment=ft.MainAxisAlignment.START
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
    
    # Barra personalizada con fondo degradado
        # Barra personalizada responsive con fondo degradado

    barra_superior = ft.Container(
    height=90,
    padding=ft.padding.symmetric(horizontal=10),
    gradient=ft.LinearGradient(
        begin=ft.alignment.center_left,
        end=ft.alignment.center_right,
        colors=["#0f2027", "#203a43", "#2c5364"],
    ),
    content=ft.Row(
        controls=[
            ft.Container(content=texto_empresa, expand=True, alignment=ft.alignment.center_left),
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    )

    # Contenido principal
    contenido = ft.Column([
        ft.Text("Bienvenido a EvermountSolutions"),
        ft.Text("Control de plagas profesional. Haz clic en el botón para contactarnos."),
        fila_carrusel 
    ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
        # Sección del carrusel debajo del contenido principal

    def ajustar_tamanos(e=None):
        ancho = page.width
        if ancho < 450:
            texto_empresa.controls[0].size = 14
            texto_empresa.controls[1].size = 14
        elif ancho < 600:
            texto_empresa.controls[0].size = 18
            texto_empresa.controls[1].size = 18
        else:
            texto_empresa.controls[0].size = 26
            texto_empresa.controls[1].size = 26
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

        texto_empresa.update()
        page.update()

    # Llamar al inicio y cuando se cambie el tamaño
    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data == "shown" else None

    # Agregar todo a la página
    page.add(barra_superior, contenido)
    asyncio.create_task(rotar_sets())
    ajustar_tamanos()
# Ejecutar en navegador
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))

