# components/slides.py
import flet as ft
import asyncio

def create_slides_controller(
    page: ft.Page,
    contenido: ft.Column,
    construir_contenido_slide_insectos,  # función del módulo insectos
    mostrar_info_insecto,                # callback para abrir diálogo info
    start_anim_insectos,                 # inicia anim de iconos (devuelve task)
    stop_anim_insectos,                  # detiene anim de iconos
    on_enter_slides=None,                # callback opcional para parar carrusel u otros
):
    """
    Devuelve: set_slides, mostrar_slide, navegar_slide, get_index
    - set_slides(slides_list): establece la lista de slides activa
    - mostrar_slide(idx): renderiza el slide idx
    - navegar_slide(nuevo_idx): navega a un índice y renderiza
    - get_index(): devuelve el índice actual
    """

    state = {
        "slides": [],
        "idx": 0,
        "anim_task": None,  # animación de iconos insectos
    }

    def _stop_insectos_anim():
        # Detiene animación previa si existe
        stop_anim_insectos()
        if state["anim_task"]:
            try:
                state["anim_task"].cancel()
            except Exception:
                pass
            state["anim_task"] = None

    def set_slides(slides_list):
        state["slides"] = slides_list or []
        state["idx"] = 0

    def get_index():
        return state["idx"]

    def mostrar_slide(idx: int):
        # Si hay callback (p. ej. parar carrusel), ejecútalo
        if callable(on_enter_slides):
            on_enter_slides()

        if not state["slides"]:
            return

        idx = max(0, min(idx, len(state["slides"]) - 1))
        state["idx"] = idx
        slide = state["slides"][idx]

        # limpiar y preparar
        contenido.controls.clear()
        _stop_insectos_anim()

        flecha_ancho = 46
        ancho_card = min(
            int(page.width - flecha_ancho * 2 - 12),
            430 if page.width > 600 else 340
        )
        size_titulo = 18 if page.width < 400 else 24
        size_parrafo = 14 if page.width < 400 else 16

        # Gestos para swipe
        pan_dx = [0]
        def on_pan_start(e): pan_dx[0] = 0
        def on_pan_update(e): pan_dx[0] += e.delta_x
        def on_pan_end(e):
            if pan_dx[0] < -50 and state["idx"] < len(state["slides"]) - 1:
                navegar_slide(state["idx"] + 1)
            elif pan_dx[0] > 50 and state["idx"] > 0:
                navegar_slide(state["idx"] - 1)
            pan_dx[0] = 0

        # Cabecera del slide
        contenido_slide = [
            ft.Container(
                content=ft.Text(
                    slide["titulo"],
                    size=size_titulo,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=["#0f2027", "#203a43", "#2c5364"],
                ),
                padding=ft.padding.symmetric(vertical=8, horizontal=10),
                border_radius=8,
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=8),
            ),
        ]

        # Cuerpo con textos/íconos insectos
        controles, imagenes_animadas = construir_contenido_slide_insectos(
            slide,
            mostrar_info_insecto,
            size_parrafo=size_parrafo,
        )
        contenido_slide.extend(controles)

        # Altura de la card
        max_card_height = int(page.height * (0.66 if page.width < 600 else 0.80))
        if max_card_height < 220:
            max_card_height = 220

        contenido_slide_column = ft.Column(
            controls=contenido_slide,
            alignment=ft.MainAxisAlignment.START,
            spacing=16,
            scroll="auto",
            height=max_card_height,
        )

        card = ft.Container(
            width=ancho_card,
            padding=ft.padding.symmetric(
                vertical=18,
                horizontal=8 if page.width < 400 else 18
            ),
            bgcolor=ft.Colors.WHITE,
            border_radius=16,
            border=ft.border.all(2, ft.Colors.BLACK),
            content=contenido_slide_column,
            alignment=ft.alignment.center,
        )

        gesture_card = ft.GestureDetector(
            content=card,
            on_pan_start=on_pan_start,
            on_pan_update=on_pan_update,
            on_pan_end=on_pan_end,
        )

        # Flechas
        arrow_left = (
            ft.IconButton(
                icon=ft.Icons.ARROW_LEFT,
                icon_color=ft.Colors.BLUE_700,
                icon_size=30,
                on_click=lambda e: navegar_slide(state["idx"] - 1),
            )
            if state["idx"] > 0
            else ft.Container(width=flecha_ancho)
        )

        arrow_right = (
            ft.IconButton(
                icon=ft.Icons.ARROW_RIGHT,
                icon_color=ft.Colors.BLUE_700,
                icon_size=30,
                on_click=lambda e: navegar_slide(state["idx"] + 1),
            )
            if state["idx"] < len(state["slides"]) - 1
            else ft.Container(width=flecha_ancho)
        )
        
        contenido.controls.append(
            ft.Row(
                [
                    ft.Container(arrow_left, alignment=ft.alignment.center, width=flecha_ancho),
                    ft.Container(gesture_card, alignment=ft.alignment.center, expand=True),
                    ft.Container(arrow_right, alignment=ft.alignment.center, width=flecha_ancho),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=False,
            )
        )
        contenido.update()

        # arrancar animación de iconos si corresponde
        if imagenes_animadas:
            state["anim_task"] = start_anim_insectos(imagenes_animadas)

    def navegar_slide(nuevo_idx: int):
        mostrar_slide(nuevo_idx)

    return set_slides, mostrar_slide, navegar_slide, get_index
