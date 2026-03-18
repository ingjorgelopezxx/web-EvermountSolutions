from components.service_detail_template import render_service_detail


def render_servicio_termitas(
    page,
    contenedor,
    *,
    termitas_img_url: str = "https://i.postimg.cc/CK2jHKwJ/termitas-detalle.png",
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        title="Tratamiento de Termitas",
        lead_text=(
            "Las termitas pueden causar danos estructurales graves en viviendas, empresas y "
            "construcciones de madera si no se detectan a tiempo. Aplicamos tratamientos "
            "especializados para eliminar actividad y proteger la estructura a largo plazo."
        ),
        benefits=[
            "Diagnostico tecnico con deteccion de actividad y danos.",
            "Tratamientos localizados e integrales perimetrales y estructurales.",
            "Uso de termiticidas de ultima generacion aprobados por ISP.",
            "Programas de monitoreo y proteccion post-tratamiento.",
        ],
        image_url=termitas_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Proteccion estructural",
            "Monitoreo y seguimiento",
        ],
        metricas=[
            ("ISP", "Productos aprobados"),
            ("PRO", "Revision tecnica"),
            ("LONG", "Proteccion prolongada"),
        ],
        proceso=[
            ("1", "Inspeccion de actividad y alcance"),
            ("2", "Tratamiento segun estructura"),
            ("3", "Monitoreo y recomendaciones"),
        ],
        usos=[
            "Casas",
            "Cabanas",
            "Bodegas",
            "Colegios",
        ],
        highlight_text="Protegemos estructuras vulnerables con tratamientos tecnicos y monitoreo continuo.",
        title_sizes=(22, 28, 44),
    )
