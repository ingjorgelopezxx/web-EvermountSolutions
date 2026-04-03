from components.service_detail_template import render_service_detail
from functions.asset_sources import SERVICE_DETAIL_IMAGES


def render_servicio_sanitizacion(
    page,
    contenedor,
    *,
    sanitizacion_img_url: str = SERVICE_DETAIL_IMAGES["sanitizacion"],
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        cache_key="servicio_sanitizacion",
        title="Desinfección y Sanitización de Ambientes",
        lead_text=(
            "Protege la salud de tu familia, empleados y clientes con nuestros servicios de sanitización "
            "profesional. Eliminamos virus, bacterias, hongos y malos olores de forma segura, rápida y eficaz."
        ),
        benefits=[
            "Aplicación con nebulizador ULV o termonebulización.",
            "Uso de productos certificados por ISP y amigables con el medio ambiente.",
            "Ideal para hogares, oficinas, clínicas, escuelas y empresas.",
            "Previene contagios y garantiza ambientes más saludables.",
        ],
        image_url=sanitizacion_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Cobertura residencial y comercial",
            "Protocolos seguros y certificados",
        ],
        metricas=[
            ("ULV", "Aplicación técnica"),
            ("ISP", "Productos certificados"),
            ("24/7", "Atención rápida"),
        ],
        proceso=[
            ("1", "Evaluación del área y foco sanitario"),
            ("2", "Aplicación segura según necesidad"),
            ("3", "Recomendaciones y seguimiento"),
        ],
        usos=[
            "Hogares",
            "Oficinas",
            "Clínicas",
            "Empresas",
        ],
        highlight_text="Ideal para ambientes que requieren control sanitario confiable y una ejecución segura.",
        title_sizes=(26, 32, 48),
    )
