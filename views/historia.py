import flet as ft


def create_historia(page: ft.Page):
    COLOR_TITULO = "#0D2943"
    TEXTO_SIZE = 14
    SUBTITULO_SIZE = 18

    subtitulo = ft.Text(
        "Compromiso y Trabajo en Equipo",
        size=SUBTITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
        text_align=ft.TextAlign.CENTER,
    )

    texto_principal = ft.Text(
        "Evermount Solutions nació de la visión de dos hermanos con una meta común: "
        "brindar un servicio de excelencia en el control de plagas, con ética, responsabilidad ambiental "
        "y atención cercana.\n\n"
        "Contamos con formación técnica, experiencia en terreno y una vocación clara por el servicio. "
        "Nuestra empresa combina el profesionalismo de una gran compañía con la calidez de una atención "
        "personalizada.",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK_87,
        text_align=ft.TextAlign.JUSTIFY,
    )

    subtitulo2 = ft.Text(
        "¿Qué nos diferencia?",
        size=SUBTITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
    )

    bullet1 = ft.Text(
        "- Somos una empresa certificada y en constante actualización.",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK_87,
    )
    bullet2 = ft.Text(
        "- Cada cliente es tratado como si fuera parte de nuestra familia.",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK_87,
    )
    bullet3 = ft.Text(
        "- Actuamos con transparencia, eficacia y puntualidad.",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK_87,
    )

    lista_diferencias = ft.Column(
        [
            bullet1,
            bullet2,
            bullet3,
        ],
        spacing=5,
    )

    contenedor = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            [
                subtitulo,
                texto_principal,
                subtitulo2,
                lista_diferencias,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
        width=page.width,
    )

    contenedor.data = {
        "sub1": subtitulo,
        "texto": texto_principal,
        "sub2": subtitulo2,
        "bullets": [bullet1, bullet2, bullet3],
    }

    return contenedor
