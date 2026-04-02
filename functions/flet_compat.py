import flet as ft


def apply_flet_compat() -> None:
    alignment_aliases = {
        "center": ft.Alignment(0, 0),
        "center_left": ft.Alignment(-1, 0),
        "center_right": ft.Alignment(1, 0),
        "top_left": ft.Alignment(-1, -1),
        "top_center": ft.Alignment(0, -1),
        "top_right": ft.Alignment(1, -1),
        "bottom_center": ft.Alignment(0, 1),
        "bottom_right": ft.Alignment(1, 1),
    }

    for name, value in alignment_aliases.items():
        if not hasattr(ft.alignment, name):
            setattr(ft.alignment, name, value)

    if not hasattr(ft, "ScrollKey"):
        def _scroll_key(value: str):
            return value
        ft.ScrollKey = _scroll_key

    if not hasattr(ft, "BoxFit"):
        image_fit = getattr(ft, "ImageFit", None)
        if image_fit is not None:
            class _BoxFitCompat:
                CONTAIN = getattr(image_fit, "CONTAIN", None)
                COVER = getattr(image_fit, "COVER", None)
                FILL = getattr(image_fit, "FILL", None)
                FIT_HEIGHT = getattr(image_fit, "FIT_HEIGHT", None)
                FIT_WIDTH = getattr(image_fit, "FIT_WIDTH", None)
                NONE = getattr(image_fit, "NONE", None)
                SCALE_DOWN = getattr(image_fit, "SCALE_DOWN", None)

            ft.BoxFit = _BoxFitCompat
