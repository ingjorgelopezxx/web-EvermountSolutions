import flet as ft

def create_quienes(page: ft.Page):
    COLOR_TITULO = "#0D2943"  # azul oscuro corporativo
    TEXTO_SIZE = 14
    SUBTITULO_SIZE = 18
    ICON_SIZE = 40

    # --- Subtítulo ---
    subtitulo = ft.Text(
        "Evermount Solutions - Pest Defense",
        size=SUBTITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO,
        text_align=ft.TextAlign.CENTER,
    )

    # --- Texto principal ---
    texto_principal = ft.Text(
        "Somos una empresa familiar dedicada con pasión al control y manejo integral de plagas. Fundada "
        "por dos hermanos, nuestra misión es proteger hogares, empresas y comunidades con soluciones "
        "efectivas, responsables y personalizadas.\n\n"
        "Confía en nosotros para mantener tus espacios seguros, limpios y libres de plagas, con tecnología avanzada y atención profesional.\n\n"
        "🛡️ Confianza familiar, protección garantizada.",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK87,
        text_align=ft.TextAlign.JUSTIFY,
    )

    # --- Contenedor principal ---
    contenedor = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            [
                subtitulo,
                texto_principal,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        width=page.width
    )

    return contenedor



