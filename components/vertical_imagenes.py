import asyncio

import flet as ft

IMAGENES = [
    "https://i.postimg.cc/15nLZNp7/imagen1.jpg",
    "https://i.postimg.cc/RZwyW5pc/imagen2.jpg",
    "https://i.postimg.cc/BvgzC50b/imagen3.jpg",
    "https://i.postimg.cc/FRCnM91Q/imagen4.jpg",
    "https://i.postimg.cc/9FN0WFkY/Whats-App-Image-2025-11-17-at-5-58-09-PM.jpg",
    "https://i.postimg.cc/Xq5W44BD/Whats-App-Image-2025-11-17-at-5-58-10-PM.jpg",
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
        bgcolor=ft.Colors.BLACK_12,
        border_radius=12,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        alignment=ft.alignment.center,
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
                imagen.src = IMAGENES[idx[0] % len(IMAGENES)]
                page.update()
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
                        ft.Text(title, size=13 if es_pc_tablet else 14, weight=ft.FontWeight.BOLD, color="#0D2943"),
                        ft.Text(text, size=body_size, color=ft.Colors.BLACK_87, text_align=ft.TextAlign.LEFT),
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

    header_programa = ft.Row(
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
                        "Planes de mantenimiento pensados para continuidad operativa y proteccion constante.",
                        size=13 if es_pc_tablet else 14,
                        color="#5F6E79",
                        text_align=ft.TextAlign.LEFT,
                    ),
                ],
                spacing=2,
                expand=True,
            ),
        ],
        spacing=12,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    texto_presentacion = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        border=ft.Border.all(1, "#D8E2E8"),
        height=340 if es_pc_tablet else None,
        padding=ft.Padding.symmetric(horizontal=18, vertical=18),
        shadow=ft.BoxShadow(
            blur_radius=12,
            spread_radius=1,
            color=ft.Colors.BLACK_26,
            offset=ft.Offset(2, 4),
        ),
        content=ft.Column(
            [
                ft.Container(height=4, bgcolor="#0D2943", border_radius=999),
                header_programa,
                benefit(ft.Icons.EVENT_AVAILABLE, "Visitas programadas", "Seguimiento tecnico y control preventivo durante todo el ano."),
                benefit(ft.Icons.DESCRIPTION, "Informes y certificados", "Documentacion de aplicacion y respaldo de cada servicio."),
                benefit(ft.Icons.SHIELD, "Cobertura integral", "Adaptado a espacios residenciales, comerciales e industriales."),
                ft.Container(height=6),
            ],
            spacing=14,
        ),
    )

    planes_header = ft.Row(
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
    )

    lista_planes = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        border=ft.Border.all(1, "#D8E2E8"),
        height=240 if es_pc_tablet else None,
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        shadow=ft.BoxShadow(
            blur_radius=12,
            spread_radius=1,
            color=ft.Colors.BLACK_26,
            offset=ft.Offset(2, 4),
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
    )
    bloque_texto.data = {
        "top_card": texto_presentacion,
        "bottom_card": lista_planes,
        "gap": 14,
        "base_width": 420,
    }

    bloque_carrusel = carrusel_control

    return bloque_texto, bloque_carrusel, start, stop
