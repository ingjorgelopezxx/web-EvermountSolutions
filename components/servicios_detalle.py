from components.service_detail_template import render_service_detail
from functions.asset_sources import SERVICE_DETAIL_IMAGES


def render_servicio_desratizacion(
    page,
    contenedor,
    *,
    rat_img_url: str = SERVICE_DETAIL_IMAGES["roedores"],
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        cache_key="servicio_roedores",
        title="Desratización Profesional",
        lead_text=(
            "Los roedores son una de las plagas más peligrosas por los daños estructurales que causan "
            "y las enfermedades que transmiten. Nuestro servicio de desratización incluye diagnóstico, "
            "control activo y sellado de accesos."
        ),
        benefits=[
            "Inspección detallada para detectar nidos y rutas.",
            "Estrategias inteligentes: cebos, trampas y estaciones seguras.",
            "Recomendaciones de cierre y sellado estructural.",
            "Mantenemos tu propiedad libre de roedores con mínima interrupción.",
        ],
        image_url=rat_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Control activo en puntos críticos",
            "Protección para hogares y empresas",
        ],
        metricas=[
            ("24/7", "Respuesta oportuna"),
            ("360", "Revisión de accesos"),
            ("SAFE", "Control seguro"),
        ],
        proceso=[
            ("1", "Inspección de focos, rutas y evidencia"),
            ("2", "Instalación de control y estaciones"),
            ("3", "Seguimiento y recomendaciones preventivas"),
        ],
        usos=[
            "Hogares",
            "Bodegas",
            "Locales",
            "Empresas",
        ],
        highlight_text="Protegemos tus espacios con control técnico y seguimiento preventivo.",
        title_sizes=(26, 32, 48),
    )
