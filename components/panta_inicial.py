# panta_inicial.py
import flet as ft
from components.carrusel import create_carrusel  # 👈 importa tu carrusel

def get_pantalla_inicial(page: ft.Page):
    """
    Retorna un contenedor con:
    - Fila de íconos con acciones (llamada, correo, ubicación)
    - Carrusel de imágenes debajo
    """

    # --- Carrusel ---
    carrusel, start_carrusel, stop_carrusel = create_carrusel(page, intervalo=3)


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
                        ft.Text("+56999724454", **texto_style)
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
    )

    # --- Columna completa ---
    contenedor = ft.Column(
        [
            ft.Container(
                content=fila_iconos,
                padding=ft.padding.only(left=10, right=20, top=10, bottom=10),
                bgcolor=None,
            ),
            carrusel   # 👈 carrusel debajo de la fila de iconos
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    # 👇 Devuelvo también funciones del carrusel por si quieres controlarlo desde main
    return contenedor, start_carrusel, stop_carrusel

