from components.service_detail_template import render_service_detail
from functions.asset_sources import SERVICE_DETAIL_IMAGES


def render_servicio_rastreros(
    page,
    contenedor,
    *,
    rastreros_insectos_img_url: str = SERVICE_DETAIL_IMAGES["rastreros"],
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        cache_key="servicio_rastreros",
        title="Control de Insectos Rastreros",
        lead_text=(
            "Los insectos rastreros contaminan alimentos, generan molestias y pueden transmitir "
            "enfermedades. Trabajamos con métodos modernos y productos certificados para erradicar "
            "cucarachas, hormigas, pulgas y otras especies."
        ),
        benefits=[
            "Diagnóstico personalizado.",
            "Tratamientos focalizados y residuales.",
            "Técnicas no invasivas, seguras para personas y mascotas.",
            "Servicio disponible en casas, departamentos, empresas y locales comerciales.",
        ],
        image_url=rastreros_insectos_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Control residual y focalizado",
            "Métodos seguros para el entorno",
        ],
        metricas=[
            ("360", "Diagnóstico técnico"),
            ("SAFE", "Aplicación segura"),
            ("PLUS", "Cobertura ampliada"),
        ],
        proceso=[
            ("1", "Revisión de actividad y escondites"),
            ("2", "Aplicación según especie y nivel"),
            ("3", "Seguimiento y prevención"),
        ],
        usos=[
            "Casas",
            "Deptos",
            "Bodegas",
            "Locales",
        ],
        highlight_text="Tratamos focos de insectos rastreros con precisión y mínima interrupción.",
        title_sizes=(26, 32, 48),
    )
