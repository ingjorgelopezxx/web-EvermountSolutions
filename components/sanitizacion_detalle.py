from components.service_detail_template import render_service_detail


def render_servicio_sanitizacion(
    page,
    contenedor,
    *,
    sanitizacion_img_url: str = "https://i.postimg.cc/zGfdKtvL/desinfeccion-Photoroom-Photoroom.png",
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        cache_key="servicio_sanitizacion",
        title="Desinfeccion y Sanitizacion de Ambientes",
        lead_text=(
            "Protege la salud de tu familia, empleados y clientes con nuestros servicios de sanitizacion "
            "profesional. Eliminamos virus, bacterias, hongos y malos olores de forma segura, rapida y eficaz."
        ),
        benefits=[
            "Aplicacion con nebulizador ULV o termonebulizacion.",
            "Uso de productos certificados por ISP y amigables con el medio ambiente.",
            "Ideal para hogares, oficinas, clinicas, escuelas y empresas.",
            "Previene contagios y garantiza ambientes mas saludables.",
        ],
        image_url=sanitizacion_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Cobertura residencial y comercial",
            "Protocolos seguros y certificados",
        ],
        metricas=[
            ("ULV", "Aplicacion tecnica"),
            ("ISP", "Productos certificados"),
            ("24/7", "Atencion rapida"),
        ],
        proceso=[
            ("1", "Evaluacion del area y foco sanitario"),
            ("2", "Aplicacion segura segun necesidad"),
            ("3", "Recomendaciones y seguimiento"),
        ],
        usos=[
            "Hogares",
            "Oficinas",
            "Clinicas",
            "Empresas",
        ],
        highlight_text="Ideal para ambientes que requieren control sanitario confiable y una ejecucion segura.",
        title_sizes=(26, 32, 48),
    )
