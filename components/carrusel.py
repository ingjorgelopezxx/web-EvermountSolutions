import asyncio
import flet as ft
from functions.asset_sources import CARRUSEL_HOME_IMAGES
from functions.resize_coordinator import register_resize_handler

IMAGENES = [
    *CARRUSEL_HOME_IMAGES,
]

def create_carrusel(page: ft.Page, intervalo: int = 3):
    idx = [0]
    activo = [False]
    tarea_rotacion = [None]
    tarea_resize = [None]  # debounce

    # --- Breakpoints ---
    def get_device_class() -> str:
        w = page.width or 0
        if w < 600:
            return "mobile"
        elif w < 1020:
            return "tablet"
        return "desktop"

    def compute_size():
        w = page.width or 360
        cls = get_device_class()
        if cls == "mobile":
            h_min, h_max = 200, 420
        elif cls == "tablet":
            h_min, h_max = 280, 540
        else:
            h_min, h_max = 200, 420
        h_calc = (w * 9) / 16
        h = max(h_min, min(h_calc, h_max))
        return w, h

    w0, h0 = compute_size()
    imagen = ft.Image(
        src=IMAGENES[0],
        fit=ft.BoxFit.FILL,
        width=w0,
        height=h0,
    )
    contenedor = ft.Container(
        content=imagen,
        expand=False,
        width=w0,
        height=h0,
    )

    # --- Resize con debounce ---
    async def _resize_debounced():
        try:
            await asyncio.sleep(0.06)

            # si no está montado, no hacemos nada
            if getattr(contenedor, "page", None) is None or getattr(imagen, "page", None) is None:
                return

            w, h = compute_size()
            imagen.width = w
            imagen.height = h
            contenedor.width = w
            contenedor.height = h

            # re-check justo antes de update (evita carreras)
            if getattr(contenedor, "page", None) is None:
                return

            try:
                contenedor.update()
            except AssertionError:
                return

        except asyncio.CancelledError:
            return
        except Exception:
            return

    def _on_resize_local(e=None):
        if tarea_resize[0] is not None:
            try:
                tarea_resize[0].cancel()
            except Exception:
                pass
            finally:
                tarea_resize[0] = None
        tarea_resize[0] = page.run_task(_resize_debounced)

    register_resize_handler(page, "home_carrusel", _on_resize_local)

    # --- Rotación automática ---
    async def _rotar():
        try:
            while activo[0]:
                if getattr(imagen, "page", None) is not None:
                    imagen.src = IMAGENES[idx[0] % len(IMAGENES)]
                    try:
                        imagen.update()
                    except AssertionError:
                        return
                    idx[0] = (idx[0] + 1) % len(IMAGENES)
                await asyncio.sleep(intervalo)
        except asyncio.CancelledError:
            pass

    def start_carrusel():
        page.run_task(_resize_debounced)
        if tarea_rotacion[0] is None:
            activo[0] = True
            tarea_rotacion[0] = page.run_task(_rotar)

    def stop_carrusel():
        activo[0] = False

        if tarea_rotacion[0] is not None:
            try:
                tarea_rotacion[0].cancel()
            except Exception:
                pass
            finally:
                tarea_rotacion[0] = None

        # ✅ cancelar debounce resize también
        if tarea_resize[0] is not None:
            try:
                tarea_resize[0].cancel()
            except Exception:
                pass
            finally:
                tarea_resize[0] = None

    # Primer ajuste (seguro)
    page.run_task(_resize_debounced)

    return contenedor, start_carrusel, stop_carrusel
