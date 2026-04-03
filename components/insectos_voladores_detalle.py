from components.service_detail_template import render_service_detail
from functions.asset_sources import SERVICE_DETAIL_IMAGES


def render_servicio_voladores(
    page,
    contenedor,
    *,
    voladores_img_url: str = SERVICE_DETAIL_IMAGES["voladores"],
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        cache_key="servicio_voladores",
        title="Control de Insectos Voladores",
        lead_text=(
            "Los insectos voladores afectan la comodidad y pueden transmitir enfermedades en espacios "
            "interiores y exteriores. Aplicamos soluciones adaptadas para moscas, zancudos, avispas y "
            "otras especies según el entorno."
        ),
        benefits=[
            "Aplicación con equipos nebulizadores.",
            "Productos biodegradables y de bajo impacto ambiental.",
            "Tratamientos preventivos y de emergencia.",
            "Ideal para casas, patios, restaurantes, jardines y centros de eventos.",
        ],
        image_url=voladores_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Tratamientos preventivos",
            "Cobertura interior y exterior",
        ],
        metricas=[
            ("ULV", "Nebulización técnica"),
            ("FAST", "Acción rápida"),
            ("ECO", "Bajo impacto"),
        ],
        proceso=[
            ("1", "Evaluación del foco y nivel de actividad"),
            ("2", "Aplicación según zona y especie"),
            ("3", "Recomendaciones de mantención"),
        ],
        usos=[
            "Patios",
            "Restaurantes",
            "Jardines",
            "Eventos",
        ],
        highlight_text="Reducimos focos de insectos voladores con aplicaciones eficientes y controladas.",
        title_sizes=(26, 32, 48),
    )
