import flet as ft
import asyncio

# Lista de imágenes (puedes cambiar o pasar como argumento)
IMAGENES = [
    "https://i.postimg.cc/15nLZNp7/imagen1.jpg",
    "https://i.postimg.cc/RZwyW5pc/imagen2.jpg",
    "https://i.postimg.cc/BvgzC50b/imagen3.jpg",
    "https://i.postimg.cc/FRCnM91Q/imagen4.jpg",
]

def create_vertical_carousel(page: ft.Page, intervalo=3):
    """
    Carrusel vertical de imágenes en tarjetas.
    Retorna (carrusel_control, start_carousel, stop_carousel)
    """

    # Índice actual
    idx = [0]
    activo = [False]
    tarea = [None]

    # Imagen principal dentro de tarjeta
    imagen = ft.Image(
        src=IMAGENES[idx[0]],
        fit=ft.ImageFit.COVER,
        width=250,
        height=350,
        border_radius=ft.border_radius.all(12)
    )

    # Tarjeta vertical conteniendo la imagen
    tarjeta = ft.Container(
        content=imagen,
        width=250,
        height=350,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        alignment=ft.alignment.center,
    )

    # Contenedor principal del carrusel
    carrusel_control = ft.Container(
        content=tarjeta,
        alignment=ft.alignment.center,
        padding=10
    )

    # --- Rotación automática ---
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
    texto_presentacion = ft.Container(bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content= ft.Column(
        [
            ft.Text(
                "Control Mensual y Anual",
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#0D2943",  
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Ofrecemos planes de mantenimiento diseñados para mantener tus espacios protegidos durante todo el año. "
                "Nos adaptamos a tus necesidades y tipo de actividad (residencial, comercial o industrial).\n\n"
                "📆 Visitas programadas con seguimiento\n"
                "📊 Informes técnicos y certificados de aplicación\n"
                "🛡️ Control integral de plagas todo el año",
                size=14,
                color=ft.Colors.BLACK87,
                text_align=ft.TextAlign.JUSTIFY
            ),
            ft.Text(
                "Planes ideales para",
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#0D2943",  
                text_align=ft.TextAlign.CENTER
            ),
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ))

    # --- Datos de planes (texto + iconos)
    planes = [
        ("Restaurantes", ft.Icons.RESTAURANT),
        ("Supermercados", ft.Icons.SHOPPING_CART),
        ("Bodegas", ft.Icons.WAREHOUSE),
        ("Centros educativos", ft.Icons.SCHOOL),
        ("Condominios", ft.Icons.HOUSE),
        ("Empresas ", ft.Icons.VERIFIED)
    ]

    # --- Crear items con iconos
    plan_items = []
    for texto, icono in planes:
        plan_items.append(
            ft.Row(
                [
                    ft.Icon(icono, color="#0D2943", size=20),
                    ft.Text(texto, size=14, color=ft.Colors.BLACK87),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8
            )
        )

    # --- 3 filas, 2 columnas cada fila
    filas = []
    for i in range(0, len(plan_items), 2):
        fila = ft.Row(
            [
                ft.Container(content=plan_items[i], expand=True,margin=ft.margin.only(left=20)),
                ft.Container(content=plan_items[i+1], expand=True) if i+1 < len(plan_items) else ft.Container(),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            spacing=10
        )
        filas.append(fila)

    lista_planes = ft.Column(filas, spacing=8)

    # --- Contenedor completo
    contenedor_completo = ft.Column(
        [
            texto_presentacion,
            lista_planes,
            carrusel_control
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    return contenedor_completo, start, stop
