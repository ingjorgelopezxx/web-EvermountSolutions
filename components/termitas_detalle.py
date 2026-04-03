from components.service_detail_template import render_service_detail
from functions.asset_sources import SERVICE_DETAIL_IMAGES


def render_servicio_termitas(
    page,
    contenedor,
    *,
    termitas_img_url: str = SERVICE_DETAIL_IMAGES["termitas"],
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        cache_key="servicio_termitas",
        title="Tratamiento de Termitas",
        lead_text=(
            "Las termitas pueden causar daños estructurales graves en viviendas, empresas y "
            "construcciones de madera si no se detectan a tiempo. Aplicamos tratamientos "
            "especializados para eliminar actividad y proteger la estructura a largo plazo."
        ),
        benefits=[
            "Diagnóstico técnico con detección de actividad y daños.",
            "Tratamientos localizados e integrales perimetrales y estructurales.",
            "Uso de termiticidas de última generación aprobados por ISP.",
            "Programas de monitoreo y protección post-tratamiento.",
        ],
        image_url=termitas_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Protección estructural",
            "Monitoreo y seguimiento",
        ],
        metricas=[
            ("ISP", "Productos aprobados"),
            ("PRO", "Revisión técnica"),
            ("LONG", "Protección prolongada"),
        ],
        proceso=[
            ("1", "Inspección de actividad y alcance"),
            ("2", "Tratamiento según estructura"),
            ("3", "Monitoreo y recomendaciones"),
        ],
        usos=[
            "Casas",
            "Cabañas",
            "Bodegas",
            "Colegios",
        ],
        highlight_text="Protegemos estructuras vulnerables con tratamientos técnicos y monitoreo continuo.",
        title_sizes=(22, 28, 44),
    )
