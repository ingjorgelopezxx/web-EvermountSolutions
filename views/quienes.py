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
        return ft.Container(
            bgcolor=CHIP_BG,
            border_radius=14,
            padding=ft.Padding.symmetric(horizontal=12, vertical=10),
            content=ft.Row(
                [
                    ft.Icon(icon_name, size=16, color=HEADER_COLOR),
                    ft.Column(
                        [
                            ft.Text(value, size=13, weight=ft.FontWeight.BOLD, color=HEADER_COLOR),
                            ft.Text(label, size=11, color=MUTED),
                        ],
                        spacing=1,
                        tight=True,
                    ),
                ],
                spacing=8,
                tight=True,
            ),
        )

    def make_card(icon_name: str, title: str, summary: str, bullets: list[ft.Control], chips: list[ft.Control]):
        normal_shadow = ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=ft.Colors.BLACK_26,
            offset=ft.Offset(3, 4),
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
            blur_radius=12,
            spread_radius=1,
            color=ft.Colors.BLACK_26,
            offset=ft.Offset(2, 4),
        ),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=42,
                            height=42,
                            border_radius=14,
                            bgcolor=SOFT_BG,
                            alignment=ft.alignment.center,
                            content=ft.Icon(ft.Icons.BUSINESS_CENTER, size=24, color=HEADER_COLOR),
                        ),
                        ft.Column(
                            [
                                ft.Text("Quienes Somos", size=TITLE_SIZE, weight=ft.FontWeight.BOLD, color=HEADER_COLOR),
                                ft.Text("Empresa familiar con enfoque tecnico, cercano y confiable.", size=13, color=MUTED),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                    ],
                    spacing=12,
                ),
                ft.Text(
                    "Somos una empresa familiar dedicada al control y manejo integral de plagas. "
                    "Protegemos hogares, empresas y comunidades con soluciones efectivas, responsables y personalizadas.",
                    size=13,
                    color=TEXT_COLOR,
                    text_align=ft.TextAlign.LEFT,
                ),
                bullet(ft.Icons.SHIELD, "Proteccion integral", "Cuidamos espacios con protocolos modernos y seguimiento cercano."),
                bullet(ft.Icons.SUPPORT_AGENT, "Atencion profesional", "Combinamos experiencia tecnica con trato humano y acompanamiento real."),
                ft.Row(
                    [
                        info_chip(ft.Icons.GROUP, "Origen", "Empresa familiar"),
                        info_chip(ft.Icons.VERIFIED, "Estilo", "Servicio confiable"),
                    ],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
            ],
            spacing=14,
        ),
    )

    card_empresa = make_card(
        ft.Icons.BUSINESS_CENTER,
        "Evermount Solutions",
        "Base empresarial solida, cercana y orientada a resultados.",
        [
            bullet(ft.Icons.FAMILY_RESTROOM, "Origen familiar", "Nacimos con una cultura de trabajo cercana, responsable y comprometida."),
            bullet(ft.Icons.SHIELD, "Proteccion real", "Diseñamos soluciones integrales para hogares, empresas y comunidades."),
            bullet(ft.Icons.SETTINGS_SUGGEST, "Operacion profesional", "Combinamos tecnologia, criterio tecnico y seguimiento constante."),
        ],
        [
            info_chip(ft.Icons.HOME_WORK, "Cobertura", "Hogar y empresa"),
            info_chip(ft.Icons.STARS, "Sello", "Confianza y continuidad"),
        ],
    )

    card_compromiso = make_card(
        ft.Icons.HANDSHAKE,
        "Nuestro compromiso",
        "Atencion cercana con ejecucion tecnica de alto nivel.",
        [
            bullet(ft.Icons.ENGINEERING, "Experiencia en terreno", "Actuamos con conocimiento tecnico y lectura correcta de cada escenario."),
            bullet(ft.Icons.TASK_ALT, "Respuesta responsable", "Mantenemos orden, puntualidad y claridad durante todo el servicio."),
            bullet(ft.Icons.PSYCHOLOGY, "Soluciones a medida", "Evaluamos cada caso para aplicar medidas acordes al riesgo y al entorno."),
        ],
        [
            info_chip(ft.Icons.SUPPORT_AGENT, "Atencion", "Directa y humana"),
            info_chip(ft.Icons.GPP_GOOD, "Estandar", "Seguro y profesional"),
        ],
    )

    card_diferencia = make_card(
        ft.Icons.AUTO_AWESOME,
        "Lo que nos diferencia",
        "Una propuesta de servicio clara, moderna y confiable.",
        [
            bullet(ft.Icons.SCHOOL, "Actualizacion constante", "Nos mantenemos al dia en tecnicas, procesos y buenas practicas."),
            bullet(ft.Icons.VERIFIED_USER, "Confianza en el servicio", "Cada cliente es atendido con cercania, respeto y sentido de responsabilidad."),
            bullet(ft.Icons.SCHEDULE, "Cumplimiento real", "Actuamos con transparencia, eficacia y puntualidad en cada visita."),
        ],
        [
            info_chip(ft.Icons.PUBLIC, "Enfoque", "Prevencion y control"),
            info_chip(ft.Icons.DONE_ALL, "Promesa", "Claridad y seguimiento"),
        ],
    )

    cards = [card_empresa, card_compromiso, card_diferencia]

    mobile_layout = ft.Column(
        [mobile_intro],
        spacing=14,
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
            tablet_top_holder,
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    root = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=ft.Padding.symmetric(horizontal=12, vertical=12),
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
            root.padding = ft.Padding.symmetric(horizontal=0, vertical=14)
            section_w = max(760, min(int(w * 0.94), 1040))
            card_w = int((section_w - 14) / 2)
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
            root.content = desktop_layout
            root.padding = ft.Padding.symmetric(horizontal=14, vertical=16)
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
