import flet as ft
import asyncio

IMAGENES = [
    "https://i.postimg.cc/15nLZNp7/imagen1.jpg",
    "https://i.postimg.cc/RZwyW5pc/imagen2.jpg",
    "https://i.postimg.cc/BvgzC50b/imagen3.jpg",
    "https://i.postimg.cc/FRCnM91Q/imagen4.jpg",
    "https://i.postimg.cc/9FN0WFkY/Whats-App-Image-2025-11-17-at-5-58-09-PM.jpg",
    "https://i.postimg.cc/Xq5W44BD/Whats-App-Image-2025-11-17-at-5-58-10-PM.jpg",
]

def create_vertical_carousel(page: ft.Page, intervalo=3):
    # === definimos breakpoint PC/Tablet vs móvil ===
    es_pc_tablet = (page.width or 0) >= 700
    TITLE_SIZE = 18 if es_pc_tablet else 22
    BODY_SIZE = 14 if es_pc_tablet else 14
    PLAN_SIZE = 12 if es_pc_tablet else 14

    # Índice actual
    idx = [0]
    activo = [False]
    tarea = [None]

    imagen = ft.Image(
        src=IMAGENES[idx[0]],
        fit=ft.ImageFit.COVER,
        width=263,
        height=360,
        border_radius=ft.border_radius.all(12)
    )

    tarjeta = ft.Container(
        content=imagen,
        width=263,
        height=360,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        alignment=ft.alignment.center,
    )

    carrusel_control = ft.Container(
        content=tarjeta,
        alignment=ft.alignment.center,
        padding=10
    )

    async def _rotar():
        try:
            while activo[0]:
                imagen.src = IMAGENES[idx[0] % len(IMAGENES)]
                page.update()
                idx[0] = (idx[0] + 1) % len(IMAGENES)
                await asyncio.sleep(intervalo)
        except asyncio.CancelledError:
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
                )
            )
        return ft.Column(items)

    # 👉 dos columnas lado a lado
    lista_planes = ft.Row(
        [
            ft.Container(
                content=build_col(planes_col1),
                alignment=ft.alignment.top_right,
                margin=ft.margin.only(left=10), 
            ),
            ft.Container(
                content=build_col(planes_col2),
                alignment=ft.alignment.top_left,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # --- Layout: izquierda texto + lista, derecha carrusel (PC/Tablet) ---
    if es_pc_tablet:
        contenedor_completo = ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [texto_presentacion, lista_planes],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),width=400
                ),
                ft.Container(
                    content=carrusel_control,
                    alignment=ft.alignment.center,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    else:
        contenedor_completo = ft.Column(
            [
                texto_presentacion,
                lista_planes,
                carrusel_control,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

    return contenedor_completo, start, stop