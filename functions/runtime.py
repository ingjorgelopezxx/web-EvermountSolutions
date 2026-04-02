import os
import flet as ft

from functions.flet_compat import apply_flet_compat


def run_web_app() -> None:
    apply_flet_compat()

    from processes.web_app import main as web_main

    app_view = getattr(ft, "AppView", None)
    web_view = getattr(app_view, "WEB_BROWSER", None) if app_view else getattr(ft, "WEB_BROWSER", None)

    ft.app(
        target=web_main,
        view=web_view,
        port=int(os.environ.get("PORT", 8080)),
        assets_dir="assets",
    )