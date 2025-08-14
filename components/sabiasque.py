# components/sabiasque.py
import flet as ft


# Puedes cambiar/expandir estos items cuando quieras
SABIASQUE_ITEMS = [
    {
        "titulo": "¿Sabías que las cucarachas pueden vivir hasta una semana sin su cabeza?",
        "imagen": "https://www.gardentech.com/-/media/project/oneweb/gardentech/images/pest-id/bug-pest/cockroach.png",
        "texto": (
            "Las cucarachas son plagas muy resistentes y adaptables, con diversas curiosidades que las hacen fascinantes y problemáticas. "
            "Son capaces de sobrevivir sin cabeza por un tiempo, soportan altos niveles de radiación y pueden sobrevivir sin comida por semanas o sin agua por días. "
            "Además, pueden transmitir enfermedades y son atraídas por la comida y la humedad, lo que las convierte en una amenaza para la salud y la higiene. "
            "Algunas especies de cucarachas pueden vivir hasta un mes sin comida, adaptándose fácilmente a diferentes entornos, "
            "pueden correr hasta 3 millas por hora, lo que las hace muy difíciles de atrapar. Su velocidad y agilidad les permiten escapar " 
            "rápidamente de los depredadores y de los intentos de captura. Además, son capaces de girar rápidamente en ángulos agudos y esconderse en espacios reducidos. " 
            "esta capacidad de supervivencia las convierte en una de las plagas más resistentes y difíciles de eliminar. "
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
        "titulo": "¿Sabías que una sola rata puede producir hasta 2,000 descendientes en un año si no se controla su población?",
        "imagen": "https://i.postimg.cc/X7Dt0Tf1/istockphoto-1413873422-612x612.jpg",
        "texto": (
            "Las ratas tienen una gran capacidad reproductiva y, sin medidas de control, "
            "pueden convertirse rápidamente en una infestación grave. Además de los daños "
            "materiales, son portadoras de enfermedades peligrosas."
        ),
         "extra": [
        "Adaptabilidad: Las ratas pueden sobrevivir en diversos ambientes, desde alcantarillas hasta edificios, y son capaces de aplanar su cuerpo para pasar por espacios reducidos.",
        "Reproducción rápida: Una rata hembra puede tener hasta 80 crías al año, lo que lleva a infestaciones rápidamente.",
        "Transmisión de enfermedades: Las ratas transmiten enfermedades como leptospirosis, salmonelosis, peste, entre otras, a través de sus excrementos, orina y saliva.",
        "Daños estructurales: Las ratas pueden roer cables, tuberías, madera y otros materiales, causando daños a edificios y riesgo de incendios o cortocircuitos.",
        "Contaminación de alimentos: Las ratas pueden contaminar alimentos con sus excrementos y orina, lo que representa un riesgo para la salud humana.",
        "Resistencia a venenos: Algunas ratas han desarrollado resistencia a ciertos rodenticidas, lo que dificulta su control.",
        "Habilidades de natación y escalada: Las ratas son buenas nadadoras y trepadoras, lo que les permite acceder a lugares de difícil acceso.",
        "Sentido del olfato desarrollado: La rata noruega tiene un sentido del gusto muy desarrollado, lo que le permite detectar sustancias químicas en bajas concentraciones.",
        "Miedo a los depredadores: Las ratas huyen de los olores de sus depredadores, como los gatos, que contienen un compuesto químico que les causa miedo.",
        "Capacidad de saltar: Pueden saltar verticalmente hasta medio metro y horizontalmente aproximadamente un metro."
        ]
    },
    {
        "titulo": "¿Sabías que los ratones pueden vivir hasta tres años en condiciones favorables, aumentando el riesgo de infestación si no se controla?",
        "imagen": "https://i.postimg.cc/FsrS6xC9/raton-campo-mus-musculus-768x576.jpg",
       "texto": (
        "Los ratones, como plaga, tienen varias características curiosas. "
        "Son excelentes trepadores y nadadores, pueden saltar hasta 30 centímetros de altura y son muy ágiles. "
        "Además, pueden roer materiales como cemento y vidrio. "
        "También son prolíficos, con hembras capaces de tener múltiples camadas al año, "
        "y pueden reproducirse a partir de las seis semanas de edad. "
        "Los ratones también son portadores de enfermedades y pueden contaminar alimentos y superficies "
        "con sus excrementos y orina."
    ),
    "extra": [
        "Agilidad y acrobacias: Son muy ágiles, capaces de trepar por diversas superficies, caminar sobre cuerdas y cables gracias a su cola, y saltar bastante alto.",
        "Roedores versátiles: Pueden roer materiales como cemento, vidrio y aluminio, lo que les permite acceder a diferentes lugares y construir sus nidos.",
        "Comportamiento social: Los ratones pueden ser influenciados por la presión social, llegando a comer alimentos que no les gustan si observan que otros ratones los están consumiendo, según Carolina Pest.",
        "Reproducción rápida: Las hembras pueden tener hasta 15 camadas al año, y las crías pueden empezar a reproducirse a las 5-6 semanas de edad, lo que facilita la rápida expansión de una plaga, según Fox Pest Control.",
        "Transmisión de enfermedades: Los ratones pueden transmitir enfermedades a través de sus excrementos, orina, saliva y mordeduras. Algunas enfermedades que pueden transmitir son salmonelosis, hantavirus, tularemia, coriomeningitis linfocítica y peste bubónica.",
        "Transporte de parásitos: Los ratones pueden ser portadores de parásitos como pulgas, garrapatas y piojos, que pueden causar problemas adicionales de salud.",
        "Adaptación a diversos ambientes: Pueden sobrevivir en diferentes condiciones, incluso sin acceso directo al agua, ya que obtienen la humedad necesaria de sus alimentos.",
        "Comunicación ultrasónica: Los ratones se comunican entre sí utilizando ultrasonidos, frecuencias que los humanos no pueden oír.",
        "Capacidad de memoria: Pueden memorizar rutas y resolver acertijos, lo que les ayuda a encontrar refugio y comida.",
        "Nocturnidad: Los ratones son principalmente activos durante la noche, lo que dificulta su detección y control."
        ]
    },
    {
        "titulo": "¿Sabías que las termitas nunca duermen?",
        "imagen": "https://i.postimg.cc/wjVRQRQ1/termitas-1.png",
       "texto": (
        "Las termitas, aunque son importantes descomponedores en la naturaleza, "
        "pueden convertirse en una plaga destructiva para estructuras de madera. "
        "Algunos datos curiosos sobre las termitas como plaga incluyen su capacidad "
        "para reproducirse rápidamente, su preferencia por la madera como alimento, "
        "y su habilidad para causar daños significativos en poco tiempo."
    ),
        "extra": [
        "Alta tasa de reproducción: Una colonia de termitas puede tener millones de individuos, y la reina puede poner miles de huevos al día.",
        "Comportamiento social: Viven en colonias complejas con diferentes castas (obreras, soldados, reproductores) que cumplen funciones específicas.",
        "Destrucción silenciosa: Las termitas pueden dañar estructuras de madera sin ser detectadas hasta que el daño es considerable.",
        "Preferencias alimenticias: Las termitas se alimentan principalmente de madera y otros materiales que contienen celulosa, como papel y cartón.",
        "Daños estructurales: Pueden debilitar la estructura de edificios, casas y muebles, causando daños costosos de reparar.",
        "Adaptabilidad: Pueden adaptarse a diferentes ambientes y condiciones, lo que les permite infestar una variedad de estructuras.",
        "Comunicación por feromonas: Utilizan feromonas para comunicarse entre sí, lo que facilita la coordinación dentro de la colonia.",
        "Importancia ecológica: Aunque son plagas en entornos urbanos, en la naturaleza son importantes descomponedores de materia orgánica.",
        "Pueden vivir en la oscuridad: Algunas especies de termitas, como las subterráneas, viven en la oscuridad y buscan la humedad para desarrollarse.",
        "No son insectos sociales: Aunque viven en colonias, no son insectos sociales en el sentido de que no tienen una jerarquía social compleja como las abejas o las hormigas."
        ]
    },
    {
    "titulo": "¿Sabías que un nido de hormigas puede contener hasta cientos de miles de hormigas?",
    "imagen": "https://i.postimg.cc/QCGM3jqL/hormiga-eliminar-plaga.jpg",
    "texto": (
        "Las hormigas son plagas comunes en hogares y jardines, y aunque son fascinantes "
        "por su organización social y fuerza, su presencia puede ser molesta. "
        "Algunas curiosidades sobre las hormigas como plaga incluyen su capacidad "
        "para encontrar fuentes de alimento y agua en las casas, su habilidad para construir "
        "nidos en lugares inesperados como paredes y madera, y su potencial para causar "
        "daños a estructuras de madera, como las hormigas carpinteras."
    ),
    "extra": [
        "Organización social compleja: Viven en colonias estructuradas con castas como obreras, soldados y reinas, cada una con funciones específicas.",
        "Comunicación por feromonas: Se comunican químicamente para marcar rutas hacia fuentes de alimento y alertar sobre peligros.",
        "Gran fuerza física: Una hormiga puede levantar hasta 50 veces su peso corporal.",
        "Capacidad de invasión: Pueden ingresar a las viviendas a través de grietas muy pequeñas en busca de comida y agua.",
        "Hormigas carpinteras: Algunas especies, como las carpinteras, excavan madera para construir nidos, debilitando estructuras.",
        "Resistencia: Pueden adaptarse a diferentes ambientes, desde climas tropicales hasta zonas frías.",
        "Trabajo en equipo: Colaboran para transportar objetos grandes y defender la colonia.",
        "Longevidad de la reina: Algunas reinas pueden vivir varios años, produciendo miles de crías.",
        "Construcción de nidos: Pueden edificar nidos en tierra, paredes, techos e incluso aparatos eléctricos.",
        "Impacto en la salud: Algunas especies pueden morder o picar, y contaminar alimentos con bacterias."
    ]
    },
    {
    "titulo": "¿Sabías que las palomas pueden reconocer rostros humanos?",
    "imagen": "https://a.files.bbci.co.uk/worldservice/live/assets/images/2015/11/20/151120130815_paloma2_624x351_thinkstock_nocredit.jpg",
    "texto": (
        "Las palomas, aunque son aves comunes en ciudades y pueblos, pueden convertirse en una plaga problemática. "
        "Son conocidas por su capacidad de adaptarse al entorno urbano, encontrar alimento fácilmente y anidar en edificios. "
        "Además de causar daños estructurales con sus nidos y excrementos, pueden transmitir enfermedades a los humanos "
        "y atraer otros parásitos como ácaros y pulgas."
    ),
    "extra": [
        "Alta capacidad de orientación: Pueden encontrar su camino a casa desde cientos de kilómetros de distancia.",
        "Transmisión de enfermedades: Pueden portar patógenos como la histoplasmosis, criptococosis y psitacosis.",
        "Daños estructurales: Sus excrementos son corrosivos y pueden deteriorar piedra, metal y pintura.",
        "Reproducción continua: Pueden criar durante todo el año en climas templados.",
        "Alimentación oportunista: Comen restos de comida humana, granos y semillas.",
        "Atracción de parásitos: Sus nidos pueden albergar ácaros, pulgas y garrapatas.",
        "Contaminación de agua: Sus excrementos pueden ensuciar fuentes y sistemas de agua.",
        "Longevidad: En cautiverio pueden vivir más de 15 años, en libertad suelen vivir menos.",
        "Reconocimiento visual: Estudios han demostrado que pueden identificar y recordar rostros humanos.",
        "Capacidad de adaptación: Se adaptan a casi cualquier entorno urbano o rural."
    ]
    },
    {
    "titulo": "¿Sabías que las chinches pueden sobrevivir meses sin alimentarse?",
    "imagen": "https://i.postimg.cc/7YPC9MmS/chinche-cimex-lectularius.jpg",
    "texto": (
        "Las chinches de cama son insectos parásitos que se alimentan de sangre humana y de animales. "
        "A pesar de su pequeño tamaño, pueden causar gran incomodidad debido a sus picaduras, que suelen provocar picor e irritación. "
        "Son expertas en esconderse en grietas, colchones, muebles y ropa, y su control requiere un tratamiento especializado."
    ),
    "extra": [
        "Resistencia al ayuno: Pueden vivir varios meses sin alimentarse, lo que dificulta su erradicación.",
        "Actividad nocturna: Son más activas durante la noche, cuando salen a alimentarse.",
        "Preferencia por la sangre: Se alimentan exclusivamente de sangre, detectando a su huésped por el calor y el dióxido de carbono.",
        "Difícil detección: Su tamaño reducido y habilidad para esconderse las hace difíciles de encontrar.",
        "Reproducción rápida: Una hembra puede poner cientos de huevos en su vida.",
        "Dispersión fácil: Pueden trasladarse en ropa, equipaje y muebles, propagando infestaciones.",
        "Resistencia a insecticidas: Algunas poblaciones han desarrollado resistencia a productos comunes.",
        "Ausencia de transmisión de enfermedades: Aunque molestan, no se ha demostrado que transmitan enfermedades a humanos.",
        "Señales de infestación: Manchas oscuras en sábanas o muebles, pieles mudadas y un olor dulce característico.",
        "Difíciles de erradicar: Requieren tratamientos integrales y, en muchos casos, ayuda profesional."
    ]
    },
    {
    "titulo": "¿Sabías que el 50 porciento de las picaduras de pulgas pueden producir reacciones alérgicas graves en algunas personas?",
    "imagen": "https://www.gardentech.com/-/media/project/oneweb/gardentech/images/pest-id/alt-bug/flea.jpg",
    "texto": (
        "Las pulgas son pequeños insectos parásitos que se alimentan de la sangre de mamíferos y aves. "
        "A pesar de su tamaño diminuto, son capaces de causar grandes molestias debido a sus picaduras, que provocan picor intenso e irritación. "
        "Pueden transmitir enfermedades y parásitos, como la tenia, y se reproducen rápidamente, infestando mascotas y hogares."
    ),
    "extra": [
        "Capacidad de salto: Pueden saltar hasta 200 veces la longitud de su cuerpo, lo que les facilita desplazarse entre huéspedes.",
        "Ciclo de vida rápido: Pueden pasar de huevo a adulto en tan solo dos semanas en condiciones favorables.",
        "Resistencia al hambre: Los adultos pueden sobrevivir semanas sin alimentarse.",
        "Transmisión de enfermedades: Pueden transmitir peste bubónica, tifus murino y parásitos intestinales como la tenia.",
        "Adaptabilidad: Pueden infestar perros, gatos, roedores, aves y, ocasionalmente, humanos.",
        "Huevos resistentes: Los huevos pueden caer en alfombras, camas y grietas, donde permanecen hasta que las condiciones son adecuadas.",
        "Prolificidad: Una hembra puede poner hasta 50 huevos al día.",
        "Sensibilidad a vibraciones: Detectan el movimiento y calor de los posibles huéspedes a través de vibraciones y cambios de temperatura.",
        "Dificultad de control: Requieren tratamientos combinados para eliminar adultos, larvas y huevos.",
        "Picaduras agrupadas: Sus picaduras suelen aparecer en grupos o líneas, especialmente en piernas y tobillos."
    ]
    },
    {
    "titulo": "¿Sabías que las moscas domésticas pueden transmitir más de 60 enfermedades?",
    "imagen": "https://i.postimg.cc/3wZN2kmt/white-Photoroom-1.png",
    "texto": (
        "Las moscas son insectos comunes que, aunque parecen inofensivas, representan un riesgo para la salud pública. "
        "Se alimentan de materia orgánica en descomposición, basura y heces, y pueden contaminar alimentos y superficies "
        "al posarse sobre ellas. Son rápidas, difíciles de atrapar y se reproducen en grandes cantidades, lo que las convierte en una plaga persistente."
    ),
    "extra": [
        "Ciclo de vida corto: Pueden pasar de huevo a adulto en tan solo 7 a 10 días en condiciones cálidas.",
        "Reproducción masiva: Una hembra puede poner hasta 500 huevos en su vida.",
        "Transmisión de enfermedades: Propagan salmonelosis, disentería, cólera y otras infecciones.",
        "Hábitos alimenticios: Vomitan enzimas sobre los alimentos para digerirlos antes de ingerirlos.",
        "Adaptabilidad: Pueden sobrevivir en casi cualquier entorno con acceso a alimento y humedad.",
        "Resistencia: Las larvas (gusanos) pueden vivir en materia orgánica en descomposición y aguas residuales.",
        "Alcance de vuelo: Pueden recorrer varios kilómetros en busca de comida.",
        "Atracción por olores: Se sienten atraídas por olores fuertes, especialmente de comida en descomposición.",
        "Riesgo para la higiene: Contaminan alimentos y utensilios al posarse sobre ellos después de estar en basura o heces.",
        "Actividad diurna: Son más activas durante el día, especialmente en climas cálidos."
    ]
    },
]


def _img_height_for(page: ft.Page) -> int:
    """Altura de imagen adaptada a celulares, tablets y PCs."""
    if page.width < 480:      # Celulares pequeños
        return 160
    elif page.width < 768:    # Celulares grandes / Tablets pequeñas
        return 220
    elif page.width < 1200:   # Tablets grandes / Laptops
        return 280
    else:                     # Monitores grandes
        return 350


def render_sabiasque(page: ft.Page, contenedor: ft.Column, items: list | None = None):
    """
    Reemplaza el contenido principal por la sección 'Sabías que'.
    - page: ft.Page
    - contenedor: normalmente tu Column 'contenido'
    - items: lista de curiosidades (opcional). Si no se pasa, usa SABIASQUE_ITEMS.
    """
    data = items or SABIASQUE_ITEMS
    img_h = _img_height_for(page)

    # Asegura que el contenedor principal no deje espacios arriba/entre bloques
    contenedor.padding = 0
    contenedor.spacing = 0

    bloques: list[ft.Control] = []
    def _split_extra_item(p: str) -> tuple[str, str]:
        if ":" in p:
            head, tail = p.split(":", 1)
            return head.strip(), tail.strip()
        return p.strip(), ""


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
            controls=[
                ft.Text("•", size=18, color=ft.Colors.BLACK),
                ft.Container(rich_text, expand=True)  # hace wrap ocupando todo el ancho disponible
            ],
            spacing=6,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    
    for i, d in enumerate(data):
        # Separación SOLO entre bloques (no arriba del primero)
        if i > 0:
            bloques.append(ft.Container(height=12))  # pequeño espacio entre tarjetas

        bloque = ft.Container(
            # Ocupa todo el ancho disponible
            width=page.width,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            padding=12,
            margin=ft.margin.only(left=0, right=0, top=0, bottom=0),
            shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK12, offset=ft.Offset(2, 2)),
            content=ft.Column(
                [
                    ft.Text(
                        d["titulo"],
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=d["imagen"],
                            fit=ft.ImageFit.COVER,
                            border_radius=8,
                        ),
                        height=img_h,
                        border_radius=8,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        expand=True,
                    ),
                    ft.Text(
                        d["texto"],
                        size=15,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.JUSTIFY
                    ),
                    ft.Column(
                        controls=[_bullet_line(p) for p in d.get("extra", [])],
                        spacing=4,
                        expand=True,
                    )
                ],
                spacing=10,
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        bloques.append(bloque)

    contenedor.controls.clear()
    contenedor.controls.append(
        ft.Column(
            bloques,
            spacing=0,                   # sin huecos añadidos
            expand=True,
            scroll=ft.ScrollMode.AUTO,   # scroll si hace falta
        )
    )
    contenedor.update()
