import asyncio

import flet as ft


def create_valores(page: ft.Page):
    TITLE_SIZE = 20
    BODY_SIZE = 14
    HEADER_COLOR = "#0D2943"
    TEXT_COLOR = "#23313B"
    MUTED = "#5F6E79"
    SOFT_BG = "#F4F8FB"
    CHIP_BG = "#E6F0F5"
    CARD_H = 330

    def info_chip(icon_name: str, label: str, value: str):
        chip_value_size = 10 if (page.width or 0) <= 600 else 13
        chip_label_size = 9 if (page.width or 0) <= 600 else 11
        chip_padding_h = 10 if (page.width or 0) <= 600 else 12
        chip_padding_v = 8 if (page.width or 0) <= 600 else 10
        return ft.Container(
            bgcolor=CHIP_BG,
            border_radius=14,
            padding=ft.Padding.symmetric(horizontal=chip_padding_h, vertical=chip_padding_v),
            content=ft.Row(
                [
                    ft.Icon(icon_name, size=16, color=HEADER_COLOR),
                    ft.Column(
                        [
                            ft.Text(
                                value,
                                size=chip_value_size,
                                weight=ft.FontWeight.BOLD,
                                color=HEADER_COLOR,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                label,
                                size=chip_label_size,
                                color=MUTED,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
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

    def valor_item(icon_name: str, title: str, text: str):
        return ft.Container(
            bgcolor="#F7F9FB",
            border_radius=14,
            padding=ft.Padding.symmetric(horizontal=12, vertical=10),
            content=ft.Row(
                [
                    ft.Icon(icon_name, size=18, color=HEADER_COLOR),
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
            ),
        )

    def make_card(
        icon_name: str,
        title: str,
        summary: str,
        bullets: list[ft.Control],
        chips: list[ft.Control],
        fixed_h: int,
        chips_wrap: bool = True,
    ):
        normal_shadow = ft.BoxShadow(
            blur_radius=20,
            spread_radius=0,
            color="rgba(13,38,46,0.14)",
            offset=ft.Offset(0, 10),
        )
        detail_body = ft.Column(
            [
                ft.Column(bullets, spacing=10),
                ft.Row(
                    chips,
                    wrap=chips_wrap,
                    spacing=8,
                    run_spacing=8,
                ),
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
            height=fixed_h,
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
                    detail_body,
                ],
                spacing=14,
                expand=True,
            ),
        )
        card.data = {"detail_body": detail_body}
        return card

    mission_card = make_card(
        ft.Icons.FLAG,
        "Misión",
        "Dirección operativa clara, cercana y responsable.",
        [
            bullet(ft.Icons.HOME_WORK, "Cobertura integral", "Protegemos hogares, empresas y comunidades con soluciones adaptadas a cada contexto."),
            bullet(ft.Icons.SHIELD, "Servicio confiable", "Trabajamos con protocolos seguros, seguimiento técnico y enfoque preventivo."),
            bullet(ft.Icons.SETTINGS_SUGGEST, "Tecnología aplicada", "Integramos metodologías modernas para lograr resultados estables y sostenibles."),
        ],
        [
            info_chip(ft.Icons.GROUP, "Enfoque", "Cliente y equipo"),
            info_chip(ft.Icons.HEALTH_AND_SAFETY, "Prioridad", "Salud y seguridad"),
        ],
        CARD_H,
        chips_wrap=False,
    )

    vision_card = make_card(
        ft.Icons.VISIBILITY,
        "Visión",
        "Proyección empresarial con excelencia y sostenibilidad.",
        [
            bullet(ft.Icons.EMOJI_EVENTS, "Liderazgo regional", "Buscamos ser una referencia en control de plagas en Chile y Latinoamérica."),
            bullet(ft.Icons.AUTO_GRAPH, "Mejora continua", "Promovemos innovación constante, capacitación y evolución de procesos."),
            bullet(ft.Icons.SPA, "Gestión responsable", "Equilibramos rendimiento operativo con respeto por las personas y el entorno."),
        ],
        [
            info_chip(ft.Icons.TRENDING_UP, "Meta", "Crecimiento sostenible"),
            info_chip(ft.Icons.PSYCHOLOGY, "Motor", "Innovación continua"),
        ],
        CARD_H,
        chips_wrap=False,
    )

    difference_card = make_card(
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
        CARD_H,
    )

    values_items = ft.Column(
        [
            valor_item(ft.Icons.FAMILY_RESTROOM, "Compromiso familiar", "Tratamos cada cliente con dedicación, confianza y sentido de pertenencia."),
            valor_item(ft.Icons.TASK_ALT, "Responsabilidad", "Cumplimos lo prometido con procesos seguros y alto estándar técnico."),
            valor_item(ft.Icons.LIGHTBULB, "Innovación", "Aplicamos métodos modernos para prevenir y resolver con eficiencia."),
            valor_item(ft.Icons.HANDSHAKE, "Transparencia y cercanía", "Comunicamos con claridad, escuchamos y acompañamos todo el proceso."),
        ],
        spacing=10,
        scroll="auto",
        expand=True,
    )

    values_header_row = ft.Row(
        [
            ft.Container(
                width=42,
                height=42,
                border_radius=14,
                bgcolor=SOFT_BG,
                alignment=ft.alignment.center,
                content=ft.Icon(ft.Icons.VERIFIED, size=24, color=HEADER_COLOR),
            ),
            ft.Column(
                [
                    ft.Text("Valores", size=TITLE_SIZE, weight=ft.FontWeight.BOLD, color=HEADER_COLOR),
                    ft.Text("Cultura de trabajo orientada a confianza, claridad y resultados.", size=13, color=MUTED),
                ],
                spacing=2,
                expand=True,
            ),
        ],
        spacing=12,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    values_header_holder = ft.Container(content=values_header_row)
    values_body_holder = ft.Container(content=values_items, expand=True)

    values_card = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        border=ft.Border.all(1, "#D8E2E8"),
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=0,
            color="rgba(13,38,46,0.14)",
            offset=ft.Offset(0, 10),
        ),
        height=CARD_H,
        content=ft.Column(
            [
                ft.Container(height=4, bgcolor=HEADER_COLOR, border_radius=999),
                values_header_holder,
                values_body_holder,
            ],
            spacing=14,
            expand=True,
        ),
    )

    mobile_layout = ft.Column(
        [
            mission_card,
            vision_card,
            values_card,
        ],
        spacing=14,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    wrap_m = ft.Container(content=mission_card, width=420)
    wrap_v = ft.Container(content=vision_card, width=420)
    wrap_val = ft.Container(content=values_card, width=420)
    wrap_diff = ft.Container(content=difference_card, width=420)

    desktop_layout = ft.Row(
        controls=[wrap_m, wrap_v, wrap_val],
        spacing=18,
        wrap=False,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    tablet_top = ft.Row(
        controls=[wrap_m, wrap_v],
        spacing=14,
        wrap=False,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    tablet_top_holder = ft.Container(content=tablet_top, alignment=ft.alignment.center)
    tablet_values_row = ft.Row(
        controls=[wrap_val, wrap_diff],
        spacing=14,
        wrap=False,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )
    tablet_values_holder = ft.Container(content=tablet_values_row, alignment=ft.alignment.center)

    tablet_layout = ft.Column(
        controls=[
            tablet_top_holder,
            tablet_values_holder,
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    section_header = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "La base de nuestro servicio combina claridad operativa, mejora continua y cercanía con cada cliente.",
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

    mobile_stack = ft.Column(
        [
            section_header,
            mobile_layout,
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    tablet_stack = ft.Column(
        controls=[
            section_header,
            tablet_layout,
        ],
        spacing=18,
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
        width=float("inf"),
        padding=ft.Padding.symmetric(horizontal=10, vertical=14),
        border_radius=30,
        bgcolor="#F7FBFC",
        border=ft.Border.all(1, "#DFEAEE"),
        content=mobile_stack,
    )

    def apply_layout():
        w = page.width or 0

        if w <= 600:
            mode = "mobile"
            root.content = mobile_stack
            root.padding = ft.Padding.symmetric(horizontal=8, vertical=12)
            for wrap in (wrap_m, wrap_v, wrap_val):
                wrap.expand = None
                wrap.width = None
            mission_card.data["detail_body"].scroll = None
            mission_card.data["detail_body"].expand = False
            vision_card.data["detail_body"].scroll = None
            vision_card.data["detail_body"].expand = False
            values_items.scroll = None
            values_items.expand = False
            mission_card.height = None
            vision_card.height = None
            values_card.height = None
        elif w < 1100:
            mode = "tablet"
            root.content = tablet_stack
            root.padding = ft.Padding.symmetric(horizontal=6, vertical=16)
            section_w = min(int(w * 0.84), 980)
            small_w = max(200, int((section_w - 10) / 2))
            tablet_top.spacing = 10
            tablet_values_row.spacing = 10
            wrap_m.expand = None
            wrap_v.expand = None
            wrap_val.expand = None
            wrap_diff.expand = None
            wrap_m.width = small_w
            wrap_v.width = small_w
            wrap_val.width = small_w
            wrap_diff.width = small_w
            tablet_top_holder.width = section_w
            tablet_values_holder.width = section_w
            mission_card.height = 360
            vision_card.height = 360
            values_card.height = 360
            difference_card.height = 360
            mission_card.data["detail_body"].scroll = "auto"
            mission_card.data["detail_body"].expand = True
            vision_card.data["detail_body"].scroll = "auto"
            vision_card.data["detail_body"].expand = True
            values_items.scroll = "auto"
            values_items.expand = True
            values_header_holder.content = values_header_row
            values_body_holder.content = values_items
        else:
            mode = "desktop"
            root.content = desktop_stack
            root.padding = ft.Padding.symmetric(horizontal=14, vertical=18)
            for wrap in (wrap_m, wrap_v, wrap_val):
                wrap.width = None
                wrap.expand = 1
            mission_card.height = CARD_H
            vision_card.height = CARD_H
            values_card.height = CARD_H
            mission_card.data["detail_body"].scroll = "auto"
            mission_card.data["detail_body"].expand = True
            vision_card.data["detail_body"].scroll = "auto"
            vision_card.data["detail_body"].expand = True
            values_items.scroll = "auto"
            values_items.expand = True
            difference_card.height = CARD_H
            values_header_holder.content = values_header_row
            values_body_holder.content = values_items

        if mode == "mobile":
            difference_card.height = None
            values_header_holder.content = values_header_row
            values_body_holder.content = values_items

        if getattr(root, "page", None) is not None:
            root.update()

    root.data = {
        "apply_layout": apply_layout,
    }

    return root




