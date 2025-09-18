import flet as ft
import re

ALTURA_CAMPOS = 56

def validar_correo(email: str) -> bool:
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email) is not None

def main(page: ft.Page):
    page.title = "Prueba AlertDialog"

    # --- definimos el AlertDialog ---
    dialogo_alerta = ft.AlertDialog(
        modal=True,
        title=ft.Text("Correo inválido"),
        content=ft.Text("Por favor ingresa un correo con formato correcto."),
        actions=[ft.TextButton("Cerrar", on_click=lambda e: cerrar_dialogo())],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def mostrar_dialogo():
        page.dialog = dialogo_alerta   # 👈 asignar a page.dialog
        dialogo_alerta.open = True
        page.update()

    def cerrar_dialogo():
        dialogo_alerta.open = False
        page.update()

    # --- icono de advertencia ---
    warning_icon = ft.IconButton(
        icon=ft.Icons.WARNING_AMBER_ROUNDED,
        icon_color=ft.Colors.RED,
        icon_size=20,
        visible=False,
        tooltip="Correo electrónico inválido",
        style=ft.ButtonStyle(
            padding=ft.padding.all(0),
            shape=ft.RoundedRectangleBorder(radius=0)
        ),
        width=40,
        height=ALTURA_CAMPOS,
        on_click=lambda e: mostrar_dialogo()  # 👈 abrir el dialogo
    )

    # --- TextField con suffix ---
    correo_tf = ft.TextField(
        label="Correo electrónico",
        color=ft.Colors.BLACK,
        width=350,
        height=ALTURA_CAMPOS,
        suffix=warning_icon
    )

    # --- Validar en vivo ---
    def validar_correo_en_tiempo_real(e):
        v = (correo_tf.value or "").strip()
        warning_icon.visible = (v != "" and not validar_correo(v))
        page.update()

    correo_tf.on_change = validar_correo_en_tiempo_real

    nombre = ft.TextField(label="Nombre", width=350, color=ft.Colors.BLACK, height=ALTURA_CAMPOS)
    telefono = ft.TextField(label="Teléfono", width=350, color=ft.Colors.BLACK, height=ALTURA_CAMPOS)

    page.add(
        ft.Column(
            [
                ft.Text("Contáctanos", size=28, weight=ft.FontWeight.BOLD, color="#090229"),
                nombre,
                correo_tf,
                telefono,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

ft.app(target=main)
