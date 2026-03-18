import asyncio

import flet as ft


def create_quienes(page: ft.Page):
    COLOR_TITULO = "#0D2943"
    TEXTO_SIZE = 14
    SUBTITULO_SIZE = 18
    CARD_H_MATCH = 210

    titulo1 = ft.Text(
        "Evermount Solutions - Pest Defense",
        key="quienes_subtitulo",
        size=SUBTITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
        text_align=ft.TextAlign.CENTER,
    )

    texto1 = ft.Text(
        "Somos una empresa familiar dedicada con pasión al control y manejo integral de plagas. Fundada "
        "por dos hermanos, nuestra misión es proteger hogares, empresas y comunidades con soluciones "
        "efectivas, responsables y personalizadas.\n\n"
        "Confía en nosotros para mantener tus espacios seguros, limpios y libres de plagas, con tecnología "
        "avanzada y atención profesional.\n\n"
        "Confianza familiar, protección garantizada.",
        key="quienes_texto",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK_87,
        text_align=ft.TextAlign.JUSTIFY,
    )

    titulo2 = ft.Text(
        "Compromiso y Trabajo en Equipo",
        size=SUBTITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
        text_align=ft.TextAlign.CENTER,
    )

    texto2 = ft.Text(
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

    titulo3 = ft.Text(
        "¿Qué nos diferencia?",
        size=SUBTITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
        text_align=ft.TextAlign.CENTER,
    )

    bullet1 = ft.Text("- Somos una empresa certificada y en constante actualización.", size=TEXTO_SIZE, color=ft.Colors.BLACK_87)
    bullet2 = ft.Text("- Cada cliente es tratado como si fuera parte de nuestra familia.", size=TEXTO_SIZE, color=ft.Colors.BLACK_87)
    bullet3 = ft.Text("- Actuamos con transparencia, eficacia y puntualidad.", size=TEXTO_SIZE, color=ft.Colors.BLACK_87)

    lista = ft.Column([bullet1, bullet2, bullet3], spacing=6)

    layout_movil = ft.Column(
        [
            titulo1, texto1,
            ft.Divider(height=8, color="transparent"),
            titulo2, texto2,
            ft.Divider(height=8, color="transparent"),
            titulo3, lista,
        ],
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def card_3d_anim(title_ctrl: ft.Control, body_ctrl: ft.Control, fixed_h: int):
        normal_shadow = ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=ft.Colors.BLACK_26,
            offset=ft.Offset(3, 4),
        )
        hover_shadow = ft.BoxShadow(
            blur_radius=26,
            spread_radius=2,
            color=ft.Colors.BLACK_38,
            offset=ft.Offset(6, 10),
        )

        body_scroll = ft.Column([body_ctrl], scroll="auto", expand=True)

        card = ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=16,
            padding=ft.Padding.symmetric(horizontal=16, vertical=14),
            border=ft.Border.all(1, ft.Colors.BLACK_12),
            shadow=normal_shadow,
            animate=ft.Animation(220, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(120, ft.AnimationCurve.EASE_OUT),
            animate_offset=ft.Animation(220, ft.AnimationCurve.EASE_OUT),
            offset=ft.Offset(0, 0),
            scale=1.0,
            ink=True,
            height=fixed_h,
            content=ft.Column(
                [title_ctrl, body_scroll],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
        )

        def on_hover(e: ft.HoverEvent):
            hovering = e.data == "true"
            card.offset = ft.Offset(0, -0.04) if hovering else ft.Offset(0, 0)
            card.shadow = hover_shadow if hovering else normal_shadow
            card.update()

        async def on_click(e):
            card.scale = 1.03
            card.update()
            await asyncio.sleep(0.08)
            card.scale = 1.0
            card.update()

        card.on_hover = on_hover
        card.on_click = on_click
        return card

    title_style_size = 16

    card1 = card_3d_anim(
        ft.Text(titulo1.value, size=title_style_size, weight=ft.FontWeight.BOLD, color=COLOR_TITULO, text_align=ft.TextAlign.CENTER),
        ft.Text(texto1.value, size=TEXTO_SIZE, color=ft.Colors.BLACK_87, text_align=ft.TextAlign.JUSTIFY),
        fixed_h=CARD_H_MATCH,
    )
    card2 = card_3d_anim(
        ft.Text(titulo2.value, size=title_style_size, weight=ft.FontWeight.BOLD, color=COLOR_TITULO, text_align=ft.TextAlign.CENTER),
        ft.Text(texto2.value, size=TEXTO_SIZE, color=ft.Colors.BLACK_87, text_align=ft.TextAlign.JUSTIFY),
        fixed_h=CARD_H_MATCH,
    )
    card3 = card_3d_anim(
        ft.Text(titulo3.value, size=title_style_size, weight=ft.FontWeight.BOLD, color=COLOR_TITULO, text_align=ft.TextAlign.CENTER),
        ft.Column(
            [
                ft.Text(bullet1.value, size=TEXTO_SIZE, color=ft.Colors.BLACK_87),
                ft.Text(bullet2.value, size=TEXTO_SIZE, color=ft.Colors.BLACK_87),
                ft.Text(bullet3.value, size=TEXTO_SIZE, color=ft.Colors.BLACK_87),
            ],
            spacing=6,
        ),
        fixed_h=CARD_H_MATCH,
    )

    wrap1 = ft.Container(content=card1, expand=True, padding=ft.Padding.symmetric(horizontal=10, vertical=8))
    wrap2 = ft.Container(content=card2, expand=True, padding=ft.Padding.symmetric(horizontal=10, vertical=8))
    wrap3 = ft.Container(content=card3, expand=True, padding=ft.Padding.symmetric(horizontal=10, vertical=8))

    row_cards = ft.Row(
        controls=[wrap1, wrap2, wrap3],
        spacing=16,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START,
        wrap=False,
    )

    layout_3cols = ft.Column(
        [row_cards],
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    layout_tablet = ft.Column(
        [wrap1, wrap2, wrap3],
        spacing=4,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    contenedor = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=layout_movil,
        width=float("inf"),
    )

    def apply_layout():
        w = page.width or 0

        if w <= 600:
            contenedor.content = layout_movil
            wrap1.expand = None
            wrap2.expand = None
            wrap3.expand = None
            wrap1.width = None
            wrap2.width = None
            wrap3.width = None
        elif w < 1100:
            contenedor.content = layout_tablet
            wrap1.expand = None
            wrap2.expand = None
            wrap3.expand = None
            card_w = max(320, min(int(w * 0.82), 720))
            wrap1.width = card_w
            wrap2.width = card_w
            wrap3.width = card_w
        else:
            contenedor.content = layout_3cols
            wrap1.width = None
            wrap2.width = None
            wrap3.width = None
            wrap1.expand = 1
            wrap2.expand = 1
            wrap3.expand = 1

        if getattr(contenedor, "page", None) is not None:
            contenedor.update()

    contenedor.data = {
        "apply_layout": apply_layout,
        "texts": [titulo1, texto1, titulo2, texto2, titulo3, bullet1, bullet2, bullet3],
    }

    return contenedor
