
import flet as ft

def build(page: ft.Page, ctx):
    numero_whatsapp = "+56937539304"
    return ft.Container(
        expand=True,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Contactos", size=24, weight=ft.FontWeight.BOLD),
                ft.Text(f"WhatsApp: {numero_whatsapp}"),
                ft.Text("Instagram: @evermountsolutions"),
                ft.Text("Facebook: /evermountsolutions"),
            ],
        ),
    )
