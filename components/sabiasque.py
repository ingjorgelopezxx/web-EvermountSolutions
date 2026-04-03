# components/sabiasque.py
import flet as ft
from functions.asset_sources import SABIASQUE_IMAGES

# --------- Datos ----------
SABIASQUE_ITEMS = [
    {
        "especie": "Cucarachas",
        "titulo": "¿Sabías que las cucarachas pueden vivir hasta una semana sin su cabeza?",
        "imagen": SABIASQUE_IMAGES["cucarachas"],
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
        "imagen": SABIASQUE_IMAGES["ratas"],
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
        "imagen": SABIASQUE_IMAGES["ratones"],
        "texto": (
            "Excelentes trepadores y nadadores; saltan hasta 30 cm. Pueden roer cemento y vidrio. "
            "Reproducción prolífica desde las 6 semanas. Transmiten enfermedades y contaminan alimentos y superficies."
        ),
        "extra": [
            "Agilidad y acrobacias: Trepan por diversas superficies y caminan sobre cables.",
            "Roedores versátiles: Roen cemento, vidrio y aluminio.",
            "Comportamiento social: Pueden imitar hábitos alimenticios de otros ratones.",
            "Reproducción rápida: Hasta 15 camadas al año; crías fértiles a las 5-6 semanas.",
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
        "imagen": SABIASQUE_IMAGES["termitas"],
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
        "imagen": SABIASQUE_IMAGES["hormigas"],
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
        "imagen": SABIASQUE_IMAGES["palomas"],
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
        "imagen": SABIASQUE_IMAGES["chinches"],
        "texto": (
            "Parásitos de sangre; causan picor e irritación. Se esconden en grietas, colchones y muebles. Su control requiere tratamiento especializado."
        ),
        "extra": [
            "Ayuno: Meses sin comer.",
            "Nocturnas: Se alimentan de noche.",
            "Hematófagas: Detectan calor y CO2.",
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
        "imagen": SABIASQUE_IMAGES["pulgas"],
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
        "imagen": SABIASQUE_IMAGES["moscas"],
        "texto": (
            "Comunes pero riesgosas para la salud pública. Se alimentan de materia en descomposición y contaminan alimentos al posarse."
        ),
        "extra": [
            "Ciclo corto: 7-10 días a adulto.",
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
def _species_theme(especie: str) -> dict:
    themes = {
        "Cucarachas": {"icon": ft.Icons.BUG_REPORT, "accent": "#7B3F00", "soft": "#F7E7D6"},
        "Ratas": {"icon": ft.Icons.PEST_CONTROL_RODENT, "accent": "#5B4A3F", "soft": "#EEE7E1"},
        "Ratones": {"icon": ft.Icons.PEST_CONTROL_RODENT, "accent": "#6B5A4A", "soft": "#EFEAE4"},
        "Termitas": {"icon": ft.Icons.HOME_WORK, "accent": "#8A5A2B", "soft": "#F5E8DA"},
        "Hormigas": {"icon": ft.Icons.HUB, "accent": "#8B4513", "soft": "#F5E7DB"},
        "Palomas": {"icon": ft.Icons.CRUELTY_FREE, "accent": "#3F5F7A", "soft": "#E5EEF5"},
        "Chinches": {"icon": ft.Icons.BED, "accent": "#7A2F4B", "soft": "#F5E2EA"},
        "Pulgas": {"icon": ft.Icons.PETS, "accent": "#6E3D2A", "soft": "#F3E6DE"},
        "Moscas": {"icon": ft.Icons.AIR, "accent": "#41616F", "soft": "#E3EFF3"},
    }
    return themes.get(especie, {"icon": ft.Icons.INFO, "accent": "#0F3D47", "soft": "#E7F0F2"})


def _summary_metrics(item: dict) -> list[tuple[str, str]]:
    especie = (item.get("especie") or "").lower()
    metrics_by_species = {
        "cucarachas": [("1 sem", "Sin cabeza"), ("40 min", "Sin respirar"), ("Nocturnas", "Actividad")],
        "ratas": [("80", "Crías/año"), ("0.5 m", "Salto vertical"), ("1 m", "Salto largo")],
        "ratones": [("3 años", "Vida útil"), ("15", "Camadas/año"), ("30 cm", "Salto vertical")],
        "termitas": [("Miles", "Huevos/día"), ("24/7", "Actividad"), ("Alta", "Daño oculto")],
        "hormigas": [("50x", "Su peso"), ("Miles", "Por colonia"), ("Años", "Reina longeva")],
        "palomas": [("100s km", "Orientación"), ("15+", "Años"), ("Todo año", "Cría")],
        "chinches": [("Meses", "Sin comer"), ("Noche", "Actividad"), ("100s", "Huevos")],
        "pulgas": [("200x", "Longitud de salto"), ("50/día", "Huevos"), ("2 sem", "Ciclo rápido")],
        "moscas": [("60+", "Enfermedades"), ("500", "Huevos"), ("7-10 días", "De huevo a adulto")],
    }
    return metrics_by_species.get(especie, [("Alta", "Adaptación"), ("Riesgo", "Sanitario"), ("Clave", "Prevención")])


def _img_height_for(page: ft.Page) -> int:
    if page.width < 480:
        return 160
    elif page.width < 768:
        return 220
    elif page.width < 1200:
        return 280
    else:
        return 320

def _bullet_line(p: str, font_size: int) -> ft.Row:
    if ":" in p:
        head, body = p.split(":", 1)
    else:
        head, body = p, ""
    rich_text = ft.Text(
        spans=[
            ft.TextSpan(
                f"{head.strip()}: ",
                ft.TextStyle(
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
            ),
            ft.TextSpan(body.strip(), ft.TextStyle(color=ft.Colors.BLACK)),
        ],
        size=font_size,
        text_align=ft.TextAlign.LEFT,
    )
    return ft.Row(
        controls=[
            ft.Text("•", size=font_size + 4, color=ft.Colors.BLACK),
            ft.Container(rich_text, expand=True),
        ],
        spacing=6,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )


# --------- Render principal ----------
def render_sabiasque(page: ft.Page, contenedor: ft.Column, items: list | None = None):
    """
    Muestra una CUADRÍCULA de especies; al seleccionar una tarjeta, muestra el DETALLE.
    """
    async def _push_route_async(route: str):
        await page.push_route(route)

    def push_route(route: str):
        page.run_task(_push_route_async, route)

    data = items or SABIASQUE_ITEMS
    contenedor.padding = 0
    contenedor.spacing = 0

    # ---- Métricas responsive para el Grid ----
    def _grid_metrics(page: ft.Page) -> tuple[int, float, int, int]:
        w = page.width
        if w < 480:            # Celular
            return (160, 0.68, 8, 10)
        elif w < 768:          # Tablet
            return (220, 0.90, 10, 12)
        elif w < 1200:         # Laptop
            return (200, 0.96, 10, 12)
        else:                  # Desktop
            return (240, 1.00, 12, 14)

    mx, ar, sp, rsp = _grid_metrics(page)

    grid = ft.GridView(
        max_extent=mx,
        child_aspect_ratio=ar,
        spacing=sp,
        run_spacing=rsp,
    )

    def _apply_grid_metrics():
        mx, ar, sp, rsp = _grid_metrics(page)
        grid.max_extent = mx
        grid.child_aspect_ratio = ar
        grid.spacing = sp
        grid.run_spacing = rsp

    def _tile(idx: int, item: dict, page: ft.Page) -> ft.Container:
        nombre = item.get("especie") or item.get("titulo", f"Item {idx+1}")
        img = item.get("imagen", "")
        w = page.width or 0
        is_big = w >= 600  # tablet / PC
        title_size = 16 if w < 900 else (12 if w < 1600 else 14)
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
            on_click=lambda e, i=idx: push_route(f"/sabiasque/{i}"),
            padding=0,
            content=ft.Column(
                expand=True,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Container(height=4, bgcolor="#123F49"),
                    ft.Container(
                        expand=80,
                        alignment=ft.alignment.center,
                        padding=ft.Padding.only(top=12, left=12, right=12),
                        content=ft.Container(
                            border_radius=18,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            content=ft.Image(src=img, fit=ft.BoxFit.COVER),
                        ),
                    ),
                    ft.Container(
                        expand=20,
                        alignment=ft.alignment.center,
                        padding=ft.Padding.only(left=14, right=14, top=8, bottom=10),
                        content=ft.Text(
                            nombre,
                            size=title_size if is_big else 13,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=1 if w >= 1020 else 2,
                            overflow=ft.TextOverflow.ELLIPSIS,
                            color="#123640",
                        ),
                    ),
                ],
            ),
        )

    # ---- Vista de grilla ----
    def show_grid():
        # Limpieza SEGURA del contenedor (evita errores de remove en Flet)
        while len(contenedor.controls) > 0:
            try:
                contenedor.controls.pop()
            except Exception:
                break

        is_big = (page.width or 0) >= 600  # tablet y PC
        header = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Selecciona la especie",
                        size=28 if is_big else 24,
                        weight=ft.FontWeight.BOLD,
                        color="#0F3D47",
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
            ),
        )


        grid.controls.clear()
        for i, it in enumerate(data):
            grid.controls.append(_tile(i, it, page))

        try:
            _apply_grid_metrics()
        except Exception:
            pass

        sabiasque_column = ft.Column(
            controls=[header, grid],
            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        contenedor.controls.append(
            ft.Container(
                content=sabiasque_column,
                padding=ft.Padding.only(top=4, bottom=8),
                alignment=ft.alignment.center,
            )
        )
        # ðŸ‘ˆ NO llamamos page.update aquÃ­; se hace en el router

    # ---- Vista de detalle ----
    def show_detail(index: int):
        d = data[index]
        img_h = _img_height_for(page)
        theme = _species_theme(d.get("especie", ""))
        metricas = _summary_metrics(d)

        w = page.width or 0
        is_tablet = 600 <= w < 980
        is_desktop = w >= 980
        is_big = w >= 600
        title_size = 33 if is_desktop else (28 if is_tablet else 21)
        subtitle_size = 15 if is_big else 13
        text_size = 17 if is_desktop else (16 if is_tablet else 15)
        bullet_size = 16 if is_big else 14

        badge = ft.Container(
            bgcolor=theme["soft"],
            border_radius=999,
            padding=ft.Padding.symmetric(horizontal=14, vertical=8),
            content=ft.Row(
                spacing=8,
                tight=True,
                controls=[
                    ft.Icon(theme["icon"], size=18, color=theme["accent"]),
                    ft.Text(d.get("especie", "Especie"), size=subtitle_size, weight=ft.FontWeight.BOLD, color=theme["accent"]),
                ],
            ),
        )

        titulo = ft.Text(
            d.get("titulo", d.get("especie", "Detalle")),
            size=title_size,
            weight=ft.FontWeight.BOLD,
            color="#122531",
            text_align=ft.TextAlign.CENTER,
        )

        resumen = ft.Container(
            bgcolor="#F5F8FA",
            border_radius=18,
            padding=ft.Padding.symmetric(horizontal=18, vertical=16),
            content=ft.Text(
                d.get("texto", ""),
                size=text_size,
                color=ft.Colors.BLACK_87,
                text_align=ft.TextAlign.LEFT,
            ),
        )

        tablet_intro = ft.Container(
            bgcolor=theme["soft"],
            border_radius=16,
            padding=ft.Padding.symmetric(horizontal=14, vertical=12),
            content=ft.Column(
                spacing=6,
                controls=[
                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.NEWSPAPER, size=16, color=theme["accent"]),
                            ft.Text("Dato destacado", size=subtitle_size, weight=ft.FontWeight.BOLD, color=theme["accent"]),
                        ],
                    ),
                    ft.Text(
                        (d.get("extra", [""])[0].split(":", 1)[1].strip() if d.get("extra") and ":" in d.get("extra", [""])[0] else d.get("texto", ""))[:130] + "...",
                        size=bullet_size - 1,
                        color=ft.Colors.BLACK_87,
                        text_align=ft.TextAlign.LEFT,
                    ),
                ],
            ),
        )

        metric_cards = []
        for valor, label in metricas:
            metric_cards.append(
                ft.Container(
                    col={"xs": 12, "sm": 4},
                    bgcolor=ft.Colors.WHITE,
                    border_radius=18,
                    padding=ft.Padding.symmetric(horizontal=12, vertical=14),
                    shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK_12, offset=ft.Offset(0, 3)),
                    content=ft.Column(
                        spacing=4,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(valor, size=20 if is_big else 18, weight=ft.FontWeight.BOLD, color=theme["accent"], text_align=ft.TextAlign.CENTER),
                            ft.Text(label, size=subtitle_size, color=ft.Colors.BLACK_87, text_align=ft.TextAlign.CENTER),
                        ],
                    ),
                )
            )

        stats = ft.ResponsiveRow(columns=12, spacing=10, run_spacing=10, controls=metric_cards)

        destacados = d.get("extra", [])[:3]
        resto = d.get("extra", [])[3:]

        highlight_cards = []
        for texto in destacados:
            head = texto.split(":", 1)[0].strip()
            body = texto.split(":", 1)[1].strip() if ":" in texto else texto
            highlight_cards.append(
                ft.Container(
                    col={"xs": 12, "md": 4},
                    bgcolor=theme["soft"],
                    border_radius=18,
                    padding=ft.Padding.symmetric(horizontal=14, vertical=14),
                    content=ft.Column(
                        spacing=6,
                        controls=[
                            ft.Row(
                                spacing=8,
                                controls=[
                                    ft.Icon(theme["icon"], size=16, color=theme["accent"]),
                                    ft.Text(head, size=subtitle_size, weight=ft.FontWeight.BOLD, color=theme["accent"]),
                                ],
                            ),
                            ft.Text(body, size=bullet_size, color=ft.Colors.BLACK_87, text_align=ft.TextAlign.LEFT),
                        ],
                    ),
                )
            )

        hallazgos = ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            padding=ft.Padding.symmetric(horizontal=18, vertical=18),
            shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK_12, offset=ft.Offset(0, 3)),
            content=ft.Column(
                spacing=12,
                controls=[
                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.LIGHTBULB, size=18, color=theme["accent"]),
                            ft.Text("Hallazgos clave", size=subtitle_size + 1, weight=ft.FontWeight.BOLD, color=theme["accent"]),
                        ],
                    ),
                    ft.ResponsiveRow(columns=12, spacing=12, run_spacing=12, controls=highlight_cards),
                    ft.Column(
                        controls=[_bullet_line(p, bullet_size) for p in resto],
                        spacing=6,
                    ),
                ],
            ),
        )

        image_card = ft.Container(
            bgcolor="#FBFCFD",
            border_radius=22,
            padding=ft.Padding.symmetric(horizontal=20, vertical=16),
            alignment=ft.alignment.center,
            content=ft.Image(
                src=d.get("imagen", ""),
                fit=ft.BoxFit.CONTAIN,
                height=img_h if not is_big else (img_h if is_tablet else img_h + 30),
                opacity=1.0,
            ),
        )

        tablet_side_facts = []
        for texto in (d.get("extra", [])[:2] if d.get("extra") else []):
            head = texto.split(":", 1)[0].strip()
            body = texto.split(":", 1)[1].strip() if ":" in texto else texto
            tablet_side_facts.append(
                ft.Container(
                    bgcolor=theme["soft"],
                    border_radius=16,
                    padding=ft.Padding.symmetric(horizontal=12, vertical=12),
                    content=ft.Column(
                        spacing=6,
                        controls=[
                            ft.Row(
                                spacing=8,
                                controls=[
                                    ft.Icon(theme["icon"], size=15, color=theme["accent"]),
                                    ft.Text(head, size=subtitle_size, weight=ft.FontWeight.BOLD, color=theme["accent"]),
                                ],
                            ),
                            ft.Text(body, size=bullet_size - 1, color=ft.Colors.BLACK_87, text_align=ft.TextAlign.LEFT),
                        ],
                    ),
                )
            )

        tablet_side_panel = ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            padding=ft.Padding.symmetric(horizontal=14, vertical=14),
            shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK_12, offset=ft.Offset(0, 3)),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.ARTICLE, size=18, color=theme["accent"]),
                            ft.Text("Perfil rapido", size=subtitle_size + 1, weight=ft.FontWeight.BOLD, color=theme["accent"]),
                        ],
                    ),
                    *tablet_side_facts,
                ],
            ),
        )

        if is_desktop:
            top_section = ft.Row(
                spacing=24,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Container(
                        expand=7,
                        content=ft.Column(
                            spacing=16,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            controls=[badge, titulo, resumen, stats],
                        ),
                    ),
                    ft.Container(expand=5, content=image_card),
                ],
            )
        elif is_tablet:
            top_section = ft.Column(
                spacing=16,
                controls=[
                    ft.Row(
                        spacing=18,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Container(
                                expand=6,
                                content=ft.Column(
                                    spacing=12,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                    controls=[badge, titulo, tablet_intro],
                                ),
                            ),
                            ft.Container(
                                expand=4,
                                content=image_card,
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=18,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Container(
                                expand=6,
                                content=ft.Column(
                                    spacing=14,
                                    controls=[resumen, stats],
                                ),
                            ),
                            ft.Container(
                                expand=4,
                                content=tablet_side_panel,
                            ),
                        ],
                    ),
                ],
            )
        else:
            top_section = ft.Column(
                spacing=14,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[badge, titulo, image_card, resumen, stats],
            )

        bloque = ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=18,
            padding=20,
            shadow=ft.BoxShadow(1, 10, ft.Colors.BLACK_12, offset=ft.Offset(0, 4)),
            content=ft.Column(
                spacing=18,
                controls=[top_section, hallazgos],
            ),
        )

        detail_view = ft.ListView(
            spacing=8,
            controls=[bloque],
            auto_scroll=False,
        )

        # Limpieza segura
        while len(contenedor.controls) > 0:
            try:
                contenedor.controls.pop()
            except Exception:
                break

        contenedor.controls.append(
            ft.Container(
                content=detail_view,
                padding=ft.Padding.only(top=4, bottom=8),
            )
        )
        # ðŸ‘ˆ NO llamamos page.update aquÃ­; se hace en el router

    # ---- Router interno de Sabías que ----
    def on_route_change(e: ft.RouteChangeEvent):
        route = (e.route or "/sabiasque").strip()
        if route.startswith("/sabiasque/"):
            try:
                idx = int(route.split("/")[-1])
            except ValueError:
                idx = 0
            show_detail(idx)
        else:
            show_grid()

    def _reset_to_grid():
        page.route = "/sabiasque"   
        show_grid()

    # Exponer helpers al page para usarlos desde main.py
    setattr(page, "_sabiasque_reset_to_grid", _reset_to_grid)
    setattr(page, "_sabiasque_router", on_route_change)
    setattr(page, "_sabiasque_show_grid", show_grid)
    setattr(page, "_sabiasque_show_detail", show_detail)

