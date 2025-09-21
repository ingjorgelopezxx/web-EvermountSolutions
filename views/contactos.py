# components/contactos.py
import flet as ft

def create_contactos_row(page: ft.Page) -> ft.Container:
    """
    Devuelve la fila de iconos de contacto.
    """

    # --- Datos de contacto ---
    numero_telefono = "+56999724454"
    enlace_llamada = f"tel:{numero_telefono}"
    enlace_correo = "mailto:operaciones@evermountsolutions.cl?subject=Consulta&body=Hola, quisiera más información"
    enlace_ubicacion = "https://maps.google.com/?q=EvermountSolutions+Chile"

    texto_style = dict(size=14, weight=ft.FontWeight.W_600, color=ft.Colors.BLACK)

    def abrir_llamada(e):
        page.launch_url(enlace_llamada)

    def abrir_correo(e):
        page.launch_url(enlace_correo)

    def abrir_maps(e):
        page.launch_url(enlace_ubicacion)

    # --- Fila de iconos ---
    fila_iconos = ft.Row(
        [
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.PHONE, color=ft.Colors.BLUE, size=24),
                        ft.Text(numero_telefono, **texto_style)
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
                on_click=abrir_llamada,
                ink=True,
                padding=5
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREEN, size=24),
                        ft.Text("E-Mail", **texto_style)
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
                on_click=abrir_correo,
                ink=True,
                padding=5
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED, size=24),
                        ft.Text("Ubicación", **texto_style)
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
                on_click=abrir_maps,
                ink=True,
                padding=5
            ),
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=20,
        key="fila_iconos"  # 👈 clave única para scroll_to
    )

    return fila_iconos
