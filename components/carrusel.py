import asyncio
import flet as ft

IMAGENES = [
    "https://i.postimg.cc/nzZ8YggY/Chat-GPT-Image-16-sept-2025-11-00-13-p-m.png",
    "https://i.postimg.cc/D0XY9c9y/roedores.png",
    "https://i.postimg.cc/QdbnZCy5/voladores-insectos.png",
    "https://i.postimg.cc/bJ2Trw3m/termitas.png",
    "https://i.postimg.cc/hGQxb3Tj/voladores-aves.png",
    "https://i.postimg.cc/C13hWvW5/insectos-rastreros.png",
    "https://i.postimg.cc/g0bcQM1r/programas-mensuales.png",
]

def create_carrusel(page: ft.Page, intervalo: int = 3):
    idx = [0]
    activo = [False]
    tarea = [None]

    # --- Calcular ancho y altura inicial (16:9) ---
    ancho = page.width
    altura = max(200, ancho * 9 / 16)  # mínimo 200px

    # Imagen inicial
    imagen = ft.Image(
        src=IMAGENES[0],
        fit=ft.ImageFit.FILL,
        width=ancho,
        height=altura,
    )

    # Contenedor expansible
    contenedor = ft.Container(
        content=imagen,
        expand=True,
    )

    # --- Ajustar altura al redimensionar ---
    def ajustar_altura(e=None):
        ancho_nuevo = page.width
        altura_nueva = max(200, ancho_nuevo * 9 / 16)
        imagen.width = ancho_nuevo
        imagen.height = altura_nueva
        page.update()  # refresca todo

    # Conectar al evento on_resize
    page.on_resize = ajustar_altura

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

    return contenedor, start, stop
