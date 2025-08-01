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
    slide_actual = 0  # Variable para llevar el control del slide
    animacion_empresa_task = [None]  # Usamos lista para mutabilidad
    
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
                    "Si deseas obtener mas información referente a la empresa "
                    "has clic sobre el boton ubicado en la esquina superior derecha.",
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

    async def animar_empresa_ciclo():
        while True:
            container_boton_empresa.scale = 1.18
            container_boton_empresa.update()
            await asyncio.sleep(0.7)
            container_boton_empresa.scale = 1.0
            container_boton_empresa.update()
            await asyncio.sleep(0.7)



    # Funcion animacion Botones
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
        scale=1.0,             # <--- Necesario para animar
        animate_scale=200,     # <--- Necesario para animar
    )


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

        # Función para reemplazar el contenido
        # --- Contenidos para el carrusel/presentación ---
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
        # Puedes agregar más slides aquí si lo deseas
    ]

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

    
    slides = slides_quienes  # por defecto, o como prefieras
    def mostrar_slide(idx):
        global carrusel_activo
        global slides
        carrusel_activo = False
        contenido.controls.clear()
        # Ancho responsive para el card
        ancho_card = min(int(page.width * 0.8), 380)
        if page.width < 350:
            ancho_card = int(page.width * 0.98)

        size_titulo = 18 if page.width < 400 else 24
        size_parrafo = 14 if page.width < 400 else 16

            # Usamos una lista para mutabilidad del valor inicial
        # Guarda el acumulado de movimiento horizontal
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



        card = ft.Container(
            width=ancho_card,
            padding=ft.padding.symmetric(vertical=18, horizontal=8 if page.width < 400 else 18),
            bgcolor=ft.Colors.WHITE,
            border_radius=16,
            border=ft.border.all(2, ft.Colors.BLACK),
            content=ft.Column([
                # Título destacado con fondo degradado
                ft.Container(
                    content=ft.Text(
                        slides[idx]["titulo"],
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
                    margin=ft.margin.only(bottom=8)
                ),
                # Párrafos ordenados sin sangría, separados y limpios
                *[
                    ft.Text(
                        parrafo,
                        size=size_parrafo,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.LEFT,
                    )
                    for parrafo in slides[idx]["contenido"]
                ]
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=16),
            alignment=ft.alignment.center
        )
        # -- Aquí envolvemos el card con el detector de gestos
        gesture_card = ft.GestureDetector(
            content=card,
            on_pan_start=on_pan_start,
            on_pan_update=on_pan_update,
            on_pan_end=on_pan_end
        )


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


    def navegar_slide(nuevo_idx):
        global slide_actual
        slide_actual = nuevo_idx
        mostrar_slide(slide_actual)

    # --- Modifica show_info ---
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
            mostrar_slide(0)
        
        elif opt == "Historia":
            carrusel_activo = False
            animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
            slides = slides_historia
            slide_actual = 0
            mostrar_slide(0)
            
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


    # Menú de empresa
    # Menú de empresa
    menu_data = [
        ("Inicio",     ft.Icons.HOME),   
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
            height=230,
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
    # Overlay oculto para cerrar el menu al hacer clic fuera de el
    page.overlay.extend([dropdown, intro_modal])
    page.update()
    asyncio.create_task(rotar_sets())
    asyncio.create_task(animacion_alternada())
    animacion_empresa_task[0] = page.run_task(animar_empresa_ciclo)
    ajustar_tamanos()
   
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))
