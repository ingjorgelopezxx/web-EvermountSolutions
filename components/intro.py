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

    # Tarjeta del modal (clicks aquí NO cierran el modal)
    modal_card = ft.Container(
        width=350,
        height=430,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        padding=20,
        on_click=lambda e: None,  # "consume" el click para que no cierre el overlay
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
            spacing=12,
        ),
    )

    # Overlay de pantalla completa (posición absoluta en Stack)
    intro = ft.Container(
        left=0, top=0, right=0, bottom=0,     # 👈 ocupa todo el viewport dentro del Stack
        visible=False,
        bgcolor=ft.Colors.BLACK54,            # fondo semitransparente
        alignment=ft.alignment.center,
        on_click=lambda e: hide_intro(),      # clic fuera de la tarjeta cierra
        content=modal_card,
    )

    def show_intro():
        intro.visible = True
        page.update()

    def hide_intro():
        intro.visible = False
        page.update()

    return intro, show_intro, hide_intro
