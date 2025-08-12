# components/insectos.py
import flet as ft
import asyncio

# —— Datos (antes en main) ——
INFO_INSECTOS = {
    "cucarachas": {"titulo": "Cucarachas", "descripcion": "Las cucarachas son una de las plagas más comunes. Se reproducen rápidamente y pueden transmitir enfermedades. Eliminamos todo tipo de cucarachas utilizando cebos, geles y productos seguros para personas y mascotas."},
    "hormigas": {"titulo": "Hormigas", "descripcion": "Las hormigas invaden hogares y comercios en busca de alimento. Realizamos diagnóstico y aplicación de productos focalizados para erradicarlas desde el nido."},
    "chinches": {"titulo": "Chinches de cama", "descripcion": "Las chinches se esconden en camas y muebles, causando picaduras y molestias. Utilizamos técnicas avanzadas de detección y tratamientos térmicos y químicos."},
    "pulgas": {"titulo": "Pulgas", "descripcion": "Las pulgas afectan a mascotas y personas, transmitiendo enfermedades y causando picazón. Aplicamos tratamientos en interiores y exteriores para su total erradicación."},
    "moscas": {"titulo": "Moscas", "descripcion": "Las moscas son portadoras de bacterias y virus. Utilizamos trampas, cebos y nebulización para su control en ambientes residenciales y comerciales."},
    "zancudos": {"titulo": "Zancudos (mosquitos)", "descripcion": "Los zancudos pueden transmitir enfermedades como dengue y zika. Realizamos tratamientos preventivos y de choque en zonas de riesgo, patios y jardines."},
    "avispas": {"titulo": "Avispas", "descripcion": "Las avispas pueden ser peligrosas por sus picaduras. Localizamos y retiramos nidos de manera segura, usando métodos no invasivos y productos específicos."},
    "raton": {"titulo": "Ratón", "descripcion": "Los ratones suelen invadir viviendas y negocios buscando alimento y refugio. Suelen causar daños en cables, muebles y contaminar alimentos. Utilizamos trampas, cebos y barreras físicas para erradicarlos de forma segura."},
    "rata": {"titulo": "Rata", "descripcion": "Las ratas pueden causar daños severos en la estructura e instalaciones, además de ser portadoras de enfermedades graves. Aplicamos estrategias inteligentes y seguras para su control y eliminamos rutas de ingreso."},
    "termita_subterranea": {"titulo": "Termita subterránea", "descripcion": "Las termitas subterráneas construyen nidos bajo tierra y acceden a las estructuras a través de túneles. Se alimentan de madera y pueden causar daños graves en poco tiempo. Utilizamos tratamientos de barrera y cebos específicos para su erradicación."},
    "termita_madera_seca": {"titulo": "Termita de madera seca", "descripcion": "Las termitas de madera seca infestan principalmente maderas secas y muebles. Son difíciles de detectar, pero con métodos de inyección y productos de última generación logramos su control eficaz sin afectar el entorno."},
    "termita_otros": {"titulo": "Otras especies de termitas", "descripcion": "Existen diversas especies de termitas que pueden atacar diferentes tipos de madera y estructuras. Realizamos diagnóstico y tratamiento personalizado para cada caso, asegurando la máxima protección de tu propiedad."},
    "palomas": {"titulo": "Palomas", "descripcion": "Las palomas pueden anidar en techos y cornisas, ensuciando con excremento y transmitiendo enfermedades. Instalamos sistemas anti-posamiento y realizamos limpieza y prevención para evitar su retorno."},
    "tortolas": {"titulo": "Tórtolas", "descripcion": "Las tórtolas se adaptan bien a ambientes urbanos, causando molestias y suciedad. Usamos barreras físicas y métodos amigables para disuadir su anidación en lugares críticos."},
    "gorriones": {"titulo": "Gorriones", "descripcion": "Los gorriones forman colonias numerosas y pueden causar daños en almacenes y centros de distribución. Nuestra solución es ética, evitando daños y facilitando el desplazamiento de las aves."},
    "aves_otros": {"titulo": "Otras especies de aves", "descripcion": "Controlamos también otras especies invasoras que puedan causar daños o problemas sanitarios, adaptando el sistema de control a cada situación para proteger la estructura y la salud de las personas."},
}

ICONOS_INSECTOS = {
    "cucarachas": "https://cdn-icons-png.flaticon.com/512/8005/8005026.png",
    "hormigas":   "https://static.vecteezy.com/system/resources/previews/015/211/725/non_2x/ant-icon-cartoon-style-vector.jpg",
    "chinches":   "https://cdn-icons-png.flaticon.com/512/1850/1850155.png",
    "pulgas":     "https://cdn-icons-png.flaticon.com/512/2295/2295144.png",
    "moscas":     "https://cdn-icons-png.flaticon.com/512/1357/1357476.png",
    "zancudos":   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR29MlAGMA1uNdMVEQtGxDEuh_gLjc_vf1H4w&s",
    "avispas":    "https://static.vecteezy.com/system/resources/previews/014/285/415/non_2x/agression-wasp-icon-outline-style-vector.jpg",
    "raton":      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_KKIyhsZpTWOzWNYwJLRLKheBjk4EAPefqw&s",
    "rata":       "https://static.vecteezy.com/system/resources/previews/014/986/360/non_2x/rat-icon-cartoon-style-vector.jpg",
    "termita_subterranea": "https://cdn-icons-png.freepik.com/512/4982/4982504.png",
    "termita_madera_seca": "https://thumbs.dreamstime.com/b/icono-vectorial-de-color-plano-%C3%BAnico-la-madera-los-insectos-termite-157353067.jpg",
    "termita_otros": "https://i.postimg.cc/85r8Fs7m/trt.png",
    "palomas": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM-8j_vQCe1wXK-otbgAAlnYQIynlY9rampQ&s",
    "tortolas": "https://png.pngtree.com/png-vector/20230315/ourmid/pngtree-vector-turtledove-png-image_6650452.png",
    "gorriones": "https://st3.depositphotos.com/4233957/34474/v/450/depositphotos_344748232-stock-illustration-sparrow-small-city-bird-illustration.jpg",
    "aves_otros": "https://i.postimg.cc/KYBwFww0/aves-urbanas.png",
}

def construir_contenido_slide_insectos(slide: dict, mostrar_info_insecto, size_parrafo: int = 16):
    """
    Devuelve (controls, imagenes_animadas)
      - controls: lista de controles Flet para el contenido del slide
      - imagenes_animadas: lista de ft.Image que se animarán (las de los íconos)
    Maneja:
      - strings => Text
      - dict {"tipo":"clickable_row","items":[{"nombre","id"},...]} => fila de íconos clicables
    """
    controls = []
    imagenes_animadas = []

    for parrafo in slide.get("contenido", []):
        # Caso 1: fila especial de íconos clicables
        if isinstance(parrafo, dict) and parrafo.get("tipo") == "clickable_row":
            row_controles = []
            for item in parrafo.get("items", []):
                icon_src = ICONOS_INSECTOS.get(item["id"], "")
                img_insecto = ft.Image(
                    src=icon_src,
                    width=34, height=34,
                    fit=ft.ImageFit.CONTAIN,
                    scale=1.0,
                    animate_scale=200,
                    tooltip=item["nombre"],
                )
                imagenes_animadas.append(img_insecto)

                # ¡OJO con la lambda! capturamos el id como default arg
                cont = ft.Container(
                    content=img_insecto,
                    width=46, height=46,
                    border_radius=33,
                    bgcolor=ft.Colors.WHITE,
                    shadow=ft.BoxShadow(1, 6, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
                    alignment=ft.alignment.center,
                    on_click=(lambda e, _id=item["id"]: mostrar_info_insecto(_id)),
                    ink=True,
                )

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

            controls.append(
                ft.Row(row_controles, alignment=ft.MainAxisAlignment.CENTER, spacing=7)
            )

        # Caso 2: texto plano (string)
        else:
            if isinstance(parrafo, str):
                controls.append(
                    ft.Text(
                        parrafo,
                        size=size_parrafo,
                        color=ft.Colors.BLACK,
                        text_align=ft.TextAlign.LEFT,
                    )
                )
            else:
                # Si llega otra estructura no prevista, la ignoramos o la mostramos cruda
                controls.append(ft.Text(str(parrafo), size=size_parrafo))

    return controls, imagenes_animadas

def create_insectos_support(page: ft.Page):
    """
    Crea el modal y helpers para mostrar info de insectos y animar sus íconos.
    Retorna: (modal_insecto, mostrar_info_insecto, start_anim, stop_anim)
    """
    modal_insecto = ft.AlertDialog(
        modal=True,
        title=ft.Text(""),
        content=ft.Text(""),
        actions=[],
    )

    def _cerrar_modal(e=None):
        modal_insecto.open = False
        page.update()

    modal_insecto.actions.append(ft.TextButton("Cerrar", on_click=_cerrar_modal))

    def mostrar_info_insecto(insecto_id: str):
        data = INFO_INSECTOS.get(insecto_id)
        if data:
            modal_insecto.title.value = data["titulo"]
            modal_insecto.content.value = data["descripcion"]
            modal_insecto.open = True
            page.dialog = modal_insecto
            page.update()

    task_ref = [None]

    async def _animar_insectos(imgs):
        try:
            while True:
                for img in imgs:
                    img.scale = 1.17
                    img.update()
                await asyncio.sleep(0.4)
                for img in imgs:
                    img.scale = 1.0
                    img.update()
                await asyncio.sleep(0.4)
        except Exception:
            pass

    def start_anim(imgs):
        stop_anim()
        task_ref[0] = page.run_task(_animar_insectos, imgs)
        return task_ref[0]

    def stop_anim():
        if task_ref[0]:
            task_ref[0].cancel()
            task_ref[0] = None

    return modal_insecto, mostrar_info_insecto, start_anim, stop_anim
