import flet as ft


def apply_flet_compat() -> None:
    alignment_aliases = {
        "center": ft.Alignment(0, 0),
        "center_left": ft.Alignment(-1, 0),
        "center_right": ft.Alignment(1, 0),
        "top_left": ft.Alignment(-1, -1),
        "top_center": ft.Alignment(0, -1),
        "top_right": ft.Alignment(1, -1),
        "bottom_right": ft.Alignment(1, 1),
    }

    for name, value in alignment_aliases.items():
        if not hasattr(ft.alignment, name):
            setattr(ft.alignment, name, value)
