import flet as ft
from functions.asset_sources import SERVICE_MENU_IMAGES


SERVICIOS = [
    {"titulo": "Roedores", "imagen": SERVICE_MENU_IMAGES["roedores"], "ruta": "/servicios/roedores"},
    {"titulo": "Desinfección y Sanitización", "imagen": SERVICE_MENU_IMAGES["sanitizacion"], "ruta": "/servicios/sanitizacion"},
    {"titulo": "Insectos Voladores", "imagen": SERVICE_MENU_IMAGES["voladores"], "ruta": "/servicios/voladores"},
    {"titulo": "Insectos Rastreros", "imagen": SERVICE_MENU_IMAGES["rastreros"], "ruta": "/servicios/rastreros"},
    {"titulo": "Tratamiento Termitas", "imagen": SERVICE_MENU_IMAGES["termitas"], "ruta": "/servicios/termitas"},
    {"titulo": "Aves Urbanas", "imagen": SERVICE_MENU_IMAGES["aves"], "ruta": "/servicios/aves"},
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
                max_extent=160,
                aspect=0.68,
                spacing=8,
                run=10,
                title_sz=13,
                heading_sz=24,
                img_pct=68,
                txt_pct=32,
            )
        if w < 900:
            return dict(
                max_extent=240,
                aspect=0.92,
                spacing=10,
                run=12,
                title_sz=16,
                heading_sz=28,
                img_pct=78,
                txt_pct=22,
            )
        if w < 1600:
            return dict(
                max_extent=200,
                aspect=0.96,
                spacing=10,
                run=12,
                title_sz=12,
                heading_sz=28,
                img_pct=80,
                txt_pct=20,
            )
        return dict(
            max_extent=280,
            aspect=1.00,
            spacing=12,
            run=14,
            title_sz=14,
            heading_sz=34,
            img_pct=82,
            txt_pct=18,
        )

    def _card(item: dict, sz: dict) -> ft.Container:
        return ft.Container(
            bgcolor="#FCFEFF",
            border_radius=22,
            border=ft.Border.all(1, "#DBE7EC"),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(
                blur_radius=18,
                spread_radius=0,
                color="rgba(17,56,66,0.14)",
                offset=ft.Offset(0, 8),
            ),
            ink=True,
            on_click=lambda e: push_route(item["ruta"]),
            content=ft.Column(
                expand=True,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Container(height=4, bgcolor="#123F49"),
                    ft.Container(
                        expand=sz["img_pct"],
                        alignment=ft.alignment.center,
                        padding=ft.Padding.only(top=12, left=12, right=12),
                        content=ft.Container(
                            border_radius=18,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            content=ft.Image(src=item["imagen"], fit=ft.BoxFit.COVER),
                        ),
                    ),
                    ft.Container(
                        expand=sz["txt_pct"],
                        alignment=ft.alignment.center,
                        padding=ft.Padding.only(left=14, right=14, top=8, bottom=10),
                        content=ft.Column(
                            [
                                ft.Text(
                                    item["titulo"],
                                    size=sz["title_sz"],
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER,
                                    max_lines=1 if (page.width or 0) >= 1020 else 2,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                    color="#123640",
                                ),
                            ],
                            spacing=0,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                ],
            ),
        )

    heading = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(
            [
                ft.Text(
                    "Selecciona el tipo de servicio",
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color="#0F3D47",
                    size=24,
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
        spacing=18,
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

        heading_title = heading.content.controls[0]
        heading_title.size = sz["heading_sz"]
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

        if getattr(contenedor, "page", None) is not None:
            contenedor.update()

    _build_grid()
    contenedor.data = contenedor.data or {}
    contenedor.data["rebuild"] = _build_grid
