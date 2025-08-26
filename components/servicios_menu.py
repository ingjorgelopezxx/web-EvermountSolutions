# components/menu_servicios.py
import flet as ft

SERVICIOS = [
    {"titulo": "Roedores", "imagen": "https://i.postimg.cc/4NLHX4nH/Chat-GPT-Image-26-ago-2025-03-08-53-p-m.png"},
    {"titulo": "Desinfección y Sanitización Ambientes", "imagen": "https://i.postimg.cc/Kc6FhdDr/Chat-GPT-Image-26-ago-2025-03-32-59-p-m.png"},
    {"titulo": "Insectos Voladores", "imagen": "https://i.postimg.cc/zvkh5JW3/Chat-GPT-Image-26-ago-2025-02-22-27-p-m.jpg"},
    {"titulo": "Insectos Rastreros", "imagen": "https://i.postimg.cc/D0zscS8F/Chat-GPT-Image-26-ago-2025-03-18-37-p-m.png"},
    {"titulo": "Tratamiento Termitas", "imagen": "https://i.postimg.cc/3JTQW24P/Chat-GPT-Image-26-ago-2025-03-13-04-p-m.png"},
    {"titulo": "Aves Urbanas", "imagen": "https://i.postimg.cc/HnWjCFgt/Chat-GPT-Image-26-ago-2025-03-09-31-p-m.png"},
]

def render_menu_servicios(page: ft.Page, contenedor: ft.Column):
    """Renderiza un menú de servicios con tarjetas de altura uniforme."""

    # Breakpoints → métricas de grid, proporciones y texto
    def _sizes():
        w = page.width or 800
        if w < 480:              # 📱 móvil
            return dict(max_extent=160, aspect=0.70, spacing=6, run_spacing=8, title_sz=12)
        elif w < 900:            # 📲 tablet
            return dict(max_extent=200, aspect=0.78, spacing=10, run_spacing=12, title_sz=14)
        else:                    # 💻 PC
            return dict(max_extent=260, aspect=0.86, spacing=12, run_spacing=14, title_sz=16)

    def _snack(msg: str):
        page.snack_bar = ft.SnackBar(content=ft.Text(msg))
        page.snack_bar.open = True
        page.update()

    def _card(item: dict, title_size: int) -> ft.Container:
        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
            ink=True,
            on_click=lambda e: _snack(f"Seleccionaste {item['titulo']}"),
            content=ft.Column(
                expand=True,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    # Imagen ocupa siempre la parte superior
                    ft.Container(
                        expand=3,  # proporción flexible
                        alignment=ft.alignment.center,
                        content=ft.Image(src=item["imagen"], fit=ft.ImageFit.COVER),
                    ),
                    # Texto ocupa siempre la parte inferior
                    ft.Container(
                        expand=1,
                        alignment=ft.alignment.center,
                        padding=ft.padding.symmetric(horizontal=6, vertical=8),
                        content=ft.Text(
                            item["titulo"],
                            size=title_size,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=2,  # 🔑 garantiza altura uniforme
                            overflow=ft.TextOverflow.ELLIPSIS,
                            color=ft.Colors.BLACK,
                        ),
                    ),
                ],
            ),
        )

    # Construye / reconstruye el grid
    def _build_grid():
        sz = _sizes()
        grid.max_extent = sz["max_extent"]
        grid.child_aspect_ratio = sz["aspect"]
        grid.spacing = sz["spacing"]
        grid.run_spacing = sz["run_spacing"]
        grid.controls.clear()
        for it in SERVICIOS:
            grid.controls.append(_card(it, sz["title_sz"]))
        grid.update()

    # Grid base
    grid = ft.GridView(expand=True)

    # Montaje
    contenedor.controls.clear()
    contenedor.controls.append(grid)
    contenedor.update()

    _build_grid()

    # Responsivo en tiempo real
    def _on_resize(e):
        _build_grid()

    page.on_resize = _on_resize
