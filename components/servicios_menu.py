import flet as ft


SERVICIOS = [
    {"titulo": "Roedores", "imagen": "https://i.postimg.cc/cLvXDbLz/Chat-GPT-Image-26-ago-2025-03-08-53-p-m-Photoroom.png", "ruta": "/servicios/roedores"},
    {"titulo": "Desinfección y Sanitización", "imagen": "https://i.postimg.cc/zGfdKtvL/desinfeccion-Photoroom-Photoroom.png", "ruta": "/servicios/sanitizacion"},
    {"titulo": "Insectos Voladores", "imagen": "https://i.postimg.cc/V6hZkjmS/white-Photoroom-Photoroom.png", "ruta": "/servicios/voladores"},
    {"titulo": "Insectos Rastreros", "imagen": "https://i.postimg.cc/Kzx7yqmM/Chat-GPT-Image-26-ago-2025-03-18-37-p-m-Photoroom.png", "ruta": "/servicios/rastreros"},
    {"titulo": "Tratamiento Termitas", "imagen": "https://i.postimg.cc/rpLxSn0R/Chat-GPT-Image-26-ago-2025-03-13-04-p-m-Photoroom.png", "ruta": "/servicios/termitas"},
    {"titulo": "Aves Urbanas", "imagen": "https://i.postimg.cc/wjzDN4sJ/Chat-GPT-Image-26-ago-2025-03-09-31-p-m-Photoroom.png", "ruta": "/servicios/aves"},
]


def render_menu_servicios(page: ft.Page, contenedor: ft.Column):
    async def _push_route_async(route: str):
        await page.push_route(route)

    def push_route(route: str):
        page.run_task(_push_route_async, route)

    def _sizes():
        w = page.width or 800

        if w < 480:
            return dict(
                max_extent=160, aspect=0.60, spacing=8, run=10,
                title_sz=13, heading_sz=24,
                img_pct=60, txt_pct=40
            )
        if w < 900:
            return dict(
                max_extent=240, aspect=0.78, spacing=10, run=12,
                title_sz=16, heading_sz=28,
                img_pct=70, txt_pct=30
            )
        if w < 1600:
            return dict(
                max_extent=200, aspect=0.82, spacing=10, run=12,
                title_sz=14, heading_sz=28,
                img_pct=72, txt_pct=28
            )
        return dict(
            max_extent=280, aspect=0.88, spacing=12, run=14,
            title_sz=18, heading_sz=34,
            img_pct=75, txt_pct=25
        )

    def _card(item: dict, sz: dict) -> ft.Container:
        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK_26, offset=ft.Offset(2, 2)),
            ink=True,
            on_click=lambda e: push_route(item["ruta"]),
            content=ft.Column(
                expand=True,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Container(
                        expand=sz["img_pct"],
                        alignment=ft.alignment.center,
                        content=ft.Image(src=item["imagen"], fit=ft.BoxFit.COVER),
                    ),
                    ft.Container(
                        expand=sz["txt_pct"],
                        alignment=ft.alignment.center,
                        padding=ft.Padding.symmetric(horizontal=8, vertical=8),
                        content=ft.Text(
                            item["titulo"],
                            size=sz["title_sz"],
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

    heading = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Text(
            "Seleccionar Servicio",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            color="#0F3D47",
            size=24,
        ),
    )

    grid = ft.GridView(expand=False)

    grid_holder = ft.Container(
        alignment=ft.alignment.center,
        content=grid,
        width=None,
    )

    inner_column = ft.Column(
        controls=[heading, grid_holder],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    wrapper = ft.Container(
        content=inner_column,
        alignment=ft.alignment.center,
        width=None,
    )

    contenedor.controls.clear()
    contenedor.controls.append(wrapper)
    contenedor.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    contenedor.alignment = ft.MainAxisAlignment.CENTER
    contenedor.update()

    def _build_grid():
        sz = _sizes()
        w = page.width or 800

        heading.content.size = sz["heading_sz"]

        if w < 480:
            wrapper.width = None
        else:
            wrapper.width = min(w * 0.9, 1600)

        n = len(SERVICIOS)
        spacing = sz["spacing"]
        cell = sz["max_extent"]

        if w >= 1020:
            avail = wrapper.width or w
            max_cell_to_fit = (avail - (n - 1) * spacing) / n
            cell = min(cell, max_cell_to_fit)
            cell = max(180, cell)

        grid.max_extent = cell
        grid.child_aspect_ratio = sz["aspect"]
        grid.spacing = spacing
        grid.run_spacing = sz["run"]

        if w >= 1020:
            grid_holder.width = n * cell + (n - 1) * spacing
        else:
            grid_holder.width = None

        grid.controls.clear()
        for it in SERVICIOS:
            grid.controls.append(_card(it, sz))

        wrapper.update()
        grid.update()
        heading.update()
        contenedor.update()
        page.update()

    _build_grid()
    contenedor.data = contenedor.data or {}
    contenedor.data["rebuild"] = _build_grid
