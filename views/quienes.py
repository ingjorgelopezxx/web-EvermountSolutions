import flet as ft


def create_quienes(page: ft.Page):
    HEADER_COLOR = "#0D2943"
    TEXT_COLOR = "#23313B"
    MUTED = "#5F6E79"
    SOFT_BG = "#F4F8FB"
    CHIP_BG = "#E6F0F5"
    TITLE_SIZE = 20
    CARD_H = 330

    def bullet(icon_name: str, title: str, text: str):
        return ft.Row(
            [
                ft.Container(
                    width=28,
                    height=28,
                    border_radius=14,
                    bgcolor=CHIP_BG,
                    alignment=ft.alignment.center,
                    content=ft.Icon(icon_name, size=15, color=HEADER_COLOR),
                ),
                ft.Column(
                    [
                        ft.Text(title, size=13, weight=ft.FontWeight.BOLD, color=HEADER_COLOR),
                        ft.Text(text, size=12, color=TEXT_COLOR, text_align=ft.TextAlign.LEFT),
                    ],
                    spacing=2,
                    expand=True,
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    def info_chip(icon_name: str, label: str, value: str):
        chip_value_size = 10 if (page.width or 0) <= 600 else 13
        chip_label_size = 9 if (page.width or 0) <= 600 else 11
        return ft.Container(
            bgcolor=CHIP_BG,
            border_radius=14,
            padding=ft.Padding.symmetric(horizontal=10 if (page.width or 0) <= 600 else 12, vertical=8 if (page.width or 0) <= 600 else 10),
            content=ft.Row(
                [
                    ft.Icon(icon_name, size=16, color=HEADER_COLOR),
                    ft.Column(
                        [
                            ft.Text(value, size=chip_value_size, weight=ft.FontWeight.BOLD, color=HEADER_COLOR, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text(label, size=chip_label_size, color=MUTED, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                        ],
                        spacing=1,
                        tight=True,
                        expand=True,
                    ),
                ],
                spacing=8,
                tight=True,
            ),
            expand=1 if (page.width or 0) <= 600 else None,
        )

    def make_card(icon_name: str, title: str, summary: str, bullets: list[ft.Control], chips: list[ft.Control]):
        normal_shadow = ft.BoxShadow(
            blur_radius=20,
            spread_radius=0,
            color="rgba(13,38,46,0.14)",
            offset=ft.Offset(0, 10),
        )

        body = ft.Column(
            [
                ft.Column(bullets, spacing=10),
                ft.Row(chips, wrap=True, spacing=8, run_spacing=8),
            ],
            spacing=14,
            scroll="auto",
            expand=True,
        )

        card = ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            border=ft.Border.all(1, "#D8E2E8"),
            padding=ft.Padding.symmetric(horizontal=18, vertical=16),
            shadow=normal_shadow,
            height=CARD_H,
            content=ft.Column(
                [
                    ft.Container(height=4, bgcolor=HEADER_COLOR, border_radius=999),
                    ft.Row(
                        [
                            ft.Container(
                                width=42,
                                height=42,
                                border_radius=14,
                                bgcolor=SOFT_BG,
                                alignment=ft.alignment.center,
                                content=ft.Icon(icon_name, size=24, color=HEADER_COLOR),
                            ),
                            ft.Column(
                                [
                                    ft.Text(title, size=TITLE_SIZE, weight=ft.FontWeight.BOLD, color=HEADER_COLOR),
                                    ft.Text(summary, size=13, color=MUTED, text_align=ft.TextAlign.LEFT),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    body,
                ],
                spacing=14,
                expand=True,
            ),
        )
        card.data = {"body": body}
        return card

    mobile_intro = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=18,
        border=ft.Border.all(1, "#D8E2E8"),
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=0,
            color="rgba(13,38,46,0.14)",
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Una empresa familiar que combina cercanía, criterio técnico y seguimiento constante en cada servicio.",
                    size=13,
                    color=TEXT_COLOR,
                    text_align=ft.TextAlign.LEFT,
                ),
                bullet(ft.Icons.SHIELD, "Protección integral", "Cuidamos espacios con protocolos modernos y seguimiento cercano."),
                bullet(ft.Icons.SUPPORT_AGENT, "Atención profesional", "Combinamos experiencia técnica con trato humano y acompañamiento real."),
                ft.Row(
                    [
                        info_chip(ft.Icons.GROUP, "Origen", "Empresa familiar"),
                        info_chip(ft.Icons.VERIFIED, "Estilo", "Servicio confiable"),
                    ],
                    wrap=False,
                    spacing=8,
                ),
            ],
            spacing=14,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        alignment=ft.alignment.center_left,
    )

    card_empresa = make_card(
        ft.Icons.BUSINESS_CENTER,
        "Evermount Solutions",
        "Base empresarial sólida, cercana y orientada a resultados.",
        [
            bullet(ft.Icons.FAMILY_RESTROOM, "Origen familiar", "Nacimos con una cultura de trabajo cercana, responsable y comprometida."),
            bullet(ft.Icons.SHIELD, "Protección real", "Diseñamos soluciones integrales para hogares, empresas y comunidades."),
            bullet(ft.Icons.SETTINGS_SUGGEST, "Operación profesional", "Combinamos tecnología, criterio técnico y seguimiento constante."),
        ],
        [
            info_chip(ft.Icons.HOME_WORK, "Cobertura", "Hogar y empresa"),
            info_chip(ft.Icons.STARS, "Sello", "Confianza y continuidad"),
        ],
    )

    card_compromiso = make_card(
        ft.Icons.HANDSHAKE,
        "Nuestro compromiso",
        "Atención cercana con ejecución técnica de alto nivel.",
        [
            bullet(ft.Icons.ENGINEERING, "Experiencia en terreno", "Actuamos con conocimiento técnico y lectura correcta de cada escenario."),
            bullet(ft.Icons.TASK_ALT, "Respuesta responsable", "Mantenemos orden, puntualidad y claridad durante todo el servicio."),
            bullet(ft.Icons.PSYCHOLOGY, "Soluciones a medida", "Evaluamos cada caso para aplicar medidas acordes al riesgo y al entorno."),
        ],
        [
            info_chip(ft.Icons.SUPPORT_AGENT, "Atención", "Directa y humana"),
            info_chip(ft.Icons.GPP_GOOD, "Estándar", "Seguro y profesional"),
        ],
    )

    card_diferencia = make_card(
        ft.Icons.AUTO_AWESOME,
        "Lo que nos diferencia",
        "Una propuesta de servicio clara, moderna y confiable.",
        [
            bullet(ft.Icons.SCHOOL, "Actualización constante", "Nos mantenemos al día en técnicas, procesos y buenas prácticas."),
            bullet(ft.Icons.VERIFIED_USER, "Confianza en el servicio", "Cada cliente es atendido con cercanía, respeto y sentido de responsabilidad."),
            bullet(ft.Icons.SCHEDULE, "Cumplimiento real", "Actuamos con transparencia, eficacia y puntualidad en cada visita."),
        ],
        [
            info_chip(ft.Icons.PUBLIC, "Enfoque", "Prevención y control"),
            info_chip(ft.Icons.DONE_ALL, "Promesa", "Claridad y seguimiento"),
        ],
    )

    cards = [card_empresa, card_compromiso, card_diferencia]

    section_header = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Una empresa familiar que combina cercanía, criterio técnico y seguimiento constante en cada servicio.",
                    size=13,
                    color=MUTED,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
    )

    mobile_layout = ft.Column(
        [section_header, mobile_intro],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    wrap1 = ft.Container(content=card_empresa, width=420)
    wrap2 = ft.Container(content=card_compromiso, width=420)
    wrap3 = ft.Container(content=card_diferencia, width=420)

    desktop_layout = ft.Row(
        controls=[wrap1, wrap2, wrap3],
        spacing=18,
        wrap=False,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    tablet_top_holder = ft.Container(
        content=ft.Row(
            [wrap1, wrap2],
            spacing=14,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
        alignment=ft.alignment.center,
    )
    tablet_layout = ft.Column(
        [
            section_header,
            tablet_top_holder,
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    desktop_stack = ft.Column(
        [
            section_header,
            desktop_layout,
        ],
        spacing=18,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    root = ft.Container(
        bgcolor="#F7FBFC",
        border_radius=30,
        border=ft.Border.all(1, "#DFEAEE"),
        padding=ft.Padding.symmetric(horizontal=12, vertical=14),
        content=mobile_layout,
        width=float("inf"),
    )

    def apply_layout():
        w = page.width or 0

        if w <= 600:
            mode = "mobile"
            root.content = mobile_layout
            root.padding = ft.Padding.symmetric(horizontal=10, vertical=12)
            for wrap in (wrap1, wrap2, wrap3):
                wrap.expand = None
                wrap.width = None
            for card in cards:
                card.height = None
                card.data["body"].scroll = None
                card.data["body"].expand = False
        elif w < 1100:
            mode = "tablet"
            root.content = tablet_layout
            root.padding = ft.Padding.symmetric(horizontal=6, vertical=14)
            section_w = min(int(w * 0.84), 980)
            card_w = max(200, int((section_w - 10) / 2))
            if isinstance(tablet_top_holder.content, ft.Row):
                tablet_top_holder.content.spacing = 10
            for wrap in (wrap1, wrap2):
                wrap.expand = None
                wrap.width = card_w
            tablet_top_holder.width = section_w
            for card in cards:
                card.height = None
                card.data["body"].scroll = None
                card.data["body"].expand = False
        else:
            mode = "desktop"
            root.content = desktop_stack
            root.padding = ft.Padding.symmetric(horizontal=14, vertical=18)
            for wrap in (wrap1, wrap2, wrap3):
                wrap.width = None
                wrap.expand = 1
            for card in cards:
                card.height = CARD_H
                card.data["body"].scroll = "auto"
                card.data["body"].expand = True

        if getattr(root, "page", None) is not None:
            root.update()

    root.data = {
        "apply_layout": apply_layout,
        "cards": cards,
    }

    return root

