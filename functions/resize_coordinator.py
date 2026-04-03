from __future__ import annotations

from collections import OrderedDict
from typing import Callable

import flet as ft


ResizeHandler = Callable[[object | None], None]


def _ensure_resize_dispatcher(page: ft.Page) -> OrderedDict[str, ResizeHandler]:
    registry = getattr(page, "_resize_handler_registry", None)
    if registry is not None:
        return registry

    registry = OrderedDict()
    previous_handler = getattr(page, "on_resized", None)

    def _dispatch_resize(event):
        for handler in list(registry.values()):
            try:
                handler(event)
            except Exception:
                pass

        if callable(previous_handler) and previous_handler is not _dispatch_resize:
            try:
                previous_handler(event)
            except Exception:
                pass

    page._resize_handler_registry = registry
    page._resize_dispatcher = _dispatch_resize
    page._resize_previous_handler = previous_handler
    page.on_resized = _dispatch_resize
    return registry


def register_resize_handler(page: ft.Page, key: str, handler: ResizeHandler) -> None:
    registry = _ensure_resize_dispatcher(page)
    registry[key] = handler


def unregister_resize_handler(page: ft.Page, key: str) -> None:
    registry = getattr(page, "_resize_handler_registry", None)
    if registry is None:
        return
    registry.pop(key, None)


def trigger_registered_resize(page: ft.Page, event=None) -> None:
    dispatcher = getattr(page, "_resize_dispatcher", None)
    if callable(dispatcher):
        dispatcher(event)
