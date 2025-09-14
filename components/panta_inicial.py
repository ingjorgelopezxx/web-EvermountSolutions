# panta_inicial.py
import flet as ft

def get_pantalla_inicial(page: ft.Page):
    """
    Retorna un contenedor con fila de íconos y textos:
    - Llamada (abre la app de teléfono con número cargado)
    - Correo (abre cliente de correo)
    - Ubicación (abre Google Maps)
    con texto a la derecha de cada ícono, alineados a la derecha.
    """

    # Datos de contacto (ajusta a tus necesidades)
    numero_telefono = "+56999724454"   # 👈 este es el número que se marcará
    enlace_llamada = f"tel:{numero_telefono}"  # 👈 esquema tel para abrir marcador
    enlace_correo = "mailto:info@evermountsolutions.cl?subject=Consulta&body=Hola, quisiera más información"
    enlace_ubicacion = "https://maps.google.com/?q=EvermountSolutions+Chile"  # ajusta con tu dirección real

    # Estilo para los textos
    texto_style = dict(size=14, weight=ft.FontWeight.W_600, color=ft.Colors.BLACK)

    # Funciones para abrir links
    def abrir_llamada(e):
        page.launch_url(enlace_llamada)  # abrir marcador telefónico en móviles

    def abrir_correo(e):
        page.launch_url(enlace_correo)

    def abrir_maps(e):
        page.launch_url(enlace_ubicacion)

    fila = ft.Row(
        [
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.PHONE, color=ft.Colors.BLUE, size=24),
                        ft.Text("Llamada", **texto_style)
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
                on_click=abrir_llamada,  # 👈 acción al hacer clic
                ink=True,
                padding=5
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREEN, size=24),
                        ft.Text("Correo", **texto_style)
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
                on_click=abrir_correo,  # 👈 acción al hacer clic
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
                on_click=abrir_maps,  # 👈 acción al hacer clic
                ink=True,
                padding=5
            ),
        ],
        alignment=ft.MainAxisAlignment.END,   # 👈 todo hacia la derecha
        spacing=20,
    )

    contenedor = ft.Container(
        content=fila,
        padding=ft.padding.only(left=10, right=20, top=10, bottom=10),
        bgcolor=None,
        border_radius=0,
    )

    return contenedor
