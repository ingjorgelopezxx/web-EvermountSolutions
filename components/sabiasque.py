# components/sabiasque.py
import flet as ft


# Puedes cambiar/expandir estos items cuando quieras
SABIASQUE_ITEMS = [
    {
        "titulo": "¿Sabías que las cucarachas pueden vivir hasta una semana sin su cabeza?",
        "imagen": "https://www.gardentech.com/-/media/project/oneweb/gardentech/images/pest-id/bug-pest/cockroach.png",
        "texto": (
            "Tienen un sistema nervioso que les permite sobrevivir un tiempo sin ella, "
            "aunque finalmente mueren por falta de agua. Además, pueden aguantar hasta "
            "40 minutos sin respirar y soportar niveles de radiación que matarían a un humano. "
            "¡Por eso es tan importante controlarlas con expertos como Fumigax!"
        ),
    },
    {
        "titulo": "¿Sabías que una sola rata puede producir hasta 2,000 descendientes en un año si no se controla su población?",
        "imagen": "https://i.postimg.cc/X7Dt0Tf1/istockphoto-1413873422-612x612.jpg",
        "texto": (
            "Las ratas tienen una gran capacidad reproductiva y, sin medidas de control, "
            "pueden convertirse rápidamente en una infestación grave. Además de los daños "
            "materiales, son portadoras de enfermedades peligrosas. ¡Por eso el control de plagas es esencial!"
        ),
    },
]


def _img_height_for(page: ft.Page) -> int:
    """Altura de imagen adaptada a celulares, tablets y PCs."""
    if page.width < 480:      # Celulares pequeños
        return 160
    elif page.width < 768:    # Celulares grandes / Tablets pequeñas
        return 220
    elif page.width < 1200:   # Tablets grandes / Laptops
        return 280
    else:                     # Monitores grandes
        return 350


def render_sabiasque(page: ft.Page, contenedor: ft.Column, items: list | None = None):
    """
    Reemplaza el contenido principal por la sección 'Sabías que'.
    - page: ft.Page
    - contenedor: normalmente tu Column 'contenido'
    - items: lista de curiosidades (opcional). Si no se pasa, usa SABIASQUE_ITEMS.
    """
    data = items or SABIASQUE_ITEMS
    img_h = _img_height_for(page)

    # Asegura que el contenedor principal no deje espacios arriba/entre bloques
    contenedor.padding = 0
    contenedor.spacing = 0

    bloques: list[ft.Control] = []

    for i, d in enumerate(data):
        # Separación SOLO entre bloques (no arriba del primero)
        if i > 0:
            bloques.append(ft.Container(height=12))  # pequeño espacio entre tarjetas

        bloque = ft.Container(
            # Ocupa todo el ancho disponible
            width=page.width,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            padding=12,
            margin=ft.margin.only(left=0, right=0, top=0, bottom=0),
            shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK12, offset=ft.Offset(2, 2)),
            content=ft.Column(
                [
                    ft.Text(
                        d["titulo"],
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.LEFT,
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=d["imagen"],
                            fit=ft.ImageFit.COVER,
                            border_radius=8,
                        ),
                        height=img_h,
                        border_radius=8,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        expand=True,
                    ),
                    ft.Text(
                        d["texto"],
                        size=15,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.LEFT,
                    ),
                ],
                spacing=10,
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        bloques.append(bloque)

    contenedor.controls.clear()
    contenedor.controls.append(
        ft.Column(
            bloques,
            spacing=0,                   # sin huecos añadidos
            expand=True,
            scroll=ft.ScrollMode.AUTO,   # scroll si hace falta
        )
    )
    contenedor.update()
