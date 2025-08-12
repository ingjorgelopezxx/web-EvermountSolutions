import json
import flet as ft
import asyncio
import os
from views.servicios import slides_servicios as servicios_slides
from views.programas import slide_programas_control as programas_slides 
from views.quienes import slides_quienes as quienes_slides 
from views.historia import slides_historia as historia_slides 
from components.botones import create_boton_empresa, create_botones_redes
from components.insectos import ICONOS_INSECTOS, create_insectos_support, construir_contenido_slide_insectos
from components.intro import create_intro_overlay
from components.carrusel import create_carrusel, DEFAULT_IMAGE_SETS
from components.slides import create_slides_controller

def main(page: ft.Page):
    # Inicializamos las propiedades de la pagina
    page.title = "EvermountSolutions"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    
    # Usamos lista para mutabilidad, inicializamos la variable 
    animacion_empresa_task = [None]     # ahora guardará el task del pulso del botón empresa
    animacion_redes_task = [None]       # task del bounce de redes    

    # intro, insectos y carrusel (devuelven helpers que usaremos luego)
    intro_modal, show_intro, hide_intro = create_intro_overlay(page)
    show_intro()
    modal_insecto, mostrar_info_insecto, start_anim_insectos, stop_anim_insectos = create_insectos_support(page)
    fila_carrusel, set_sets_imagenes, start_carrusel, stop_carrusel, set_first_set = create_carrusel(
    page, tam=3, sets=DEFAULT_IMAGE_SETS
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
    
    #Funcion para detener el carrusel de imagenes 
    def parar_carrusel():
            stop_carrusel()
            if fila_carrusel in contenido.controls:
                contenido.controls.remove(fila_carrusel)
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

    # Contactos Redes Sociales
    numero_whatsapp = "+56937539304"
    contacto_whatsapp = f"https://wa.me/{numero_whatsapp}?text=Hola"
    contacto_instagram = "https://instagram.com/evermountsolutions"
    contacto_facebook = "https://facebook.com/evermountsolutions"

     # --- Botón EMPRESA (header) ---
    def toggle_menu(e):
        dropdown.visible = not dropdown.visible
        if dropdown.visible:
            # menú abierto → detener pulso (usa la API del componente)
            stop_pulso_empresa()
            animacion_empresa_task[0] = None
        else:
            # menú cerrado → reanudar pulso (usa la API del componente)
            animacion_empresa_task[0] = start_pulso_empresa()
        page.update()

    # Crear botones, menu y header
    container_boton_empresa, start_pulso_empresa, stop_pulso_empresa = create_boton_empresa(page, toggle_menu)
    animacion_empresa_task[0] = start_pulso_empresa()   # ← arranque inicial
    # --- Botones REDES ---
    boton_facebook, boton_instagram, boton_whatsapp, start_bounce, stop_bounce = create_botones_redes(
        page, contacto_whatsapp, contacto_instagram, contacto_facebook
    )

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
            if animacion_empresa_task[0] is None:
                animacion_empresa_task[0] = start_pulso_empresa()
            page.update()
            
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

    # Creamos la fila donde estaran los botones inferiores
    Botones_agregar = ft.Row([boton_facebook,boton_instagram,boton_whatsapp],alignment=ft.MainAxisAlignment.END,vertical_alignment=ft.CrossAxisAlignment.END)

    # Agregamos un contenedor para incluir los botones y le asigamos un fondo
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

    ####### FUNCIONES #######
    # --- Modifica show_info (Funcion para saber que opcion del menu se selecciono) ---
    def show_info(opt):
        global slide_actual,slides
        dropdown.visible = False
        if animacion_empresa_task[0] is None:
            animacion_empresa_task[0] = start_pulso_empresa()
        page.update()
        contenido.controls.clear()
        if opt == "Inicio":
            if fila_carrusel not in contenido.controls:
                contenido.controls.append(fila_carrusel)
            contenido.update()
            page.update()
            async def kick():
                await asyncio.sleep(0)
                set_first_set()
                start_carrusel()
            page.run_task(kick)
            
        elif opt == "Quiénes Somos":
            set_slides(quienes_slides)
            mostrar_slide(0)
        elif opt == "Servicios":
            set_slides(servicios_slides)
            mostrar_slide(0)
        elif opt == "Programas":
            set_slides(programas_slides)
            mostrar_slide(0)
        elif opt == "Historia":
            set_slides(historia_slides)
            mostrar_slide(0)
        elif opt == "Ubicación":
            parar_carrusel()
            contenido.controls.append(
                ft.Text("dirección de empresa", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
            )
            contenido.update()

    # 🔧 Inicializa el carrusel en el primer render
    def _init_carousel_after_mount():
        async def _kick():
            # un tick para asegurar que los controles ya están montados
            await asyncio.sleep(0)
            set_first_set()
            start_carrusel()
        page.run_task(_kick)
    _init_carousel_after_mount()

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
        show_intro()
        # Cerrar menú si está abierto
        dropdown.visible = False
        # Cerrar modal de insecto si estaba abierto
        modal_insecto.open = False
        page.dialog = None  # <--- Opcional, asegura que no queda el modal "huérfano"
        # Mostrar contenido inicial (texto y carrusel)
        contenido.controls.clear()
        contenido.controls.extend([
            ft.Text("Bienvenido a EvermountSolutions", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            ft.Text("Control de plagas profesional. Haz clic en los botones.", color=ft.Colors.BLACK),
            fila_carrusel,  # <- Agrega fila_carrusel primero
        ])
        contenido.update()  # <-- MUY IMPORTANTE: actualiza el contenido aquí
        page.update()          # <- asegura que los controles ya “viven” en la page
        set_first_set()        # <- ahora sí es seguro
        start_carrusel()
    page.on_connect = on_connect

    page.on_resize = ajustar_tamanos
    page.on_window_event = lambda e: ajustar_tamanos() if e.data=="shown" else None
        # Iniciar animaciones
    animacion_empresa_task[0] = start_pulso_empresa()
    animacion_redes_task[0] = start_bounce()
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.overlay.extend([dropdown, intro_modal,modal_insecto])
    page.update()
    ajustar_tamanos()
   
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))