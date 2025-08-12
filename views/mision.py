
import flet as ft

def build(page: ft.Page, ctx):
    return ft.Container(
        expand=True,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Misión", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Nuestra misión es brindar soluciones efectivas y responsables en control de plagas."),
            ],
        ),
    )
