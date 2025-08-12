# components/intro.py
import flet as ft

def create_intro_overlay(page: ft.Page):
    imagen_logo = ft.Container(
        content=ft.Image(
            src="https://i.postimg.cc/8PvSgg5x/logo-mobile-dark.png",
            fit=ft.ImageFit.COVER,
        ),
        width=256, height=128,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.top_center,
    )

    intro = ft.Container(
        expand=True,
        visible=False,
        bgcolor=ft.Colors.BLACK54,
        alignment=ft.alignment.center,
        content=ft.Container(
            width=350, height=430,
            bgcolor=ft.Colors.WHITE,
            border_radius=10, padding=20,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("", expand=True),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                on_click=lambda e: hide_intro(),
                                icon_color=ft.Colors.BLACK,
                            ),
                        ]
                    ),
                    imagen_logo,
                    ft.Text("¡Bienvenidos!", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.Text(
                        "Aquí encontrarás todo lo referente al control de plagas profesional "
                        "navega por la página y usa los botones para contactarte.",
                        color=ft.Colors.BLACK
                    ),
                    ft.Text(
                        "Si deseas obtener más información referente a la empresa "
                        "haz clic sobre el botón ubicado en la esquina superior derecha.",
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_900
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    def show_intro():
        intro.visible = True
        page.update()

    def hide_intro():
        intro.visible = False
        page.update()

    return intro, show_intro, hide_intro
