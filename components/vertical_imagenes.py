import asyncio

import flet as ft
from functions.asset_sources import PROGRAM_IMAGES

IMAGENES = [
    *PROGRAM_IMAGES,
]


def create_vertical_carousel(page: ft.Page, intervalo=3):
    es_pc_tablet = (page.width or 0) >= 700
    title_size = 18 if es_pc_tablet else 22
    body_size = 14
    plan_size = 12 if es_pc_tablet else 14

    idx = [0]
    activo = [False]
    tarea = [None]

    card_w = 263
    card_h = 360

    imagen = ft.Image(
        src=IMAGENES[idx[0]],
        fit=ft.BoxFit.FILL,
        width=card_w,
        height=card_h,
    )

    tarjeta = ft.Container(
        content=imagen,
        width=card_w,
        height=card_h,
        bgcolor="#FDFEFE",
        border_radius=24,
        border=ft.Border.all(1, "#D9E5EA"),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            blur_radius=18,
            spread_radius=0,
            color="rgba(12,38,46,0.15)",
            offset=ft.Offset(0, 10),
        ),
    )

    carrusel_control = ft.Container(
        content=tarjeta,
        alignment=ft.alignment.center,
        padding=0,
    )
    carrusel_control.data = {"tarjeta": tarjeta, "imagen": imagen}

    async def _rotar():
        try:
            while activo[0]:
                if getattr(imagen, "page", None) is not None:
                    imagen.src = IMAGENES[idx[0] % len(IMAGENES)]
                    try:
                        imagen.update()
                    except AssertionError:
                        return
                    except Exception:
                        return
                    idx[0] = (idx[0] + 1) % len(IMAGENES)
                await asyncio.sleep(intervalo)
        except asyncio.CancelledError:
            pass

    def start():
        if tarea[0] is None:
            activo[0] = True
            tarea[0] = page.run_task(_rotar)

    def stop():
        activo[0] = False
        if tarea[0] is not None:
            tarea[0].cancel()
            tarea[0] = None

    def benefit(icon_name, title, text):
        return ft.Row(
            [
                ft.Container(
                    width=28,
                    height=28,
                    border_radius=14,
                    bgcolor="#E6F0F5",
                    alignment=ft.alignment.center,
                    content=ft.Icon(icon_name, color="#0D2943", size=15),
                ),
                ft.Column(
                    [
                        ft.Text(title, size=13 if es_pc_tablet else 14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                        ft.Text(text, size=body_size, color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT),
                    ],
                    spacing=2,
                    expand=True,
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    def plan_item(texto, icono):
        return ft.Container(
            bgcolor="#F7F9FB",
            border_radius=14,
            padding=ft.Padding.symmetric(horizontal=12, vertical=10),
            content=ft.Row(
                [
                    ft.Icon(icono, color="#0D2943", size=18),
                    ft.Text(texto, size=plan_size, color=ft.Colors.BLACK_87),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    planes_col1 = [
        ("Restaurantes", ft.Icons.RESTAURANT),
        ("Bodegas", ft.Icons.WAREHOUSE),
        ("Condominios", ft.Icons.HOUSE),
    ]

    planes_col2 = [
        ("Supermercados", ft.Icons.SHOPPING_CART),
        ("Centros educativos", ft.Icons.SCHOOL),
        ("Empresas", ft.Icons.VERIFIED),
    ]

    header_programa = ft.Column(
        [
            ft.Container(
                bgcolor="#E6F1F4",
                border_radius=999,
                padding=ft.Padding.symmetric(horizontal=12, vertical=6),
                content=ft.Text(
                    "Programas preventivos",
                    size=12,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
            ),
            ft.Row(
                [
                    ft.Container(
                        width=42,
                        height=42,
                        border_radius=14,
                        bgcolor="#F4F8FB",
                        alignment=ft.alignment.center,
                        content=ft.Icon(ft.Icons.DATE_RANGE, size=24, color="#0D2943"),
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "Control Mensual y Anual",
                                size=title_size,
                                weight=ft.FontWeight.BOLD,
                                color="#0D2943",
                                text_align=ft.TextAlign.LEFT,
                            ),
                            ft.Text(
                                "Planes preventivos pensados para continuidad operativa, control constante y menor improvisación.",
                                size=13 if es_pc_tablet else 14,
                                color=ft.Colors.BLACK,
                                text_align=ft.TextAlign.LEFT,
                            ),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=10,
    )

    texto_presentacion = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        border=ft.Border.all(1, "#D8E2E8"),
        height=388 if es_pc_tablet else None,
        padding=ft.Padding.symmetric(horizontal=18, vertical=18),
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=0,
            color="rgba(13,38,46,0.14)",
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            [
                ft.Container(height=4, bgcolor="#0D2943", border_radius=999),
                header_programa,
                benefit(ft.Icons.EVENT_AVAILABLE, "Visitas programadas", "Seguimiento técnico y control preventivo durante todo el año."),
                benefit(ft.Icons.DESCRIPTION, "Informes y certificados", "Documentación de aplicación y respaldo de cada servicio."),
                benefit(ft.Icons.SHIELD, "Cobertura integral", "Adaptado a espacios residenciales, comerciales e industriales."),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO if es_pc_tablet else ft.ScrollMode.HIDDEN,
        ),
    )

    planes_header = ft.Column(
        [
            ft.Container(
                bgcolor="#EEF5F7",
                border_radius=999,
                padding=ft.Padding.symmetric(horizontal=12, vertical=6),
                content=ft.Text(
                    "Cobertura por rubro",
                    size=12,
                    weight=ft.FontWeight.BOLD,
                    color="#4D6771",
                ),
            ),
            ft.Row(
                [
                    ft.Container(
                        width=38,
                        height=38,
                        border_radius=12,
                        bgcolor="#F4F8FB",
                        alignment=ft.alignment.center,
                        content=ft.Icon(ft.Icons.BUSINESS, size=22, color="#0D2943"),
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "Planes ideales para",
                                size=title_size,
                                weight=ft.FontWeight.BOLD,
                                color="#0D2943",
                                text_align=ft.TextAlign.LEFT,
                            ),
                            ft.Text(
                                "Cobertura flexible para distintos tipos de actividad.",
                                size=13 if es_pc_tablet else 14,
                                color="#5F6E79",
                                text_align=ft.TextAlign.LEFT,
                            ),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=10,
    )

    lista_planes = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        border=ft.Border.all(1, "#D8E2E8"),
        height=240 if es_pc_tablet else None,
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=0,
            color="rgba(13,38,46,0.14)",
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            [
                ft.Container(height=4, bgcolor="#0D2943", border_radius=999),
                planes_header,
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Column([plan_item(texto, icono) for texto, icono in planes_col1], spacing=8),
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Column([plan_item(texto, icono) for texto, icono in planes_col2], spacing=8),
                            expand=True,
                        ),
                    ],
                    spacing=12,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ],
            spacing=14,
        ),
    )

    bloque_texto = ft.Container(
        content=ft.Column(
            [texto_presentacion, lista_planes],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
        ),
        width=420,
        padding=ft.Padding.only(top=4, bottom=4),
    )
    bloque_texto.data = {
        "top_card": texto_presentacion,
        "bottom_card": lista_planes,
        "gap": 14,
        "base_width": 420,
    }

    bloque_carrusel = carrusel_control

    return bloque_texto, bloque_carrusel, start, stop


