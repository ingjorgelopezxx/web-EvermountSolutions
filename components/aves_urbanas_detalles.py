from components.service_detail_template import render_service_detail
from functions.asset_sources import SERVICE_DETAIL_IMAGES


def render_servicio_aves_urbanas(
    page,
    contenedor,
    *,
    aves_img_url: str = SERVICE_DETAIL_IMAGES["aves"],
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
            "Instalación de sistemas anti-posamiento como pinchos, redes o tensores.",
            "Prevención de anidación y acumulación de excrementos.",
            "Inspección técnica y asesoría personalizada.",
            "Soluciones éticas y respetuosas con la fauna.",
        ],
        image_url=aves_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Métodos éticos de exclusión",
            "Reducción de focos sanitarios",
        ],
        metricas=[
            ("SAFE", "Control no letal"),
            ("TECH", "Inspección técnica"),
            ("CLEAN", "Prevención sanitaria"),
        ],
        proceso=[
            ("1", "Levantamiento de zonas criticas"),
            ("2", "Instalación de exclusión y protección"),
            ("3", "Seguimiento y recomendaciones"),
        ],
        usos=[
            "Techos",
            "Industrias",
            "Iglesias",
            "Edificios",
        ],
        highlight_text="Alejamos aves invasoras con soluciones técnicas, seguras y respetuosas.",
        title_sizes=(22, 30, 44),
    )
