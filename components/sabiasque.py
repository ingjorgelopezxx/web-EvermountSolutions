# components/sabiasque.py
import flet as ft

# --------- Datos ----------
SABIASQUE_ITEMS = [
    {
        "especie": "Cucarachas",
        "titulo": "¿Sabías que las cucarachas pueden vivir hasta una semana sin su cabeza?",
        "imagen": "https://www.gardentech.com/-/media/project/oneweb/gardentech/images/pest-id/bug-pest/cockroach.png",
        "texto": (
            "Las cucarachas son plagas muy resistentes y adaptables, con diversas curiosidades que las hacen fascinantes y problemáticas. "
            "Son capaces de sobrevivir sin cabeza por un tiempo, soportan altos niveles de radiación y pueden sobrevivir sin comida por semanas o sin agua por días. "
            "Además, pueden transmitir enfermedades y son atraídas por la comida y la humedad. Algunas especies pueden vivir hasta un mes sin comida y correr hasta 3 millas por hora."
        ),
        "extra": [
            "Resistencia: Pueden sobrevivir sin cabeza por hasta una semana y pueden aguantar la respiración hasta por 40 minutos.",
            "Adaptabilidad: Se adaptan a diversos ambientes, pero prefieren interiores cálidos y húmedos, cerca de fuentes de alimento y agua.",
            "Transmisión de enfermedades: Transmiten salmonela, E. coli y otras bacterias peligrosas.",
            "Comportamiento: Son nocturnas, se esconden de la luz y atraen a otras mediante rastros químicos.",
            "Reproducción: Se multiplican rápidamente, generando infestaciones graves.",
            "Alimentación: Comen desde alimentos humanos y de mascotas hasta basura y materia orgánica.",
            "Impacto en la salud: Pueden causar alergias y asma, sobre todo en niños.",
            "No solo la cucaracha americana: También hay otras plagas como la oriental y la alemana.",
            "Evitar pisarlas: Al aplastarlas pueden dispersar bacterias y gérmenes peligrosos."
        ]
    },
    {
        "especie": "Ratas",
        "titulo": "¿Sabías que una sola rata puede producir hasta 2,000 descendientes en un año si no se controla su población?",
        "imagen": "https://i.postimg.cc/X7Dt0Tf1/istockphoto-1413873422-612x612.jpg",
        "texto": (
            "Las ratas tienen gran capacidad reproductiva y, sin control, se convierten rápidamente en una infestación. "
            "Además de daños materiales, son portadoras de enfermedades peligrosas."
        ),
        "extra": [
            "Adaptabilidad: Sobreviven en alcantarillas y edificios, y pueden aplanar su cuerpo para pasar por espacios reducidos.",
            "Reproducción rápida: Una hembra puede tener hasta 80 crías al año.",
            "Transmisión de enfermedades: Leptospirosis, salmonelosis, peste, entre otras.",
            "Daños estructurales: Roen cables, tuberías y madera; riesgo de incendios.",
            "Contaminación de alimentos: Excrementos y orina contaminan alimentos.",
            "Resistencia a venenos: Algunas son resistentes a rodenticidas.",
            "Habilidades: Buenas nadadoras y trepadoras.",
            "Olfato desarrollado: Detectan sustancias químicas a bajas concentraciones.",
            "Miedo a depredadores: Olores de gatos pueden ahuyentarlas.",
            "Capacidad de salto: Hasta 0,5 m vertical y ~1 m horizontal."
        ]
    },
    {
        "especie": "Ratones",
        "titulo": "¿Sabías que los ratones pueden vivir hasta tres años en condiciones favorables?",
        "imagen": "https://i.postimg.cc/FsrS6xC9/raton-campo-mus-musculus-768x576.jpg",
        "texto": (
            "Excelentes trepadores y nadadores; saltan hasta 30 cm. Pueden roer cemento y vidrio. "
            "Reproducción prolífica desde las 6 semanas. Transmiten enfermedades y contaminan alimentos y superficies."
        ),
        "extra": [
            "Agilidad y acrobacias: Trepan por diversas superficies y caminan sobre cables.",
            "Roedores versátiles: Roen cemento, vidrio y aluminio.",
            "Comportamiento social: Pueden imitar hábitos alimenticios de otros ratones.",
            "Reproducción rápida: Hasta 15 camadas al año; crías fértiles a las 5–6 semanas.",
            "Transmisión de enfermedades: Salmonelosis, hantavirus, etc.",
            "Parásitos: Portan pulgas, garrapatas y piojos.",
            "Adaptación: Pueden obtener agua de los alimentos.",
            "Comunicación ultrasónica: Usan frecuencias inaudibles para humanos.",
            "Memoria: Recuerdan rutas y resuelven problemas simples.",
            "Nocturnidad: Más activos de noche."
        ]
    },
    {
        "especie": "Termitas",
        "titulo": "¿Sabías que las termitas nunca duermen?",
        "imagen": "https://i.postimg.cc/wjVRQRQ1/termitas-1.png",
        "texto": (
            "Descomponedores clave en la naturaleza, pero destructivas en estructuras de madera. "
            "Se reproducen rápido, prefieren la celulosa y pueden causar daños significativos."
        ),
        "extra": [
            "Alta tasa de reproducción: La reina puede poner miles de huevos al día.",
            "Comportamiento social: Colonias con castas (obreras, soldados, reproductores).",
            "Destrucción silenciosa: Dañan sin ser detectadas durante mucho tiempo.",
            "Preferencias alimenticias: Madera, papel y cartón.",
            "Daños estructurales: Debilitan vigas y muebles.",
            "Adaptabilidad: Se ajustan a diversos ambientes.",
            "Feromonas: Coordinan la colonia con señales químicas.",
            "Importancia ecológica: Descomponen materia orgánica.",
            "Oscuridad y humedad: Algunas viven en ambientes oscuros y húmedos.",
            "Nota: Su organización social es compleja (a diferencia de lo que suelen creer)."
        ]
    },
    {
        "especie": "Hormigas",
        "titulo": "¿Sabías que un nido de hormigas puede contener cientos de miles de individuos?",
        "imagen": "https://i.postimg.cc/QCGM3jqL/hormiga-eliminar-plaga.jpg",
        "texto": (
            "Plagas comunes en hogares y jardines. Encuentran comida/agua con facilidad, construyen nidos en lugares inesperados y pueden dañar madera (carpinteras)."
        ),
        "extra": [
            "Organización social: Colonias con castas y funciones definidas.",
            "Feromonas: Marcan rutas hacia alimento y alertan peligros.",
            "Fuerza: Pueden levantar hasta 50 veces su peso.",
            "Invasión: Entran por pequeñas grietas buscando recursos.",
            "Carpinteras: Excavación de madera para nidos.",
            "Resistencia: Se adaptan a climas diversos.",
            "Trabajo en equipo: Transporte colaborativo y defensa.",
            "Longevidad de reinas: Algunas viven años.",
            "Nidos: En tierra, paredes y techos.",
            "Salud: Algunas muerden/pican y contaminan alimentos."
        ]
    },
    {
        "especie": "Palomas",
        "titulo": "¿Sabías que las palomas pueden reconocer rostros humanos?",
        "imagen": "https://a.files.bbci.co.uk/worldservice/live/assets/images/2015/11/20/151120130815_paloma2_624x351_thinkstock_nocredit.jpg",
        "texto": (
            "Comunes en ciudades; pueden ser plaga por daños y enfermedades. Nidos y excrementos afectan estructuras y atraen parásitos."
        ),
        "extra": [
            "Orientación: Regresan a casa desde cientos de km.",
            "Enfermedades: Histoplasmosis, criptococosis y psitacosis.",
            "Daño corrosivo: Excrementos deterioran piedra y metal.",
            "Reproducción: En climas templados crían todo el año.",
            "Alimentación: Restos humanos, granos y semillas.",
            "Parásitos: Ácaros, pulgas y garrapatas en nidos.",
            "Agua: Ensucian fuentes y sistemas.",
            "Longevidad: >15 años en cautiverio.",
            "Reconocimiento: Identifican rostros.",
            "Adaptación: Urbanas y rurales."
        ]
    },
    {
        "especie": "Chinches",
        "titulo": "¿Sabías que las chinches pueden sobrevivir meses sin alimentarse?",
        "imagen": "https://i.postimg.cc/7YPC9MmS/chinche-cimex-lectularius.jpg",
        "texto": (
            "Parásitos de sangre; causan picor e irritación. Se esconden en grietas, colchones y muebles. Su control requiere tratamiento especializado."
        ),
        "extra": [
            "Ayuno: Meses sin comer.",
            "Nocturnas: Se alimentan de noche.",
            "Hematófagas: Detectan calor y CO₂.",
            "Difíciles de ver: Tamaño pequeño y mucho escondite.",
            "Reproducción: Cientos de huevos por hembra.",
            "Dispersión: Viajan en ropa y equipaje.",
            "Resistencia: Algunas a insecticidas.",
            "Transmisión: No está demostrada a humanos.",
            "Señales: Manchas y olor dulce.",
            "Erradicación: Requiere tratamiento integral."
        ]
    },
    {
        "especie": "Pulgas",
        "titulo": "¿Sabías que el 50% de las picaduras de pulgas pueden causar reacciones alérgicas?",
        "imagen": "https://www.gardentech.com/-/media/project/oneweb/gardentech/images/pest-id/alt-bug/flea.jpg",
        "texto": (
            "Pequeños parásitos de mamíferos y aves. Picaduras con picor intenso. Pueden transmitir enfermedades y parásitos; se reproducen rápido."
        ),
        "extra": [
            "Salto: Hasta 200 veces su longitud.",
            "Ciclo rápido: De huevo a adulto en ~2 semanas.",
            "Ayuno: Adultos viven semanas sin comer.",
            "Enfermedades: Peste, tifus murino y tenias.",
            "Adaptación: Infestan mascotas y humanos.",
            "Huevos: Quedan en alfombras y grietas.",
            "Prolificidad: 50 huevos/día por hembra.",
            "Vibraciones: Detectan movimiento y calor.",
            "Control: Requiere atacar adultos, larvas y huevos.",
            "Picaduras: En grupos o líneas."
        ]
    },
    {
        "especie": "Moscas",
        "titulo": "¿Sabías que las moscas domésticas pueden transmitir más de 60 enfermedades?",
        "imagen": "https://i.postimg.cc/3wZN2kmt/white-Photoroom-1.png",
        "texto": (
            "Comunes pero riesgosas para la salud pública. Se alimentan de materia en descomposición y contaminan alimentos al posarse."
        ),
        "extra": [
            "Ciclo corto: 7–10 días a adulto.",
            "Prolíficas: ~500 huevos por hembra.",
            "Enfermedades: Salmonelosis, disentería, cólera.",
            "Alimentación: Enzimas sobre alimentos antes de ingerir.",
            "Adaptables: Sobreviven con alimento y humedad.",
            "Larvas: En basura y aguas residuales.",
            "Vuelo: Pueden recorrer kilómetros.",
            "Olores: Atraídas por descomposición.",
            "Higiene: Contaminan utensilios y superficies.",
            "Diurnas: Más activas con calor."
        ]
    },
]

# --------- Helpers ----------
def _img_height_for(page: ft.Page) -> int:
    if page.width < 480:
        return 160
    elif page.width < 768:
        return 220
    elif page.width < 1200:
        return 280
    else:
        return 320

def _tile_img_height_for(page: ft.Page) -> int:
    if page.width < 480:
        return 100
    elif page.width < 768:
        return 120
    elif page.width < 1200:
        return 140
    else:
        return 160

def _bullet_line(p: str) -> ft.Row:
    if ":" in p:
        head, body = p.split(":", 1)
    else:
        head, body = p, ""
    rich_text = ft.Text(
        spans=[
            ft.TextSpan(f"{head.strip()}: ", ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)),
            ft.TextSpan(body.strip(), ft.TextStyle(color=ft.Colors.BLACK)),
        ],
        size=14,
        text_align=ft.TextAlign.JUSTIFY,
    )
    return ft.Row(
        controls=[ft.Text("•", size=18, color=ft.Colors.BLACK), ft.Container(rich_text, expand=True)],
        spacing=6,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

# --------- Render principal ----------
def render_sabiasque(page: ft.Page, contenedor: ft.Column, items: list | None = None):
    """
    Muestra una CUADRÍCULA de especies; al seleccionar una tarjeta, muestra el DETALLE.
    """
    data = items or SABIASQUE_ITEMS
    contenedor.padding = 0
    contenedor.spacing = 0

    tile_img_h = _tile_img_height_for(page)

    # 1) Helpers responsive
    def _grid_metrics(page: ft.Page) -> tuple[int, float, int, int]:
        w = page.width
        if w < 480:            # Celular
            return (120, 0.86, 6, 8)     # max_extent, aspect_ratio, spacing, run_spacing
        elif w < 768:          # Tablet
            return (160, 0.86, 8, 10)
        elif w < 1200:         # Laptop
            return (200, 0.86, 10, 12)
        else:                  # Desktop
            return (240, 0.9, 12, 14)

    # 2) Crea el GridView usando esos parámetros
    mx, ar, sp, rsp = _grid_metrics(page)
    grid = ft.GridView(
        expand=True,
        max_extent=mx,
        child_aspect_ratio=ar,
        spacing=sp,
        run_spacing=rsp,
    )

    # 3) Ajusta en tiempo real cuando cambie el ancho de la ventana
    def _on_resize(e=None):
        mx, ar, sp, rsp = _grid_metrics(page)
        grid.max_extent = mx
        grid.child_aspect_ratio = ar
        grid.spacing = sp
        grid.run_spacing = rsp
        grid.update()

    page.on_resize = _on_resize

    def _tile(idx: int, item: dict, page: ft.Page) -> ft.Container:
        nombre = item.get("especie") or item.get("titulo", f"Item {idx+1}")
        img = item.get("imagen", "")

        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK12, offset=ft.Offset(2, 2)),
            ink=True,
            on_click=lambda e, i=idx: show_detail(i),
            padding=0,
            content=ft.Column(
                expand=True,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Container(  # imagen 75%
                        expand=75,
                        alignment=ft.alignment.center,
                        padding=6,
                        content=ft.Image(src=img, fit=ft.ImageFit.CONTAIN),
                    ),
                    ft.Container(  # texto 25%
                        expand=25,
                        alignment=ft.alignment.center,
                        padding=ft.padding.symmetric(horizontal=6, vertical=4),
                        content=ft.Text(
                            nombre,
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

    def show_grid():
        contenedor.controls.clear()
        contenedor.controls.append(
            ft.Column(
                controls=[
                    # Encabezado centrado con Comic Sans y Divider
                    ft.Container(
                        alignment=ft.alignment.center,
                        padding=ft.padding.symmetric(vertical=4),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=2,
                            controls=[
                                ft.Text(
                                    "Selecciona una especie",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK,
                                    text_align=ft.TextAlign.CENTER,
                                    font_family="Comic Sans MS",   # 👈 Comic Sans
                                ),
                                ft.Divider(color=ft.Colors.BLACK26, thickness=1),
                            ],
                        ),
                    ),
                    grid,
                ],
                expand=True,
                spacing=2,
            )
        )
        grid.controls.clear()
        for i, it in enumerate(data):
            grid.controls.append(_tile(i, it, page))
        contenedor.update()


    def show_detail(index: int):
        d = data[index]
        img_h = _img_height_for(page)

        bloque = ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            padding=12,
            shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK12, offset=ft.Offset(2, 2)),
            content=ft.Column(
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        d.get("titulo", d.get("especie", "Detalle")),
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(
                        height=img_h,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=8,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        content=ft.Image(src=d.get("imagen", ""), fit=ft.ImageFit.CONTAIN, opacity=1.0),
                    ),
                    ft.Text(d.get("texto", ""), size=15, color=ft.Colors.BLACK, text_align=ft.TextAlign.JUSTIFY),
                    ft.Column(controls=[_bullet_line(p) for p in d.get("extra", [])], spacing=4),
                ],
            ),
        )

        # Vista de detalle con SCROLL
        detail_view = ft.ListView(
            expand=True,
            spacing=8,
            controls=[
                ft.Row(
                    controls=[
                        ft.TextButton(
                            "← Volver",
                            style=ft.ButtonStyle(
                                color={
                                    ft.ControlState.DEFAULT: ft.Colors.BLACK,   # 👈 color negro
                                    ft.ControlState.HOVERED: ft.Colors.BLACK,  # negro también al pasar el mouse
                                },
                                text_style=ft.TextStyle(
                                    weight=ft.FontWeight.BOLD                 # 👈 negrita
                                ),
                            ),
                            on_click=lambda e: show_grid(),
                        ),
                        ft.Text(d.get("especie", "").upper(), size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(color=ft.Colors.BLACK26, thickness=1),
                bloque,
            ],
        )

        contenedor.controls.clear()
        contenedor.controls.append(detail_view)
        contenedor.update()

    # Mostrar cuadrícula inicialmente
    show_grid()
