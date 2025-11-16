import flet as ft
import asyncio

IMAGENES = [
    "https://i.postimg.cc/15nLZNp7/imagen1.jpg",
    "https://i.postimg.cc/RZwyW5pc/imagen2.jpg",
    "https://i.postimg.cc/BvgzC50b/imagen3.jpg",
    "https://i.postimg.cc/FRCnM91Q/imagen4.jpg",
]

def create_vertical_carousel(page: ft.Page, intervalo=3):
    # === breakpoints ===
    ancho = page.width or 0
    es_pc = ancho >= 1020          # 👈 SOLO PC
    es_tablet = 600 <= ancho < 1020
    es_movil = ancho < 600

    # tamaños según dispositivo
    if es_pc:
        img_w, img_h = 300, 350    # 👈 igual que video_card en PC
    elif es_tablet:
        img_w, img_h = 300, 350
    else:  # móvil
        img_w, img_h = 220, 320

    TITLE_SIZE = 24 if (es_pc or es_tablet) else 24
    BODY_SIZE = 18 if (es_pc or es_tablet) else 18
    PLAN_SIZE = 18 if (es_pc or es_tablet) else 18

    # Índice actual
    idx = [0]
    activo = [False]
    tarea = [None]

    imagen = ft.Image(
        src=IMAGENES[idx[0]],
        fit=ft.ImageFit.COVER,
        width=img_w,          # 👈 usa tamaño calculado
        height=img_h,         # 👈 usa tamaño calculado
        border_radius=ft.border_radius.all(12),
    )

    tarjeta = ft.Container(
        content=imagen,
        width=img_w,          # 👈 igual que image
        height=img_h,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        alignment=ft.alignment.center,
    )

    carrusel_control = ft.Container(
        content=tarjeta,
        alignment=ft.alignment.center,
        padding=10,
    )

    async def _rotar():
        try:
            while activo[0]:
                # Si la imagen aún no está añadida al árbol de la página,
                # esperamos un poquito y volvemos a intentar.
                if getattr(imagen, "page", None) is None:
                    await asyncio.sleep(0.1)
                    continue

                imagen.src = IMAGENES[idx[0] % len(IMAGENES)]
                # 👇 Usamos page.update(), NO imagen.update()
                page.update()

                idx[0] = (idx[0] + 1) % len(IMAGENES)
                await asyncio.sleep(intervalo)
        except asyncio.CancelledError:
            # cuando se llama stop() y se cancela la tarea
            pass


    def start():
        if tarea[0] is None:
            activo[0] = True
            tarea[0] = page.run_task(_rotar)

    def stop():
        activo[0] = False
        if tarea[0] is not None:
            tarea[0].cancel()
            tarea[0] = None

    # --- Texto de presentación ---
    texto_presentacion = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Column(
            [
                ft.Text(
                    "Control Mensual y Anual",
                    size=TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                    color="#0D2943",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Ofrecemos planes de mantenimiento diseñados para mantener tus espacios protegidos durante todo el año. "
                    "Nos adaptamos a tus necesidades y tipo de actividad (residencial, comercial o industrial).\n\n"
                    "📆 Visitas programadas con seguimiento\n"
                    "📊 Informes técnicos y certificados de aplicación\n"
                    "🛡️ Control integral de plagas todo el año",
                    size=BODY_SIZE,
                    color=ft.Colors.BLACK87,
                    text_align=ft.TextAlign.JUSTIFY,
                ),
                ft.Text(
                    "Planes ideales para",
                    size=TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                    color="#0D2943",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    planes_col1 = [
        ("Restaurantes", ft.Icons.RESTAURANT),
        ("Bodegas", ft.Icons.WAREHOUSE),
        ("Condominios", ft.Icons.HOUSE),
    ]

    planes_col2 = [
        ("Supermercados", ft.Icons.SHOPPING_CART),
        ("Centros educativos", ft.Icons.SCHOOL),
        ("Empresas", ft.Icons.VERIFIED),
    ]

    def build_col(planes):
        items = []
        for texto, icono in planes:
            items.append(
                ft.Row(
                    [
                        ft.Icon(icono, color="#0D2943", size=20),
                        ft.Text(texto, size=PLAN_SIZE, color=ft.Colors.BLACK87),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                )
            )
        return ft.Column(items, spacing=4)

    lista_planes = ft.Row(
        [
            ft.Container(
                content=build_col(planes_col1),
                expand=True,
                alignment=ft.alignment.top_right,
            ),
            ft.Container(
                content=build_col(planes_col2),
                expand=True,
                alignment=ft.alignment.top_left,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    if es_pc or es_tablet:
        contenedor_completo = ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [texto_presentacion, lista_planes],
                        spacing=10,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    expand=True,
                ),
                ft.Container(
                    content=carrusel_control,
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    else:
        contenedor_completo = ft.Column(
            [
                texto_presentacion,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

    # guardamos para posibles ajustes futuros si quieres
    contenedor_completo.data = {
        "imagen": imagen,
        "tarjeta": tarjeta,
        "activo": activo   # 👈 ESTA ES LA BANDERA QUE FALTABA
    }

    return contenedor_completo, start, stop
