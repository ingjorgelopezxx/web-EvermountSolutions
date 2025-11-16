import flet as ft

def create_valores(page: ft.Page):

    # Estilos base (móvil)
    TITULO_SIZE = 20
    TEXTO_SIZE = 14
    ICON_SIZE = 40
    COLOR_TITULO = "#0D2943"

    # --- Crear elementos individuales con keys ---
    titulo_mision = ft.Text("Misión", key="titulo_mision", size=TITULO_SIZE,
                            weight=ft.FontWeight.BOLD, color=COLOR_TITULO)

    texto_mision = ft.Text(
        "Brindar soluciones integrales, efectivas y sostenibles para el control de plagas, "
        "protegiendo hogares, empresas y comunidades con responsabilidad, compromiso y tecnología "
        "de vanguardia. Nos guiamos por los valores familiares que nos impulsan a ofrecer un servicio "
        "cercano, confiable y duradero.",
        key="texto_mision",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK87,
        text_align=ft.TextAlign.JUSTIFY
    )

    titulo_vision = ft.Text("Visión", key="titulo_vision",
                            size=TITULO_SIZE, weight=ft.FontWeight.BOLD, color=COLOR_TITULO)

    texto_vision = ft.Text(
        "Ser reconocidos como una de las empresas líderes en control de plagas en Chile y Latinoamérica, "
        "destacando por nuestra excelencia operativa, innovación constante y atención personalizada, "
        "con una gestión basada en la ética, el respeto al medio ambiente y el trabajo en equipo.",
        key="texto_vision",
        size=TEXTO_SIZE,
        color=ft.Colors.BLACK87,
        text_align=ft.TextAlign.JUSTIFY
    )

    # 🟦 VALORES CORPORATIVOS
    texto_valores = ft.Text(
        key="texto_valores",
        spans=[
            ft.TextSpan("1. Compromiso Familiar: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(
                "Nos mueve el vínculo de hermanos: trabajamos con dedicación y confianza, cuidando cada cliente como parte de nuestra propia casa.\n\n"
            ),
            ft.TextSpan("2. Responsabilidad: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(
                "Cumplimos con lo que prometemos. Protegemos la salud, los espacios y el entorno con protocolos seguros y eficientes.\n\n"
            ),
            ft.TextSpan("3. Innovación: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(
                "Aplicamos métodos modernos y tecnologías efectivas para prevenir y erradicar plagas con mínimo impacto ambiental.\n\n"
            ),
            ft.TextSpan("4. Transparencia: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(
                "Informamos con claridad y actuamos con honestidad en cada paso del servicio.\n\n"
            ),
            ft.TextSpan("5. Cercanía con el Cliente: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(
                "Ofrecemos atención personalizada, directa y humana. Escuchamos, entendemos y resolvemos.\n\n"
            ),
            ft.TextSpan("6. Sostenibilidad: ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(
                "Utilizamos productos y técnicas que cuidan la salud y respetan el medio ambiente."
            ),
        ],
        size=TEXTO_SIZE,
        text_align=ft.TextAlign.JUSTIFY,
        color=ft.Colors.BLACK87
    )

    titulo_valores = ft.Text(
        "Valores Corporativos",
        key="titulo_valores",
        size=TITULO_SIZE,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TITULO
    )

    # --- Columnas ---
    columna1 = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.FLAG, size=ICON_SIZE, color=COLOR_TITULO),
                        titulo_mision],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                texto_mision,
            ]
        )
    )

    columna2 = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.VISIBILITY, size=ICON_SIZE, color=COLOR_TITULO),
                        titulo_vision],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                texto_vision,
            ]
        )
    )

    columna3 = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.VERIFIED, size=ICON_SIZE, color=COLOR_TITULO),
                        titulo_valores],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                texto_valores,
            ]
        )
    )

    valores_row = ft.ResponsiveRow(
        controls=[
            ft.Column(
                [columna1, columna2],
                col={"xs": 12, "md": 6, "lg": 6},
                spacing=10,
            ),
            ft.Column(
                [columna3],
                col={"xs": 12, "md": 6, "lg": 6},
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        run_spacing=10,
        spacing=10,
    )


    # --- Guardamos referencias para ser modificadas desde main.py ---
    valores_row.data = {
        "titulos": [titulo_mision, titulo_vision, titulo_valores],
        "textos": [texto_mision, texto_vision, texto_valores],
    }

    return valores_row
