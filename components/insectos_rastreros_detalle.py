from components.service_detail_template import render_service_detail


def render_servicio_rastreros(
    page,
    contenedor,
    *,
    rastreros_insectos_img_url: str = "https://i.postimg.cc/Z5ZVmx43/rastreros-Photoroom-Photoroom.png",
    whatsapp_num: str = "+56999724454",
):
    render_service_detail(
        page,
        contenedor,
        title="Control de Insectos Rastreros",
        lead_text=(
            "Los insectos rastreros contaminan alimentos, generan molestias y pueden transmitir "
            "enfermedades. Trabajamos con metodos modernos y productos certificados para erradicar "
            "cucarachas, hormigas, pulgas y otras especies."
        ),
        benefits=[
            "Diagnostico personalizado.",
            "Tratamientos focalizados y residuales.",
            "Tecnicas no invasivas, seguras para personas y mascotas.",
            "Servicio disponible en casas, departamentos, empresas y locales comerciales.",
        ],
        image_url=rastreros_insectos_img_url,
        whatsapp_num=whatsapp_num,
        chips_textos=[
            "Control residual y focalizado",
            "Metodos seguros para el entorno",
        ],
        metricas=[
            ("360", "Diagnostico tecnico"),
            ("SAFE", "Aplicacion segura"),
            ("PLUS", "Cobertura ampliada"),
        ],
        proceso=[
            ("1", "Revision de actividad y escondites"),
            ("2", "Aplicacion segun especie y nivel"),
            ("3", "Seguimiento y prevencion"),
        ],
        usos=[
            "Casas",
            "Deptos",
            "Bodegas",
            "Locales",
        ],
        highlight_text="Tratamos focos de insectos rastreros con precision y minima interrupcion.",
        title_sizes=(26, 32, 48),
    )
