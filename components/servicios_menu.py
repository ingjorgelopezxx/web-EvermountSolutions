# components/menu_servicios.py
import flet as ft

SERVICIOS = [
    {
        "titulo": "Control de Roedores",
        "imagen": "https://i.postimg.cc/bYH88GG3/Chat-GPT-Image-26-ago-2025-02-28-31-p-m.png",
    },
    {
        "titulo": "Desinfección y Sanitización de Ambientes",
        "imagen": "https://i.postimg.cc/Sx8f1Vk0/desinfeccion.jpg",
    },
    {
        "titulo": "Control de Insectos Voladores",
        "imagen": "https://i.postimg.cc/zvkh5JW3/Chat-GPT-Image-26-ago-2025-02-22-27-p-m.jpg",
    },
    {
        "titulo": "Control de Insectos Rastreros",
        "imagen": "https://i.postimg.cc/zGsYc58V/insectos-rastreros.jpg",
    },
    {
        "titulo": "Tratamiento de Termitas",
        "imagen": "https://i.postimg.cc/wjVRQRQ1/termitas-1.png",
    },
    {
        "titulo": "Control de Aves Urbanas",
        "imagen": "https://i.postimg.cc/t4nL0mH4/aves-urbanas.jpg",
    },
]

def render_menu_servicios(page: ft.Page, contenedor: ft.Column):
    """Renderiza un menú de servicios con tarjetas responsivas."""

    def _grid_metrics():
        w = page.width or 800
        if w < 480:       # 📱 Celulares
            return (160, 0.7, 6, 8)   # (max_extent, aspect_ratio, spacing, run_spacing)
        elif w < 900:     # 📲 Tablets
            return (200, 0.8, 8, 10)
        else:             # 💻 PC / escritorio
            return (260, 0.9, 12, 12)

    # crear grid responsivo
    mx, ar, sp, rsp = _grid_metrics()
    grid = ft.GridView(
        expand=True,
        max_extent=mx,
        child_aspect_ratio=ar,
        spacing=sp,
        run_spacing=rsp,
    )

    # Redimensionar en runtime
    def _on_resize(e):
        mx, ar, sp, rsp = _grid_metrics()
        grid.max_extent = mx
        grid.child_aspect_ratio = ar
        grid.spacing = sp
        grid.run_spacing = rsp
        grid.update()

    page.on_resize = _on_resize

    def _card(item):
        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
            ink=True,
            on_click=lambda e: page.snack_bar.open(ft.SnackBar(ft.Text(f"Seleccionaste {item['titulo']}"))),
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    ft.Container(
                        expand=75,  # 75% imagen
                        alignment=ft.alignment.center,
                        content=ft.Image(src=item["imagen"], fit=ft.ImageFit.COVER),
                    ),
                    ft.Container(
                        expand=25,  # 25% texto
                        alignment=ft.alignment.center,
                        padding=ft.padding.symmetric(horizontal=6, vertical=8),
                        content=ft.Text(
                            item["titulo"],
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                            color=ft.Colors.BLACK,
                        ),
                    ),
                ],
            ),
        )

    # limpiar y montar
    contenedor.controls.clear()
    for it in SERVICIOS:
        grid.controls.append(_card(it))
    contenedor.controls.append(grid)
    contenedor.update()
