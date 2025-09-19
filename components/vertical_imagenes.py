import flet as ft
import asyncio

# Lista de imágenes (puedes cambiar o pasar como argumento)
IMAGENES = [
    "https://i.postimg.cc/15nLZNp7/imagen1.jpg",
    "https://i.postimg.cc/RZwyW5pc/imagen2.jpg",
    "https://i.postimg.cc/BvgzC50b/imagen3.jpg",
    "https://i.postimg.cc/FRCnM91Q/imagen4.jpg",
]

def create_vertical_carousel(page: ft.Page, intervalo=3):
    """
    Carrusel vertical de imágenes en tarjetas.
    Retorna (carrusel_control, start_carousel, stop_carousel)
    """

    # Índice actual
    idx = [0]
    activo = [False]
    tarea = [None]

    # Imagen principal dentro de tarjeta
    imagen = ft.Image(
        src=IMAGENES[idx[0]],
        fit=ft.ImageFit.COVER,
        width=250,
        height=350,
        border_radius=ft.border_radius.all(12)
    )

    # Tarjeta vertical conteniendo la imagen
    tarjeta = ft.Container(
        content=imagen,
        width=250,
        height=350,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        alignment=ft.alignment.center,
    )

    # Contenedor principal del carrusel
    carrusel_control = ft.Container(
        content=tarjeta,
        alignment=ft.alignment.center,
        padding=10
    )

    # --- Rotación automática ---
    async def _rotar():
        try:
            while activo[0]:
                imagen.src = IMAGENES[idx[0] % len(IMAGENES)]
                page.update()
                idx[0] = (idx[0] + 1) % len(IMAGENES)
                await asyncio.sleep(intervalo)
        except asyncio.CancelledError:
            pass

    def start():
        if tarea[0] is None:
            activo[0] = True
            tarea[0] = page.run_task(_rotar)

    def stop():
        activo[0] = False
        if tarea[0] is not None:
            tarea[0].cancel()
            tarea[0] = None

    return carrusel_control, start, stop
