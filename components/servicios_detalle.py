from components.service_detail_template import render_service_detail


def render_servicio_desratizacion(
    page,
    contenedor,
    *,
    rat_img_url: str = "https://i.postimg.cc/Xqgd1VwZ/raton-campo-mus-musculus-768x576-Photoroom.png",
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        title="Desratizacion Profesional",
        lead_text=(
            "Los roedores son una de las plagas mas peligrosas por los danos estructurales que causan "
            "y las enfermedades que transmiten. Nuestro servicio de desratizacion incluye diagnostico, "
            "control activo y sellado de accesos."
        ),
        benefits=[
            "Inspeccion detallada para detectar nidos y rutas.",
            "Estrategias inteligentes: cebos, trampas y estaciones seguras.",
            "Recomendaciones de cierre y sellado estructural.",
            "Mantenemos tu propiedad libre de roedores con minima interrupcion.",
        ],
        image_url=rat_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Control activo en puntos criticos",
            "Proteccion para hogares y empresas",
        ],
        metricas=[
            ("24/7", "Respuesta oportuna"),
            ("360", "Revision de accesos"),
            ("SAFE", "Control seguro"),
        ],
        proceso=[
            ("1", "Inspeccion de focos, rutas y evidencia"),
            ("2", "Instalacion de control y estaciones"),
            ("3", "Seguimiento y recomendaciones preventivas"),
        ],
        usos=[
            "Hogares",
            "Bodegas",
            "Locales",
            "Empresas",
        ],
        highlight_text="Protegemos tus espacios con control tecnico y seguimiento preventivo.",
        title_sizes=(26, 32, 48),
    )
