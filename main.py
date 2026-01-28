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

def main(page: ft.Page):
    # Inicializamos las propiedades de la pagina
    page.title = "EvermountSolutions"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    # --- Scrollbar más ancho (para el scroll de contenido / Column scroll="auto") ---
    try:
        page.theme = ft.Theme(
            scrollbar_theme=ft.ScrollbarTheme(
                thickness=14,           # 👈 prueba 12-16
                thumb_visibility=False,
                thumb_color="#B9B8B8",    # gris oscuro elegante
                track_color="transparent",
            )
        )
    except Exception as ex:
        print("No se pudo aplicar scrollbar_theme:", ex)

    # Usamos lista para mutabilidad, inicializamos la variable 
    animacion_empresa_task = [None]     # ahora guardará el task del pulso del botón empresa
    animacion_redes_task = [None]       # task del bounce de redes    

    # WhatsApp mensaje mutable
    WHATSAPP_MSG = ["Hola 👋 Evermount Solutions.%0A"
    "Me gustaría recibir información sobre los servicios de control de plagas y sus costos.%0A"
    "¿Podrían orientarme, por favor?"]   # 👈 ahora es lista de un solo valor
    
    def is_web_runtime(page: ft.Page) -> bool:
        # En tu caso estás ejecutando WEB_BROWSER, así que esto será True
        # Pero lo dejamos robusto.
        try:
            return bool(getattr(page, "web", True))
        except Exception:
            return True

    def build_video_card(page: ft.Page, youtube_id: str, w: int, h: int) -> ft.Container:
        watch_url = f"https://www.youtube.com/watch?v={youtube_id}"
        thumb_url = f"https://img.youtube.com/vi/{youtube_id}/hqdefault.jpg"

        # ✅ elementos internos con tamaño explícito (sin expand)
        img = ft.Image(
            src=thumb_url,
            width=w,
            height=h,
            fit=ft.ImageFit.COVER,
        )

        overlay = ft.Container(
            width=w,
            height=h,
            bgcolor="rgba(0,0,0,0.18)",
            alignment=ft.alignment.center,
            content=ft.Icon(ft.Icons.PLAY_CIRCLE_FILL, size=64, color=ft.Colors.RED),
        )

        stack = ft.Stack(
            width=w,
            height=h,
            controls=[img, overlay],
        )

        card = ft.Container(
            width=w,
            height=h,
            border_radius=20,
            bgcolor=ft.Colors.WHITE,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
            content=stack,
            ink=True,
            on_click=lambda e: page.launch_url(watch_url),
        )

        # ✅ guardamos referencias para poder “resizear” bien después
        card.data = {"img": img, "overlay": overlay, "stack": stack}
        return card
    
    video_card = build_video_card(page, "En49PmGEfLs", w=300, h=400)
    video_card2 = build_video_card(page, "eedRkoI9poE", w=263, h=360)
    # ✅ Tercer video (Shorts)
    video_card3 = build_video_card(page, "8YuuRWtKZZY", w=263, h=360)
    video_card4 = build_video_card(page, "XF-iT-75XOs", w=263, h=360)
    # Contactos Redes Sociales
    numero_whatsapp = "+56999724454"
    contacto_whatsapp = f"https://wa.me/{numero_whatsapp}?text={WHATSAPP_MSG}"
    contacto_instagram = "https://www.instagram.com/evermount_solutions?igsh=MTJ4YzI5aHVtZ3Fiaw=="
    contacto_facebook = "http://facebook.com/share/15bcUW9HyS"
   
    # Crear carrusel vertical
    bloque_programas, carrusel_vertical, start_vertical, stop_vertical = create_vertical_carousel(page, intervalo=3)


    valores_section = create_valores(page)
    # --- Zona multimedia: carrusel + video (layout se ajusta en ajustar_tamanos) ---
    zona_multimedia = ft.Container(
        content=carrusel_vertical,
        padding=ft.padding.only(top=14, left=10, right=10, bottom=0),  # ✅ espacio superior
    )

    COLOR_SEPARADOR_PC = "#203a43"  # similar al gradiente desactivado
    COLOR_SEPARADOR_MOBILE = "#0D2943"
    
    def crear_separador(page: ft.Page, texto: str, icono=None) -> ft.Container:
        ic = ft.Icon(icono, color=ft.Colors.WHITE, size=24) if icono else None
        tx = ft.Text(
            texto,
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        )

        contenido_row = ft.Row(
            [ic if ic else ft.Container(), tx],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        )

        sep = ft.Container(
            bgcolor="#0D2943",
            margin=ft.margin.only(top=10),
            content=contenido_row,
            alignment=ft.alignment.center,
            width=float("inf"),                 # ✅ SIEMPRE responsive
            padding=ft.padding.symmetric(vertical=8),
        )

        sep.data = sep.data or {}
        sep.data.update({
            "bg_mobile": COLOR_SEPARADOR_MOBILE,
            "txt": tx,
            "icon": ic,
        })
        return sep


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

    
    video_slot_movil = ft.Container(
        visible=False,
        alignment=ft.alignment.center,
        padding=ft.padding.only(top=10, bottom=10),
    )

    historia_section = create_historia(page)
    quienes_section = create_quienes(page)
    
    fila_iconos_header = create_contactos_row(page)
    fila_iconos_mobile = create_contactos_row(page)

    # Slot para insertar fila_iconos en la barra superior cuando sea desktop
    slot_iconos_header = ft.Container(
        visible=False,
        alignment=ft.alignment.center_right,  # alineado a la derecha
    )
    slot_iconos_header.content = fila_iconos_header

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
    ANCHO_FORM_MAX = 380
    ANCHO_FORM_MIN = 260

    form_card = ft.Container(
        key="formulario",  # ✅ AÑADE ESTA LÍNEA
        content=formulario,
        width=ANCHO_FORM_MAX,   
        padding=5,
        bgcolor="rgba(255,255,255,0.95)",
        border_radius=16,
    )

    imagen_logo_empresa = ft.Image(
    src="https://i.postimg.cc/rFxRRS5D/logo-72x72.png",
    fit=ft.ImageFit.COVER,   # llena el círculo sin dejar bordes
    )
    imagen_logo_empresa2 = ft.Image(
    src="https://i.postimg.cc/sDPWTSk5/lll.jpg",
    fit=ft.ImageFit.FILL,   # llena el círculo sin dejar bordes
    )

    inicio_responsive = ft.ResponsiveRow(
        controls=[col_pantalla, form_card],
        columns=12,
        run_spacing=10,
        spacing=10,
        key="inicio_responsive",
    )

    imagen_banner_form = ft.Image(
        src="https://i.postimg.cc/htB3zLB6/Imagen7.png",  # cambia si quieres
        fit=ft.ImageFit.FILL,
        border_radius=16,
    )
    banner_img_box = ft.Container(
        content=imagen_banner_form,
        border_radius=16,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
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
            width=220,  # ✅ ancho fijo (ajusta a gusto)
            height=52,  # ✅ alto fijo
            alignment=ft.alignment.center,
            ink=True,
            on_click=lambda e: page.launch_url(enlace_correo2),
        )


        def _hover(e):
            btn.bgcolor = COLOR_HOVER if e.data == "true" else COLOR_NORMAL
            btn.update()

        btn.on_hover = _hover
        return btn
    boton_cotiza = crear_boton_cotiza(page)
    titulo1 = ft.Text("Evermount Solutions", size=64, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    titulo2 = ft.Text("Pest Defense", size=64, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE70)

    desc_banner = ft.Text(
        "Control profesional de plagas para hogares y empresas.\n"
        "Programas mensuales, trimestrales y anuales con garantía.",
        size=28,
        color=ft.Colors.WHITE,
    )
    logo_box = ft.Container(
        content=imagen_logo_empresa2,
        width=200,
        height=200,
        border_radius=999,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
    )
    form_card_host = ft.Column(
        tight=True,
        controls=[form_card],
    )

    banner_pc = ft.Container(
        key="banner_pc",
        padding=ft.padding.symmetric(horizontal=14, vertical=10),
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
                                logo_box,
                                ft.Column([titulo1, titulo2], spacing=2),
                            ],
                            spacing=16,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        desc_banner,
                        boton_cotiza,
                    ],
                    spacing=14,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                banner_img_box, 
                form_card_host,
            ],
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        
    )

    banner_row = banner_pc.content  # 👈 referencia al Row interno del banner

    # Wrapper que se usa en el contenido
    inicio_bg = ft.Container(
        content=inicio_responsive,
        width=float("inf"),
    )
    

    def render_inicio():
        contenido.controls.clear()
        contenido.controls.extend([
           inicio_bg,separador_servicios,menu_servicios_container,separador_programas,zona_multimedia,separador_VMS,valores_section,separador_sanitizacion,video_slot_movil,separador_quienes,quienes_section,separador_historia,historia_section,separador_final])
        contenido.update()
        page.update()
        

    # Contenido central mutable
    contenido = ft.Column(
        [inicio_bg,separador_servicios,menu_servicios_container,separador_programas,zona_multimedia,separador_VMS,valores_section,separador_sanitizacion,video_slot_movil,separador_quienes,quienes_section,separador_historia,historia_section,separador_final],
        expand=True,
        alignment=ft.MainAxisAlignment.START,   # ✅ pega todo arriba
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="auto",
    )

    def asegurar_video_movil():
        zona_multimedia.content = carrusel_vertical
        safe_update(zona_multimedia)

        w = page.width or 0

        # ✅ ancho razonable y altura en 9:16 (vertical)
        target_w = max(210, min(int(w * 0.92), 340))
        target_h = int(target_w * 16 / 9)  # 👈 portrait (9:16)

        # evita que se haga demasiado alto en pantallas muy pequeñas
        if target_h > 520:
            target_h = 520
            target_w = int(target_h * 9 / 16)

        resize_video_card(video_card, target_w, target_h)

        video_slot_movil.content = video_card
        video_slot_movil.visible = True
        safe_update(video_slot_movil)


    def resize_video_card(card: ft.Container, w: int, h: int):
        card.width = w
        card.height = h

        data = card.data or {}
        st = data.get("stack")
        img = data.get("img")
        ov = data.get("overlay")

        if st:
            st.width = w
            st.height = h
        if img:
            img.width = w
            img.height = h
        if ov:
            ov.width = w
            ov.height = h

        safe_update(card)

        # Helper para remover controles sin que Flet explote
    def safe_remove(control, controls_list):
        try:
            while control in controls_list:
                controls_list.remove(control)
        except Exception:
            pass
    def safe_update(ctrl):
        try:
            if getattr(ctrl, "page", None) is not None:
                ctrl.update()
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
    slot_contactos_bajo_header = ft.Container(
        visible=False,
        alignment=ft.alignment.center,
        padding=ft.padding.symmetric(horizontal=8, vertical=6),
    )
   

    # Creamos la fila donde estaran los botones inferiores
    Botones_agregar = ft.Row([boton_sabiasque,boton_facebook,boton_instagram,boton_whatsapp],alignment=ft.MainAxisAlignment.END,vertical_alignment=ft.CrossAxisAlignment.END)
    # --- TEXTO PROMOCIONAL (solo visible en tablet/PC) ---
    promo_text = ft.Text(
        "⚡ Atención rápida | 🧪 Insumos certificados | ✔️ Respuesta inmediata | 🥇 Técnicos especializados | 🏠 Hogar y empresas",
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
        slot_contactos_bajo_header,   # ✅ AQUÍ va fila_iconos_mobile en <600
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
        ajustar_tamanos()   # ✅ fuerza layout correcto en el primer render
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
            page.scroll_to(key="formulario", duration=500)
            return

        elif opt == "Ubicación":
            contenido.controls.append(
                ft.Text("dirección de empresa", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
            )
            contenido.update()

    def create_top_tabs(show_info_callback, es_desktop=False, font_size=16, pad_x=12, pad_y=6):
        tabs = []
        for text, icon in menu_data:
            if es_desktop and text in ("Contactos", "Historia"):
                continue

            tab = ft.Container(
                content=ft.Text(
                    text,
                    size=font_size,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                padding=ft.padding.symmetric(horizontal=pad_x, vertical=pad_y),
                margin=ft.margin.symmetric(horizontal=4),
                border_radius=8,
                bgcolor="transparent",
                ink=True,
                on_click=lambda e, t=text: show_info_callback(t),
            )
            tabs.append(tab)

        return ft.Row(controls=tabs, spacing=4, alignment=ft.MainAxisAlignment.CENTER)



    def clamp(v, mn, mx):
                return max(mn, min(mx, v))
    
    def ajustar_zona_multimedia():
        w = page.width or 0

        # Tamaño base “bonito” (ajústalo a gusto)
        base_w, base_h = 263, 360

        # Escalado suave para pantallas grandes/compactas
        factor = 1.0
        if w < 1400:
            factor = clamp((w - 900) / (1400 - 900), 0.85, 1.0)

        target_w = int(base_w * factor)
        target_h = int(base_h * factor)

        target_w = clamp(target_w, 230, 320)
        target_h = clamp(target_h, 320, 460)
        
        # ✅ 1) Videos
        resize_video_card(video_card, target_w, target_h)
        resize_video_card(video_card2, target_w, target_h)
        resize_video_card(video_card3, target_w, target_h)
        resize_video_card(video_card4, target_w, target_h)
        
        # ✅ 2) Carrusel vertical (contenedor externo + tarjeta interna)
        try:

            data = carrusel_vertical.data or {}
            tarjeta = data.get("tarjeta")
            imagen  = data.get("imagen")

            if tarjeta:
                tarjeta.width = target_w
                tarjeta.height = target_h
                safe_update(tarjeta)

            if imagen:
                imagen.width = target_w
                imagen.height = target_h
                safe_update(imagen)


            safe_update(carrusel_vertical)
        except Exception as ex:
            print("resize carrusel_vertical error:", ex)


        def box_auto(ctrl, w):
                return ft.Container(
                    content=ctrl,
                    width=w,
                    padding=0,
                    margin=0,
                    alignment=ft.alignment.center,
                )
        # ✅ 3) Si usas box_fixed, pásale target_w/target_h
        def box_fixed(ctrl):
            return ft.Container(
                content=ctrl,
                width=target_w,
                height=target_h,
                padding=0,
                margin=0,
                alignment=ft.alignment.center,
            )

        # ==============================
        # Construir lista dinámica
        # ==============================
        controls_row = [
            box_auto(bloque_programas, 430),
            box_fixed(carrusel_vertical),
        ]
        if w >= 946:
            controls_row.append(box_fixed(video_card))
        if w >= 1200:
            controls_row.append(box_fixed(video_card2))
        if w > 1577:
            controls_row.append(box_fixed(video_card3))
        if w > 1900:
            controls_row.append(box_fixed(video_card4))

        zona_multimedia.content = ft.Row(
            controls=controls_row,
            spacing=18,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            wrap=True,
        )
        
        safe_update(zona_multimedia)

    def ajustar_banner_pc():
        w = page.width or 1200

        def clamp(v, mn, mx):
            return max(mn, min(mx, v))

        # ✅ factor fluido 800 -> 600
        # en 800 => t=1.0  |  en 600 => t=0.0
        t = clamp((w - 600) / (800 - 600), 0.0, 1.0)

        # ✅ factor final (en 600 será 0.68, en 800 será 1.0)
        # ajusta 0.65-0.75 según tu gusto
        f_800_600 = 0.68 + 0.32 * t

        # --- tamaños base (tu estilo original) ---
        t1 = int(w * 0.035)
        t2 = int(w * 0.032)
        td = int(w * 0.015)
        logo = int(w * 0.10)

        # 🔻 tu reducción actual <1300 (la mantenemos)
        if w < 1300:
            factor = clamp((w - 900) / (1300 - 900), 0.7, 1.0)
            t1 = int(t1 * factor)
            t2 = int(t2 * factor)
            td = int(td * factor)
            logo = int(logo * factor)

        # ✅ NUEVO: si w < 800, aplica reducción fluida hasta 600
        if w < 800:
            t1 = int(t1 * f_800_600)
            t2 = int(t2 * f_800_600)
            td = int(td * f_800_600)
            logo = int(logo * f_800_600)

        # Clamp final (más bajos cuando baja de 800)
        if w < 800:
            t1 = clamp(t1, 18, 52)
            t2 = clamp(t2, 16, 48)
            td = clamp(td, 10, 20)
            logo = clamp(logo, 70, 140)
        else:
            t1 = clamp(t1, 22, 64)
            t2 = clamp(t2, 20, 58)
            td = clamp(td, 12, 28)
            logo = clamp(logo, 90, 200)

        titulo1.size = t1
        titulo2.size = t2
        desc_banner.size = td
        logo_box.width = logo
        logo_box.height = logo
        # --- Imagen del banner (también baja de 800 a 600) ---
        img_w = clamp(int(w * 0.18), 160, 340)
        base_h = int(w * 0.22)

        if w < 1600:
            tt = (1600 - w) / (1600 - 1200)
            factor_h = 1.0 + 0.30 * clamp(tt, 0, 1)
        else:
            factor_h = 1.0

        img_h = int(base_h * factor_h)

        # ✅ si w < 800: baja más fluido
        if w < 800:
            img_h = int(img_h * (0.70 + 0.30 * t))  # en 600 -> 0.70

        img_h = clamp(img_h, 200 if w < 800 else 260, 520)

        banner_img_box.width = img_w
        banner_img_box.height = img_h

        # --- Formulario (ancho + padding fluido 800->600) ---
        if w < 800:
            # en 800 -> 280 aprox, en 600 -> 220 aprox
            form_w = int(220 + 60 * t)
            form_w = clamp(form_w, 210, 300)

            # baja padding para que entre todo
            form_card.padding = 8 if w < 700 else 10
        else:
            form_w = clamp(int(w * 0.22), ANCHO_FORM_MIN, ANCHO_FORM_MAX)
            form_card.padding = 12

        form_card.width = form_w

        safe_update(banner_pc)
        page.update()



    def aplicar_tamano_separadores():
        w = page.width or 0

        if w < 600:
            txt_size, icon_size, pad_v = 16, 18, 6
        elif w < 1300:
            txt_size, icon_size, pad_v = 18, 20, 7
        else:
            txt_size, icon_size, pad_v = 20, 24, 8

        separadores = [
            separador_servicios,
            separador_programas,
            separador_VMS,
            separador_historia,
            separador_quienes,
            separador_sanitizacion,
        ]

        for sep in separadores:
            data = sep.data or {}
            tx = data.get("txt")
            ic = data.get("icon")

            if tx:
                tx.size = txt_size
            if ic:
                ic.size = icon_size

            sep.padding = ft.padding.symmetric(vertical=pad_v)
            sep.width = float("inf")


            # ✅ update directo (ya están montados cuando se ven)
            if getattr(sep, "page", None) is not None:
                sep.update()
    
    # --- Responsive: texto + ancho automático para WhatsApp ---
    def ajustar_tamanos(e=None):
        a = page.width or 0
        # --- Guard: en el primer render a veces a==0 o viene inestable ---
        if a <= 0:
            async def _retry():
                await asyncio.sleep(0)  # 1 tick
                ajustar_tamanos()
            page.run_task(_retry)
            return

        compact = a < 1300
        wrap_titulo.visible = False   # ✅ en tablet/pc no lo uses

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
        

        # --- tamaños base por rangos ---
        if a < 600:          # móvil
            icon_size = 22
            btn_size  = 34
            logo_size = 34
            dropdown.top = 32

        elif a < 1300:       # ✅ TODO lo que sea menor a 1300 (incluye tablet y desktop compact)
            icon_size = 22
            btn_size  = 22
            logo_size = 34
            dropdown.top = 35

        else:                # >=1300
            icon_size = 12
            btn_size  = 26
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
        # Historia visible SOLO en móvil
        mostrar_historia = a < 600
        separador_historia.visible = mostrar_historia
        historia_section.visible = mostrar_historia

        # (Opcional) si quieres también ocultar el separador en tablet/pc para que no quede espacio
        if getattr(separador_historia, "page", None) is not None:
            separador_historia.update()
        if getattr(historia_section, "page", None) is not None:
            historia_section.update()


        if es_tablet or es_desktop:
            video_slot_movil.visible = False
            video_slot_movil.content = None
            safe_update(video_slot_movil)

            # si vienes desde móvil, saca el video_card del flujo móvil
            safe_remove(video_card, contenido.controls)
            safe_remove(video_card2, contenido.controls)
            safe_remove(video_card3, contenido.controls)
            safe_remove(video_card4, contenido.controls)

           # ✅ En >=600: contactos SOLO en el header (derecha)
            slot_iconos_header.content = fila_iconos_header
            slot_iconos_header.visible = True

            # ✅ Ocultar el slot bajo header y soltar el contenido
            slot_contactos_bajo_header.visible = False

            # ✅ El mobile row NO debe verse
            fila_iconos_mobile.visible = False

            safe_remove(fila_iconos_mobile, contenido.controls)

            aplicar_color_separadores(True)
            # ✅ Header compacto <1300: evita que crezca en alto
            if 600 <= a < 800:
                barra_superior.height = 50
                barra_superior.padding = ft.padding.symmetric(horizontal=6, vertical=2)
            else:
                barra_superior.height = 56 if compact else 64
                barra_superior.padding = ft.padding.symmetric(horizontal=8, vertical=4) if compact else ft.padding.symmetric(horizontal=12, vertical=8)

            barra_superior.padding = ft.padding.symmetric(horizontal=8, vertical=4) if compact else ft.padding.symmetric(horizontal=12, vertical=8)
            try:
                if isinstance(barra_superior.content, ft.Row):
                    barra_superior.content.spacing = 6 if compact else 10
            except:
                pass

            # Tabs: visibles en tablet + desktop, ocultos solo en móvil
            es_mobile = a < 600
            slot_tabs_header.visible = not es_mobile

            if not es_mobile:
                # factor compacto <1300
                factor = 1.0
                if a < 1300:
                    factor = clamp((a - 900) / (1300 - 900), 0.75, 1.0)

                # ✅ Ajuste extra < 780
                if a < 780:
                    factor2 = clamp((a - 600) / (780 - 600), 0.0, 1.0)   # 600->0, 780->1
                    tab_font = int(11 + 3 * factor2)     # 11..14
                    tab_pad_x = int(6 + 4 * factor2)     # 6..10
                    tab_pad_y = int(4 + 2 * factor2)     # 4..6
                else:
                    tab_font = int(16 * factor)
                    tab_pad_x = int(12 * factor)
                    tab_pad_y = int(6 * factor)


                # 🔥 SIEMPRE recrear tabs para que el tamaño suba y baje
                slot_tabs_header.content = create_top_tabs(
                    show_info,
                    es_desktop=(a > 600),
                    font_size=tab_font,
                    pad_x=tab_pad_x,
                    pad_y=tab_pad_y,
                )
                
            # esconder menú hamburguesa
            container_boton_empresa.visible = False
            form_card.bgcolor = ft.Colors.GREY_300
            form_card.border_radius = 16
            form_card.padding = 8 if a < 900 else 12
            form_card.shadow = ft.BoxShadow(2, 8, ft.Colors.BLACK12, offset=ft.Offset(0, 4))
            inicio_bg.content = banner_pc

            contenido.spacing = 0
 
            separador_servicios.margin = ft.margin.only(top=0)

            # --- Ajustar tamaños + layout en QUIÉNES SOMOS ---
            try:
                if quienes_section.data:
                    # Si tu quienes.py sigue usando referencias antiguas:
                    if "subtitulo" in quienes_section.data and "texto" in quienes_section.data:
                        if es_tablet or es_desktop:
                            quienes_section.data["subtitulo"].size = 14
                            quienes_section.data["texto"].size = 14
                        else:
                            quienes_section.data["subtitulo"].size = 18
                            quienes_section.data["texto"].size = 14

                    # ✅ NUEVO: si existe apply_layout, lo ejecutamos SIEMPRE
                    fn = quienes_section.data.get("apply_layout")
                    if fn:
                        fn()
            except Exception as ex:
                print("quienes apply_layout error:", ex)
            # ✅ asegurar layout de valores

            # ⚠️ Importante: asegurarnos que video_card NO esté suelto en contenido
            safe_remove(video_card, contenido.controls)

            # 👉 PC/TABLET: si "Quiénes" ya incluye contenido de Historia, no renderices Historia abajo
            safe_remove(separador_sanitizacion, contenido.controls)

            # modo tablet / PC → sin saltos de línea la firma
            separador_final.content.value = separador_final.data["oneline_text"]
            separador_final.content.size = 12
            
            async def _apply_contactos_luego():
                await asyncio.sleep(0)

                for fila in (fila_iconos_header, fila_iconos_mobile):
                    apply_fn = (fila.data or {}).get("apply_style_adaptativo")
                    if apply_fn and getattr(fila, "page", None) is not None:
                        try:
                            apply_fn()
                        except Exception as ex:
                            print("contactos apply_style_adaptativo error:", ex)

            page.run_task(_apply_contactos_luego)


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
                    if es_tablet or es_desktop:
                        wrap_titulo.visible = False
                        top_row.controls = [
                            container_logo_empresa,
                            slot_tabs_header,
                            ft.Container(expand=True),
                            slot_iconos_header,
                        ]
                    top_row.update()

            except Exception:
                pass
            # ✅ WRAP del banner SOLO cuando < 700
            if a < 700:
                # activa wrap
                banner_row.wrap = True
                banner_row.spacing = 10
                banner_row.run_spacing = 10
                banner_row.alignment = ft.MainAxisAlignment.CENTER
                banner_row.vertical_alignment = ft.CrossAxisAlignment.START

                # hace que cada bloque use casi todo el ancho (para que bajen en filas)
                w_full = int(a * 0.92)

                # 0) bloque texto (columna izquierda)
                try:
                    bloque_izq = banner_row.controls[0]   # ft.Column(...)
                    bloque_izq.width = w_full
                except Exception:
                    pass

                # 1) imagen del banner
                banner_img_box.width = w_full
                # (altura se ajusta en ajustar_banner_pc, pero aquí puedes bajar un poco)
                if banner_img_box.height:
                    banner_img_box.height = int(banner_img_box.height * 0.85)

                # 2) formulario
                form_card.width = clamp(int(a * 0.92), 220, 360)
                form_card_host.width = form_card.width  # 👈 importante para que el host no “empuje”
            else:
                # layout normal
                banner_row.wrap = False
                banner_row.run_spacing = 0
                banner_row.spacing = 0
                banner_row.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                banner_row.vertical_alignment = ft.CrossAxisAlignment.CENTER
                try:
                    bloque_izq = banner_row.controls[0]
                    bloque_izq.width = None
                except Exception:
                    pass
                form_card_host.width = None
                
            if 600 <= a < 700:
                banner_pc.padding = ft.padding.symmetric(horizontal=12, vertical=12)
            else:
                banner_pc.padding = ft.padding.symmetric(horizontal=30, vertical=18)

            ajustar_zona_multimedia()
            ajustar_banner_pc()    
            
        else:
            # ✅ MODO MÓVIL (<600): limpieza total de videos y colocar SOLO 1 debajo de sanitización
            asegurar_video_movil()

            # ✅ Contactos debajo del header
            slot_contactos_bajo_header.content = fila_iconos_mobile
            slot_contactos_bajo_header.visible = True
            fila_iconos_mobile.visible = True
            slot_iconos_header.visible = False
            slot_contactos_bajo_header.width = float("inf")                 # ✅ ocupa todo el ancho
            slot_contactos_bajo_header.alignment = ft.alignment.center      # ✅ centra su contenido
            try:
                apply_fn = (fila_iconos_mobile.data or {}).get("apply_style_adaptativo")
                if apply_fn:
                    apply_fn()  # ✅ recalcula alignment/spacing según el modo actual
            except:
                pass
            safe_update(slot_contactos_bajo_header)
            # ✅ en móvil: zona_multimedia SOLO carrusel vertical
            # ✅ en móvil: mostrar Programas (texto) + carrusel vertical
            zona_multimedia.content = ft.Column(
                controls=[
                    ft.Container(
                        content=bloque_programas,
                        width=float("inf"),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=10),
                    ft.Container(
                        content=carrusel_vertical,
                        alignment=ft.alignment.center,
                    ),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            safe_update(zona_multimedia)

        
            # ========= MODO MÓVIL (<600): RESET TOTAL =========
            aplicar_color_separadores(False)

            # header: vuelve a modo móvil real
            container_boton_empresa.visible = True
            slot_tabs_header.visible = False
            slot_tabs_header.content = None

            wrap_titulo.visible = True  # título móvil vuelve

            # restaura orden normal del header (como lo creaste al inicio)
            try:
                top_row = barra_superior.content
                if isinstance(top_row, ft.Row):
                    top_row.controls = [
                        container_logo_empresa,
                        wrap_titulo,
                        slot_tabs_header,
                        slot_iconos_header,
                        container_boton_empresa
                    ]
                    top_row.update()
            except Exception:
                pass

            # banner/inicio: vuelve al layout móvil (ResponsiveRow original)
            inicio_bg.content = inicio_responsive

            # promo solo tablet/pc
            promo_stack.visible = False

            # aplica estilo móvil a contactos (sin update si no está montado)
            apply_fn = (fila_iconos_header.data or {}).get("apply_style_adaptativo")
            if apply_fn:
                try:
                    apply_fn()
                except:
                    pass

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

        # ✅ Recalcular tarjetas servicios al cambiar tamaño
        try:
            rebuild = (menu_servicios_container.data or {}).get("rebuild")
            if rebuild:
                rebuild()
        except Exception:
            pass

        # ✅ asegurar layout de quienes en móvil
        try:
            fn = (quienes_section.data or {}).get("apply_layout")
            if fn:
                fn()
        except:
            pass
        
        try:
            fnv = (valores_section.data or {}).get("apply_layout")
            if fnv:
                fnv()
        except:
            pass

        aplicar_tamano_separadores() 
        page.update()


    # ✅ NO pises on_resized de otros componentes (ej: formulario.py)
    _prev_on_resized = page.on_resized

    def _main_chain_resized(e):
        try:
            if _prev_on_resized:
                _prev_on_resized(e)   # 👈 aquí corre ajustar_responsivo() del formulario
        except Exception:
            pass
        ajustar_tamanos(e)            # 👈 tu lógica principal

    page.on_resized = _main_chain_resized
    page.on_window_event = lambda e: ajustar_tamanos() if e.data == "shown" else None

        # Iniciar animaciones   
    animacion_empresa_task[0] = start_pulso_empresa()
    animacion_redes_task[0] = start_bounce()
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.update()
    ajustar_tamanos()
ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    port=int(os.environ.get("PORT", 8080)),
    assets_dir="assets",
)
