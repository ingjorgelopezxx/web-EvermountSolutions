import json
import flet as ft
import asyncio
import os
from views.quienes import create_quienes
from views.historia import create_historia
from views.contactos import create_contactos_row  # 👈 importar fila de iconos
from components.botones import create_boton_empresa, create_botones_redes,create_botones_redes
from components.insectos import ICONOS_INSECTOS, create_insectos_support, construir_contenido_slide_insectos
from components.intro import create_intro_overlay
from components.slides import create_slides_controller
from components.sabiasque import render_sabiasque
from components.servicios_detalle import render_servicio_desratizacion
from components.servicios_menu import render_menu_servicios
from components.sanitizacion_detalle import render_servicio_sanitizacion
from components.insectos_voladores_detalle import render_servicio_voladores
from components.insectos_rastreros_detalle import render_servicio_rastreros
from components.termitas_detalle import render_servicio_termitas
from components.aves_urbanas_detalles import render_servicio_aves_urbanas
from components.carrusel import create_carrusel 
from components.formulario import create_formulario
from components.vertical_imagenes import create_vertical_carousel
from components.valores import create_valores
from flet_webview import WebView   # 👈 ahora desde aquí

def main(page: ft.Page):
    # Inicializamos las propiedades de la pagina
    page.title = "EvermountSolutions"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0

    # Usamos lista para mutabilidad, inicializamos la variable 
    animacion_empresa_task = [None]     # ahora guardará el task del pulso del botón empresa
    animacion_redes_task = [None]       # task del bounce de redes    

    # WhatsApp mensaje mutable
    WHATSAPP_MSG = ["Hola 👋 Evermount Solutions.%0A"
    "Me gustaría recibir información sobre los servicios de control de plagas y sus costos.%0A"
    "¿Podrían orientarme, por favor?"]   # 👈 ahora es lista de un solo valor

    youtube_webview = WebView(
        url="https://www.youtube.com/embed/En49PmGEfLs?autoplay=1&mute=1&controls=1", 
        expand=True
    )

    video_card = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        padding=10,
        width=300,
        height=500,
        content=youtube_webview,
    )

    # Contactos Redes Sociales
    numero_whatsapp = "+56999724454"
    contacto_whatsapp = f"https://wa.me/{numero_whatsapp}?text={WHATSAPP_MSG}"
    contacto_instagram = "https://www.instagram.com/evermount_solutions?igsh=MTJ4YzI5aHVtZ3Fiaw=="
    contacto_facebook = "https://facebook.com/evermountsolutions"
   
    # Crear carrusel vertical
    carrusel_vertical, start_vertical, stop_vertical = create_vertical_carousel(page, intervalo=3)
    valores_section = create_valores(page)
  
    def crear_separador(page: ft.Page, texto: str) -> ft.Container:
        return ft.Container(
            bgcolor="#0D2943",  # azul oscuro
            margin=ft.margin.only(top=10),  # 👈 separación superior
            content=ft.Text(
                texto,
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
                text_align=ft.TextAlign.CENTER,
            ),
            alignment=ft.alignment.center,
            width=page.width,  # ancho completo
        )
    def crear_firma(page: ft.Page, texto: str) -> ft.Container:
        return ft.Container(
            bgcolor="#0D2943",  # azul oscuro
            content=ft.Text(
                texto,
                size=12,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
                text_align=ft.TextAlign.CENTER,
            ),
            alignment=ft.alignment.center,
            width=page.width,  # ancho completo
        )
    def crear_separador(page: ft.Page, texto: str, icono=None) -> ft.Container:
        contenido_row = ft.Row(
            [
                ft.Icon(icono, color=ft.Colors.WHITE, size=24) if icono else ft.Container(),
                ft.Text(
                    texto,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        )

        return ft.Container(
            bgcolor="#0D2943",
            margin=ft.margin.only(top=10),
            content=contenido_row,
            alignment=ft.alignment.center,
            width=page.width,
        )

    historia_section = create_historia(page)
    quienes_section = create_quienes(page)
    fila_iconos = create_contactos_row(page)
    fila_iconos.key = "contactos_iconos"  # 👈 clave única
    separador_servicios = crear_separador(page, "🪳🦟SERVICIOS🐀🐜")
    separador_servicios.key = "servicios_menu"
    separador_programas = crear_separador(page, "📅 PROGRAMAS")
    separador_programas.key = "programas_inicio"
    separador_VMS = crear_separador(page, "🏳️MISION   👁VISION   ⭐VALORES")
    separador_VMS.key = "mision"  # 👈 clave única
    separador_historia = crear_separador(page, "Historia", ft.Icons.HISTORY)
    separador_historia.key = "historia"  # 👈 clave única
    separador_quienes = crear_separador(page, "Quiénes Somos", ft.Icons.PEOPLE)
    separador_quienes.key = "quienes_somos"
    separador_final = crear_firma(page, "Desarrollo por Ing. Jorge Lopez con Tecnología Flet & Python\n Contacto: +56937539304 Instagram: jorgelopezsilva\n2025 Todos los Derechos Reservados")
    separador_sanitizacion = crear_separador(page, "🏠 Sanitización de Ambientes")
    #insectos
    modal_insecto, mostrar_info_insecto, start_anim_insectos, stop_anim_insectos = create_insectos_support(page)
    # --- Carrusel ---
    pantalla_inicial, start_carrusel, stop_carrusel  = create_carrusel(page)
    # --- Formulario ---
    formulario = create_formulario(page)
    menu_servicios_container = ft.Column(spacing=10)  # 👈 aquí pondremos el menú
    def render_inicio():
        contenido.controls.clear()
        contenido.controls.extend([
            fila_iconos,pantalla_inicial,formulario,separador_servicios,menu_servicios_container,separador_programas,carrusel_vertical,separador_VMS,valores_section,separador_sanitizacion,video_card,separador_quienes,quienes_section,separador_historia,historia_section,separador_final  
        ])
        contenido.update()
        page.update()

    # Contenido central mutable
    contenido = ft.Column(
        [fila_iconos,pantalla_inicial,formulario,separador_servicios,menu_servicios_container,separador_programas,carrusel_vertical,separador_VMS,valores_section,separador_sanitizacion,video_card,separador_quienes,quienes_section,separador_historia,historia_section,separador_final],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="auto",
    )
    

    # Flag e inicializador de Sabías que
    sabiasque_inicializado = [False]
    intro_mostrado = [False]

    def show_intro_once():
        if intro_mostrado[0]:
            return
        intro_mostrado[0] = True
        # asegúrate de que nada intercepte clics
        try:
            cerrar_menu()
            overlay_cierra_menu.visible = False
        except Exception:
            pass
        show_intro()      # <- del create_intro_overlay

    def ensure_sabiasque():
        if not sabiasque_inicializado[0]:
            render_sabiasque(page, contenido)  # registra on_route_change interno y helpers
            sabiasque_inicializado[0] = True

    def _route_handler(e: ft.RouteChangeEvent):
        r = (e.route or "/").strip()

        # Cierra menú/overlays si estuvieran abiertos
        try:
            cerrar_menu()
            overlay_cierra_menu.visible = False
        except Exception:
            pass
        
        if r == "/":
            # reconstruir contenido con pantalla_inicial
            render_inicio()

            # relanzar carrusel
            async def kick():
                await asyncio.sleep(0)
                start_carrusel()
                start_vertical()
            page.run_task(kick)

            return
        
        # --- Rutas de Sabías que ---
        if r.startswith("/sabiasque"):
            ensure_sabiasque()
            # Si el módulo registró su propio router, delega
            if hasattr(page, "_sabiasque_router"):
                page._sabiasque_router(ft.RouteChangeEvent(route=r))
            else:
                # Fallback: pinta grilla
                render_sabiasque(page, contenido)
                if hasattr(page, "_sabiasque_show_grid"):
                    page._sabiasque_show_grid()
            page.update()
            return

        if r == "/servicios/roedores":
            parar_carrusel()
            # Guarda el mensaje para WhatsApp en el storage del navegador
            page.client_storage.set(
                "whatsapp_msg",
                "Hola👋 EvermountSolutions, me gustaría agendar una visita para control de roedores 🐀. ¿Tienen disponibilidad?"
            )
            render_servicio_desratizacion(page, contenido)
            page.update()
            return
        if r == "/servicios/sanitizacion":
            parar_carrusel()
            page.client_storage.set(
                "whatsapp_msg",
                "Hola👋 EvermountSolutions, me gustaría agendar una visita para Desinfección y Sanitización de Ambientes 🧼. ¿Tienen disponibilidad?"
            )
            render_servicio_sanitizacion(page, contenido)
            page.update()
            return
        if r == "/servicios/voladores":
            parar_carrusel()
            page.client_storage.set(
                "whatsapp_msg",
                "Hola👋 EvermountSolutions, me gustaría agendar una visita para control de Insectos Voladores 🦟. ¿Tienen disponibilidad?"
            )
            render_servicio_voladores(page, contenido)
            page.update()
            return
        if r == "/servicios/rastreros":
            parar_carrusel()
            page.client_storage.set(
                "whatsapp_msg",
                "Hola👋 EvermountSolutions, me gustaría agendar una visita para control de Insectos Rastreros 🪳. ¿Tienen disponibilidad?"
            )
            render_servicio_rastreros(page, contenido)
            page.update()
            return
        if r == "/servicios/termitas":
            parar_carrusel()
            page.client_storage.set(
                "whatsapp_msg",
                "Hola👋 EvermountSolutions, me gustaría agendar una visita para control de Termitas 🐜. ¿Tienen disponibilidad?"
            )
            render_servicio_termitas(page, contenido)
            page.update()
            return
        if r == "/servicios/aves":
            parar_carrusel()
            page.client_storage.set(
                "whatsapp_msg",
                "Hola👋 EvermountSolutions, me gustaría agendar una visita para control de Aves Urbanas 🕊️. ¿Tienen disponibilidad?"
            )
            render_servicio_aves_urbanas(page, contenido)
            page.update()
            return
        # --- Inicio (cualquier otra ruta) ---
        render_inicio()

    # activa router
    page.on_route_change = _route_handler

    #Funcion para detener el carrusel de imagenes 
    def parar_carrusel():
            stop_carrusel()
            stop_vertical()
            if pantalla_inicial in contenido.controls:
                contenido.controls.remove(pantalla_inicial)
            contenido.update()  
        # ...otros elif para las demás opciones...

    # Se crea el controlador de slides (ya existe `contenido` y callbacks de insectos)
    set_slides, mostrar_slide, navegar_slide, get_slide_index = create_slides_controller(
    page=page,
    contenido=contenido,
    construir_contenido_slide_insectos=construir_contenido_slide_insectos,
    mostrar_info_insecto=mostrar_info_insecto,
    start_anim_insectos=start_anim_insectos,
    stop_anim_insectos=stop_anim_insectos,
    on_enter_slides=parar_carrusel,   # <- detiene carrusel al entrar a slides
    )

     # --- Botón EMPRESA (header) ---
    def toggle_menu(e):
        dropdown.visible = not dropdown.visible
        if dropdown.visible:
            # menú abierto → detener pulso (usa la API del componente)
            abrir_menu()
            stop_pulso_empresa()
            animacion_empresa_task[0] = None
        else:
            cerrar_menu()
            # menú cerrado → reanudar pulso (usa la API del componente)
            animacion_empresa_task[0] = start_pulso_empresa()
            
        page.update()

    # Crear botones, menu y header
    container_boton_empresa, start_pulso_empresa, stop_pulso_empresa = create_boton_empresa(page, toggle_menu)
    animacion_empresa_task[0] = start_pulso_empresa()   # ← arranque inicial
    
    # Creamos la funcion On_CLic del Boton Sabias que
    def on_sabiasque_click(e=None):
        # 1) detén carrusel si aplica
        try:
            parar_carrusel()
        except Exception:
            pass
        page.go("/sabiasque")

    def mostrar_inicio_con_intro(e=None):
        # Si YA estamos en "/"
        if page.route == "/":
            # no reconstruir, solo actualizar y scrollear
            page.update()
            page.scroll_to(key="contactos_iconos", duration=500)
            return
        contenido.controls.clear()
        # Si NO estamos en "/", reconstruir y redirigir
        page.route = "/"
        _route_handler(ft.RouteChangeEvent(route="/"))
        render_inicio()
        # Lanzar carrusel en el próximo ciclo
        async def kick():
            await asyncio.sleep(0)
            start_carrusel()
            start_vertical()
        page.run_task(kick)

    imagen_logo_empresa = ft.Image(
    src="https://i.postimg.cc/rFxRRS5D/logo-72x72.png",
    fit=ft.ImageFit.COVER,   # llena el círculo sin dejar bordes
    )

    inner = ft.Container(
        content=imagen_logo_empresa ,
        width=50, height=50,               # se actualizan en ajustar_tamanos
        border_radius=9999,                # círculo
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  # 👈 recorta a círculo
        alignment=ft.alignment.center,
    )

    container_logo_empresa = ft.Container(
        content=inner,
        width=64, height=64,               # se actualizan en ajustar_tamanos
        bgcolor=ft.Colors.BLACK12,
        border_radius=9999,                # círculo externo
        padding=7,
        on_click=mostrar_inicio_con_intro,
        ink=True,
        alignment=ft.alignment.center,
    )

    # --- Botones REDES ---
    boton_facebook, boton_instagram, boton_whatsapp, boton_sabiasque, start_bounce, stop_bounce = create_botones_redes(
        page, contacto_whatsapp, contacto_instagram, contacto_facebook, on_sabiasque_click
    )

    # Menú del Boton_Empresa
    menu_data = [
        ("Inicio",     ft.Icons.HOME),
        ("Servicios",  ft.Icons.CHECKLIST),  
        ("Programas", ft.Icons.DATE_RANGE), 
        ("Quiénes Somos", ft.Icons.PEOPLE), 
        ("Historia", ft.Icons.HISTORY), 
        ("Contactos", ft.Icons.CONTACT_PHONE),
        ("Misión-Visión", ft.Icons.FLAG),
    ]
    menu_items = []
    for text, icon in menu_data:
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

    # Funcion para cerrar el menu del boton empresa cuando el cursor no este encima 
    def cerrar_menu_hover(e):
        if e.data == "false":
            dropdown.visible = False
            cerrar_menu()
            if animacion_empresa_task[0] is None:
                animacion_empresa_task[0] = start_pulso_empresa()
            page.update()
            
    menu_column = ft.Column(controls=menu_items, spacing=0)
      # --- Overlay para cerrar el menú al hacer clic fuera ---
    overlay_cierra_menu = ft.Container(
        left=0, top=0, right=0, bottom=0,      # 👈 llena toda la viewport
        bgcolor="rgba(0,0,0,0.001)",           # casi transparente (asegura eventos)
        visible=False,
        on_click=lambda e: cerrar_menu(),      # cierra al hacer clic/tap fuera
    )
    def abrir_menu():
        dropdown.visible = True
        overlay_cierra_menu.visible = True
        stop_pulso_empresa()
        animacion_empresa_task[0] = None
        stack_raiz.update()  # 👈

    def cerrar_menu():
        dropdown.visible = False
        overlay_cierra_menu.visible = False
        # reanudar pulso si corresponde
        if animacion_empresa_task[0] is None:
            animacion_empresa_task[0] = start_pulso_empresa()
        stack_raiz.update()  # 👈

    dropdown = ft.Container(
        content=ft.Container(
            content=menu_column,
            bgcolor=ft.Colors.WHITE,
            border_radius=6,
            shadow=ft.BoxShadow(1,4,ft.Colors.BLACK26, offset=ft.Offset(0,2)),
            width=150,
            height=223,
            on_hover= cerrar_menu_hover
        ),
        visible=False,
        top=35,       # 👈 posicionalo respecto a la ventana, no con alignment/margin
        right=5,
    )

    # --- Barra superior con botón Empresa y Titulo ---
    texto_titulo = ft.Stack([
        ft.Text("EvermountSolutions – Pest Defense",
                 weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK45, top=1, left=1),
        ft.Text("EvermountSolutions – Pest Defense",
                 weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
    ])

    barra_superior = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left, end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"],
        ),
        content=ft.Row([
            container_logo_empresa, 
            ft.Container(content=texto_titulo, expand=True, alignment=ft.alignment.center_left),
            container_boton_empresa
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )   
    # Creamos la fila donde estaran los botones inferiores
    Botones_agregar = ft.Row([boton_sabiasque,boton_facebook,boton_instagram,boton_whatsapp],alignment=ft.MainAxisAlignment.END,vertical_alignment=ft.CrossAxisAlignment.END)

    # Agregamos un contenedor para incluir los botones y le asigamos un fondo
    zona_redes = ft.Container(
        content=Botones_agregar,
        bgcolor="rgba(255,255,255,0.90)",
        alignment=ft.alignment.center
    )

    contenido_base = ft.Column([
        barra_superior,
        contenido,
        zona_redes,
    ], expand=True, 
    spacing=0,           # sin espacios extra verticales
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,)

    stack_raiz = ft.Stack(
        controls=[
            contenido_base,        # capa 0: contenido normal
            overlay_cierra_menu,   # capa 1: overlay que capta clic fuera
            dropdown,              # capa 2: menú dropdown, arriba del overlay
        ], expand=True,    # 👈 importante Stack ocupa toda la altura
    )
    # después de crear stack_raiz con [contenido_base, overlay_cierra_menu, dropdown]
    intro_modal, show_intro, hide_intro = create_intro_overlay(page)
    stack_raiz.controls.append(intro_modal)   # 👈 lo montas encima de todo
    def on_connect(e):
        cerrar_menu()
        overlay_cierra_menu.visible = False
        # Si se abre directamente en /servicios o /sabiasque...
        if (page.route or "").startswith("/sabiasque") or (page.route or "") == "/servicios":
            _route_handler(ft.RouteChangeEvent(route=page.route or "/servicios"))
            return
        # Si la pestaña se abrió en /sabiasque o /sabiasque/<idx>...
        if (page.route or "").startswith("/sabiasque"):
            ensure_sabiasque()
            page.go(page.route or "/sabiasque")
            return
        
        # Render inicial
        render_inicio()

        # Mostrar intro una sola vez
        show_intro_once()

        # Iniciar carrusel tras un tick
        async def _kick():
            await asyncio.sleep(0)
            start_carrusel()
            start_vertical()
        page.run_task(_kick)

    page.on_connect = on_connect

    # Cuando se monte la página, iniciar carrusel imagenes verticales
    async def iniciar():
        await asyncio.sleep(0)
        start_vertical()
    page.run_task(iniciar)

    page.add(
        ft.Container(
            content=stack_raiz,
            expand=True,           # 👈 asegura ocupar todo el viewport
        )
    )
    # Esto inyecta el grid de servicios en el contenedor vacío
    render_menu_servicios(page, menu_servicios_container)
    # Fallback: en el próximo tick, intenta mostrar el intro una vez
    async def _first_paint_intro():
        await asyncio.sleep(0)
        show_intro_once()

    page.run_task(_first_paint_intro)
    ####### FUNCIONES #######
    # --- Modifica show_info (Funcion para saber que opcion del menu se selecciono) ---
    def show_info(opt):
        global slide_actual,slides
        cerrar_menu()  # cerramos el menú siempre
        dropdown.visible = False
        if animacion_empresa_task[0] is None:
            animacion_empresa_task[0] = start_pulso_empresa()
        page.update()
        
        if opt == "Inicio":
            mostrar_inicio_con_intro()
        elif opt == "Quiénes Somos":
            page.scroll_to(key="quienes_somos", duration=500)
            return
        elif opt == "Servicios":
            page.scroll_to(key="servicios_menu", duration=500)
            return
        elif opt == "Programas":
            page.update()
            page.scroll_to(key="programas_inicio", duration=500)
            return
        elif opt == "Historia":
            page.update()
            page.scroll_to(key="historia", duration=500)
            return
        elif opt == "Misión-Visión":
            page.scroll_to(key="mision", duration=500)
            return
        elif opt == "Contactos":
            page.scroll_to(key="contactos_iconos", duration=500)
            return

        elif opt == "Ubicación":
            contenido.controls.append(
                ft.Text("dirección de empresa", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
            )
            contenido.update()

    # 🔧 Inicializa el carrusel en el primer render
    def _init_carousel_after_mount():
        async def _kick():
            # un tick para asegurar que los controles ya están montados
            await asyncio.sleep(0)
            start_carrusel()
            start_vertical()
        page.run_task(_kick)
    _init_carousel_after_mount()

    # --- Responsive: texto + ancho automático para WhatsApp ---
    def ajustar_tamanos(e=None):
        a = page.width

        # --- Escala del título ---
        s = 15 if a < 480 else 24 if a < 900 else 28
        texto_titulo.controls[0].size = s
        texto_titulo.controls[1].size = s
        texto_titulo.update()

        # tamaño del botón empresa (icono + área táctil) + Logo empresa
        if a < 450:   # móviles
            icon_size = 26
            btn_size = 36
            logo_size = 42
            dropdown.top = 32
        elif a < 800: # tablets
            icon_size = 32
            btn_size = 44
            logo_size = 54
            dropdown.top = 40
        else:         # desktop
            icon_size = 38
            btn_size = 52
            logo_size = 66
            dropdown.top = 45

        # 1) tamaño del contenedor (área clickeable visual)
        container_boton_empresa.width = btn_size
        container_boton_empresa.height = btn_size

        # 2) tamaño del ícono del IconButton interno
        inner_btn = container_boton_empresa.content
        if isinstance(inner_btn, ft.IconButton):
            inner_btn.icon_size = icon_size
            # Si necesitas asegurar padding cero en runtime:
            inner_btn.style = ft.ButtonStyle(
                padding=ft.padding.all(0),
                shape=ft.RoundedRectangleBorder(radius=9999),
            )

        # ejemplo de escalado
        container_logo_empresa.width = logo_size
        container_logo_empresa.height = logo_size
        container_logo_empresa.border_radius = logo_size // 2
        inner_size = logo_size - 10   # margen/padding
        container_logo_empresa.content.width = inner_size
        container_logo_empresa.content.height = inner_size
        container_logo_empresa.content.border_radius = inner_size // 2

        page.update()

    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data=="shown" else None
        # Iniciar animaciones
    animacion_empresa_task[0] = start_pulso_empresa()
    animacion_redes_task[0] = start_bounce()
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.update()
    ajustar_tamanos()
   
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))