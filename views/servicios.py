
import flet as ft

# Slides de Servicios (extraídos del código original)
slides_servicios = [
    {
        "titulo": "Soluciones eficaces para todo tipo de plagas",
        "contenido": [
            "En Evermount Solutions ofrecemos servicios integrales y adaptados a cada necesidad, tanto para clientes residenciales como comerciales e industriales.",
            "• Control de insectos rastreros (cucarachas, hormigas, chinches, pulgas)",
            "• Control de insectos voladores (moscas, zancudos, avispas)",
            "• Control de roedores (ratones, ratas)",
            "• Tratamiento de termitas",
            "• Tratamiento de aves",
            "• Desinfección y sanitización de ambientes",
            "• Programas de control mensual y anual",
            "🔬 Usamos productos certificados y amigables con el medio ambiente."
        ]
    },
    {
        "titulo": "🪳 Control de Insectos Rastreros",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Cucaracha", "id": "cucarachas"},
                    {"nombre": "Hormiga", "id": "hormigas"},
                    {"nombre": "Chinche", "id": "chinches"},
                    {"nombre": "Pulga", "id": "pulgas"},
                ]
            },
            "Los insectos rastreros no solo causan molestias, sino que también pueden contaminar alimentos y transmitir enfermedades. En Evermount Solutions, utilizamos métodos modernos y productos certificados para erradicar cucarachas, hormigas, chinches de cama y pulgas de forma segura y efectiva.",
            "✅ Diagnóstico personalizado",
            "✅ Tratamientos focalizados y residuales",
            "✅ Técnicas no invasivas, seguras para personas y mascotas",
            "📍Servicio disponible en casas, departamentos, empresas, bodegas y locales comerciales."
        ]
    },
    {
        "titulo": "🦟 Control de Insectos Voladores",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Moscas", "id": "moscas"},
                    {"nombre": "Zancudos", "id": "zancudos"},
                    {"nombre": "Avispas", "id": "avispas"},
                ]
            },
            "Los insectos voladores son transmisores de enfermedades y afectan la comodidad en espacios interiores y exteriores. Contamos con soluciones efectivas para controlar moscas, zancudos (mosquitos), avispas y otros insectos voladores, adaptadas a cada tipo de ambiente.",
            "💨 Aplicación con equipos nebulizadores",
            "🌿 Productos biodegradables y de bajo impacto ambiental",
            "🕒 Tratamientos preventivos y de emergencia",
            "Ideal para: casas, patios, restaurantes, empresas de alimentos, jardines y centros de eventos.",
        ]
    },
    {
        "titulo": "🐀 Control de Roedores",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Ratón", "id": "raton"},
                    {"nombre": "Rata", "id": "rata"},
                ]
            },
            "Los roedores son una de las plagas más peligrosas por los daños estructurales que causan y las enfermedades que transmiten. Nuestro servicio de desratización incluye diagnóstico, control activo y sellado de accesos.",
            "🔍 Inspección detallada para detectar nidos y rutas",
            "🧠 Estrategias inteligentes: cebos, trampas, estaciones seguras",
            "🚪 Recomendaciones de cierre y sellado estructural",
            "💡 Mantenemos tu propiedad libre de roedores con mínima interrupción.",
        ]
    },
    {
        "titulo": "🐜 Tratamiento de Termitas",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Subterránea", "id": "termita_subterranea"},
                    {"nombre": "Madera", "id": "termita_madera_seca"},
                    {"nombre": "Otras", "id": "termita_otros"},
                ]
            },
            "Las termitas pueden causar daños estructurales graves en viviendas, empresas y construcciones de madera si no se detectan y tratan a tiempo. En Evermount Solutions - Pest Defense realizamos tratamientos especializados para eliminar termitas y proteger tus estructuras a largo plazo.",
            "🔍 Diagnóstico técnico con detección de actividad y daños",
            "🏠 Tratamientos localizados e integrales (perimetrales y estructurales)",
            "🧪 Uso de termiticidas de última generación aprobados por ISP",
            "🔄 Programas de monitoreo post-tratamiento",
            "💡 Ideal para casas, cabañas, construcciones nuevas, bodegas, colegios y centros comerciales."
        ]
    },
    {
        "titulo": "🕊️ Control de Aves Urbanas",
        "contenido": [
            {
                "tipo": "clickable_row",
                "items": [
                    {"nombre": "Palomas", "id": "palomas"},
                    {"nombre": "Tórtolas", "id": "tortolas"},
                    {"nombre": "Gorriones", "id": "gorriones"},
                    {"nombre": "Otras", "id": "aves_otros"},
                ]
            },
            "Las aves pueden convertirse en una plaga cuando anidan en techos, cornisas, galpones o equipos de ventilación, generando suciedad, malos olores y riesgos sanitarios. Nuestro servicio de control de aves está diseñado para alejar sin dañar, utilizando métodos seguros y autorizados.",
            "⚙️ Instalación de sistemas anti-posamiento (pinchos, redes, tensores, gel repelente)",
            "🚫 Prevención de anidación y acumulación de excrementos",
            "📋 Inspección técnica y asesoría personalizada",
            "🌿 Soluciones éticas y respetuosas con la fauna",
            "🛠️ Recomendado para: industrias, iglesias, colegios, techos de viviendas, galpones, restaurantes y edificios públicos."
        ]
    },
]

