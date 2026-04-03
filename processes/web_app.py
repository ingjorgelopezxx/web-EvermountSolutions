import flet as ft
import asyncio
from functions.asset_sources import HOME_HERO_BADGE_LOGO, HOME_HERO_IMAGE, HOME_HERO_LOGO
from functions.flet_actions import launch_url
from functions.resize_coordinator import register_resize_handler
from views.quienes import create_quienes
from views.historia import create_historia
from views.contactos import create_contactos_row  # Ã°Å¸â€˜Ë† importar fila de iconos
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
from processes.navigation import create_navigation
from processes.routes import create_route_handler
from processes.app_shell import (
    create_bottom_shell,
    create_content_base,
    create_dropdown_menu,
    create_header,
    create_overlay,
    create_root_stack,
    create_title_wrap,
)
from processes.layout import (
    adjust_banner_pc as layout_adjust_banner_pc,
    adjust_multimedia_zone as layout_adjust_multimedia_zone,
    apply_separator_sizes as layout_apply_separator_sizes,
    clamp as layout_clamp,
    get_content_widths as layout_get_content_widths,
)
from processes.ui_helpers import (
    COLOR_SEPARADOR_MOBILE,
    COLOR_SEPARADOR_PC,
    build_video_card as ui_build_video_card,
    create_separator as ui_create_separator,
    create_signature as ui_create_signature,
    create_signature_with_icons as ui_create_signature_with_icons,
    resize_video_card as ui_resize_video_card,
    safe_remove as ui_safe_remove,
    safe_update as ui_safe_update,
)

def main(page: ft.Page):
    # Inicializamos las propiedades de la pagina
    page.title = "EvermountSolutions"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    # --- Scrollbar mÃ¡s ancho (para el scroll de contenido / Column scroll="auto") ---
    try:
        page.theme = ft.Theme(
            scrollbar_theme=ft.ScrollbarTheme(
                thickness=14,
                thumb_visibility=False,
                thumb_color=ft.Colors.BLACK,
                track_color="transparent",
            )
        )
    except Exception as ex:
        print("No se pudo aplicar scrollbar_theme:", ex)

    # Usamos lista para mutabilidad, inicializamos la variable 
    animacion_empresa_task = [None]
    animacion_redes_task = [None]

    # WhatsApp mensaje mutable
    WHATSAPP_MSG = [
        "Hola Evermount Solutions.%0A"
        "Me gustaría recibir información sobre los servicios de control de plagas y sus costos.%0A"
        "¿Podrían orientarme, por favor?"
    ]
    
    def is_web_runtime(page: ft.Page) -> bool:
        # En tu caso estÃ¡s ejecutando WEB_BROWSER, asÃ­ que esto serÃ¡ True
        # Pero lo dejamos robusto.
        try:
            return bool(getattr(page, "web", True))
        except Exception:
            return True

    scroll_keys = {
        "cont_pantalla": ft.ScrollKey("cont_pantalla"),
        "inicio_responsive": ft.ScrollKey("inicio_responsive"),
        "banner_pc": ft.ScrollKey("banner_pc"),
        "servicios_menu": ft.ScrollKey("servicios_menu"),
        "programas_inicio": ft.ScrollKey("programas_inicio"),
        "mision": ft.ScrollKey("mision"),
        "historia": ft.ScrollKey("historia"),
        "quienes_somos": ft.ScrollKey("quienes_somos"),
        "formulario": ft.ScrollKey("formulario"),
    }


    def build_video_card(page: ft.Page, youtube_id: str, w: int, h: int) -> ft.Container:
        return ui_build_video_card(page, youtube_id, w, h, launch_url)
    
    video_card = build_video_card(page, "En49PmGEfLs", w=300, h=400)
    video_card2 = build_video_card(page, "eedRkoI9poE", w=263, h=360)
    # Ã¢Å“â€¦ Tercer video (Shorts)
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
        bgcolor="#F6FAFB",
        border_radius=32,
        border=ft.Border.all(1, "#DDE8EC"),
        padding=ft.Padding.only(top=14, left=10, right=10, bottom=0),  # Ã¢Å“â€¦ espacio superior
        margin=ft.Margin.symmetric(horizontal=8, vertical=6),
    )

    
    def crear_separador(page: ft.Page, texto: str, icono=None) -> ft.Container:
        return ui_create_separator(page, texto, icono)


    def crear_firma(page: ft.Page, texto: str) -> ft.Container:
        return ui_create_signature(page, texto)

    def crear_firma_con_iconos() -> tuple[ft.Control, ft.Control, ft.Control]:
        return ui_create_signature_with_icons()


    video_slot_movil = ft.Container(
        visible=False,
        alignment=ft.alignment.center,
        padding=ft.Padding.only(top=10, bottom=10),
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

    separador_servicios = crear_separador(page, "Servicios", ft.Icons.CHECKLIST)
    separador_servicios.key = scroll_keys["servicios_menu"]
    separador_programas = crear_separador(page, "Programas", ft.Icons.DATE_RANGE)
    separador_programas.key = scroll_keys["programas_inicio"]
    separador_VMS = crear_separador(
        page,
        "Misión | Visión | Valores",
        [
            ("Misión", ft.Icons.FLAG),
            ("Visión", ft.Icons.VISIBILITY),
            ("Valores", ft.Icons.VERIFIED),
        ],
    )
    separador_VMS.key = scroll_keys["mision"]
    separador_historia = crear_separador(page, "Historia", ft.Icons.HISTORY)
    separador_historia.key = scroll_keys["historia"]
    separador_quienes = crear_separador(page, "Quiénes Somos", ft.Icons.PEOPLE)
    separador_quienes.key = scroll_keys["quienes_somos"]
    separador_final = crear_firma(
        page,
        "Desarrollo por Ing. Jorge Lopez con tecnología Flet y Python\n"
        "Tel: +56937539304        Instagram: jorgelopezsilva\n"
        "2025 (c) Todos los derechos reservados"
    )
    separador_final.bgcolor = "#B9B8B8"
    footer_mobile, footer_tablet, footer_inline = crear_firma_con_iconos()
    separador_final.content = footer_mobile
    separador_final.data.update({
        "footer_inline": footer_inline,
        "footer_tablet": footer_tablet,
        "footer_mobile": footer_mobile,
    })

    separador_sanitizacion = crear_separador(page, "Sanitización de Ambientes", ft.Icons.SANITIZER)
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
        # --- Helper: iniciar carruseles sÃ³lo si ya estÃ¡n montados ---
    def _is_mounted(ctrl) -> bool:
        try:
            return ctrl.page is not None
        except Exception:
            return False

    async def _kick_carruseles():
        # Espera un tick para que el Ã¡rbol se monte
        await asyncio.sleep(0)

        # Carrusel principal: solo si ya estÃ¡ montado
        if _is_mounted(pantalla_inicial):
            start_carrusel()

        # Carrusel vertical: SIEMPRE lo arrancamos
        # porque dentro de _rotar() ya esperas a que imagen.page no sea None
        start_vertical()

    # --- Formulario ---
    formulario = create_formulario(page)
    menu_servicios_container = ft.Column(spacing=10)  # Ã°Å¸â€˜Ë† aquÃƒÂ­ pondremos el menÃƒÂº

    # 1) Crear wrappers
    cont_pantalla = ft.Container(content=pantalla_inicial, border_radius=0, padding=0, key=scroll_keys["cont_pantalla"])
    cont_form     = ft.Container(content=formulario,       border_radius=0, padding=0)
    ANCHO_FORM_PC = 380
    # 2) Crear ResponsiveRow
    col_pantalla = ft.Container(content=cont_pantalla, col={"xs": 12, "md": 10, "lg": 10})
    ANCHO_FORM_MAX = 380
    ANCHO_FORM_MIN = 260

    form_card = ft.Container(
        key=scroll_keys["formulario"],  # Ã¢Å“â€¦ destino de scroll
        content=formulario,
        width=ANCHO_FORM_MAX,   
        padding=5,
        bgcolor="rgba(255,255,255,0.95)",
        border_radius=16,
    )

    imagen_logo_empresa = ft.Image(
    src=HOME_HERO_LOGO,
    fit=ft.BoxFit.CONTAIN,
    )
    imagen_logo_empresa2 = ft.Image(
    src=HOME_HERO_BADGE_LOGO,
    fit=ft.BoxFit.FILL,   # llena el cÃ­rculo sin dejar bordes
    )

    inicio_responsive = ft.ResponsiveRow(
        controls=[col_pantalla, form_card],
        columns=12,
        run_spacing=10,
        spacing=10,
        key=scroll_keys["inicio_responsive"],
    )

    inicio_mobile = ft.Column(
        controls=[
            ft.Container(
                content=cont_pantalla,
                width=float("inf"),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=form_card,
                width=float("inf"),
                alignment=ft.alignment.center,
            ),
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        key=scroll_keys["inicio_responsive"],
    )

    imagen_banner_form = ft.Image(
        src=HOME_HERO_IMAGE,
        fit=ft.BoxFit.FILL,
        border_radius=16,
    )
    banner_img_box = ft.Container(
        content=imagen_banner_form,
        border_radius=0,
        clip_behavior=ft.ClipBehavior.NONE,
        padding=0,
        margin=0,
        bgcolor="transparent",
    )

    enlace_correo2 = "mailto:operaciones@evermountsolutions.cl?subject=Consulta&body=Hola, quisiera más información"
    def crear_boton_cotiza(page: ft.Page):
        COLOR_NORMAL = "#F6FBFC"
        COLOR_HOVER  = "#DDEEF2"
        TEXTO_COLOR  = "#123F49"

        texto = ft.Text(
            "Solicitar evaluación",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=TEXTO_COLOR,
        )

        btn = ft.Container(
            content=texto,
            bgcolor=COLOR_NORMAL,
            border_radius=18,
            border=ft.Border.all(1, "#D8E7EB"),
            shadow=ft.BoxShadow(
                blur_radius=14,
                spread_radius=0,
                color="rgba(6,32,41,0.14)",
                offset=ft.Offset(0, 6),
            ),
            width=230,
            height=54,
            alignment=ft.alignment.center,
            ink=True,
            on_click=lambda e: launch_url(page, enlace_correo2),
        )

        def _hover(e):
            btn.bgcolor = COLOR_HOVER if e.data == "true" else COLOR_NORMAL
            btn.update()

        btn.on_hover = _hover
        return btn

    boton_cotiza = crear_boton_cotiza(page)
    hero_badge = ft.Container(
        bgcolor="rgba(255,255,255,0.10)",
        border_radius=999,
        border=ft.Border.all(1, "rgba(255,255,255,0.14)"),
        padding=ft.Padding.symmetric(horizontal=14, vertical=6),
        content=ft.Text(
            "Atención técnica para hogares, empresas y comunidades",
            size=12,
            weight=ft.FontWeight.BOLD,
            color="#D9EEF4",
            text_align=ft.TextAlign.CENTER,
        ),
    )
    titulo1 = ft.Text("Evermount Solutions", size=64, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    titulo2 = ft.Text("Pest Defense", size=64, weight=ft.FontWeight.BOLD, color="#9FD2DE")

    desc_banner = ft.Text(
        "Protegemos espacios críticos con diagnóstico técnico, aplicación segura y seguimiento profesional.\n"
        "Programas mensuales, trimestrales y anuales para continuidad operativa y control preventivo.",
        size=24,
        color="#DCEEF3",
    )
    hero_trust = ft.Row(
        [
            ft.Container(
                bgcolor="rgba(255,255,255,0.08)",
                border_radius=999,
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                content=ft.Text("Respuesta comercial ágil", size=12, weight=ft.FontWeight.BOLD, color="#E7F5F8"),
            ),
            ft.Container(
                bgcolor="rgba(255,255,255,0.08)",
                border_radius=999,
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                content=ft.Text("Visitas programadas", size=12, weight=ft.FontWeight.BOLD, color="#E7F5F8"),
            ),
            ft.Container(
                bgcolor="rgba(255,255,255,0.08)",
                border_radius=999,
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                content=ft.Text("Cobertura hogar y empresa", size=12, weight=ft.FontWeight.BOLD, color="#E7F5F8"),
            ),
        ],
        wrap=True,
        spacing=10,
        run_spacing=10,
    )

    logo_box = ft.Container(
        content=imagen_logo_empresa2,
        width=200,
        height=200,
        bgcolor=ft.Colors.WHITE,
        border_radius=999,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.Border.all(3, ft.Colors.WHITE),
        shadow=ft.BoxShadow(
            blur_radius=30,
            spread_radius=0,
            color="rgba(7,24,32,0.25)",
            offset=ft.Offset(0, 12),
        ),
    )
    hero_text_block = ft.Column(
        [
            hero_badge,
            ft.Row(
                [
                    logo_box,
                    ft.Column([titulo1, titulo2], spacing=2),
                ],
                spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            desc_banner,
            hero_trust,
            boton_cotiza,
        ],
        spacing=14,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    form_card_host = ft.Column(
        tight=True,
        controls=[form_card],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    banner_pc = ft.Container(
        key=scroll_keys["banner_pc"],
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#08181E", "#123743", "#1F5967"],
        ),
        border_radius=30,
        shadow=ft.BoxShadow(
            blur_radius=26,
            spread_radius=0,
            color="rgba(7,24,32,0.20)",
            offset=ft.Offset(0, 10),
        ),
        content=ft.Row(
            [
                hero_text_block,
                banner_img_box, 
                form_card_host,
            ],
            spacing=18,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
        ),
        
    )

    banner_row = banner_pc.content  # Ã°Å¸â€˜Ë† referencia al Row interno del banner

    # Wrapper que se usa en el contenido
    inicio_bg = ft.Container(
        content=inicio_responsive,
        width=float("inf"),
        padding=ft.Padding.symmetric(horizontal=8, vertical=8),
    )
    

    def render_inicio():
        contenido.controls.clear()
        contenido.controls.extend([
           inicio_bg,separador_servicios,menu_servicios_container,separador_programas,zona_multimedia,separador_VMS,valores_section,separador_sanitizacion,video_slot_movil,separador_quienes,quienes_section,separador_historia,historia_section,separador_final])
        contenido.update()
        

    # Contenido central mutable
    contenido = ft.Column(
        [inicio_bg,separador_servicios,menu_servicios_container,separador_programas,zona_multimedia,separador_VMS,valores_section,separador_sanitizacion,video_slot_movil,separador_quienes,quienes_section,separador_historia,historia_section,separador_final],
        expand=True,
        alignment=ft.MainAxisAlignment.START,   # Ã¢Å“â€¦ pega todo arriba
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="auto",
    )

    push_route, scroll_to_key, scroll_content_top = create_navigation(page, contenido, scroll_keys)

    def asegurar_video_movil():
        zona_multimedia.content = carrusel_vertical
        safe_update(zona_multimedia)

        w = page.width or 0

        # Ã¢Å“â€¦ ancho razonable y altura en 9:16 (vertical)
        target_w = max(210, min(int(w * 0.92), 340))
        target_h = int(target_w * 16 / 9)  # Ã°Å¸â€˜Ë† portrait (9:16)

        # evita que se haga demasiado alto en pantallas muy pequeÃ±as
        if target_h > 520:
            target_h = 520
            target_w = int(target_h * 9 / 16)

        resize_video_card(video_card, target_w, target_h)

        video_slot_movil.content = video_card
        video_slot_movil.visible = True
        safe_update(video_slot_movil)


    def resize_video_card(card: ft.Container, w: int, h: int):
        ui_resize_video_card(card, w, h)

    def safe_remove(control, controls_list):
        ui_safe_remove(control, controls_list)

    def safe_update(ctrl):
        ui_safe_update(ctrl)

    # Flag e inicializador de SabÃ­as que
    sabiasque_inicializado = [False]
    intro_mostrado = [False]

    def show_intro_once():
        if intro_mostrado[0]:
            return
        intro_mostrado[0] = True
        # asegÃºrate de que nada intercepte clics
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

    #Funcion para detener el carrusel de imagenes 
    def parar_carrusel():
        stop_carrusel()
        stop_vertical()
        # Ã¢ÂÅ’ No quites pantalla_inicial del contenido; si quieres ocultarlo, oculta el contenedor:
        # if pantalla_inicial in contenido.controls: ...
        # Ã¢Å“â€¦ Mejor: no remover nada aquÃƒÂ­. Solo detener.
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

     # --- BotÃ³n EMPRESA (header) ---
    def toggle_menu(e):
        dropdown.visible = not dropdown.visible
        if dropdown.visible:
            # menÃƒÂº abierto Ã¢â€ â€™ detener pulso (usa la API del componente)
            abrir_menu()
            stop_pulso_empresa()
            animacion_empresa_task[0] = None
        else:
            cerrar_menu()
            # menÃƒÂº cerrado Ã¢â€ â€™ reanudar pulso (usa la API del componente)
            animacion_empresa_task[0] = start_pulso_empresa()
            
        safe_update(stack_raiz)

    # Crear botones, menu y header
    container_boton_empresa, start_pulso_empresa, stop_pulso_empresa = create_boton_empresa(page, toggle_menu)
    animacion_empresa_task[0] = start_pulso_empresa()   # Ã¢â€ Â arranque inicial
    
    # Creamos la funcion On_CLic del Boton Sabias que
    def on_sabiasque_click(e=None):
        # 1) detÃ©n carrusel si aplica
        try:
            parar_carrusel()
        except Exception:
            pass
        push_route("/sabiasque")

    def mostrar_inicio_con_intro(e=None):
            # cierra menÃº/overlays por si acaso
            try:
                cerrar_menu()
                overlay_cierra_menu.visible = False
            except Exception:
                pass

            # Delega al router. No limpies contenido ni llames render_inicio aquÃ­.
            push_route("/")
            
            # Scroll automÃ¡tico solo en tablet/PC
            if (page.width or 0) >= 600:
                # Dar un pequeÃ±o tiempo para permitir que el contenido se reconstruya
                async def _scroll():
                    width = page.width or 0
                    if width >= 1020:
                        target = "banner_pc"
                        start_duration = 400
                    else:
                        target = "formulario"
                        start_duration = 300
                    for wait_time, target_duration in ((0.9, start_duration), (0.45, 0), (0.8, 0)):
                        await asyncio.sleep(wait_time)
                        try:
                            await contenido.scroll_to(
                                scroll_key=scroll_keys[target],
                                duration=target_duration,
                            )
                            return
                        except RuntimeError:
                            continue
                        except Exception:
                            break

                page.run_task(_scroll)
            else:
                scroll_to_key("cont_pantalla", duration=200)

    container_logo_empresa = ft.Container(
        content=imagen_logo_empresa,
        width=64, height=64,               # se actualizan en ajustar_tamanos
        bgcolor=ft.Colors.WHITE,
        border_radius=9999,                # cÃ­rculo externo
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.Border.all(3, ft.Colors.WHITE),
        shadow=ft.BoxShadow(
            blur_radius=30,
            spread_radius=0,
            color="rgba(7,24,32,0.25)",
            offset=ft.Offset(0, 12),
        ),
        padding=4,
        on_click=mostrar_inicio_con_intro,
        ink=True,
        alignment=ft.alignment.center,
    )

    # --- Botones REDES ---
    boton_facebook, boton_instagram, boton_whatsapp, boton_sabiasque, start_bounce, stop_bounce = create_botones_redes(
        page, contacto_whatsapp, contacto_instagram, contacto_facebook, on_sabiasque_click
    )

    # Menu del Boton_Empresa
    menu_data = [
        ("Inicio", ft.Icons.HOME),
        ("Servicios", ft.Icons.CHECKLIST),
        ("Programas", ft.Icons.DATE_RANGE),
        ("Quiénes Somos", ft.Icons.PEOPLE),
        ("Historia", ft.Icons.HISTORY),
        ("Contactos", ft.Icons.CONTACT_PHONE),
        ("Misión-Visión", ft.Icons.FLAG),
    ]

    def cerrar_menu_hover(e):
        if e.data == "false":
            dropdown.visible = False
            cerrar_menu()
            if animacion_empresa_task[0] is None:
                animacion_empresa_task[0] = start_pulso_empresa()
            safe_update(stack_raiz)

    def on_menu_select(text):
        show_info(text)

    _, dropdown = create_dropdown_menu(menu_data, on_menu_select, cerrar_menu_hover)
    overlay_cierra_menu = create_overlay(lambda e: cerrar_menu())

    def abrir_menu():
        dropdown.visible = True
        overlay_cierra_menu.visible = True
        stop_pulso_empresa()
        animacion_empresa_task[0] = None
        stack_raiz.update()

    def cerrar_menu():
        dropdown.visible = False
        overlay_cierra_menu.visible = False
        if animacion_empresa_task[0] is None:
            animacion_empresa_task[0] = start_pulso_empresa()
        stack_raiz.update()

    _, wrap_titulo = create_title_wrap()
    barra_superior = create_header(
        container_logo_empresa,
        wrap_titulo,
        slot_tabs_header,
        slot_iconos_header,
        container_boton_empresa,
    )
    slot_contactos_bajo_header = ft.Container(
        visible=False,
        alignment=ft.alignment.center,
        padding=ft.Padding.symmetric(horizontal=8, vertical=6),
    )
    promo_items, promo_labels_text, promo_flotante, promo_stack, barra_inferior, zona_redes = create_bottom_shell(
        [boton_sabiasque, boton_facebook, boton_instagram, boton_whatsapp]
    )

    contenido_base = create_content_base(
        barra_superior,
        slot_contactos_bajo_header,
        contenido,
        zona_redes,
    )

    async def marquee_loop():
        return

        VELOCIDAD = 90
        PAUSA_FIN = 0.8

        while True:
            if not promo_stack.visible:
                await asyncio.sleep(0.5)
                continue

            ancho = zona_redes.width or page.width or 900
            texto_ancho = len(promo_labels_text) * 10 + len(promo_items) * 36
            x_inicial = ancho
            x_final = -texto_ancho
            t0 = time.time()

            while True:
                t = time.time() - t0
                x = x_inicial - VELOCIDAD * t

                if x < x_final:
                    break

                promo_flotante.left = x
                promo_flotante.update()
                await asyncio.sleep(0.01)

            await asyncio.sleep(PAUSA_FIN)

    intro_modal, show_intro, hide_intro = create_intro_overlay(page)
    stack_raiz = create_root_stack(contenido_base, overlay_cierra_menu, dropdown, intro_modal)
    form_layer_data = formulario.data or {}
    form_status_modal = form_layer_data.get("status_modal")
    if form_status_modal is not None:
        stack_raiz.controls.append(form_status_modal)

    def on_connect(e):
        push_route(page.route or "/")
        show_intro_once()
        ajustar_tamanos()

    page.on_connect = on_connect

    page.add(
        ft.Container(
            content=stack_raiz,
            expand=True,
        )
    )
    # Inicia carruseles tras montar el Ã¡rbol
    page.run_task(_kick_carruseles)
    page.run_task(marquee_loop)
    # Esto inyecta el grid de servicios en el contenedor vacÃ­o
    render_menu_servicios(page, menu_servicios_container)

    # Fallback: en el prÃ³ximo tick, intenta mostrar el intro una vez
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
        if opt == "Inicio":
            mostrar_inicio_con_intro()
        elif opt == "Quiénes Somos":
            scroll_to_key("quienes_somos", duration=500)
            return
        elif opt == "Servicios":
            scroll_to_key("servicios_menu", duration=500)
            return
        elif opt == "Programas":
            scroll_to_key("programas_inicio", duration=500)
            return
        elif opt == "Historia":
            scroll_to_key("historia", duration=500)
            return
        elif opt == "Misión-Visión":
            scroll_to_key("mision", duration=500)
            return
        elif opt == "Contactos":
            scroll_to_key("formulario", duration=500)
            return

        elif opt == "Ubicación":
            contenido.controls.append(
                ft.Text("Dirección de empresa", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
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
                    color="#DCEEF3",
                ),
                padding=ft.Padding.symmetric(horizontal=pad_x, vertical=pad_y),
                margin=ft.Margin.symmetric(horizontal=4),
                border_radius=8,
                bgcolor="transparent",
                ink=True,
                on_click=lambda e, t=text: show_info_callback(t),
            )
            tabs.append(tab)

        return ft.Row(controls=tabs, spacing=4, alignment=ft.MainAxisAlignment.CENTER)



    def clamp(v, mn, mx):
                return layout_clamp(v, mn, mx)

    def get_content_widths(w: int):
        return layout_get_content_widths(w)
    
    def ajustar_zona_multimedia():
        layout_adjust_multimedia_zone(
            page,
            bloque_programas=bloque_programas,
            carrusel_vertical=carrusel_vertical,
            zona_multimedia=zona_multimedia,
            video_cards=[video_card, video_card2, video_card3, video_card4],
            resize_video_card=resize_video_card,
            safe_update=safe_update,
        )
    def ajustar_banner_pc():
        layout_adjust_banner_pc(
            page,
            banner_pc=banner_pc,
            hero_text_block=hero_text_block,
            titulo1=titulo1,
            titulo2=titulo2,
            desc_banner=desc_banner,
            logo_box=logo_box,
            banner_img_box=banner_img_box,
            form_card=form_card,
            form_card_host=form_card_host,
            ancho_form_min=ANCHO_FORM_MIN,
            ancho_form_max=ANCHO_FORM_MAX,
            safe_update=safe_update,
        )


    def aplicar_tamano_separadores():
        layout_apply_separator_sizes(
            page,
            [
                separador_servicios,
                separador_programas,
                separador_VMS,
                separador_historia,
                separador_quienes,
                separador_sanitizacion,
            ],
        )    

    def ajustar_elementos_promocionales(a: int, es_tablet: bool, es_desktop: bool, compact_desktop: bool):
        hero_badge.width = None
        hero_badge.padding = ft.Padding.symmetric(horizontal=14, vertical=6)
        if isinstance(hero_badge.content, ft.Text):
            hero_badge.content.size = 12 if a >= 900 else 11

        hero_trust.spacing = 10 if a >= 900 else 8
        hero_trust.run_spacing = 10 if a >= 900 else 8

        for chip in hero_trust.controls:
            if isinstance(chip, ft.Container):
                chip.padding = ft.Padding.symmetric(
                    horizontal=12 if a >= 900 else 10,
                    vertical=8 if a >= 900 else 7,
                )
                if isinstance(chip.content, ft.Text):
                    chip.content.size = 12 if a >= 900 else 11

        if compact_desktop:
            hero_badge.width = float("inf")
            hero_trust.alignment = ft.MainAxisAlignment.CENTER
            boton_cotiza.width = clamp(int(a * 0.52), 210, 260)
            boton_cotiza.height = 50
            if isinstance(boton_cotiza.content, ft.Text):
                boton_cotiza.content.size = 18
        elif es_tablet:
            hero_trust.alignment = ft.MainAxisAlignment.START
            boton_cotiza.width = 210
            boton_cotiza.height = 48
            if isinstance(boton_cotiza.content, ft.Text):
                boton_cotiza.content.size = 17
        elif es_desktop:
            hero_trust.alignment = ft.MainAxisAlignment.START
            boton_cotiza.width = 230
            boton_cotiza.height = 54
            if isinstance(boton_cotiza.content, ft.Text):
                boton_cotiza.content.size = 20

        promo_row = promo_flotante.content if isinstance(promo_flotante.content, ft.Row) else None
        if promo_row is not None:
            if es_tablet:
                promo_row.wrap = True
                promo_row.spacing = 4
                promo_row.run_spacing = 2
                promo_stack.height = 58
                zona_redes.padding = ft.Padding.symmetric(horizontal=10, vertical=8)
                for ctrl in promo_row.controls:
                    if isinstance(ctrl, ft.Row):
                        ctrl.spacing = 4
                        for sub in ctrl.controls:
                            if isinstance(sub, ft.Icon):
                                sub.size = 14
                            elif isinstance(sub, ft.Text):
                                sub.size = 12
                    elif isinstance(ctrl, ft.Text):
                        ctrl.size = 13
            else:
                promo_row.wrap = False
                promo_row.spacing = 10
                promo_row.run_spacing = 0
                promo_stack.height = 46
                zona_redes.padding = ft.Padding.symmetric(horizontal=14, vertical=10)
                for ctrl in promo_row.controls:
                    if isinstance(ctrl, ft.Row):
                        ctrl.spacing = 6
                        for sub in ctrl.controls:
                            if isinstance(sub, ft.Icon):
                                sub.size = 18
                            elif isinstance(sub, ft.Text):
                                sub.size = 16
                    elif isinstance(ctrl, ft.Text):
                        ctrl.size = 18

    # --- Responsive: texto + ancho automÃ¡tico para WhatsApp ---
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
        section_w, text_section_w = get_content_widths(a)
        wrap_titulo.visible = False   # Ã¢Å“â€¦ en tablet/pc no lo uses

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
        

        # --- tamaÃ±os base por rangos ---
        if a < 600:          # mÃ³vil
            icon_size = 22
            btn_size  = 34
            logo_size = 34
            dropdown.top = 32

        elif a < 1300:       # Ã¢Å“â€¦ TODO lo que sea menor a 1300 (incluye tablet y desktop compact)
            icon_size = 22
            btn_size  = 22
            logo_size = 34
            dropdown.top = 35

        else:                # >=1300
            icon_size = 12
            btn_size  = 26
            logo_size = 40
            dropdown.top = 35

        # 1) tamaÃ±o del contenedor (Ã¡rea clickeable visual)
        container_boton_empresa.width = btn_size
        container_boton_empresa.height = btn_size

        # 2) tamaÃ±o del Ã­cono del IconButton interno
        inner_btn = container_boton_empresa.content
        if isinstance(inner_btn, ft.IconButton):
            inner_btn.icon_size = icon_size
            inner_btn.style = ft.ButtonStyle(
                padding=ft.Padding.all(0),
                shape=ft.RoundedRectangleBorder(radius=9999),
            )

        # ejemplo de escalado Logo
        container_logo_empresa.width = logo_size
        container_logo_empresa.height = logo_size
        container_logo_empresa.border_radius = logo_size // 2
        image_size = logo_size - 8
        container_logo_empresa.content.width = image_size
        container_logo_empresa.content.height = image_size

        # ==== NUEVO: mover fila_iconos y video segÃºn ancho ====
        es_desktop = a >= 1020
        es_tablet = 600 <= a < 1020
        compact_desktop = 600 <= a < 700

        inicio_bg.width = float("inf")
        banner_pc.width = float("inf")
        zona_multimedia.width = float("inf")
        menu_servicios_container.width = float("inf")
        inicio_bg.padding = ft.Padding.symmetric(horizontal=4, vertical=6) if a < 700 else ft.Padding.symmetric(horizontal=8, vertical=8)
        zona_multimedia.border_radius = 24 if a < 700 else 32
        zona_multimedia.margin = ft.Margin.symmetric(horizontal=4 if a < 700 else 8, vertical=6)
        valores_section.width = float("inf") if es_desktop else (text_section_w if text_section_w else float("inf"))
        quienes_section.width = float("inf") if es_desktop else (text_section_w if text_section_w else float("inf"))
        historia_section.width = text_section_w if text_section_w else float("inf")
        separador_final.width = float("inf")

        for sep in [
            separador_servicios,
            separador_programas,
            separador_VMS,
            separador_historia,
            separador_quienes,
            separador_sanitizacion,
        ]:
            sep.width = float("inf")
        # Historia visible SOLO en mÃ³vil
        mostrar_historia = a < 600
        separador_historia.visible = mostrar_historia
        historia_section.visible = mostrar_historia

        # (Opcional) si quieres tambiÃ©n ocultar el separador en tablet/pc para que no quede espacio
        if getattr(separador_historia, "page", None) is not None:
            separador_historia.update()
        if getattr(historia_section, "page", None) is not None:
            historia_section.update()


        if es_tablet or es_desktop:
            video_slot_movil.visible = False
            video_slot_movil.content = None
            safe_update(video_slot_movil)

            # si vienes desde mÃ³vil, saca el video_card del flujo mÃ³vil
            safe_remove(video_card, contenido.controls)
            safe_remove(video_card2, contenido.controls)
            safe_remove(video_card3, contenido.controls)
            safe_remove(video_card4, contenido.controls)

           # Ã¢Å“â€¦ En >=600: contactos SOLO en el header (derecha)
            slot_iconos_header.content = fila_iconos_header
            slot_iconos_header.visible = True

            # Ã¢Å“â€¦ Ocultar el slot bajo header y soltar el contenido
            slot_contactos_bajo_header.visible = False

            # Ã¢Å“â€¦ El mobile row NO debe verse
            fila_iconos_mobile.visible = False

            safe_remove(fila_iconos_mobile, contenido.controls)

            aplicar_color_separadores(True)
            # Ã¢Å“â€¦ Header compacto <1300: evita que crezca en alto
            if 600 <= a < 800:
                barra_superior.height = 50
                barra_superior.padding = ft.Padding.symmetric(horizontal=6, vertical=2)
            else:
                barra_superior.height = 56 if compact else 64
                barra_superior.padding = ft.Padding.symmetric(horizontal=8, vertical=4) if compact else ft.Padding.symmetric(horizontal=12, vertical=8)

            barra_superior.padding = ft.Padding.symmetric(horizontal=8, vertical=4) if compact else ft.Padding.symmetric(horizontal=12, vertical=8)
            try:
                if isinstance(barra_superior.content, ft.Row):
                    barra_superior.content.spacing = 6 if compact else 10
            except:
                pass

            # Tabs: visibles en tablet + desktop, ocultos solo en mÃ³vil
            es_mobile = a < 600
            slot_tabs_header.visible = not es_mobile

            if not es_mobile:
                # factor compacto <1300
                factor = 1.0
                if a < 1300:
                    factor = clamp((a - 900) / (1300 - 900), 0.75, 1.0)

                # Ã¢Å“â€¦ Ajuste extra < 780
                if a < 780:
                    factor2 = clamp((a - 600) / (780 - 600), 0.0, 1.0)   # 600->0, 780->1
                    tab_font = int(11 + 3 * factor2)     # 11..14
                    tab_pad_x = int(6 + 4 * factor2)     # 6..10
                    tab_pad_y = int(4 + 2 * factor2)     # 4..6
                else:
                    tab_font = int(16 * factor)
                    tab_pad_x = int(12 * factor)
                    tab_pad_y = int(6 * factor)


                # Ã°Å¸â€Â¥ SIEMPRE recrear tabs para que el tamaÃƒÂ±o suba y baje
                slot_tabs_header.content = create_top_tabs(
                    show_info,
                    es_desktop=(a > 600),
                    font_size=tab_font,
                    pad_x=tab_pad_x,
                    pad_y=tab_pad_y,
                )
                
            # esconder menÃº hamburguesa
            container_boton_empresa.visible = False
            form_card.bgcolor = "rgba(255,255,255,0.06)"
            form_card.border_radius = 16
            form_card.padding = 8 if a < 900 else 12
            form_card.shadow = ft.BoxShadow(2, 8, ft.Colors.BLACK_12, offset=ft.Offset(0, 4))
            inicio_bg.content = banner_pc

            contenido.spacing = 0
 
            separador_servicios.margin = ft.Margin.only(top=0)

            # --- Ajustar tamaÃƒÂ±os + layout en QUIÃƒâ€°NES SOMOS ---
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

                    # Ã¢Å“â€¦ NUEVO: si existe apply_layout, lo ejecutamos SIEMPRE
                    fn = quienes_section.data.get("apply_layout")
                    if fn:
                        fn()
            except Exception as ex:
                print("quienes apply_layout error:", ex)
            # Ã¢Å“â€¦ asegurar layout de valores

            # Ã¢Å¡Â Ã¯Â¸Â Importante: asegurarnos que video_card NO estÃƒÂ© suelto en contenido
            safe_remove(video_card, contenido.controls)

            # Ã°Å¸â€˜â€° PC/TABLET: si "QuiÃƒÂ©nes" ya incluye contenido de Historia, no renderices Historia abajo
            safe_remove(separador_sanitizacion, contenido.controls)

            # modo tablet / PC Ã¢â€ â€™ sin saltos de lÃƒÂ­nea la firma
            separador_final.content = separador_final.data["footer_tablet"] if es_tablet else separador_final.data["footer_inline"]
            
            async def _apply_contactos_luego():
                await asyncio.sleep(0)

                for fila in (fila_iconos_header, fila_iconos_mobile):
                    apply_fn = (fila.data or {}).get("apply_style_adaptativo")
                    if not apply_fn:
                        continue
                    try:
                        _ = fila.page
                    except Exception:
                        continue
                    try:
                        apply_fn()
                    except Exception as ex:
                        print("contactos apply_style_adaptativo error:", ex)

            page.run_task(_apply_contactos_luego)


            # mostrar promo
            promo_stack.visible = True
            # Ã°Å¸â€˜â€¡ NUEVO: asegurar que el carrusel vertical estÃƒÂ¡ activo
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
            # Ã¢Å“â€¦ WRAP del banner SOLO cuando < 700
            if compact_desktop:
                # activa wrap
                banner_row.wrap = True
                banner_row.spacing = 14
                banner_row.run_spacing = 14
                banner_row.alignment = ft.MainAxisAlignment.CENTER
                banner_row.vertical_alignment = ft.CrossAxisAlignment.START

                # hace que cada bloque use casi todo el ancho (para que bajen en filas)
                w_full = min(int(a * 0.92), text_section_w or int(a * 0.92))

                # 0) bloque texto (columna izquierda)
                try:
                    bloque_izq = banner_row.controls[0]   # ft.Column(...)
                    bloque_izq.width = clamp(w_full, 420, 760)
                except Exception:
                    pass

                # 1) imagen del banner
                if a < 900:
                    banner_img_box.width = clamp(int(a * 0.92), 280, 520)
                else:
                    banner_img_box.width = clamp(int(a * 0.42), 300, 420)
                # (altura se ajusta en ajustar_banner_pc, pero aquÃ­ puedes bajar un poco)
                if banner_img_box.height and a < 900:
                    banner_img_box.height = int(banner_img_box.height * 0.92)

                # 2) formulario
                if a < 900:
                    form_card.width = clamp(int(a * 0.92), 220, 360)
                else:
                    form_card.width = clamp(int(a * 0.34), 280, 360)
                form_card_host.width = form_card.width  # Ã°Å¸â€˜Ë† importante para que el host no Ã¢â‚¬Å“empujeÃ¢â‚¬Â
            else:
                # layout normal
                banner_row.wrap = False
                banner_row.run_spacing = 0
                banner_row.spacing = 12 if es_tablet else 0
                banner_row.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                banner_row.vertical_alignment = ft.CrossAxisAlignment.CENTER
                try:
                    bloque_izq = banner_row.controls[0]
                    if es_tablet:
                        bloque_izq.width = clamp(int(a * 0.31), 220, 270)
                    else:
                        bloque_izq.width = clamp(int(a * 0.45), 520, 680)
                except Exception:
                    pass
                form_card_host.width = form_card.width
                
            if 600 <= a < 700:
                banner_pc.padding = ft.Padding.symmetric(horizontal=12, vertical=12)
            else:
                banner_pc.padding = ft.Padding.symmetric(horizontal=30, vertical=18)

            ajustar_elementos_promocionales(a, es_tablet, es_desktop, compact_desktop)
            ajustar_zona_multimedia()
            ajustar_banner_pc()    
            
        else:
            # Ã¢Å“â€¦ MODO MÃƒâ€œVIL (<600): limpieza total de videos y colocar SOLO 1 debajo de sanitizaciÃƒÂ³n
            asegurar_video_movil()

            # Ã¢Å“â€¦ Contactos debajo del header
            slot_contactos_bajo_header.content = fila_iconos_mobile
            slot_contactos_bajo_header.visible = True
            fila_iconos_mobile.visible = True
            slot_iconos_header.visible = False
            slot_contactos_bajo_header.width = float("inf")                 # Ã¢Å“â€¦ ocupa todo el ancho
            slot_contactos_bajo_header.alignment = ft.alignment.center      # Ã¢Å“â€¦ centra su contenido
            try:
                apply_fn = (fila_iconos_mobile.data or {}).get("apply_style_adaptativo")
                if apply_fn:
                    apply_fn()  # Ã¢Å“â€¦ recalcula alignment/spacing segÃƒÂºn el modo actual
            except:
                pass
            safe_update(slot_contactos_bajo_header)
            # Ã¢Å“â€¦ en mÃƒÂ³vil: zona_multimedia SOLO carrusel vertical
            # Ã¢Å“â€¦ en mÃƒÂ³vil: mostrar Programas (texto) + carrusel vertical
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
            zona_multimedia.padding = ft.Padding.symmetric(horizontal=6, vertical=12)
            safe_update(zona_multimedia)

        
            # ========= MODO MÃƒâ€œVIL (<600): RESET TOTAL =========
            aplicar_color_separadores(False)

            # header: vuelve a modo mÃ³vil real
            container_boton_empresa.visible = True
            slot_tabs_header.visible = False
            slot_tabs_header.content = None

            wrap_titulo.visible = True  # tÃ­tulo mÃ³vil vuelve

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

            # banner/inicio: en mÃ³vil usamos una columna explÃ­cita para asegurar
            # que el carrusel principal quede arriba del formulario.
            inicio_bg.content = inicio_mobile

            # promo solo tablet/pc
            promo_stack.visible = False
            separador_final.content = separador_final.data["footer_mobile"]

            # aplica estilo mÃ³vil a contactos (sin update si no estÃ¡ montado)
            apply_fn = (fila_iconos_header.data or {}).get("apply_style_adaptativo")
            if apply_fn:
                try:
                    apply_fn()
                except:
                    pass

            barra_inferior.alignment = ft.MainAxisAlignment.END
            # Ã°Å¸â€˜â€¡ Asegurarnos de que separador_sanitizacion EXISTE en contenido
            if separador_sanitizacion not in contenido.controls:
                try:
                    # idealmente despuÃ©s de valores_section
                    idx_val = contenido.controls.index(valores_section)
                    contenido.controls.insert(idx_val + 1, separador_sanitizacion)
                except ValueError:
                    try:
                        # o antes de separador_quienes
                        idx_q = contenido.controls.index(separador_quienes)
                        contenido.controls.insert(idx_q, separador_sanitizacion)
                    except ValueError:
                        # Ãºltimo recurso: al final
                        contenido.controls.append(separador_sanitizacion)

        # Ã¢Å“â€¦ Recalcular tarjetas servicios al cambiar tamaÃƒÂ±o
        try:
            rebuild = (menu_servicios_container.data or {}).get("rebuild")
            if rebuild:
                rebuild()
        except Exception:
            pass

        # Ã¢Å“â€¦ asegurar layout de quienes en mÃƒÂ³vil
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
        safe_update(stack_raiz)


    # Ã¢Å“â€¦ NO pises on_resized de otros componentes (ej: formulario.py)
    resize_task_ref = [None]

    async def _debounced_resize_adjustment():
        try:
            await asyncio.sleep(0.08)
            ajustar_tamanos()
        except asyncio.CancelledError:
            pass

    def _schedule_resize_adjustment():
        if resize_task_ref[0] is not None:
            try:
                resize_task_ref[0].cancel()
            except Exception:
                pass
            finally:
                resize_task_ref[0] = None
        resize_task_ref[0] = page.run_task(_debounced_resize_adjustment)

    last_layout_width = [int(page.width or 0)]

    async def _watch_width_changes():
        try:
            while True:
                await asyncio.sleep(0.18)
                current_width = int(page.width or 0)
                if current_width <= 0:
                    continue
                if current_width != last_layout_width[0]:
                    last_layout_width[0] = current_width
                    _schedule_resize_adjustment()
        except asyncio.CancelledError:
            pass

    def _main_chain_resized(e):
        _schedule_resize_adjustment()

    register_resize_handler(page, "main_layout", _main_chain_resized)
    page.on_media_change = lambda e: _schedule_resize_adjustment()
    page.on_window_event = lambda e: _schedule_resize_adjustment() if e.data == "shown" else None
    page.run_task(_watch_width_changes)

    service_routes = {
        "/servicios/roedores": (
            render_servicio_desratizacion,
            "Hola Evermount Solutions, me gustaria agendar una visita para control de roedores. ¿Tienen disponibilidad?",
        ),
        "/servicios/sanitizacion": (
            render_servicio_sanitizacion,
            "Hola Evermount Solutions, me gustaria agendar una visita para desinfeccion y sanitizacion de ambientes. ¿Tienen disponibilidad?",
        ),
        "/servicios/voladores": (
            render_servicio_voladores,
            "Hola Evermount Solutions, me gustaria agendar una visita para control de insectos voladores. ¿Tienen disponibilidad?",
        ),
        "/servicios/rastreros": (
            render_servicio_rastreros,
            "Hola Evermount Solutions, me gustaria agendar una visita para control de insectos rastreros. ¿Tienen disponibilidad?",
        ),
        "/servicios/termitas": (
            render_servicio_termitas,
            "Hola Evermount Solutions, me gustaria agendar una visita para control de termitas. ¿Tienen disponibilidad?",
        ),
        "/servicios/aves": (
            render_servicio_aves_urbanas,
            "Hola Evermount Solutions, me gustaria agendar una visita para control de aves urbanas. ¿Tienen disponibilidad?",
        ),
    }

    page.on_route_change = create_route_handler(
        page=page,
        contenido=contenido,
        render_inicio=render_inicio,
        ajustar_tamanos=ajustar_tamanos,
        kick_carruseles=_kick_carruseles,
        ensure_sabiasque=ensure_sabiasque,
        parar_carrusel=parar_carrusel,
        scroll_content_top=scroll_content_top,
        cont_pantalla=cont_pantalla,
        cont_form=cont_form,
        cerrar_menu=cerrar_menu,
        overlay_cierra_menu=overlay_cierra_menu,
        service_routes=service_routes,
    )

        # Iniciar animaciones   
    animacion_empresa_task[0] = start_pulso_empresa()
    animacion_redes_task[0] = start_bounce()
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.update()
    ajustar_tamanos()






