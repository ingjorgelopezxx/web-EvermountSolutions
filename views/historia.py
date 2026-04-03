import flet as ft


def create_historia(page: ft.Page):
    header_color = "#0D2943"
    text_color = "#23313B"
    muted = "#5F6E79"
    soft_bg = "#F4F8FB"
    chip_bg = "#E6F0F5"

    def bullet(icon_name: str, title: str, text: str):
        return ft.Row(
            [
                ft.Container(
                    width=28,
                    height=28,
                    border_radius=14,
                    bgcolor=chip_bg,
                    alignment=ft.alignment.center,
                    content=ft.Icon(icon_name, size=15, color=header_color),
                ),
                ft.Column(
                    [
                        ft.Text(title, size=13, weight=ft.FontWeight.BOLD, color=header_color),
                        ft.Text(text, size=12, color=text_color, text_align=ft.TextAlign.LEFT),
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
            bgcolor=chip_bg,
            border_radius=14,
            padding=ft.Padding.symmetric(horizontal=10 if (page.width or 0) <= 600 else 12, vertical=8 if (page.width or 0) <= 600 else 10),
            content=ft.Row(
                [
                    ft.Icon(icon_name, size=16, color=header_color),
                    ft.Column(
                        [
                            ft.Text(value, size=chip_value_size, weight=ft.FontWeight.BOLD, color=header_color, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text(label, size=chip_label_size, color=muted, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
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

    contenedor = ft.Container(
        bgcolor="#F7FBFC",
        border_radius=30,
        border=ft.Border.all(1, "#DFEAEE"),
        padding=ft.Padding.symmetric(horizontal=14, vertical=14),
        width=float("inf"),
        content=ft.Column(
            [
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [
                            ft.Text(
                                "Un proyecto familiar construido desde la confianza, el trabajo en equipo y la vocación de servicio.",
                                size=13,
                                color=muted,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        spacing=8,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    border_radius=22,
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
                            ft.Container(height=4, bgcolor=header_color, border_radius=999),
                            ft.Row(
                                [
                                    ft.Container(
                                        width=42,
                                        height=42,
                                        border_radius=14,
                                        bgcolor=soft_bg,
                                        alignment=ft.alignment.center,
                                        content=ft.Icon(ft.Icons.HISTORY_EDU, size=24, color=header_color),
                                    ),
                                    ft.Column(
                                        [
                                            ft.Text("Historia de la empresa", size=20, weight=ft.FontWeight.BOLD, color=header_color),
                                            ft.Text("Origen familiar, trabajo en equipo y una forma cercana de servir.", size=13, color=muted),
                                        ],
                                        spacing=2,
                                        expand=True,
                                    ),
                                ],
                                spacing=12,
                                vertical_alignment=ft.CrossAxisAlignment.START,
                            ),
                            bullet(
                                ft.Icons.GROUP,
                                "Compromiso y trabajo en equipo",
                                "Evermount Solutions nació de la visión de dos hermanos con una meta común: brindar un servicio de excelencia en control de plagas con ética, responsabilidad ambiental y atención cercana.",
                            ),
                            bullet(
                                ft.Icons.ENGINEERING,
                                "Experiencia y vocación",
                                "Contamos con formación técnica, experiencia en terreno y una vocación clara por el servicio, combinando profesionalismo con trato personalizado.",
                            ),
                            bullet(
                                ft.Icons.VERIFIED_USER,
                                "Qué nos diferencia",
                                "Somos una empresa certificada, en constante actualización, con atención transparente, eficaz y puntual.",
                            ),
                            ft.Row(
                                [
                                    info_chip(ft.Icons.FAMILY_RESTROOM, "Origen", "Empresa familiar"),
                                    info_chip(ft.Icons.STARS, "Enfoque", "Servicio cercano"),
                                ],
                                wrap=False,
                                spacing=8,
                            ),
                        ],
                        spacing=14,
                    ),
                ),
            ],
            spacing=18,
        ),
    )

    contenedor.data = {"styled": True}
    return contenedor

