import json
import flet as ft
import asyncio
import os

async def main(page: ft.Page):
    page.title = "Demo Menú Empresa"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0

    # Variable para activar o desactivar carrusel de imagen
    carrusel_activo = True

    # Variable para llevar el control del slide (posiciones para deslizar)
    slide_actual = 0  

    # Usamos lista para mutabilidad, inicializamos la variable 
    animacion_empresa_task = [None]  
    animacion_insectos_task = [None]

    # Imagen del Logo de Bienvenida
    imagen_logo = ft.Container(
        content=ft.Image(src="https://i.postimg.cc/8PvSgg5x/logo-mobile-dark.png", fit=ft.ImageFit.COVER),
        width=256,
        height=128,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.top_center,   # ⬅️ Esto lo alinea arriba
    )
    # Funcion para cerrar la pantalla de Bienvenida
    def close_intro(e):
        intro_modal.visible = False
        page.update()
    
    # Intro de la pagina
    intro_modal = ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLACK54,  # fondo semitransparente
        alignment=ft.alignment.center,
        content=ft.Container(
            width=350,
            height=430,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            padding=20,
            content=ft.Column([
                # Botón de cierre (X)
                ft.Row([
                    ft.Text("", expand=True),  # empuja la X a la derecha
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        on_click=close_intro,
                        icon_color=ft.Colors.BLACK
                    )
                ]),
                # Logo en la parte superior
                imagen_logo,
                # Título en negro y negrita
                ft.Text(
                    "¡Bienvenidos!",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),
                ft.Text(
                    "Aquí encontrarás todo lo referente al control de plagas profesional "
                    "navega por la página y usa los botones para contactarte.",
                    color=ft.Colors.BLACK
                ),
                # Descripción en negro y negrita
                ft.Text(
                    "Si deseas obtener más información referente a la empresa "
                    "has clic sobre el botón ubicado en la esquina superior derecha.",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )
    )

    # Imagenes visibles para el Carrusel 
    imagenes_visibles = [ft.Image(width=110, height=70, fit=ft.ImageFit.COVER, border_radius=8)
                         for _ in range(3)]
    # Fila Para Carrusel de Imagenes
    fila_carrusel = ft.Row(controls=imagenes_visibles, scroll="always", spacing=10)
    #Imagenes para El Carrusel
    sets_imagenes = [
        ["https://irp.cdn-website.com/fe74ab3f/dms3rep/multi/3-c76791a1.jpg", "https://inoclean.cl/wp-content/uploads/2021/12/Plagas.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXeZ7ElGw51_JF6TZuylsCHQcXd-e_GyV7mA&s"],
        ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxriBp7gAvC3DeO0ZsaDqinL-7dZCJ_ulUmx_B3ad-QOo911PD0nwmsyZFBF3dK_bTzsw&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTimFMgOc-bNR1xeYjxD__RbzP0LApis-ovRuggm-TM0CPZl6OBeSj8TCc3Ph1sYVIjhcg&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAF2blxqmgt_0N7htQAMCDfn8thMHzWPy0z9a7_tdSsSgxDzYD9GiinavAWy8CpM7Ndl0&usqp=CAU"],
    ]
    # Funcion para rotar las imagenes del Carrusel
    async def rotar_sets():
        idx = 0
        while True:
            if carrusel_activo and fila_carrusel in contenido.controls:
                for i, img in enumerate(imagenes_visibles):
                    img.src = sets_imagenes[idx][i]
                    img.update()
                await asyncio.sleep(3)
                idx = (idx + 1) % len(sets_imagenes)
            else:
                await asyncio.sleep(0.5)


    # Contactos Redes Sociales
    contacto_whatsapp = f"https://wa.me/{"+56937539304"}?text=Hola"
    contacto_instagram = "https://instagram.com/evermountsolutions"
    contacto_facebook = "https://facebook.com/evermountsolutions"

    # Imagenes de los Botones
    imagen_boton_whatsapp = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
        fit=ft.ImageFit.COVER,
        scale=1.0, animate_scale=200, tooltip="Contáctanos por WhatsApp"
    )

    imagen_boton_empresa = ft.Image(
        src= "https://i.postimg.cc/rFxRRS5D/logo-72x72.png", fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Menú Empresa"
    )
    
    imagen_boton_instagram = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg",
        fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Síguenos en Instagram"
    )

    imagen_boton_facebook = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/b/b9/2023_Facebook_icon.svg",
        width=60, height=60, fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Síguenos en Facebook"
    )
    # Funcion para alternar animacion de botones
    async def animacion_alternada():
     while True:
        for img in [imagen_boton_whatsapp, imagen_boton_instagram,imagen_boton_facebook]:
            img.scale = 1.2
            img.update()
            await asyncio.sleep(0.4)
            img.scale = 1.0
            img.update()
            await asyncio.sleep(0.4)

    # Funcion para animar todo el boton_empresa
    async def animar_empresa_ciclo():
        while True:
            container_boton_empresa.scale = 1.18
            container_boton_empresa.update()
            await asyncio.sleep(0.7)
            container_boton_empresa.scale = 1.0
            container_boton_empresa.update()
            await asyncio.sleep(0.7)
    
    # Funcion para animar las imagenes de los insectos
    async def animar_insectos_ciclo(imagenes):
        try:
            while True:
                for img in imagenes:
                    img.scale = 1.17
                    img.update()
                await asyncio.sleep(0.4)
                for img in imagenes:
                    img.scale = 1.0
                    img.update()
                await asyncio.sleep(0.4)
        except Exception:
            # Puede ser cancelada si se cambia de slide
            pass


    # Funcion animacion Botones redes sociales 
    def animar_boton_whatsapp(e):
        imagen_boton_whatsapp.scale = 1.1 if e.data=="true" else 1.0
        imagen_boton_whatsapp.update()   
    def animar_boton_instagram(e):
        imagen_boton_instagram.scale = 1.1 if e.data=="true" else 1.0
        imagen_boton_instagram.update()   
    def animar_boton_facebook(e):
        imagen_boton_facebook.scale = 1.1 if e.data=="true" else 1.0
        imagen_boton_facebook.update() 

    # Menu de Boton Empresa
    def toggle_menu(e):
        dropdown.visible = not dropdown.visible
        if dropdown.visible:
            # Detiene la animación si está corriendo
            if animacion_empresa_task[0] is not None:
                animacion_empresa_task[0].cancel()
                animacion_empresa_task[0] = None
        else:
            # Relanza la animación solo si no existe
            if animacion_empresa_task[0] is None:
                animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)

        page.update()


    # Boton de Empresa en Barra Superior
    container_boton_empresa = ft.Container(
        content=ft.Container(
            content=imagen_boton_empresa,
            width=50,
            height=50,
            border_radius=25,
            bgcolor=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#ffffff", "#dcdcdc"]
            ),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=ft.Colors.BLACK38,
                offset=ft.Offset(3, 3)
            ),
            on_click=toggle_menu,
            ink=True,
            alignment=ft.alignment.center
        ),
        width=64,
        height=64,
        bgcolor=ft.Colors.BLACK12,  # Fondo circular más visible
        border_radius=32,
        padding=7,  # Espaciado interno
        scale=1.0,            
        animate_scale=200,     
    )

    # Boton de Whatsapp 
    boton_whatsapp = ft.Container(
        content=imagen_boton_whatsapp,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        on_click=lambda _: page.launch_url(contacto_whatsapp),
        on_hover=animar_boton_whatsapp,
        ink=True,
    )

    # Boton de Instagram
    boton_instragram = ft.Container(
        content=imagen_boton_instagram,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        on_click=lambda _: page.launch_url(contacto_instagram),
        on_hover=animar_boton_instagram,
        ink=True,
    )

    # Boton de Facebook
    boton_facebook = ft.Container(
        content=imagen_boton_facebook,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=None,  # sin fondo
        shadow=None,   # sin sombra
        on_click=lambda _: page.launch_url(contacto_facebook),
        on_hover=animar_boton_facebook,
        ink=False,     # sin efecto de tinta
    )
    
    # Contenido central mutable
    contenido = ft.Column(
        [ft.Text("Bienvenido a EvermountSolutions"),
            ft.Text("Control de plagas profesional. Haz clic en los botones."),
            fila_carrusel],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Informacion que tendran los slides (pantallas para deslizar)
    # slides Quienes Somos
    slides_quienes = [
        {
            "titulo": "Bienvenidos!",
            "contenido": [
                "Somos una empresa familiar dedicada con pasión al control y manejo integral de plagas. Fundada por dos hermanos, nuestra misión es proteger hogares, empresas y comunidades con soluciones efectivas, responsables y personalizadas.",
                "Confía en nosotros para mantener tus espacios seguros, limpios y libres de plagas, con tecnología avanzada y atención profesional.",
                "🛡️ Confianza familiar, protección garantizada."
            ]
        },
        {
            "titulo": "Nuestra Filosofía",
            "contenido": [
                "La ética, el profesionalismo y la innovación son pilares de nuestro trabajo.",
                "Cuidamos el medio ambiente y la salud de nuestros clientes."
            ]
        },
    ]

    # slides Historia
    slides_historia = [
        {
            "titulo": "Historia",
            "contenido": [
                "Una historia de compromiso y trabajo en equipo",
                "Evermount Solutions nació de la visión de dos hermanos con una meta común: brindar un servicio de excelencia en el control de plagas, con ética, responsabilidad ambiental y atención cercana.",
                "Contamos con formación técnica, experiencia en terreno y una vocación clara por el servicio. Nuestra empresa combina el profesionalismo de una gran compañía con la calidez de una atención personalizada.",
            ]
        },
        {
            "titulo": "¿Qué nos diferencia?",
            "contenido": [
                "• Somos una empresa certificada y en constante actualización.",
                "• Cada cliente es tratado como si fuera parte de nuestra familia.",
                "• Actuamos con transparencia, eficacia y puntualidad.",
            ]
        }
    ]
    slide_programas_control = [
    {
        "titulo": "Control Periódico, Mensual y Anual",
        "contenido": [
            "Ofrecemos planes de mantenimiento diseñados para mantener tus espacios protegidos durante todo el año. Nos adaptamos a tus necesidades y tipo de actividad (residencial, comercial o industrial).",
            "📆 Visitas programadas con seguimiento",
            "📊 Informes técnicos y certificados de aplicación",
            "🛡️ Control integral de plagas todo el año",
            "🟢 Planes ideales para:",
            "• Restaurantes\n• Supermercados\n• Bodegas\n• Centros educativos\n• Condominios\n• Empresas con auditorías sanitarias"
        ]
    },
       {
        "titulo": "🏠 Desinfección y Sanitización de Ambientes",
        "contenido": [
            "Protege la salud de tu familia, empleados y clientes con nuestros servicios de sanitización profesional. Eliminamos virus, bacterias, hongos y malos olores de forma segura, rápida y eficaz.",
            "🧼 Aplicación con nebulizador ULV o termonebulización",
            "🌱 Uso de productos certificados por ISP y amigables con el medio ambiente",
            "💼 Ideal para hogares, oficinas, clínicas, escuelas y empresas",
            "🚫 Previene contagios y garantiza ambientes más saludables."
        ]
    }
    ]
    slides_servicios = [
    {
        "titulo": "Soluciones eficaces para todo tipo de plagas",
        "contenido": [
            "En Evermount Solutions ofrecemos servicios integrales y adaptados a cada necesidad, tanto para clientes residenciales como comerciales e industriales.",
            "• Control de insectos rastreros (cucarachas, hormigas, chinches, pulgas)",
            "• Control de insectos voladores (moscas, zancudos, avispas)",
            "• Control de roedores (ratones, ratas)",
            "• Tratamiento de termitas",
            "• Tratamiento de aves",
            "• Desinfección y sanitización de ambientes",
            "• Programas de control mensual y anual",
            "🔬 Usamos productos certificados y amigables con el medio ambiente."
        ]
    },
    {
        "titulo": "🪳 Control de Insectos Rastreros",
        "contenido": [
            # Este elemento será un Row o una lista de botones/links
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Cucaracha", "id": "cucarachas"},
                    {"nombre": "Hormiga", "id": "hormigas"},
                    {"nombre": "Chinche", "id": "chinches"},
                    {"nombre": "Pulga", "id": "pulgas"},
                ]
            },
            "Los insectos rastreros no solo causan molestias, sino que también pueden contaminar alimentos y transmitir enfermedades. En Evermount Solutions, utilizamos métodos modernos y productos certificados para erradicar cucarachas, hormigas, chinches de cama y pulgas de forma segura y efectiva.",
            "✅ Diagnóstico personalizado",
            "✅ Tratamientos focalizados y residuales",
            "✅ Técnicas no invasivas, seguras para personas y mascotas",
            "📍Servicio disponible en casas, departamentos, empresas, bodegas y locales comerciales."
        ]
    },
    
    {
        "titulo": "🦟 Control de Insectos Voladores",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Moscas", "id": "moscas"},
                    {"nombre": "Zancudos", "id": "zancudos"},
                    {"nombre": "Avispas", "id": "avispas"},
                ]
            },
            "Los insectos voladores son transmisores de enfermedades y afectan la comodidad en espacios interiores y exteriores. Contamos con soluciones efectivas para controlar moscas, zancudos (mosquitos), avispas y otros insectos voladores, adaptadas a cada tipo de ambiente.",
            "💨 Aplicación con equipos nebulizadores",
            "🌿 Productos biodegradables y de bajo impacto ambiental",
            "🕒 Tratamientos preventivos y de emergencia",
            "Ideal para: casas, patios, restaurantes, empresas de alimentos, jardines y centros de eventos.",
        ]
    },
    {
        "titulo": "🐀 Control de Roedores",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Ratón", "id": "raton"},
                    {"nombre": "Rata", "id": "rata"},
                ]
            },
            "Los roedores son una de las plagas más peligrosas por los daños estructurales que causan y las enfermedades que transmiten. Nuestro servicio de desratización incluye diagnóstico, control activo y sellado de accesos.",
            "🔍 Inspección detallada para detectar nidos y rutas",
            "🧠 Estrategias inteligentes: cebos, trampas, estaciones seguras",
            "🚪 Recomendaciones de cierre y sellado estructural",
            "💡 Mantenemos tu propiedad libre de roedores con mínima interrupción."
        ]
    },
    {
        "titulo": "🐜 Tratamiento de Termitas",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Subterránea", "id": "termita_subterranea"},
                    {"nombre": "Madera seca", "id": "termita_madera_seca"},
                    {"nombre": "Otras especies", "id": "termita_otros"},
                ]
            },
            "Las termitas pueden causar daños estructurales graves en viviendas, empresas y construcciones de madera si no se detectan y tratan a tiempo. En Evermount Solutions - Pest Defense realizamos tratamientos especializados para eliminar termitas y proteger tus estructuras a largo plazo.",
            "🔍 Diagnóstico técnico con detección de actividad y daños",
            "🏠 Tratamientos localizados e integrales (perimetrales y estructurales)",
            "🧪 Uso de termiticidas de última generación aprobados por ISP",
            "🔄 Programas de monitoreo post-tratamiento",
            "💡 Ideal para casas, cabañas, construcciones nuevas, bodegas, colegios y centros comerciales."
        ]
    },
    {
    "titulo": "🕊️ Control de Aves Urbanas",
    "contenido": [
        {
            "tipo": "clickable_row",
            "items": [
                {"nombre": "Palomas", "id": "palomas"},
                {"nombre": "Tórtolas", "id": "tortolas"},
                {"nombre": "Gorriones", "id": "gorriones"},
                {"nombre": "Otras especies", "id": "aves_otros"},
            ]
        },
        "Las aves pueden convertirse en una plaga cuando anidan en techos, cornisas, galpones o equipos de ventilación, generando suciedad, malos olores y riesgos sanitarios. Nuestro servicio de control de aves está diseñado para alejar sin dañar, utilizando métodos seguros y autorizados.",
        "⚙️ Instalación de sistemas anti-posamiento (pinchos, redes, tensores, gel repelente)",
        "🚫 Prevención de anidación y acumulación de excrementos",
        "📋 Inspección técnica y asesoría personalizada",
        "🌿 Soluciones éticas y respetuosas con la fauna",
        "🛠️ Recomendado para: industrias, iglesias, colegios, techos de viviendas, galpones, restaurantes y edificios públicos."
    ]
    },
    # ...puedes agregar más slides aquí
    ]
    
    #diccionario de insectos
    info_insectos = {
        "cucarachas": {
            "titulo": "Cucarachas",
            "descripcion": "Las cucarachas son una de las plagas más comunes. Se reproducen rápidamente y pueden transmitir enfermedades. Eliminamos todo tipo de cucarachas utilizando cebos, geles y productos seguros para personas y mascotas."
        },
        "hormigas": {
            "titulo": "Hormigas",
            "descripcion": "Las hormigas invaden hogares y comercios en busca de alimento. Realizamos diagnóstico y aplicación de productos focalizados para erradicarlas desde el nido."
        },
        "chinches": {
            "titulo": "Chinches de cama",
            "descripcion": "Las chinches se esconden en camas y muebles, causando picaduras y molestias. Utilizamos técnicas avanzadas de detección y tratamientos térmicos y químicos."
        },
        "pulgas": {
            "titulo": "Pulgas",
            "descripcion": "Las pulgas afectan a mascotas y personas, transmitiendo enfermedades y causando picazón. Aplicamos tratamientos en interiores y exteriores para su total erradicación."
        },
        "moscas": {
        "titulo": "Moscas",
        "descripcion": "Las moscas son portadoras de bacterias y virus. Utilizamos trampas, cebos y nebulización para su control en ambientes residenciales y comerciales."
        },
        "zancudos": {
            "titulo": "Zancudos (mosquitos)",
            "descripcion": "Los zancudos pueden transmitir enfermedades como dengue y zika. Realizamos tratamientos preventivos y de choque en zonas de riesgo, patios y jardines."
        },
        "avispas": {
            "titulo": "Avispas",
            "descripcion": "Las avispas pueden ser peligrosas por sus picaduras. Localizamos y retiramos nidos de manera segura, usando métodos no invasivos y productos específicos."
        },
        "raton": {
        "titulo": "Ratón",
        "descripcion": "Los ratones suelen invadir viviendas y negocios buscando alimento y refugio. Suelen causar daños en cables, muebles y contaminar alimentos. Utilizamos trampas, cebos y barreras físicas para erradicarlos de forma segura."
        },
        "rata": {
            "titulo": "Rata",
            "descripcion": "Las ratas pueden causar daños severos en la estructura e instalaciones, además de ser portadoras de enfermedades graves. Aplicamos estrategias inteligentes y seguras para su control y eliminamos rutas de ingreso."
        },
        "termita_subterranea": {
        "titulo": "Termita subterránea",
        "descripcion": "Las termitas subterráneas construyen nidos bajo tierra y acceden a las estructuras a través de túneles. Se alimentan de madera y pueden causar daños graves en poco tiempo. Utilizamos tratamientos de barrera y cebos específicos para su erradicación."
        },
        "termita_madera_seca": {
            "titulo": "Termita de madera seca",
            "descripcion": "Las termitas de madera seca infestan principalmente maderas secas y muebles. Son difíciles de detectar, pero con métodos de inyección y productos de última generación logramos su control eficaz sin afectar el entorno."
        },
        "termita_otros": {
            "titulo": "Otras",
            "descripcion": "Existen diversas especies de termitas que pueden atacar diferentes tipos de madera y estructuras. Realizamos diagnóstico y tratamiento personalizado para cada caso, asegurando la máxima protección de tu propiedad."
        },
        "palomas": {
        "titulo": "Palomas",
        "descripcion": "Las palomas pueden anidar en techos y cornisas, ensuciando con excremento y transmitiendo enfermedades. Instalamos sistemas anti-posamiento y realizamos limpieza y prevención para evitar su retorno."
        },
        "tortolas": {
            "titulo": "Tórtolas",
            "descripcion": "Las tórtolas se adaptan bien a ambientes urbanos, causando molestias y suciedad. Usamos barreras físicas y métodos amigables para disuadir su anidación en lugares críticos."
        },
        "gorriones": {
            "titulo": "Gorriones",
            "descripcion": "Los gorriones forman colonias numerosas y pueden causar daños en almacenes y centros de distribución. Nuestra solución es ética, evitando daños y facilitando el desplazamiento de las aves."
        },
        "aves_otros": {
            "titulo": "Otras",
            "descripcion": "Controlamos también otras especies invasoras que puedan causar daños o problemas sanitarios, adaptando el sistema de control a cada situación para proteger la estructura y la salud de las personas."
        },
    }
    
    
    # Modal para el dialogo de insectos
    modal_insecto = ft.AlertDialog(
        modal=True,
        title=ft.Text(""),
        content=ft.Text(""),
        actions=[ft.TextButton("Cerrar", on_click=lambda e: cerrar_modal())]
    )

    # Funcion para cerrar modal de insectos
    def cerrar_modal():
        modal_insecto.open = False
        page.update()


    def mostrar_info_insecto(insecto_id):
        data = info_insectos.get(insecto_id)
        if data:
            modal_insecto.title.value = data["titulo"]
            modal_insecto.content.value = data["descripcion"]
            modal_insecto.open = True
            page.dialog = modal_insecto
            page.update()


    # Inicializamos la variable slides 
    slides = slides_quienes 

    # Funcion para mostrar los slides
    def mostrar_slide(idx):
        global carrusel_activo
        global slides
        carrusel_activo = False
        contenido.controls.clear()
        slide = slides[idx]
        imagenes_animadas = []  # <-- aquí irán las img para animar
       # Detener animación de insectos si hay una previa
        if animacion_insectos_task[0]:
            animacion_insectos_task[0].cancel()
            animacion_insectos_task[0] = None
        # Ancho automatico para los diferentes tamaños de pantalla, responsive para el card y el texto interno
        ancho_card = min(int(page.width * 0.8), 380)
        if page.width < 350:
            ancho_card = int(page.width * 0.98)
                    
        size_titulo = 18 if page.width < 400 else 24
        size_parrafo = 14 if page.width < 400 else 16

        # variable pan_dx Guarda el acumulado de movimiento horizontal
        pan_dx = [0]
        def on_pan_start(e):
            pan_dx[0] = 0  # Resetea en cada inicio
        def on_pan_update(e):
            pan_dx[0] += e.delta_x  # Acumula desplazamiento horizontal
        def on_pan_end(e):
            # Cambia de slide si el desplazamiento es suficiente
            if pan_dx[0] < -50 and idx < len(slides) - 1:
                navegar_slide(idx + 1)
            elif pan_dx[0] > 50 and idx > 0:
                navegar_slide(idx - 1)
            pan_dx[0] = 0

        
        # --- Prepara la lista de controles del slide ---
        contenido_slide = [
            ft.Container(
                content=ft.Text(
                    slide["titulo"],
                    size=size_titulo,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=["#0f2027", "#203a43", "#2c5364"],
                ),
                padding=ft.padding.symmetric(vertical=8, horizontal=10),
                border_radius=8,
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=8),
            ),
        ]
        imagenes_insectos = {
            "cucarachas": "https://cdn-icons-png.flaticon.com/512/8005/8005026.png",    # Puedes usar el enlace de tu preferencia
            "hormigas":   "https://static.vecteezy.com/system/resources/previews/015/211/725/non_2x/ant-icon-cartoon-style-vector.jpg",
            "chinches":   "https://cdn-icons-png.flaticon.com/512/1850/1850155.png",
            "pulgas":     "https://cdn-icons-png.flaticon.com/512/2295/2295144.png",
            "moscas": "https://cdn-icons-png.flaticon.com/512/1357/1357476.png",
            "zancudos": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR29MlAGMA1uNdMVEQtGxDEuh_gLjc_vf1H4w&s",
            "avispas": "https://static.vecteezy.com/system/resources/previews/014/285/415/non_2x/agression-wasp-icon-outline-style-vector.jpg",
            "raton": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_KKIyhsZpTWOzWNYwJLRLKheBjk4EAPefqw&s",
            "rata": "https://static.vecteezy.com/system/resources/previews/014/986/360/non_2x/rat-icon-cartoon-style-vector.jpg",
            "termita_subterranea": "https://cdn-icons-png.freepik.com/512/4982/4982504.png",
            "termita_madera_seca": "https://thumbs.dreamstime.com/b/icono-vectorial-de-color-plano-%C3%BAnico-la-madera-los-insectos-termite-157353067.jpg",
            "termita_otros": "https://i.postimg.cc/85r8Fs7m/trt.png",
            "palomas": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM-8j_vQCe1wXK-otbgAAlnYQIynlY9rampQ&s",
            "tortolas": "https://png.pngtree.com/png-vector/20230315/ourmid/pngtree-vector-turtledove-png-image_6650452.png",
            "gorriones": "https://st3.depositphotos.com/4233957/34474/v/450/depositphotos_344748232-stock-illustration-sparrow-small-city-bird-illustration.jpg",
            "aves_otros": "https://i.postimg.cc/KYBwFww0/aves-urbanas.png",
        }


        # Para almacenar las referencias de los contenedores animados
        insectos_animados = [] 
        # El resto de tu lógica para agregar los textos:
        for parrafo in slide["contenido"]:
            # Si es la fila especial de insectos:
            if isinstance(parrafo, dict) and parrafo.get("tipo") == "clickable_row":
                row_controles = []
                for item in parrafo["items"]:
                    img_insecto = ft.Image(
                        src=imagenes_insectos[item["id"]],
                        width=34, height=34,
                        fit=ft.ImageFit.CONTAIN,
                        scale=1.0,
                        animate_scale=200,
                        tooltip=item["nombre"]
                    )
                    imagenes_animadas.append(img_insecto)
                    # Container para animación y clic
                    cont = ft.Container(
                        content=img_insecto,
                        width=46, height=46,
                        border_radius=33,
                        bgcolor=ft.Colors.WHITE,
                        shadow=ft.BoxShadow(1, 6, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
                        alignment=ft.alignment.center,
                        on_click=lambda e, id=item["id"]: mostrar_info_insecto(id),
                        ink=True
                    )
                    insectos_animados.append(cont)
                    # Ahora arma columna imagen + texto
                    row_controles.append(
                        ft.Column(
                            [
                                cont,
                                ft.Text(
                                    item["nombre"],
                                    size=12,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=4,
                        )
                    )
                contenido_slide.append(
                    ft.Row(row_controles, alignment=ft.MainAxisAlignment.CENTER, spacing=18)
                )
            else:
                contenido_slide.append(
                    ft.Text(
                        parrafo,
                        size=size_parrafo,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.LEFT,
                    )
                )
         # --- Calcula el alto estimado del contenido (solo una referencia simple) ---
        texto_total = sum([len(str(p)) for p in slide["contenido"]])
        lineas_estimadas = texto_total // 55 + len(slide["contenido"])  # 55 chars por línea aprox
        alto_estimado = 60 + lineas_estimadas * 24  # 60px header, 24px por línea

        # Limites para el alto del card
        if page.width < 600:
            margen_redes = 120
            max_card_height = int(page.height * 0.70)
            if page.height - margen_redes < max_card_height:
                max_card_height = page.height - margen_redes
        else:
            margen_redes = 160
            max_card_height = int(page.height * 0.80)
            if page.height - margen_redes < max_card_height:
                max_card_height = page.height - margen_redes

        # Si el alto estimado es MENOR que el máximo, NO pones height (card se ajusta solo)
        # Si el alto estimado es MAYOR que el máximo, sí pones height y scroll
        if alto_estimado < max_card_height:
            contenido_slide_column = ft.Column(
                controls=contenido_slide,
                alignment=ft.MainAxisAlignment.START,
                spacing=16,
                scroll=None,  # No scroll, se adapta solo
            )
        else:
            contenido_slide_column = ft.Column(
                controls=contenido_slide,
                alignment=ft.MainAxisAlignment.START,
                spacing=16,
                scroll="auto",
                height=max_card_height,
            )
        card = ft.Container(
            width=ancho_card,
            padding=ft.padding.symmetric(vertical=18, horizontal=8 if page.width < 400 else 18),
            bgcolor=ft.Colors.WHITE,
            border_radius=16,
            border=ft.border.all(2, ft.Colors.BLACK),
            content=contenido_slide_column,   # <-- AQUÍ
            alignment=ft.alignment.center,
            # No pongas expand=True aquí, así solo hace scroll el contenido interno
        )

        # -- Aquí envolvemos el card con el detector de gestos
        gesture_card = ft.GestureDetector(
            content=card,
            on_pan_start=on_pan_start,
            on_pan_update=on_pan_update,
            on_pan_end=on_pan_end
        )

        # Funciones de las flechas para desplazar las pantallas a izquierda o derecha 
        row_controls = []
        if idx > 0:
            row_controls.append(
                ft.IconButton(
                    icon=ft.Icons.ARROW_LEFT,
                    icon_color=ft.Colors.BLUE_700,
                    icon_size=30,
                    on_click=lambda e: navegar_slide(idx-1)
                )
            )
        row_controls.append(gesture_card)
        if idx < len(slides)-1:
            row_controls.append(
                ft.IconButton(
                    icon=ft.Icons.ARROW_RIGHT,
                    icon_color=ft.Colors.BLUE_700,
                    icon_size=30,
                    on_click=lambda e: navegar_slide(idx+1)
                )
            )

        # Contenedor de las flechas 
        contenido.controls.append(
            ft.Container(
                content=ft.Row(
                    row_controls,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=False
                ),
                expand=False,
                alignment=ft.alignment.center
            )
        )
        contenido.update()
        # 🟢 -- Aquí va la magia: animar si corresponde --
        if len(imagenes_animadas) > 0:
            animacion_insectos_task[0] = page.run_task(animar_insectos_ciclo, imagenes_animadas)
    # Funcion para saber en que posicion esta el slide
    def navegar_slide(nuevo_idx):
        global slide_actual
        slide_actual = nuevo_idx
        mostrar_slide(slide_actual)

    # --- Modifica show_info (Funcion para saber que opcion del menu se selecciono) ---
    def show_info(opt):
        global carrusel_activo
        global slide_actual,slides
        dropdown.visible = False
        page.update()
        contenido.controls.clear()
        if opt == "Inicio":
            carrusel_activo = True
            contenido.controls.clear()
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            contenido.controls.extend([
                ft.Text("Bienvenido a EvermountSolutions", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Text("Control de plagas profesional. Haz clic en los botones.", color=ft.Colors.BLACK),
                fila_carrusel,
            ])
            contenido.update()
        elif opt == "Quiénes Somos":
            carrusel_activo = False  
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            slides = slides_quienes
            slide_actual = 0
            mostrar_slide(slide_actual)
        elif opt == "Servicios":
            carrusel_activo = False
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            slides = slides_servicios
            slide_actual = 0
            mostrar_slide(slide_actual)
        elif opt == "Programas":
            carrusel_activo = False
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            slides = slide_programas_control   # <--- USA EL SLIDE NUEVO AQUÍ
            slide_actual = 0
            mostrar_slide(slide_actual)
        elif opt == "Historia":
            carrusel_activo = False
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            slides = slides_historia
            slide_actual = 0
            mostrar_slide(slide_actual)
        elif opt == "Ubicación":
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            contenido.controls.append(
                ft.Text("dirección de empresa", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
            )
            contenido.update()
        # ...otros elif para las demás opciones...

    # Funcion para cerrar el menu del boton empresa cuando el cursor no este encima 
    def cerrar_menu_hover(e):
    # Si el mouse sale del menú, se cierra
        if e.data == "false" :
            dropdown.visible = False
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            page.update()

    # Menú del Boton_Empresa
    menu_data = [
        ("Inicio",     ft.Icons.HOME),
        ("Servicios",  ft.Icons.CHECKLIST),  
        ("Programas", ft.Icons.DATE_RANGE), 
        ("Quiénes Somos", ft.Icons.PEOPLE), 
        ("Historia", ft.Icons.HISTORY), 
        ("Contactos", ft.Icons.CONTACT_PHONE),
        ("Ubicación",  ft.Icons.PLACE),
        ("Misión",     ft.Icons.FLAG),
        ("Visión",     ft.Icons.VISIBILITY),
    ]
    menu_items = []
    for text, icon in menu_data:
        # ¡Truco correcto para que funcione!
        item = ft.Container(
            content=ft.Row([
                ft.Icon(icon, size=20, color=ft.Colors.BLACK54),
                ft.Text(text, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
            ]),
            padding=ft.padding.symmetric(vertical=6, horizontal=12),
            bgcolor=ft.Colors.WHITE,
            border_radius=4,
            on_click=lambda e, t=text: show_info(t),  # Captura valor correctamente
            ink=True,
        )
        menu_items.append(item)

    menu_column = ft.Column(controls=menu_items, spacing=0)
    dropdown = ft.Container(
        content=ft.Container(
            content=menu_column,
            bgcolor=ft.Colors.WHITE,
            border_radius=6,
            shadow=ft.BoxShadow(1,4,ft.Colors.BLACK26, offset=ft.Offset(0,2)),
            width=150,
            height=290,
            on_hover= cerrar_menu_hover
        ),
        visible=False,
        alignment=ft.alignment.top_right,
        margin=ft.margin.only(top=70, right=10),
    )
   
    # --- Barra superior con botón Empresa y Titulo ---
    texto_titulo = ft.Stack([
        ft.Text("EvermountSolutions – Pest Defense",
                size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK45, top=1, left=1),
        ft.Text("EvermountSolutions – Pest Defense",
                size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
    ])

    barra_superior = ft.Container(
        padding=ft.padding.symmetric(horizontal=10, vertical=8),
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left, end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"],
        ),
        content=ft.Row([
            ft.Container(content=texto_titulo, expand=True, alignment=ft.alignment.center_left),
            container_boton_empresa
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )   
    Botones_agregar = ft.Row([boton_facebook,boton_instragram,boton_whatsapp],alignment=ft.MainAxisAlignment.END,vertical_alignment=ft.CrossAxisAlignment.END)

    zona_redes = ft.Container(
        content=Botones_agregar,
        bgcolor="rgba(255,255,255,0.90)",
        alignment=ft.alignment.center
    )


    # Montaje final
    page.add(
        ft.Column([
            barra_superior,
            contenido,
            zona_redes,
        ], expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
    # --- Responsive: texto + ancho automático para WhatsApp ---
    def ajustar_tamanos(e=None):
        a = page.width
        # título
        s = 14 if a<450 else 18 if a<600 else 26
        texto_titulo.controls[0].size = s
        texto_titulo.controls[1].size = s
        texto_titulo.update()
        page.update()

    def on_connect(e):
        # Mostrar modal de bienvenida
        intro_modal.visible = True

        # Cerrar menú si está abierto
        dropdown.visible = False

        # Cerrar modal de insecto si estaba abierto
        modal_insecto.open = False   # <--- LÍNEA CLAVE
        page.dialog = None           # <--- Opcional, asegura que no queda el modal "huérfano"
        # Mostrar contenido inicial (texto y carrusel)
        global carrusel_activo
        carrusel_activo = True
        contenido.controls.clear()
        contenido.controls.extend([
            ft.Text("Bienvenido a EvermountSolutions", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            ft.Text("Control de plagas profesional. Haz clic en los botones.", color=ft.Colors.BLACK),
            fila_carrusel,  # <- Agrega fila_carrusel primero
        ])
        contenido.update()  # <-- MUY IMPORTANTE: actualiza el contenido aquí

        # Ahora SÍ puedes actualizar las imágenes porque ya están en pantalla
        for i, img in enumerate(imagenes_visibles):
            img.src = sets_imagenes[0][i]
            img.update()

        page.update()

    page.on_connect = on_connect
    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data=="shown" else None
    animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.overlay.extend([dropdown, intro_modal,modal_insecto])
    page.update()
    asyncio.create_task(rotar_sets())
    asyncio.create_task(animacion_alternada())
    ajustar_tamanos()
   
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))
