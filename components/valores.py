import asyncio

import flet as ft


def create_valores(page: ft.Page):
    TITULO_SIZE = 20
    TEXTO_SIZE = 14
    ICON_SIZE = 34
    COLOR_TITULO = "#0D2943"
    CARD_H_MATCH = 260

    def card_3d_anim(
        header_row: ft.Control,
        body: ft.Control,
        fixed_h: int | None = None,
        scroll_body: bool = False,
    ):
        normal_shadow = ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=ft.Colors.BLACK_26,
            offset=ft.Offset(3, 4),
        )
        hover_shadow = ft.BoxShadow(
            blur_radius=28,
            spread_radius=2,
            color=ft.Colors.BLACK_38,
            offset=ft.Offset(6, 12),
        )

        if scroll_body:
            body_wrapped = ft.Column([body], scroll="auto", expand=True)
        else:
            body_wrapped = body

        card = ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=18,
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
                [header_row, body_wrapped],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True if scroll_body else False,
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

    titulo_mision = ft.Text(
        "Misión",
        key="titulo_mision",
        size=TITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
    )
    texto_mision = ft.Text(
        "Brindar soluciones integrales, efectivas y sostenibles para el control de plagas, "
        "protegiendo hogares, empresas y comunidades con responsabilidad, compromiso y tecnología "
        "de vanguardia. Nos guiamos por los valores familiares que nos impulsan a ofrecer un servicio "
        "cercano, confiable y duradero.",
        key="texto_mision",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK_87,
        text_align=ft.TextAlign.JUSTIFY,
    )

    titulo_vision = ft.Text(
        "Visión",
        key="titulo_vision",
        size=TITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
    )
    texto_vision = ft.Text(
        "Ser reconocidos como una de las empresas líderes en control de plagas en Chile y Latinoamérica, "
        "destacando por nuestra excelencia operativa, innovación constante y atención personalizada, "
        "con una gestión basada en la ética, el respeto al medio ambiente y el trabajo en equipo.",
        key="texto_vision",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK_87,
        text_align=ft.TextAlign.JUSTIFY,
    )

    titulo_valores = ft.Text(
        "Valores Corporativos",
        key="titulo_valores",
        size=TITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
    )

    texto_valores = ft.Text(
        key="texto_valores",
        spans=[
            ft.TextSpan("1. Compromiso Familiar: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan("Nos mueve el vínculo de hermanos: trabajamos con dedicación y confianza, cuidando cada cliente como parte de nuestra propia casa.\n\n"),
            ft.TextSpan("2. Responsabilidad: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan("Cumplimos con lo que prometemos. Protegemos la salud, los espacios y el entorno con protocolos seguros y eficientes.\n\n"),
            ft.TextSpan("3. Innovación: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan("Aplicamos métodos modernos y tecnologías efectivas para prevenir y erradicar plagas con mínimo impacto ambiental.\n\n"),
            ft.TextSpan("4. Transparencia: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan("Informamos con claridad y actuamos con honestidad en cada paso del servicio.\n\n"),
            ft.TextSpan("5. Cercanía con el Cliente: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan("Ofrecemos atención personalizada, directa y humana. Escuchamos, entendemos y resolvemos.\n\n"),
            ft.TextSpan("6. Sostenibilidad: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan("Utilizamos productos y técnicas que cuidan la salud y respetan el medio ambiente."),
        ],
        size=TEXTO_SIZE,
        text_align=ft.TextAlign.JUSTIFY,
        color=ft.Colors.BLACK_87,
    )

    header_mision = ft.Row(
        [ft.Icon(ft.Icons.FLAG, size=ICON_SIZE, color=COLOR_TITULO), titulo_mision],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
    header_vision = ft.Row(
        [ft.Icon(ft.Icons.VISIBILITY, size=ICON_SIZE, color=COLOR_TITULO), titulo_vision],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
    header_valores = ft.Row(
        [ft.Icon(ft.Icons.VERIFIED, size=ICON_SIZE, color=COLOR_TITULO), titulo_valores],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    layout_mobile = ft.Column(
        [
            header_mision,
            texto_mision,
            ft.Divider(height=10, color="transparent"),
            header_vision,
            texto_vision,
            ft.Divider(height=10, color="transparent"),
            header_valores,
            texto_valores,
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    card_mision = card_3d_anim(
        header_mision,
        texto_mision,
        fixed_h=CARD_H_MATCH,
        scroll_body=True,
    )
    card_vision = card_3d_anim(
        header_vision,
        texto_vision,
        fixed_h=CARD_H_MATCH,
        scroll_body=True,
    )
    card_valores = card_3d_anim(
        header_valores,
        texto_valores,
        fixed_h=CARD_H_MATCH,
        scroll_body=True,
    )

    wrap_m = ft.Container(content=card_mision, width=420)
    wrap_v = ft.Container(content=card_vision, width=420)
    wrap_va = ft.Container(content=card_valores, width=640)

    row_cards = ft.Row(
        controls=[wrap_m, wrap_v, wrap_va],
        spacing=16,
        run_spacing=16,
        wrap=False,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    top_row_tablet = ft.Row(
        controls=[wrap_m, wrap_v],
        spacing=14,
        wrap=False,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    layout_tablet = ft.Column(
        controls=[
            top_row_tablet,
            ft.Container(
                content=wrap_va,
                alignment=ft.alignment.center,
            ),
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    root = ft.Container(
        width=float("inf"),
        padding=ft.Padding.symmetric(horizontal=8, vertical=12),
        content=layout_mobile,
    )

    def apply_layout():
        w = page.width or 0

        if w <= 600:
            root.content = layout_mobile
            wrap_m.expand = None
            wrap_v.expand = None
            wrap_va.expand = None
            wrap_m.width = None
            wrap_v.width = None
            wrap_va.width = None
        elif w < 1100:
            root.content = layout_tablet
            wrap_m.expand = None
            wrap_v.expand = None
            wrap_va.expand = None
            small_w = int(w * 0.43)
            wrap_m.width = max(250, min(small_w, 360))
            wrap_v.width = max(250, min(small_w, 360))
            wrap_va.width = max(520, min(int(w * 0.88), 860))
        else:
            root.content = row_cards
            wrap_m.width = None
            wrap_v.width = None
            wrap_va.width = None
            wrap_m.expand = 1
            wrap_v.expand = 1
            wrap_va.expand = 1

        if getattr(root, "page", None) is not None:
            root.update()

    root.data = {
        "apply_layout": apply_layout,
        "titulos": [titulo_mision, titulo_vision, titulo_valores],
        "textos": [texto_mision, texto_vision, texto_valores],
    }

    return root
