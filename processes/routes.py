from types import SimpleNamespace

import flet as ft


def create_route_handler(
    *,
    page: ft.Page,
    contenido: ft.Column,
    render_inicio,
    ajustar_tamanos,
    kick_carruseles,
    ensure_sabiasque,
    parar_carrusel,
    scroll_content_top,
    cont_pantalla: ft.Control,
    cont_form: ft.Control,
    cerrar_menu,
    overlay_cierra_menu: ft.Control,
    service_routes: dict[str, tuple[callable, str]],
):
    def _route_handler(e: ft.RouteChangeEvent):
        route = (e.route or "/").strip()

        try:
            cerrar_menu()
            overlay_cierra_menu.visible = False
        except Exception:
            pass

        if route == "/":
            render_inicio()
            cont_pantalla.visible = True
            cont_form.visible = True
            ajustar_tamanos()
            page.run_task(kick_carruseles)
            return

        if route.startswith("/sabiasque"):
            ensure_sabiasque()
            if hasattr(page, "_sabiasque_router"):
                page._sabiasque_router(SimpleNamespace(route=route))
            else:
                if hasattr(page, "_sabiasque_show_grid"):
                    page._sabiasque_show_grid()
            return

        service_config = service_routes.get(route)
        if service_config:
            render_fn, whatsapp_message = service_config
            parar_carrusel()
            page.session.store.set("whatsapp_msg", whatsapp_message)
            render_fn(page, contenido)
            scroll_content_top()
            return

        render_inicio()

    return _route_handler
