import json
from flet import Ref
import time
import flet as ft
import asyncio
from types import SimpleNamespace
import os
from functions.flet_actions import launch_url
from views.quienes import create_quienes
from views.historia import create_historia
from views.contactos import create_contactos_row  # ðŸ‘ˆ importar fila de iconos
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
                thickness=14,
                thumb_visibility=False,
                thumb_color="#B9B8B8",    # gris oscuro elegante
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
        # En tu caso estás ejecutando WEB_BROWSER, así que esto será True
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

    async def _push_route_async(route: str):
        await page.push_route(route)

    def push_route(route: str):
        page.run_task(_push_route_async, route)

    async def _scroll_to_async(scroll_key_name: str, duration: int = 0):
        if (page.route or "/") != "/":
            await page.push_route("/")
            await asyncio.sleep(0.35)

        for wait_time, target_duration in ((0.35, duration), (0.55, 0), (0.85, 0)):
            await asyncio.sleep(wait_time)
            try:
                await contenido.scroll_to(
                    scroll_key=scroll_keys[scroll_key_name],
                    duration=target_duration,
                )
                return
            except RuntimeError:
                continue
            except Exception:
                break

    def scroll_to_key(scroll_key: str, duration: int = 0):
        page.run_task(_scroll_to_async, scroll_key, duration)

    async def _scroll_content_top_async():
        for wait_time in (0.0, 0.12, 0.28):
            if wait_time:
                await asyncio.sleep(wait_time)
            try:
                await contenido.scroll_to(offset=0, duration=0)
                return
            except RuntimeError:
                continue
            except Exception:
                break

    def scroll_content_top():
        page.run_task(_scroll_content_top_async)

    def build_video_card(page: ft.Page, youtube_id: str, w: int, h: int) -> ft.Container:
        watch_url = f"https://www.youtube.com/watch?v={youtube_id}"
        thumb_url = f"https://img.youtube.com/vi/{youtube_id}/hqdefault.jpg"

        # âœ… elementos internos con tamaÃ±o explÃ­cito (sin expand)
        img = ft.Image(
            src=thumb_url,
            width=w,
            height=h,
            fit=ft.BoxFit.COVER,
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
            shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK_26, offset=ft.Offset(2, 2)),
            content=stack,
            ink=True,
            on_click=lambda e: launch_url(page, watch_url),
        )

        # âœ… guardamos referencias para poder â€œresizearâ€ bien despuÃ©s
        card.data = {"img": img, "overlay": overlay, "stack": stack}
        return card
    
    video_card = build_video_card(page, "En49PmGEfLs", w=300, h=400)
    video_card2 = build_video_card(page, "eedRkoI9poE", w=263, h=360)
    # âœ… Tercer video (Shorts)
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
        padding=ft.Padding.only(top=14, left=10, right=10, bottom=0),  # âœ… espacio superior
    )

    COLOR_SEPARADOR_PC = "#203a43"  # similar al gradiente desactivado
    COLOR_SEPARADOR_MOBILE = "#0D2943"
    
    def crear_separador(page: ft.Page, texto: str, icono=None) -> ft.Container:
        tx = None
        ic = None
        if isinstance(icono, list) and icono and isinstance(icono[0], tuple):
            bloques = []
            for idx, (label, icn) in enumerate(icono):
                bloques.append(
                    ft.Row(
                        [
                            ft.Icon(icn, color=ft.Colors.WHITE, size=20),
                            ft.Text(
                                label,
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        spacing=6,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                )
                if idx < len(icono) - 1:
                    bloques.append(
                        ft.Text(
                            "|",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        )
                    )
            contenido_row = ft.Row(
                bloques,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=8,
                wrap=False,
            )
        elif isinstance(icono, (list, tuple)):
            iconos = [
                ft.Icon(icn, color=ft.Colors.WHITE, size=22)
                for icn in icono
            ]
            ic = ft.Row(
                iconos,
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        else:
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
            margin=ft.Margin.only(top=10),
            content=contenido_row,
            alignment=ft.alignment.center,
            width=float("inf"),                 # âœ… SIEMPRE responsive
            padding=ft.Padding.symmetric(vertical=8),
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

    def crear_firma_con_iconos() -> tuple[ft.Control, ft.Control, ft.Control]:
        def _inline_item(icon_name, label, size=12):
            return ft.Row(
                [
                    ft.Icon(icon_name, size=size + 2, color="#202325"),
                    ft.Text(label, size=size, weight=ft.FontWeight.BOLD, color="#202325"),
                ],
                spacing=4,
                tight=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

        footer_inline = ft.Row(
            [
                ft.Text("Desarrollo por Ing. Jorge Lopez con tecnología", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
                ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.WEB, "Flet"),
                ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.CODE, "Python"),
                ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.PHONE, "+56937539304"),
                ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.CAMERA_ALT, "jorgelopezsilva"),
                ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
                ft.Text("2025 (c) Todos los derechos reservados", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
            ],
            spacing=8,
            wrap=True,
            run_spacing=6,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        footer_tablet = ft.Row(
            [
                ft.Text("Desarrollo Ing. Jorge Lopez", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
                ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.WEB, "Flet", 9),
                ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.CODE, "Python", 9),
                ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.PHONE, "+56937539304", 9),
                ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
                _inline_item(ft.Icons.CAMERA_ALT, "jorgelopezsilva", 9),
                ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
                ft.Text("2025 (c)", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
            ],
            spacing=4,
            wrap=False,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        footer_mobile = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Desarrollo Ing. Jorge Lopez", size=10, weight=ft.FontWeight.BOLD, color="#202325"),
                        ft.Text("|", size=10, weight=ft.FontWeight.BOLD, color="#202325"),
                        _inline_item(ft.Icons.WEB, "Flet", 11),
                        ft.Text("|", size=11, weight=ft.FontWeight.BOLD, color="#202325"),
                        _inline_item(ft.Icons.CODE, "Python", 11),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        _inline_item(ft.Icons.PHONE, "+56937539304", 11),
                        ft.Text("|", size=11, weight=ft.FontWeight.BOLD, color="#202325"),
                        _inline_item(ft.Icons.CAMERA_ALT, "jorgelopezsilva", 11),
                        ft.Text("|", size=11, weight=ft.FontWeight.BOLD, color="#202325"),
                        ft.Text("2025 (c)", size=10, weight=ft.FontWeight.BOLD, color="#202325"),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=4,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return footer_mobile, footer_tablet, footer_inline


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
        # --- Helper: iniciar carruseles sólo si ya están montados ---
    def _is_mounted(ctrl) -> bool:
        try:
            return ctrl.page is not None
        except Exception:
            return False

    async def _kick_carruseles():
        # Espera un tick para que el árbol se monte
        await asyncio.sleep(0)

        # Carrusel principal: solo si ya está montado
        if _is_mounted(pantalla_inicial):
            start_carrusel()

        # Carrusel vertical: SIEMPRE lo arrancamos
        # porque dentro de _rotar() ya esperas a que imagen.page no sea None
        start_vertical()

    # --- Formulario ---
    formulario = create_formulario(page)
    menu_servicios_container = ft.Column(spacing=10)  # ðŸ‘ˆ aquÃ­ pondremos el menÃº

    # 1) Crear wrappers
    cont_pantalla = ft.Container(content=pantalla_inicial, border_radius=0, padding=0, key=scroll_keys["cont_pantalla"])
    cont_form     = ft.Container(content=formulario,       border_radius=0, padding=0)
    ANCHO_FORM_PC = 380
    # 2) Crear ResponsiveRow
    col_pantalla = ft.Container(content=cont_pantalla, col={"xs": 12, "md": 10, "lg": 10})
    ANCHO_FORM_MAX = 380
    ANCHO_FORM_MIN = 260

    form_card = ft.Container(
        key=scroll_keys["formulario"],  # âœ… destino de scroll
        content=formulario,
        width=ANCHO_FORM_MAX,   
        padding=5,
        bgcolor="rgba(255,255,255,0.95)",
        border_radius=16,
    )

    imagen_logo_empresa = ft.Image(
    src="https://i.postimg.cc/rFxRRS5D/logo-72x72.png",
    fit=ft.BoxFit.COVER,   # llena el círculo sin dejar bordes
    )
    imagen_logo_empresa2 = ft.Image(
    src="https://i.postimg.cc/sDPWTSk5/lll.jpg",
    fit=ft.BoxFit.FILL,   # llena el círculo sin dejar bordes
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
        src="https://i.postimg.cc/htB3zLB6/Imagen7.png",  # cambia si quieres
        fit=ft.BoxFit.FILL,
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
            width=220,  # âœ… ancho fijo (ajusta a gusto)
            height=52,  # âœ… alto fijo
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
    titulo1 = ft.Text("Evermount Solutions", size=64, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    titulo2 = ft.Text("Pest Defense", size=64, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE_70)

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
        key=scroll_keys["banner_pc"],
        padding=ft.Padding.symmetric(horizontal=14, vertical=10),
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

    banner_row = banner_pc.content  # ðŸ‘ˆ referencia al Row interno del banner

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
        alignment=ft.MainAxisAlignment.START,   # âœ… pega todo arriba
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="auto",
    )

    def asegurar_video_movil():
        zona_multimedia.content = carrusel_vertical
        safe_update(zona_multimedia)

        w = page.width or 0

        # âœ… ancho razonable y altura en 9:16 (vertical)
        target_w = max(210, min(int(w * 0.92), 340))
        target_h = int(target_w * 16 / 9)  # ðŸ‘ˆ portrait (9:16)

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
            # âž• recolocar fila_iconos segÃºn ancho actual (desktop / tablet / mÃ³vil)
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
                page._sabiasque_router(SimpleNamespace(route=r))
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
            page.session.store.set(
                "whatsapp_msg",
                "Hola Evermount Solutions, me gustaría agendar una visita para control de roedores. ¿Tienen disponibilidad?"
            )
            render_servicio_desratizacion(page, contenido)
            scroll_content_top()
            page.update()
            return
        if r == "/servicios/sanitizacion":
            parar_carrusel()
            page.session.store.set(
                "whatsapp_msg",
                "Hola Evermount Solutions, me gustaría agendar una visita para desinfección y sanitización de ambientes. ¿Tienen disponibilidad?"
            )
            render_servicio_sanitizacion(page, contenido)
            scroll_content_top()
            page.update()
            return
        if r == "/servicios/voladores":
            parar_carrusel()
            page.session.store.set(
                "whatsapp_msg",
                "Hola Evermount Solutions, me gustaría agendar una visita para control de insectos voladores. ¿Tienen disponibilidad?"
            )
            render_servicio_voladores(page, contenido)
            scroll_content_top()
            page.update()
            return
        if r == "/servicios/rastreros":
            parar_carrusel()
            page.session.store.set(
                "whatsapp_msg",
                "Hola Evermount Solutions, me gustaría agendar una visita para control de insectos rastreros. ¿Tienen disponibilidad?"
            )
            render_servicio_rastreros(page, contenido)
            scroll_content_top()
            page.update()
            return
        if r == "/servicios/termitas":
            parar_carrusel()
            page.session.store.set(
                "whatsapp_msg",
                "Hola Evermount Solutions, me gustaría agendar una visita para control de termitas. ¿Tienen disponibilidad?"
            )
            render_servicio_termitas(page, contenido)
            scroll_content_top()
            page.update()
            return
        if r == "/servicios/aves":
            parar_carrusel()
            page.session.store.set(
                "whatsapp_msg",
                "Hola Evermount Solutions, me gustaría agendar una visita para control de aves urbanas. ¿Tienen disponibilidad?"
            )
            render_servicio_aves_urbanas(page, contenido)
            scroll_content_top()
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
        # âŒ No quites pantalla_inicial del contenido; si quieres ocultarlo, oculta el contenedor:
        # if pantalla_inicial in contenido.controls: ...
        # âœ… Mejor: no remover nada aquÃ­. Solo detener.
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
            # menÃº abierto â†’ detener pulso (usa la API del componente)
            abrir_menu()
            stop_pulso_empresa()
            animacion_empresa_task[0] = None
        else:
            cerrar_menu()
            # menÃº cerrado â†’ reanudar pulso (usa la API del componente)
            animacion_empresa_task[0] = start_pulso_empresa()
            
        page.update()

    # Crear botones, menu y header
    container_boton_empresa, start_pulso_empresa, stop_pulso_empresa = create_boton_empresa(page, toggle_menu)
    animacion_empresa_task[0] = start_pulso_empresa()   # â† arranque inicial
    
    # Creamos la funcion On_CLic del Boton Sabias que
    def on_sabiasque_click(e=None):
        # 1) detén carrusel si aplica
        try:
            parar_carrusel()
        except Exception:
            pass
        push_route("/sabiasque")

    def mostrar_inicio_con_intro(e=None):
            # cierra menú/overlays por si acaso
            try:
                cerrar_menu()
                overlay_cierra_menu.visible = False
            except Exception:
                pass

            # Delega al router. No limpies contenido ni llames render_inicio aquí.
            push_route("/")
            
            # Scroll automático solo en tablet/PC
            if (page.width or 0) >= 600:
                # Dar un pequeño tiempo para permitir que el contenido se reconstruya
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

    inner = ft.Container(
        content=imagen_logo_empresa ,
        width=50, height=50,               # se actualizan en ajustar_tamanos
        border_radius=9999,                # círculo
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,  # ðŸ‘ˆ recorta a cÃ­rculo
        alignment=ft.alignment.center,
    )

    container_logo_empresa = ft.Container(
        content=inner,
        width=64, height=64,               # se actualizan en ajustar_tamanos
        bgcolor=ft.Colors.BLACK_12,
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
                ft.Icon(icon, size=20, color=ft.Colors.BLACK_54),
                ft.Text(text, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK_87),
            ]),
            padding=ft.Padding.symmetric(vertical=6, horizontal=12),
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
        left=0, top=0, right=0, bottom=0,      # ðŸ‘ˆ llena toda la viewport
        bgcolor="rgba(0,0,0,0.001)",           # casi transparente (asegura eventos)
        visible=False,
        on_click=lambda e: cerrar_menu(),      # cierra al hacer clic/tap fuera
    )
    def abrir_menu():
        dropdown.visible = True
        overlay_cierra_menu.visible = True
        stop_pulso_empresa()
        animacion_empresa_task[0] = None
        stack_raiz.update()  # ðŸ‘ˆ

    def cerrar_menu():
        dropdown.visible = False
        overlay_cierra_menu.visible = False
        # reanudar pulso si corresponde
        if animacion_empresa_task[0] is None:
            animacion_empresa_task[0] = start_pulso_empresa()
        stack_raiz.update()  # ðŸ‘ˆ

    dropdown = ft.Container(
        content=ft.Container(
            content=menu_column,
            bgcolor=ft.Colors.WHITE,
            border_radius=6,
            shadow=ft.BoxShadow(1,4,ft.Colors.BLACK_26, offset=ft.Offset(0,2)),
            width=150,
            height=223,
            on_hover= cerrar_menu_hover
        ),
        visible=False,
        top=35,       # ðŸ‘ˆ posicionalo respecto a la ventana, no con alignment/margin
        right=5,
    )

    # --- Barra superior con Titulo (solo móvil) ---
    texto_titulo = ft.Stack([
        ft.Text("EvermountSolutions - Pest Defense",
                weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK_45, top=1, left=1),
        ft.Text("EvermountSolutions - Pest Defense",
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
        padding=ft.Padding.symmetric(horizontal=8, vertical=6),
    )
   

    # Creamos la fila donde estaran los botones inferiores
    Botones_agregar = ft.Row([boton_sabiasque,boton_facebook,boton_instagram,boton_whatsapp],alignment=ft.MainAxisAlignment.END,vertical_alignment=ft.CrossAxisAlignment.END)
    # --- TEXTO PROMOCIONAL (solo visible en tablet/PC) ---
    promo_text = ft.Text(
        "Atención rápida | Insumos certificados | Respuesta inmediata | Técnicos especializados | Hogar y empresas",
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

    promo_items = [
        ("Atención rápida", ft.Icons.FLASH_ON),
        ("Insumos certificados", ft.Icons.VERIFIED),
        ("Respuesta inmediata", ft.Icons.SUPPORT_AGENT),
        ("Técnicos especializados", ft.Icons.HANDYMAN),
        ("Hogar y empresas", ft.Icons.HOME_WORK),
    ]
    promo_labels_text = " | ".join(label for label, _ in promo_items)
    promo_controls = []
    for idx, (label, icon_name) in enumerate(promo_items):
        promo_controls.append(
            ft.Row(
                [
                    ft.Icon(icon_name, size=18, color=ft.Colors.BLACK),
                    ft.Text(
                        label,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK,
                    ),
                ],
                spacing=6,
                tight=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        if idx < len(promo_items) - 1:
            promo_controls.append(
                ft.Text("|", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
            )
    promo_text = ft.Row(
        promo_controls,
        spacing=10,
        tight=True,
        wrap=False,
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    promo_flotante.content = promo_text

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
        slot_contactos_bajo_header,   # âœ… AQUÃ va fila_iconos_mobile en <600
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
            # Si no es visible (modo mÃ³vil) â†’ espera sin animar
            if not promo_stack.visible:
                await asyncio.sleep(0.5)
                continue

            # ancho área visible
            ancho = zona_redes.width or page.width or 900

            # estimación de ancho del texto
            texto_ancho = len(promo_labels_text) * 10 + len(promo_items) * 36

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
        ], expand=True,    # ðŸ‘ˆ importante Stack ocupa toda la altura
    )
    # después de crear stack_raiz con [contenido_base, overlay_cierra_menu, dropdown]
    intro_modal, show_intro, hide_intro = create_intro_overlay(page)
    stack_raiz.controls.append(intro_modal)   # ðŸ‘ˆ lo montas encima de todo
    def on_connect(e):
        # Render inicial
        push_route(page.route or "/")
        # Intro una vez
        show_intro_once()
        ajustar_tamanos()   # âœ… fuerza layout correcto en el primer render
    page.on_connect = on_connect

    page.add(
        ft.Container(
            content=stack_raiz,
            expand=True,           # ðŸ‘ˆ asegura ocupar todo el viewport
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
            scroll_to_key("quienes_somos", duration=500)
            return
        elif opt == "Servicios":
            scroll_to_key("servicios_menu", duration=500)
            return
        elif opt == "Programas":
            page.update()
            scroll_to_key("programas_inicio", duration=500)
            return
        elif opt == "Historia":
            page.update()
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
                    color=ft.Colors.WHITE,
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
                return max(mn, min(mx, v))

    def get_content_widths(w: int):
        if w < 600:
            return None, None
        if w < 900:
            base = min(int(w * 0.96), 860)
            return base, base
        if w < 1280:
            base = min(int(w * 0.94), 1120)
            return base, min(base, 1040)
        if w < 1600:
            base = min(int(w * 0.92), 1320)
            return base, min(base, 1180)
        base = min(int(w * 0.90), 1480)
        return base, min(base, 1240)
    
    def ajustar_zona_multimedia():
        w = page.width or 0

        program_data = bloque_programas.data or {}
        top_card = program_data.get("top_card")
        bottom_card = program_data.get("bottom_card")
        gap_cards = program_data.get("gap", 14)
        section_base_w, text_section_w = get_content_widths(w)
        section_w = section_base_w or int(w * 0.94)
        if w >= 1100:
            section_w = min(int(w * 0.97), 1760)

        if 700 <= w < 1020:
            left_w = clamp(int(section_w * 0.31), 335, 380)
            top_h = 372
            bottom_h = 245
            side_pad = 0
        elif 1020 <= w < 1400:
            left_w = clamp(int(section_w * 0.26), 350, 390)
            top_h = 340
            bottom_h = 245
            side_pad = 0
        else:
            left_w = clamp(int(section_w * 0.24), 340, 390)
            top_h = 340
            bottom_h = 245
            side_pad = 0

        if top_card:
            top_card.height = top_h
            safe_update(top_card)
        if bottom_card:
            bottom_card.height = bottom_h
            safe_update(bottom_card)

        bloque_programas.width = left_w
        target_h = top_h + bottom_h + gap_cards

        media_count = 1
        if w >= 1120:
            media_count += 1
        if w >= 1500:
            media_count += 1
        if w >= 1820:
            media_count += 1
        if w >= 2140:
            media_count += 1

        controls_count = 1 + media_count
        total_gap = 18 * max(0, controls_count - 1)
        available_media_w = max(
            220,
            int((section_w - left_w - total_gap) / media_count),
        )
        if w < 1020:
            target_w = clamp(available_media_w, 280, 460)
        elif w < 1600:
            proportional_w = int(target_h * 0.72)
            target_w = clamp(max(available_media_w, proportional_w), 300, 500)
        else:
            proportional_w = int(target_h * 0.78)
            target_w = clamp(max(available_media_w, proportional_w), 320, 540)

        resize_video_card(video_card, target_w, target_h)
        resize_video_card(video_card2, target_w, target_h)
        resize_video_card(video_card3, target_w, target_h)
        resize_video_card(video_card4, target_w, target_h)

        try:
            data = carrusel_vertical.data or {}
            tarjeta = data.get("tarjeta")
            imagen = data.get("imagen")

            if tarjeta:
                tarjeta.width = target_w
                tarjeta.height = target_h
                safe_update(tarjeta)

            if imagen:
                imagen.width = target_w
                imagen.height = target_h
                safe_update(imagen)

            carrusel_vertical.width = target_w
            carrusel_vertical.height = target_h
            safe_update(carrusel_vertical)
        except Exception as ex:
            print("resize carrusel_vertical error:", ex)

        def box_auto(ctrl, width_value):
            return ft.Container(
                content=ctrl,
                width=width_value,
                padding=0,
                margin=0,
                alignment=ft.alignment.center,
            )

        def box_fixed(ctrl):
            return ft.Container(
                content=ctrl,
                width=target_w,
                height=target_h,
                padding=0,
                margin=0,
                alignment=ft.alignment.center,
            )

        controls_row = [
            box_auto(bloque_programas, left_w),
            box_fixed(carrusel_vertical),
        ]
        if w >= 1120:
            controls_row.append(box_fixed(video_card))
        if w >= 1500:
            controls_row.append(box_fixed(video_card2))
        if w >= 1820:
            controls_row.append(box_fixed(video_card3))
        if w >= 2140:
            controls_row.append(box_fixed(video_card4))

        content_total_w = left_w + (target_w * media_count) + (18 * max(0, len(controls_row) - 1))

        contenido_programas = ft.Row(
            controls=controls_row,
            spacing=18,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            wrap=False,
        )

        if w >= 1020:
            zona_multimedia.padding = ft.Padding.symmetric(horizontal=side_pad, vertical=14)
            zona_multimedia.content = ft.Container(
                width=section_w,
                alignment=ft.alignment.center,
                content=ft.Row(
                    controls=[ft.Container(width=content_total_w, content=contenido_programas)],
                    scroll=ft.ScrollMode.AUTO,
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            )
        else:
            zona_multimedia.padding = ft.Padding.symmetric(horizontal=side_pad, vertical=14)
            zona_multimedia.content = ft.Container(
                width=section_w,
                alignment=ft.alignment.center,
                content=contenido_programas,
            )

        safe_update(zona_multimedia)

    def ajustar_banner_pc():
        w = page.width or 1200

        def clamp(v, mn, mx):
            return max(mn, min(mx, v))

        # âœ… factor fluido 800 -> 600
        # en 800 => t=1.0  |  en 600 => t=0.0
        t = clamp((w - 600) / (800 - 600), 0.0, 1.0)

        # âœ… factor final (en 600 serÃ¡ 0.68, en 800 serÃ¡ 1.0)
        # ajusta 0.65-0.75 según tu gusto
        f_800_600 = 0.68 + 0.32 * t

        # --- tamaños base (tu estilo original) ---
        t1 = int(w * 0.035)
        t2 = int(w * 0.032)
        td = int(w * 0.015)
        logo = int(w * 0.10)

        # ðŸ”» tu reducciÃ³n actual <1300 (la mantenemos)
        if w < 1300:
            factor = clamp((w - 900) / (1300 - 900), 0.7, 1.0)
            t1 = int(t1 * factor)
            t2 = int(t2 * factor)
            td = int(td * factor)
            logo = int(logo * factor)

        # âœ… NUEVO: si w < 800, aplica reducciÃ³n fluida hasta 600
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
        elif w < 1020:
            t1 = clamp(int(w * 0.024), 18, 28)
            t2 = clamp(int(w * 0.021), 16, 24)
            td = clamp(int(w * 0.0105), 10, 13)
            logo = clamp(int(w * 0.075), 58, 82)
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
        if w < 1020:
            img_w = clamp(int(w * 0.18), 135, 175)
        else:
            img_w = clamp(int(w * (0.24 if w < 1260 else 0.18)), 220 if w < 1260 else 160, 360 if w < 1260 else 340)
        base_h = int(w * 0.22)

        if w < 1600:
            tt = (1600 - w) / (1600 - 1200)
            factor_h = 1.0 + 0.30 * clamp(tt, 0, 1)
        else:
            factor_h = 1.0

        img_h = int(base_h * factor_h)

        # âœ… si w < 800: baja mÃ¡s fluido
        if w < 800:
            img_h = int(img_h * (0.70 + 0.30 * t))  # en 600 -> 0.70

        if w < 1020:
            img_h = clamp(int(img_h * 0.78), 180, 250)
        else:
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
        elif w < 1020:
            form_w = clamp(int(w * 0.31), 225, 260)
            form_card.padding = 8
        elif w < 1260:
            form_w = clamp(int(w * 0.28), 280, 360)
            form_card.padding = 10
        else:
            form_w = clamp(int(w * 0.22), ANCHO_FORM_MIN, ANCHO_FORM_MAX)
            form_card.padding = 12

        form_card.width = form_w

        safe_update(banner_pc)



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

            sep.padding = ft.Padding.symmetric(vertical=pad_v)
            sep.width = float("inf")


            # âœ… update directo (ya estÃ¡n montados cuando se ven)
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
        section_w, text_section_w = get_content_widths(a)
        wrap_titulo.visible = False   # âœ… en tablet/pc no lo uses

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

        elif a < 1300:       # âœ… TODO lo que sea menor a 1300 (incluye tablet y desktop compact)
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
                padding=ft.Padding.all(0),
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
        compact_desktop = 600 <= a < 700

        inicio_bg.width = float("inf")
        banner_pc.width = float("inf")
        zona_multimedia.width = float("inf")
        menu_servicios_container.width = float("inf")
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

           # âœ… En >=600: contactos SOLO en el header (derecha)
            slot_iconos_header.content = fila_iconos_header
            slot_iconos_header.visible = True

            # âœ… Ocultar el slot bajo header y soltar el contenido
            slot_contactos_bajo_header.visible = False

            # âœ… El mobile row NO debe verse
            fila_iconos_mobile.visible = False

            safe_remove(fila_iconos_mobile, contenido.controls)

            aplicar_color_separadores(True)
            # âœ… Header compacto <1300: evita que crezca en alto
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

            # Tabs: visibles en tablet + desktop, ocultos solo en móvil
            es_mobile = a < 600
            slot_tabs_header.visible = not es_mobile

            if not es_mobile:
                # factor compacto <1300
                factor = 1.0
                if a < 1300:
                    factor = clamp((a - 900) / (1300 - 900), 0.75, 1.0)

                # âœ… Ajuste extra < 780
                if a < 780:
                    factor2 = clamp((a - 600) / (780 - 600), 0.0, 1.0)   # 600->0, 780->1
                    tab_font = int(11 + 3 * factor2)     # 11..14
                    tab_pad_x = int(6 + 4 * factor2)     # 6..10
                    tab_pad_y = int(4 + 2 * factor2)     # 4..6
                else:
                    tab_font = int(16 * factor)
                    tab_pad_x = int(12 * factor)
                    tab_pad_y = int(6 * factor)


                # ðŸ”¥ SIEMPRE recrear tabs para que el tamaÃ±o suba y baje
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
            form_card.shadow = ft.BoxShadow(2, 8, ft.Colors.BLACK_12, offset=ft.Offset(0, 4))
            inicio_bg.content = banner_pc

            contenido.spacing = 0
 
            separador_servicios.margin = ft.Margin.only(top=0)

            # --- Ajustar tamaÃ±os + layout en QUIÃ‰NES SOMOS ---
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

                    # âœ… NUEVO: si existe apply_layout, lo ejecutamos SIEMPRE
                    fn = quienes_section.data.get("apply_layout")
                    if fn:
                        fn()
            except Exception as ex:
                print("quienes apply_layout error:", ex)
            # âœ… asegurar layout de valores

            # âš ï¸ Importante: asegurarnos que video_card NO estÃ© suelto en contenido
            safe_remove(video_card, contenido.controls)

            # ðŸ‘‰ PC/TABLET: si "QuiÃ©nes" ya incluye contenido de Historia, no renderices Historia abajo
            safe_remove(separador_sanitizacion, contenido.controls)

            # modo tablet / PC â†’ sin saltos de lÃ­nea la firma
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
            # ðŸ‘‡ NUEVO: asegurar que el carrusel vertical estÃ¡ activo
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
            # âœ… WRAP del banner SOLO cuando < 700
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
                # (altura se ajusta en ajustar_banner_pc, pero aquí puedes bajar un poco)
                if banner_img_box.height and a < 900:
                    banner_img_box.height = int(banner_img_box.height * 0.92)

                # 2) formulario
                if a < 900:
                    form_card.width = clamp(int(a * 0.92), 220, 360)
                else:
                    form_card.width = clamp(int(a * 0.34), 280, 360)
                form_card_host.width = form_card.width  # ðŸ‘ˆ importante para que el host no â€œempujeâ€
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
                        bloque_izq.width = None
                except Exception:
                    pass
                form_card_host.width = form_card.width if es_tablet else None
                
            if 600 <= a < 700:
                banner_pc.padding = ft.Padding.symmetric(horizontal=12, vertical=12)
            else:
                banner_pc.padding = ft.Padding.symmetric(horizontal=30, vertical=18)

            ajustar_zona_multimedia()
            ajustar_banner_pc()    
            
        else:
            # âœ… MODO MÃ“VIL (<600): limpieza total de videos y colocar SOLO 1 debajo de sanitizaciÃ³n
            asegurar_video_movil()

            # âœ… Contactos debajo del header
            slot_contactos_bajo_header.content = fila_iconos_mobile
            slot_contactos_bajo_header.visible = True
            fila_iconos_mobile.visible = True
            slot_iconos_header.visible = False
            slot_contactos_bajo_header.width = float("inf")                 # âœ… ocupa todo el ancho
            slot_contactos_bajo_header.alignment = ft.alignment.center      # âœ… centra su contenido
            try:
                apply_fn = (fila_iconos_mobile.data or {}).get("apply_style_adaptativo")
                if apply_fn:
                    apply_fn()  # âœ… recalcula alignment/spacing segÃºn el modo actual
            except:
                pass
            safe_update(slot_contactos_bajo_header)
            # âœ… en mÃ³vil: zona_multimedia SOLO carrusel vertical
            # âœ… en mÃ³vil: mostrar Programas (texto) + carrusel vertical
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

        
            # ========= MODO MÃ“VIL (<600): RESET TOTAL =========
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

            # banner/inicio: en móvil usamos una columna explícita para asegurar
            # que el carrusel principal quede arriba del formulario.
            inicio_bg.content = inicio_mobile

            # promo solo tablet/pc
            promo_stack.visible = False
            separador_final.content = separador_final.data["footer_mobile"]

            # aplica estilo móvil a contactos (sin update si no está montado)
            apply_fn = (fila_iconos_header.data or {}).get("apply_style_adaptativo")
            if apply_fn:
                try:
                    apply_fn()
                except:
                    pass

            barra_inferior.alignment = ft.MainAxisAlignment.END
            # ðŸ‘‡ Asegurarnos de que separador_sanitizacion EXISTE en contenido
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

        # âœ… Recalcular tarjetas servicios al cambiar tamaÃ±o
        try:
            rebuild = (menu_servicios_container.data or {}).get("rebuild")
            if rebuild:
                rebuild()
        except Exception:
            pass

        # âœ… asegurar layout de quienes en mÃ³vil
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


    # âœ… NO pises on_resized de otros componentes (ej: formulario.py)
    _prev_on_resized = page.on_resized
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
        try:
            if _prev_on_resized:
                _prev_on_resized(e)
        except Exception:
            pass
        _schedule_resize_adjustment()

    page.on_resized = _main_chain_resized
    page.on_media_change = lambda e: _schedule_resize_adjustment()
    page.on_window_event = lambda e: _schedule_resize_adjustment() if e.data == "shown" else None
    page.run_task(_watch_width_changes)

        # Iniciar animaciones   
    animacion_empresa_task[0] = start_pulso_empresa()
    animacion_redes_task[0] = start_bounce()
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.update()
    ajustar_tamanos()



