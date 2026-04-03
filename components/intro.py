import flet as ft

from functions.asset_sources import INTRO_LOGO


def create_intro_overlay(page: ft.Page):
    def texto_info_actual() -> str:
        if (page.width or 0) >= 600:
            return (
                "Si deseas obtener más información referente a la empresa, "
                "haz clic en las pestañas ubicadas en la parte superior izquierda."
            )
        return (
            "Si deseas obtener más información referente a la empresa, "
            "haz clic sobre el menú ubicado en la esquina superior derecha."
        )

    imagen_logo = ft.Container(
        content=ft.Image(
            src=INTRO_LOGO,
            fit=ft.BoxFit.COVER,
        ),
        width=256,
        height=128,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.top_center,
    )

    texto_info = ft.Text(
        texto_info_actual(),
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_900,
        text_align=ft.TextAlign.CENTER,
    )

    modal_card = ft.Container(
        width=350,
        height=430,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=20,
        on_click=lambda e: None,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("", expand=True),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.BLACK,
                            on_click=lambda e: hide_intro(),
                        ),
                    ]
                ),
                imagen_logo,
                ft.Text(
                    "¡Bienvenidos!",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(
                    "Aquí encontrarás todo lo referente al control profesional de plagas. "
                    "Navega por la página y usa los botones para contactarte.",
                    color=ft.Colors.BLACK,
                    text_align=ft.TextAlign.CENTER,
                ),
                texto_info,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        ),
    )

    intro = ft.Container(
        left=0,
        top=0,
        right=0,
        bottom=0,
        visible=False,
        bgcolor=ft.Colors.BLACK_54,
        alignment=ft.alignment.center,
        on_click=lambda e: hide_intro(),
        content=modal_card,
    )

    def show_intro():
        texto_info.value = texto_info_actual()
        intro.visible = True
        page.update()

    def hide_intro():
        intro.visible = False
        page.update()

    return intro, show_intro, hide_intro
