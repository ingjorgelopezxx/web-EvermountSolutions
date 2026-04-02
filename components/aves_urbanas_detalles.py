from components.service_detail_template import render_service_detail


def render_servicio_aves_urbanas(
    page,
    contenedor,
    *,
    aves_img_url: str = "https://i.postimg.cc/MGBy5SXS/avesurbanas.png",
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        cache_key="servicio_aves",
        title="Control de Aves Urbanas",
        lead_text=(
            "Las aves pueden convertirse en una plaga cuando anidan en techos, cornisas, galpones "
            "o equipos de ventilacion, generando suciedad, malos olores y riesgos sanitarios. "
            "Aplicamos metodos seguros para alejar sin danar."
        ),
        benefits=[
            "Instalacion de sistemas anti-posamiento como pinchos, redes o tensores.",
            "Prevencion de anidacion y acumulacion de excrementos.",
            "Inspeccion tecnica y asesoria personalizada.",
            "Soluciones eticas y respetuosas con la fauna.",
        ],
        image_url=aves_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Metodos eticos de exclusion",
            "Reduccion de focos sanitarios",
        ],
        metricas=[
            ("SAFE", "Control no letal"),
            ("TECH", "Inspeccion tecnica"),
            ("CLEAN", "Prevencion sanitaria"),
        ],
        proceso=[
            ("1", "Levantamiento de zonas criticas"),
            ("2", "Instalacion de exclusion y proteccion"),
            ("3", "Seguimiento y recomendaciones"),
        ],
        usos=[
            "Techos",
            "Industrias",
            "Iglesias",
            "Edificios",
        ],
        highlight_text="Alejamos aves invasoras con soluciones tecnicas, seguras y respetuosas.",
        title_sizes=(22, 30, 44),
    )
