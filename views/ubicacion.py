
import flet as ft

def build(page: ft.Page, ctx):
    # Vista simple con texto de ubicación
    return ft.Container(
        expand=True,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Ubicación", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text("Av. Siempre Viva 742, Santiago", color=ft.Colors.BLACK87),
            ],
        ),
    )
