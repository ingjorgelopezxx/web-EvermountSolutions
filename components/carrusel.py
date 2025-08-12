# components/carrusel.py
import asyncio
import flet as ft

# --- Sets de imágenes por defecto (puedes editarlos aquí) ---
DEFAULT_IMAGE_SETS = [
    [
        "https://irp.cdn-website.com/fe74ab3f/dms3rep/multi/3-c76791a1.jpg",
        "https://inoclean.cl/wp-content/uploads/2021/12/Plagas.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXeZ7ElGw51_JF6TZuylsCHQcXd-e_GyV7mA&s",
    ],
    [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxriBp7gAvC3DeO0ZsaDqinL-7dZCJ_ulUmx_B3ad-QOo911PD0nwmsyZFBF3dK_bTzsw&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTimFMgOc-bNR1xeYjxD__RbzP0LApis-ovRuggm-TM0CPZl6OBeSj8TCc3Ph1sYVIjhcg&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAF2blxqmgt_0N7htQAMCDfn8thMHzWPy0z9a7_tdSsSgxDzYD9GiinavAWy8CpM7Ndl0&usqp=CAU",
    ],
]

def create_carrusel(page: ft.Page, tam: int = 3, sets=None):
    """
    Crea un carrusel con 'tam' imágenes visibles.

    - Si 'sets' es None, usa DEFAULT_IMAGE_SETS.
    - Devuelve: (fila_carrusel, set_sets_imagenes, start, stop, set_first_set)
    """
    # Estado interno
    _sets = [*(sets or DEFAULT_IMAGE_SETS)]
    _idx = [0]
    _task = [None]
    _active = [False]

    imagenes_visibles = [
        ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8)
        for _ in range(tam)
    ]

    fila_carrusel = ft.Row(
        controls=imagenes_visibles,
        scroll="always",
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def _apply_set(i: int):
        if not _sets or not _sets[0]:
            return
          # si la fila NO está montada, abortar silenciosamente
        if fila_carrusel.page is None:
            return
        set_imgs = _sets[i]
        for pos, img in enumerate(imagenes_visibles):
            img.src = set_imgs[pos % len(set_imgs)]
        fila_carrusel.update()   

    async def _apply_set_safe_async():
         # da un tick al loop para asegurar montaje
        await asyncio.sleep(0)
        _apply_set(_idx[0])

    def set_sets_imagenes(new_sets):
        """Reemplaza los sets del carrusel en caliente."""
        if not isinstance(new_sets, list) or len(new_sets) == 0:
            raise ValueError("new_sets debe ser una lista de listas con al menos un set.")
        _sets.clear()
        _sets.extend(new_sets)
        _idx[0] = 0

    def set_first_set():
         # ejecución diferida para evitar AssertionError al primer render
        page.run_task(_apply_set_safe_async)
        
    async def _rotar():
            try:
                while _active[0]:
                    await _apply_set_safe_async()
                    await asyncio.sleep(3)
                    if _sets and _sets[0]:
                        _idx[0] = (_idx[0] + 1) % len(_sets)
            except asyncio.CancelledError:
                pass

    def start():
            if _task[0] is not None:
                return _task[0]
            _active[0] = True
            _task[0] = page.run_task(_rotar)
            return _task[0]

    def stop():
            _active[0] = False
            if _task[0] is not None:
                try:
                    _task[0].cancel()
                finally:
                    _task[0] = None

    def set_sets_imagenes(new_sets):
            if not isinstance(new_sets, list) or not new_sets:
                raise ValueError("new_sets debe ser lista de listas con al menos un set.")
            _sets.clear()
            _sets.extend(new_sets)
            _idx[0] = 0

    return fila_carrusel, set_sets_imagenes, start, stop, set_first_set
