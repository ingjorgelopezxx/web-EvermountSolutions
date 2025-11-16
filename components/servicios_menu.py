# components/menu_servicios.py
import flet as ft

SERVICIOS = [
    {"titulo": "Roedores", "imagen": "https://i.postimg.cc/4NLHX4nH/Chat-GPT-Image-26-ago-2025-03-08-53-p-m.png","ruta": "/servicios/roedores"},
    {"titulo": "Desinfección y Sanitización", "imagen": "https://i.postimg.cc/zGfdKtvL/desinfeccion-Photoroom-Photoroom.png","ruta": "/servicios/sanitizacion"},
    {"titulo": "Insectos Voladores", "imagen": "https://i.postimg.cc/V6hZkjmS/white-Photoroom-Photoroom.png","ruta": "/servicios/voladores"},
    {"titulo": "Insectos Rastreros", "imagen": "https://i.postimg.cc/D0zscS8F/Chat-GPT-Image-26-ago-2025-03-18-37-p-m.png","ruta": "/servicios/rastreros"},
    {"titulo": "Tratamiento Termitas", "imagen": "https://i.postimg.cc/3JTQW24P/Chat-GPT-Image-26-ago-2025-03-13-04-p-m.png","ruta": "/servicios/termitas"},
    {"titulo": "Aves Urbanas", "imagen": "https://i.postimg.cc/HnWjCFgt/Chat-GPT-Image-26-ago-2025-03-09-31-p-m.png","ruta": "/servicios/aves"},
]

def render_menu_servicios(page: ft.Page, contenedor: ft.Column):
    """
    Menú responsivo con tarjetas usando porcentajes al estilo 'Sabías que'.
    Encabezado superior: 'Seleccionar Servicio'.
    """

    def _sizes():
        w = page.width or 800
        if w < 480:    # 📱 móvil
            return dict(
                max_extent=160, aspect=0.60, spacing=8, run=10,
                title_sz=13, heading_sz=24,
                img_pct=60, txt_pct=40
            )
        elif w < 900:  # 📲 tablet
            return dict(
                max_extent=240, aspect=0.78, spacing=10, run=12,
                title_sz=16, heading_sz=28,
                img_pct=70, txt_pct=30
            )
        else:          # 💻 desktop
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
            shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
            ink=True,
            on_click=lambda e: page.go(item["ruta"]),
            content=ft.Column(
                expand=True,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Container(
                        expand=sz["img_pct"],
                        alignment=ft.alignment.center,
                        content=ft.Image(src=item["imagen"], fit=ft.ImageFit.COVER),
                    ),
                    ft.Container(
                        expand=sz["txt_pct"],
                        alignment=ft.alignment.center,
                        padding=ft.padding.symmetric(horizontal=8, vertical=8),
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

    # --- Heading ---
    heading = ft.Container(
        alignment=ft.alignment.center,
        content=ft.Text(
            "Seleccionar Servicio",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            color="#0F3D47",
            size=24,
        )
    )

    # Grid de servicios
    grid = ft.GridView(
        expand=True,   # se expandirá SOLO dentro del wrapper (que tiene ancho limitado)
    )

    # Column interna que contiene heading + grid
    inner_column = ft.Column(
        controls=[heading, grid],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # wrapper que vamos a centrar y limitar de ancho
    wrapper = ft.Container(
        content=inner_column,
        alignment=ft.alignment.center,
        width=None,   # se ajusta en _build_grid según ancho de pantalla
    )

    # metemos solo el wrapper en el contenedor que viene de main
    contenedor.controls.clear()
    contenedor.controls.append(wrapper)
    contenedor.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    contenedor.alignment = ft.MainAxisAlignment.CENTER
    contenedor.update()

    def _build_grid():
        sz = _sizes()
        w = page.width or 800

        # ajustar heading
        heading.content.size = sz["heading_sz"]

        # ajustar grid
        grid.max_extent = sz["max_extent"]
        grid.child_aspect_ratio = sz["aspect"]
        grid.spacing = sz["spacing"]
        grid.run_spacing = sz["run"]

        # ancho del wrapper:
        # - móvil: ocupa todo
        # - tablet / desktop: máx 900 px y centrado
        if w < 480:
            wrapper.width = None
        else:
            wrapper.width = min(w * 0.9, 1600)

        # reconstruir cards
        grid.controls.clear()
        for it in SERVICIOS:
            grid.controls.append(_card(it, sz))

        wrapper.update()
        grid.update()
        heading.update()
        contenedor.update()
        page.update()

    # primera construcción
    _build_grid()

    # volver a calcular cuando cambie el tamaño
    def on_resize(e):
        _build_grid()

    # OJO: si ya usas page.on_resized en otra parte, haz un wrapper central allí
    page.on_resized = on_resize
