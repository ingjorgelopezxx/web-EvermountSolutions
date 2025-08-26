# components/menu_servicios.py
import math
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
    """
    Menú de servicios responsivo con GridView (compatible con Flet sin Wrap/ResponsiveRow).
    - Todas las tarjetas comparten altura por breakpoint.
    - Se reserva altura de texto para 2 líneas (no se corta).
    """

    # Breakpoints y métricas (ajusta aquí si quieres más altura en móvil)
    def _sizes():
        w = page.width or 800
        if w < 480:   # 📱 móvil (ej. 375 x 667)
            return dict(
                max_extent=200,      # ancho máx de cada tile
                title_sz=12,         # tamaño de fuente título
                title_pad_v=8,       # padding vertical del área de texto
                img_h=130,           # altura fija imagen
                spacing=8,
                run_spacing=10,
            )
        elif w < 900: # 📲 tablet
            return dict(
                max_extent=240,
                title_sz=15,
                title_pad_v=10,
                img_h=150,
                spacing=10,
                run_spacing=12,
            )
        else:         # 💻 desktop
            return dict(
                max_extent=280,
                title_sz=18,
                title_pad_v=12,
                img_h=170,
                spacing=12,
                run_spacing=14,
            )

    def _snack(msg: str):
        page.snack_bar = ft.SnackBar(content=ft.Text(msg))
        page.snack_bar.open = True
        page.update()

    # Construye UNA tarjeta usando alturas fijas pre-calculadas
    def _card(item: dict, sz: dict) -> ft.Container:
        # Altura necesaria para 2 líneas de texto (aprox. line-height 1.3)
        line_h = 1.30
        text_h = math.ceil(sz["title_sz"] * line_h * 2) + (sz["title_pad_v"] * 2)

        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(1, 3, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
            ink=True,
            on_click=lambda e: _snack(f"Seleccionaste {item['titulo']}"),
            content=ft.Column(
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    # Imagen con altura fija
                    ft.Container(
                        height=sz["img_h"],
                        alignment=ft.alignment.center,
                        content=ft.Image(src=item["imagen"], fit=ft.ImageFit.COVER),
                    ),
                    # Área de texto con altura exacta para 2 líneas
                    ft.Container(
                        height=text_h,
                        alignment=ft.alignment.center,
                        padding=ft.padding.symmetric(horizontal=6, vertical=sz["title_pad_v"]),
                        content=ft.Text(
                            item["titulo"],
                            size=sz["title_sz"],
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=2,                         # 🔒 solo 2 líneas
                            overflow=ft.TextOverflow.ELLIPSIS,   # … si excede
                            color=ft.Colors.BLACK,
                        ),
                    ),
                ],
            ),
        )

    # Re-construye el GridView con el aspect_ratio correcto según las alturas
    def _build_grid():
        sz = _sizes()

        # Altura total estimada de la tarjeta = imagen + texto (misma para todas)
        line_h = 1.30
        text_h = math.ceil(sz["title_sz"] * line_h * 2) + (sz["title_pad_v"] * 2)
        card_h = sz["img_h"] + text_h

        grid.max_extent = sz["max_extent"]
        grid.spacing = sz["spacing"]
        grid.run_spacing = sz["run_spacing"]

        # child_aspect_ratio = ancho / alto
        # aproximamos ancho ~= max_extent (GridView calcula el real, pero esto alinea bastante bien)
        grid.child_aspect_ratio = sz["max_extent"] / card_h

        grid.controls.clear()
        for it in SERVICIOS:
            grid.controls.append(_card(it, sz))
        grid.update()

    # Grid base
    grid = ft.GridView(expand=True)

    # Montaje en el contenedor destino
    contenedor.controls.clear()
    contenedor.controls.append(grid)
    contenedor.update()

    # Primera construcción
    _build_grid()

    # Responsivo en tiempo real
    def _on_resize(e):
        _build_grid()

    page.on_resize = _on_resize
