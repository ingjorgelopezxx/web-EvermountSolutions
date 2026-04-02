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
        return ft.Container(
            bgcolor=chip_bg,
            border_radius=14,
            padding=ft.Padding.symmetric(horizontal=12, vertical=10),
            content=ft.Row(
                [
                    ft.Icon(icon_name, size=16, color=header_color),
                    ft.Column(
                        [
                            ft.Text(value, size=13, weight=ft.FontWeight.BOLD, color=header_color),
                            ft.Text(label, size=11, color=muted),
                        ],
                        spacing=1,
                        tight=True,
                    ),
                ],
                spacing=8,
                tight=True,
            ),
        )

    contenedor = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=20,
        border=ft.Border.all(1, "#D8E2E8"),
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        shadow=ft.BoxShadow(
            blur_radius=12,
            spread_radius=1,
            color=ft.Colors.BLACK_26,
            offset=ft.Offset(2, 4),
        ),
        width=float("inf"),
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
                                ft.Text("Historia", size=20, weight=ft.FontWeight.BOLD, color=header_color),
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
                    "Evermount Solutions nacio de la vision de dos hermanos con una meta comun: brindar un servicio de excelencia en control de plagas con etica, responsabilidad ambiental y atencion cercana.",
                ),
                bullet(
                    ft.Icons.ENGINEERING,
                    "Experiencia y vocacion",
                    "Contamos con formacion tecnica, experiencia en terreno y una vocacion clara por el servicio, combinando profesionalismo con trato personalizado.",
                ),
                bullet(
                    ft.Icons.VERIFIED_USER,
                    "Que nos diferencia",
                    "Somos una empresa certificada, en constante actualizacion, con atencion transparente, eficaz y puntual.",
                ),
                ft.Row(
                    [
                        info_chip(ft.Icons.FAMILY_RESTROOM, "Origen", "Empresa familiar"),
                        info_chip(ft.Icons.STARS, "Enfoque", "Servicio cercano"),
                    ],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
            ],
            spacing=14,
        ),
    )

    contenedor.data = {"styled": True}
    return contenedor
