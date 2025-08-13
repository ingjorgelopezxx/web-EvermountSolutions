# components/sabiasque.py
import flet as ft


# Puedes cambiar/expandir estos items cuando quieras
SABIASQUE_ITEMS = [
    {
        "titulo": "¿Sabías que las cucarachas pueden vivir hasta una semana sin su cabeza?",
        "imagen": "https://www.gardentech.com/-/media/project/oneweb/gardentech/images/pest-id/bug-pest/cockroach.png",
        "texto": (
            "Las cucarachas son plagas muy resistentes y adaptables, con diversas curiosidades que las hacen fascinantes y problemáticas. "
            "Son capaces de sobrevivir sin cabeza por un tiempo, soportan altos niveles de radiación y pueden sobrevivir sin comida por semanas o sin agua por días. "
            "Además, pueden transmitir enfermedades y son atraídas por la comida y la humedad, lo que las convierte en una amenaza para la salud y la higiene."
            "Algunas especies de cucarachas pueden vivir hasta un mes sin comida, adaptándose fácilmente a diferentes entornos, "
            "pueden correr hasta 3 millas por hora, lo que las hace muy difíciles de atrapar. Su velocidad y agilidad les permiten escapar " 
            "rápidamente de los depredadores y de los intentos de captura. Además, son capaces de girar rápidamente en ángulos agudos y esconderse en espacios reducidos. " 
            "esta capacidad de supervivencia las convierte en una de las plagas más resistentes y difíciles de eliminar. "
        ),
        "extra": [
            "Resistencia: Pueden sobrevivir sin cabeza por hasta una semana y pueden aguantar la respiración hasta por 40 minutos.",
            "Adaptabilidad: Se adaptan a diversos ambientes, pero prefieren interiores cálidos y húmedos, cerca de fuentes de alimento y agua.",
            "Transmisión de enfermedades: Transmiten salmonela, E. coli y otras bacterias peligrosas.",
            "Comportamiento: Son nocturnas, se esconden de la luz y atraen a otras mediante rastros químicos.",
            "Reproducción: Se multiplican rápidamente, generando infestaciones graves.",
            "Alimentación: Comen desde alimentos humanos y de mascotas hasta basura y materia orgánica.",
            "Impacto en la salud: Pueden causar alergias y asma, sobre todo en niños.",
            "No solo la cucaracha americana: También hay otras plagas como la oriental y la alemana.",
            "Evitar pisarlas: Al aplastarlas pueden dispersar bacterias y gérmenes peligrosos."
        ]
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
    {
        "titulo": "¿Sabías que las termitas nunca duermen?",
        "imagen": "https://i.postimg.cc/zD0Rq1dr/termitas-1.png",
        "texto": (
            "Estas pequeñas plagas trabajan sin descanso, día y noche, comiendo madera y debilitando estructuras. "
            "Su actividad constante puede causar daños graves a edificios y muebles si no se controla a tiempo. ¡Protege tu hogar con un control de plagas profesional y mantén a las termitas lejos!"
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
                        text_align=ft.TextAlign.CENTER,
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
                        text_align=ft.TextAlign.JUSTIFY,
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(
                    [
                     ft.Text("•", size=18,color=ft.Colors.BLACK),
                                ft.Text(
                                    p.split(":", 1)[0] + ":",
                                    size=14,color=ft.Colors.BLACK,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    p.split(":", 1)[1].strip() if ":" in p else "",
                                    size=14,color=ft.Colors.BLACK
                                )
                            ],
                            spacing=6
                        )
                        for p in d.get("extra", [])
                    ],
                    spacing=2
                ) if "extra" in d else ft.Container()
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
