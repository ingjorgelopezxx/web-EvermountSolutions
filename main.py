import json
from flet import Ref
import time
import flet as ft
import asyncio
import os
from views.quienes import create_quienes
from views.historia import create_historia
from views.contactos import create_contactos_row  # 👈 importar fila de iconos
from components.botones import create_boton_empresa, create_botones_redes
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
        url="https://www.youtube.com/embed/En49PmGEfLs?autoplay=0&mute=1&controls=1", 
    )
    youtube_webview2 = WebView(
        url="https://youtube.com/embed/eedRkoI9poE?autoplay=0&mute=1&controls=1", 
    )

    video_card = ft.Container(
        border_radius=20,                    # 🔥 Bordes redondeados estilo carrusel
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  
        bgcolor="transparent",               # Sin fondo
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),  
        padding=0,                           # Sin marco blanco
        width=300,
        height=400,
        content=ft.Container(
            border_radius=20,                # 🔥 Recorte interno redondeado
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=youtube_webview
        ),
    )

    video_card2 = ft.Container(
        border_radius=20,                    # 🔥 Bordes redondeados estilo carrusel
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  
        bgcolor="transparent",               # Sin fondo
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),  
        padding=0,                           # Sin marco blanco
        width=263,
        height=360,
        content=ft.Container(
            border_radius=20,                # 🔥 Recorte interno redondeado
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=youtube_webview2
        ),
    )

    # Contactos Redes Sociales
    numero_whatsapp = "+56999724454"
    contacto_whatsapp = f"https://wa.me/{numero_whatsapp}?text={WHATSAPP_MSG}"
    contacto_instagram = "https://www.instagram.com/evermount_solutions?igsh=MTJ4YzI5aHVtZ3Fiaw=="
    contacto_facebook = "http://facebook.com/share/15bcUW9HyS"
   
    # Crear carrusel vertical
    carrusel_vertical, start_vertical, stop_vertical = create_vertical_carousel(page, intervalo=3)

    valores_section = create_valores(page)
    # --- Zona multimedia: carrusel + video (layout se ajusta en ajustar_tamanos) ---
    zona_multimedia = ft.Container(
        content=carrusel_vertical,
    )
    COLOR_SEPARADOR_PC = "#203a43"  # similar al gradiente desactivado
    COLOR_SEPARADOR_MOBILE = "#0D2943"
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
        # texto multi-línea original (para móviles)
        txt = ft.Text(
            texto,
            size=12,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        )

        cont = ft.Container(
            bgcolor="#0D2943",  # azul oscuro (estilo móvil)
            content=txt,
            alignment=ft.alignment.center,
            width=None,
        )

        # guardamos info para poder cambiar estilos según el dispositivo
        cont.data = {
            "mobile_bg": "#0D2943",
            "raw_text": texto,                            # con saltos de línea
            "oneline_text": " ".join(texto.split()),      # sin saltos (los reemplaza por espacios)
        }
        return cont

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
        # Slot para insertar fila_iconos en la barra superior cuando sea desktop
    slot_iconos_header = ft.Container(
        visible=False,
        alignment=ft.alignment.center_right,  # alineado a la derecha
    )
    slot_tabs_header = ft.Container(
        visible=False,
        alignment=ft.alignment.center,
    )

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
    separador_final = crear_firma(page, "🛠 Desarrollo por Ing. Jorge Lopez con ⚡Tecnología Flet & 🐍Python\n 📞: +56937539304        📸: jorgelopezsilva\n2025 ©️Todos los Derechos Reservados")
    separador_final.bgcolor = "#B9B8B8"        # gris corporativo claro
    separador_final.content.color = "#202325" # texto gris oscuro elegante
    separador_final.content.size = 8

    separador_sanitizacion = crear_separador(page, "🏠 Sanitización de Ambientes")
    #insectos
    separador_servicios.data = {"bg_mobile": COLOR_SEPARADOR_MOBILE}
    separador_programas.data = {"bg_mobile": COLOR_SEPARADOR_MOBILE}
    separador_VMS.data = {"bg_mobile": COLOR_SEPARADOR_MOBILE}
    separador_historia.data = {"bg_mobile": COLOR_SEPARADOR_MOBILE}
    separador_quienes.data = {"bg_mobile": COLOR_SEPARADOR_MOBILE}
    separador_sanitizacion.data = {"bg_mobile": COLOR_SEPARADOR_MOBILE}

    modal_insecto, mostrar_info_insecto, start_anim_insectos, stop_anim_insectos = create_insectos_support(page)
    # --- Carrusel ---
    pantalla_inicial, start_carrusel, stop_carrusel  = create_carrusel(page)
        # --- Helper: iniciar carruseles sólo si ya están montados ---
    async def _kick_carruseles():
        # Espera un tick para que el árbol se monte
        await asyncio.sleep(0)

        # Carrusel principal: solo si ya está montado
        if getattr(pantalla_inicial, "page", None) is not None:
            start_carrusel()

        # Carrusel vertical: SIEMPRE lo arrancamos
        # porque dentro de _rotar() ya esperas a que imagen.page no sea None
        start_vertical()

    # --- Formulario ---
    formulario = create_formulario(page)
    menu_servicios_container = ft.Column(spacing=10)  # 👈 aquí pondremos el menú

    # 1) Crear wrappers
    cont_pantalla = ft.Container(content=pantalla_inicial, border_radius=0, padding=0, key="cont_pantalla")
    cont_form     = ft.Container(content=formulario,       border_radius=0, padding=0)
    ANCHO_FORM_PC = 380
    # 2) Crear ResponsiveRow
    col_pantalla = ft.Container(content=cont_pantalla, col={"xs": 12, "md": 10, "lg": 10})
    col_form = ft.Container(
    content=ft.Container(
        content=formulario,
        width=ANCHO_FORM_PC,
        padding=20,
        bgcolor="rgba(255,255,255,0.95)",  # blanco ligeramente opaco en PC
        border_radius=16,
    ),
    col={"xs": 12, "md": 12, "lg": 4},
    alignment=ft.alignment.center_right,
)

    col_spacer = ft.Container(col={"xs": 12, "md": 10, "lg": 10}, expand=True)

    imagen_logo_empresa = ft.Image(
    src="https://i.postimg.cc/rFxRRS5D/logo-72x72.png",
    fit=ft.ImageFit.COVER,   # llena el círculo sin dejar bordes
    )
    imagen_logo_empresa2 = ft.Image(
    src="https://i.postimg.cc/sDPWTSk5/lll.jpg",
    fit=ft.ImageFit.FILL,   # llena el círculo sin dejar bordes
    )

    inicio_responsive = ft.ResponsiveRow(
        controls=[col_pantalla, col_form],
        columns=12,
        run_spacing=10,
        spacing=10,
        key="inicio_responsive",
    )

    imagen_banner_form = ft.Image(
        src="https://i.postimg.cc/htB3zLB6/Imagen7.png",  # cambia si quieres
        fit=ft.ImageFit.COVER,
        border_radius=16,
    )
    enlace_correo2 = "mailto:operaciones@evermountsolutions.cl?subject=Consulta&body=Hola, quisiera más información"
    def crear_boton_cotiza(page: ft.Page):
        COLOR_NORMAL = ft.Colors.WHITE
        COLOR_HOVER  = "#D8E6EC"
        TEXTO_COLOR  = "#203a43"

        texto = ft.Text(
            "Cotiza ahora",
            size=22,
            weight=ft.FontWeight.BOLD,
            color=TEXTO_COLOR,
        )

        btn = ft.Container(
            content=texto,
            bgcolor=COLOR_NORMAL,
            border_radius=14,
            padding=ft.padding.symmetric(horizontal=26, vertical=16),
            alignment=ft.alignment.center,
            ink=True,
            on_click=lambda e: page.launch_url(enlace_correo2),
        )

        def _hover(e):
            btn.bgcolor = COLOR_HOVER if e.data == "true" else COLOR_NORMAL
            btn.update()

        btn.on_hover = _hover
        return btn

    
    ALTO_INICIO_PC = 580  # opcional: altura fija del bloque en PC (puedes poner None)
    banner_pc = ft.Container(
        key="banner_pc",
        expand=True,
        height=ALTO_INICIO_PC,
        padding=ft.padding.symmetric(horizontal=60, vertical=40),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#0f2027", "#203a43", "#2c5364"],
        ),
        content=ft.Row(
            [
                ft.Column(
                        [
                            ft.Row(
                                [
                                    # Logo
                                    ft.Container(
                                        content=imagen_logo_empresa2,
                                        width=200,
                                        height=200,
                                        border_radius=999,
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                    ),

                                    # Textos
                                    ft.Column(
                                        [
                                            ft.Text(
                                                "Evermount Solutions",
                                                size=64,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                            ),
                                            ft.Text(
                                                "Pest Defense",
                                                size=64,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE70,
                                            ),
                                        ],
                                        spacing=2,
                                    ),
                                ],
                                spacing=16,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),

                            ft.Text(
                                "Control profesional de plagas para hogares y empresas.\n"
                                "Programas mensuales, trimestrales y anuales con garantía.",
                                size=28,
                                color=ft.Colors.WHITE,
                            ),

                            crear_boton_cotiza(page),
                            
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
               
                # --- Spacer ---
                ft.Container(expand=True),
                # --- Columna derecha ---
                imagen_banner_form,
                # --- Formulario a la derecha ---
                col_form,
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # Wrapper que se usa en el contenido
    inicio_bg = ft.Container(
        content=inicio_responsive,
        expand=True,
        width=float("inf"),
    )
    

    def render_inicio():
        contenido.controls.clear()
        contenido.controls.extend([
           inicio_bg,separador_servicios,menu_servicios_container,separador_programas,zona_multimedia,separador_VMS,valores_section,separador_sanitizacion,separador_quienes,quienes_section,separador_historia,historia_section,separador_final])
        contenido.update()
        page.update()
        

    # Contenido central mutable
    contenido = ft.Column(
        [inicio_bg,separador_servicios,menu_servicios_container,separador_programas,zona_multimedia,separador_VMS,valores_section,separador_sanitizacion,separador_quienes,quienes_section,separador_historia,historia_section,separador_final],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="auto",
    )
    
        # Helper para remover controles sin que Flet explote
    def safe_remove(control, controls_list):
        try:
            if control in controls_list:
                controls_list.remove(control)
        except Exception:
            pass

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
            # reconstruir contenido
            render_inicio()

            # asegurar que los contenedores principales están visibles
            cont_pantalla.visible = True
            cont_form.visible = True
            # ➕ recolocar fila_iconos según ancho actual (desktop / tablet / móvil)
            ajustar_tamanos()
            # relanzar carruseles SOLO tras montaje
            page.run_task(_kick_carruseles)

            page.update()
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
        # ❌ No quites pantalla_inicial del contenido; si quieres ocultarlo, oculta el contenedor:
        # if pantalla_inicial in contenido.controls: ...
        # ✅ Mejor: no remover nada aquí. Solo detener.
        contenido.update()

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
            # cierra menú/overlays por si acaso
            try:
                cerrar_menu()
                overlay_cierra_menu.visible = False
            except Exception:
                pass

            # Delega al router. No limpies contenido ni llames render_inicio aquí.
            page.go("/")
            
            # 🔥 Scroll automático SOLO en tablet/PC
            if (page.width or 0) >= 600:
                # Dar un pequeño tiempo para permitir que el contenido se reconstruya
                async def _scroll():
                    await asyncio.sleep(0.5)  # deja que el layout se monte
                    if (page.width or 0) >= 1020:   # PC
                        page.scroll_to(key="banner_pc", duration=400)
                    else:
                        page.scroll_to(key="inicio_responsive", duration=300)

                page.run_task(_scroll)
            else: page.scroll_to(key="cont_pantalla", duration=200)

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

    # --- Barra superior con Titulo (solo móvil) ---
    texto_titulo = ft.Stack([
        ft.Text("EvermountSolutions – Pest Defense",
                weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK45, top=1, left=1),
        ft.Text("EvermountSolutions – Pest Defense",
                weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
    ])

    wrap_titulo = ft.Container(
        content=texto_titulo,
        expand=True,
        alignment=ft.alignment.center_left,
        visible=True,   # se controla en ajustar_tamanos()
    )

    barra_superior = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left, end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"],
        ),
        content=ft.Row([
            container_logo_empresa, 
            wrap_titulo,
            slot_tabs_header,
            slot_iconos_header,
            container_boton_empresa 
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )   
    # Creamos la fila donde estaran los botones inferiores
    Botones_agregar = ft.Row([boton_sabiasque,boton_facebook,boton_instagram,boton_whatsapp],alignment=ft.MainAxisAlignment.END,vertical_alignment=ft.CrossAxisAlignment.END)
    # --- TEXTO PROMOCIONAL (solo visible en tablet/PC) ---
    promo_text = ft.Text(
        "🔥 Promoción especial: 20% de descuento en programas mensuales y anuales de control de plagas. ¡Cotiza hoy mismo! 🔥",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        no_wrap=True,
        text_align=ft.TextAlign.LEFT,
    )

    # Contenedor flotante que se va a mover horizontalmente
    promo_flotante = ft.Container(
        content=promo_text,
        top=5,
        left=0,
    )

    # Stack con fondo + texto en movimiento (ocupará toda la zona izquierda)
    promo_stack = ft.Stack(
        controls=[
            ft.Container(  # fondo fijo
                bgcolor="rgba(255,255,255,0.90)",
                expand=True,
            ),
            promo_flotante,  # texto que se desplaza encima
        ],
        height=40,
        expand=True,
        visible=False,  # solo visible en tablet/PC (se maneja en ajustar_tamanos)
    )

    # Barra inferior: promo a la izquierda, redes a la derecha
    barra_inferior = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            promo_stack,     # izquierda
            Botones_agregar  # derecha
        ],
    )

    # Zona de redes (contenedor final)
    zona_redes = ft.Container(
        content=barra_inferior,
        bgcolor="rgba(255,255,255,0.90)",
        alignment=ft.alignment.center,
    )

    contenido_base = ft.Column([
        barra_superior,
        contenido,
        zona_redes,
    ], expand=True, 
    spacing=0,           # sin espacios extra verticales
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,)

    async def marquee_loop():
        await asyncio.sleep(1)

        VELOCIDAD = 90   # píxeles por segundo (ajústalo)
        PAUSA_FIN = 0.8  # pausa antes de reiniciar

        while True:
            # Si no es visible (modo móvil) → espera sin animar
            if not promo_stack.visible:
                await asyncio.sleep(0.5)
                continue

            # ancho área visible
            ancho = zona_redes.width or page.width or 900

            # estimación de ancho del texto
            texto_ancho = len(promo_text.value) * 8

            # posición inicial: fuera por la derecha
            x_inicial = ancho
            x_final = -texto_ancho

            # tiempo inicial
            t0 = time.time()

            # loop de animación suave basado en tiempo real
            while True:
                t = time.time() - t0
                x = x_inicial - VELOCIDAD * t

                if x < x_final:
                    break  # terminó el recorrido

                promo_flotante.left = x
                promo_flotante.update()

                await asyncio.sleep(0.01)  # ~100 FPS reales

            # pausa antes de reiniciar
            await asyncio.sleep(PAUSA_FIN)


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
        # Render inicial
        page.go(page.route or "/")
        # Intro una vez
        show_intro_once()
    page.on_connect = on_connect

    page.add(
        ft.Container(
            content=stack_raiz,
            expand=True,           # 👈 asegura ocupar todo el viewport
        )
    )
    # Inicia carruseles tras montar el árbol
    page.run_task(_kick_carruseles)
    page.run_task(marquee_loop)
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

    def create_top_tabs(show_info_callback, es_desktop=False):
        tabs = []
        for text, icon in menu_data:
            # ❌ ocultar en PC
            if es_desktop and text in ("Contactos", "Historia"):
                continue

            tab = ft.Container(
                content=ft.Text(
                    text,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                padding=ft.padding.symmetric(horizontal=12, vertical=6),
                margin=ft.margin.symmetric(horizontal=4),   
                border_radius=8,
                bgcolor="transparent",
                ink=True,
                on_click=lambda e, t=text: show_info_callback(t),
            )
            tabs.append(tab)

        return ft.Row(
            controls=tabs,
            spacing=4,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )


    # --- Responsive: texto + ancho automático para WhatsApp ---
    def ajustar_tamanos(e=None):
        a = page.width
        def aplicar_color_separadores(pc: bool):
            for sep in [
                separador_servicios,
                separador_programas,
                separador_VMS,
                separador_historia,
                separador_quienes,
                separador_sanitizacion,
            ]:
                if pc:
                    sep.bgcolor = COLOR_SEPARADOR_PC
                else:
                    sep.bgcolor = sep.data.get("bg_mobile", COLOR_SEPARADOR_MOBILE)

        # tamaño del botón empresa (icono + área táctil) + Logo empresa
        if a < 600:   # móviles
            icon_size = 26
            btn_size = 36
            logo_size = 42
            dropdown.top = 32
        elif a < 1020: # tablets
            icon_size = 32
            btn_size = 44
            logo_size = 54
            dropdown.top = 40
        else:         # desktop
            icon_size = 12
            btn_size = 26
            logo_size = 40
            dropdown.top = 35

        # 1) tamaño del contenedor (área clickeable visual)
        container_boton_empresa.width = btn_size
        container_boton_empresa.height = btn_size

        # 2) tamaño del ícono del IconButton interno
        inner_btn = container_boton_empresa.content
        if isinstance(inner_btn, ft.IconButton):
            inner_btn.icon_size = icon_size
            inner_btn.style = ft.ButtonStyle(
                padding=ft.padding.all(0),
                shape=ft.RoundedRectangleBorder(radius=9999),
            )

        # ejemplo de escalado Logo
        container_logo_empresa.width = logo_size
        container_logo_empresa.height = logo_size
        container_logo_empresa.border_radius = logo_size // 2
        inner_size = logo_size - 10   # margen/padding
        container_logo_empresa.content.width = inner_size
        container_logo_empresa.content.height = inner_size
        container_logo_empresa.content.border_radius = inner_size // 2

        # ==== NUEVO: mover fila_iconos y video según ancho ====
        es_desktop = a >= 1020
        es_tablet = 600 <= a < 1020

        if es_tablet or es_desktop:
            aplicar_color_separadores(True)
            # MOSTRAR PESTAÑAS EN PC
            if not slot_tabs_header.visible:
                slot_tabs_header.content = create_top_tabs(show_info, es_desktop=es_desktop)
                slot_tabs_header.visible = True
                slot_tabs_header.update()

            # esconder menú hamburguesa
            container_boton_empresa.visible = False
            col_form.bgcolor = ft.Colors.GREY_300
            col_form.border_radius = 16
            col_form.padding = 12
            col_form.shadow = ft.BoxShadow(2, 8, ft.Colors.BLACK12, offset=ft.Offset(0, 4))
            inicio_responsive.controls.clear()
            inicio_bg.content = banner_pc
            inicio_bg.height = ALTO_INICIO_PC

            contenido.spacing = 0
            # 👇 PC/Tablet: “espacio vacío” + formulario a la derecha
            inicio_responsive.controls.extend([col_spacer, col_form])
            inicio_responsive.alignment = ft.MainAxisAlignment.START
 
            separador_servicios.margin = ft.margin.only(top=0)
            # --- Ajustar tamaños de textos para Tablet y PC ---
            try:
                if valores_section.data:
                    if es_tablet or es_desktop:
                        # TITULOS tamaño 24
                        for t in valores_section.data["titulos"]:
                            t.size = 14
                        # TEXTOS tamaño 18
                        for t in valores_section.data["textos"]:
                            t.size = 14
                    else:
                        # Móvil valores originales
                        for t in valores_section.data["titulos"]:
                            t.size = 20
                        for t in valores_section.data["textos"]:
                            t.size = 14
            except:
                pass

            # --- Ajustar tamaños en QUIÉNES SOMOS ---
            try:
                if quienes_section.data:
                    if es_tablet or es_desktop:
                        quienes_section.data["subtitulo"].size = 14
                        quienes_section.data["texto"].size = 14
                    else:
                        quienes_section.data["subtitulo"].size = 18
                        quienes_section.data["texto"].size = 14
            except:
                pass
            
                # --- Ajustar tamaños en HISTORIA ---
            try:
                if historia_section.data:
                    if es_tablet or es_desktop:
                        historia_section.data["sub1"].size = 14
                        historia_section.data["sub2"].size = 14
                        historia_section.data["texto"].size = 14
                        for b in historia_section.data["bullets"]:
                            b.size = 14
                    else:
                        historia_section.data["sub1"].size = 18
                        historia_section.data["sub2"].size = 18
                        historia_section.data["texto"].size = 14
                        for b in historia_section.data["bullets"]:
                            b.size = 14
            except:
                pass

            # Tamaño del video en PC/Tablet
            video_card.width = 263
            video_card.height = 360


            # ⚠️ Importante: asegurarnos que video_card NO esté suelto en contenido
            safe_remove(video_card, contenido.controls)

            # 👉 PC/TABLET: también eliminamos el separador de sanitización del contenido
            safe_remove(separador_sanitizacion, contenido.controls)
            safe_remove(separador_historia, contenido.controls)

            
            # PC/TABLET → carrusel + DOS videos juntos
            # PC/TABLET → carrusel + 2 videos, cada uno en su “columna”
            zona_multimedia.content = ft.Row(
                [
                   carrusel_vertical,video_card,video_card2
                ],
            )

            zona_multimedia.update()

            # modo tablet / PC → sin saltos de línea la firma
            separador_final.content.value = separador_final.data["oneline_text"]
            separador_final.content.size = 12

            # fila_iconos va al header
            safe_remove(fila_iconos, contenido.controls)
            slot_iconos_header.content = fila_iconos
            slot_iconos_header.visible = True
            slot_iconos_header.update()

            # mostrar promo
            promo_stack.visible = True
            # 👇 NUEVO: asegurar que el carrusel vertical está activo
            try:
                start_vertical()
            except Exception:
                pass

            # ==== REORDENAR HEADER: tabs al lado del logo SOLO en PC ====
            try:
                top_row = barra_superior.content  # ft.Row
                if isinstance(top_row, ft.Row):
                    if es_desktop:
                        # PC: Logo + Tabs juntos, luego espacio, luego iconos + (hamburguesa oculta por tu lógica)
                        top_row.controls = [
                            container_logo_empresa,
                            slot_tabs_header,          # 👈 al lado del logo SOLO PC
                            ft.Container(expand=True),
                            slot_iconos_header,
                            container_boton_empresa,
                        ]
                    else:
                        # Móvil/Tablet: Logo + Título (solo móvil), espacio, luego lo demás
                        top_row.controls = [
                            container_logo_empresa,
                            wrap_titulo,               # 👈 solo visible en móvil
                            slot_tabs_header,          # 👈 oculto fuera de PC por el bloque anterior
                            slot_iconos_header,
                            container_boton_empresa,
                        ]
                    top_row.update()
            except Exception:
                pass

        else:
            barra_inferior.alignment = ft.MainAxisAlignment.END
            # 👇 Asegurarnos de que separador_sanitizacion EXISTE en contenido
            if separador_sanitizacion not in contenido.controls:
                try:
                    # idealmente después de valores_section
                    idx_val = contenido.controls.index(valores_section)
                    contenido.controls.insert(idx_val + 1, separador_sanitizacion)
                except ValueError:
                    try:
                        # o antes de separador_quienes
                        idx_q = contenido.controls.index(separador_quienes)
                        contenido.controls.insert(idx_q, separador_sanitizacion)
                    except ValueError:
                        # último recurso: al final
                        contenido.controls.append(separador_sanitizacion)

            # restaurar video debajo de separador_sanitizacion
            safe_remove(video_card, contenido.controls)
            
            try:
                idx = contenido.controls.index(separador_sanitizacion)
                contenido.controls.insert(idx + 1, video_card)
            except ValueError:
                contenido.controls.append(video_card)

        page.update()


    page.on_resized = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data=="shown" else None
        # Iniciar animaciones   
    animacion_empresa_task[0] = start_pulso_empresa()
    animacion_redes_task[0] = start_bounce()
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.update()
    ajustar_tamanos()
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))