import flet as ft

def create_valores(page: ft.Page):
    # Estilos comunes
    TITULO_SIZE = 20
    TEXTO_SIZE = 14
    ICON_SIZE = 40
    COLOR_TITULO = "#0D2943"  # azul oscuro

    # Columna 1: Misión
    columna1 = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.FLAG, color=COLOR_TITULO, size=ICON_SIZE),
                        ft.Text("Misión", size=TITULO_SIZE, weight=ft.FontWeight.BOLD, color=COLOR_TITULO),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text(
                    "Brindar soluciones integrales, efectivas y sostenibles para el control de plagas, "
                    "protegiendo hogares, empresas y comunidades con responsabilidad, compromiso y tecnología "
                    "de vanguardia. Nos guiamos por los valores familiares que nos impulsan a ofrecer un servicio "
                    "cercano, confiable y duradero.",
                    size=TEXTO_SIZE,
                    color=ft.Colors.BLACK87,
                    text_align=ft.TextAlign.JUSTIFY
                )
            ],
            spacing=10
        )
    )

    # Columna 2: Visión
    columna2 = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.VISIBILITY, color=COLOR_TITULO, size=ICON_SIZE),
                        ft.Text("Visión", size=TITULO_SIZE, weight=ft.FontWeight.BOLD, color=COLOR_TITULO),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text(
                    "Ser reconocidos como una de las empresas líderes en control de plagas en Chile y Latinoamérica, "
                    "destacando por nuestra excelencia operativa, innovación constante y atención personalizada, "
                    "con una gestión basada en la ética, el respeto al medio ambiente y el trabajo en equipo.",
                    size=TEXTO_SIZE,
                    color=ft.Colors.BLACK87,
                    text_align=ft.TextAlign.JUSTIFY
                )
            ],
            spacing=10
        )
    )

    # Columna 3: Valores Corporativos
    columna3 = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=10,
        expand=True,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.VERIFIED, color=COLOR_TITULO, size=ICON_SIZE),
                        ft.Text("Valores Corporativos", size=TITULO_SIZE, weight=ft.FontWeight.BOLD, color=COLOR_TITULO),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            "1.Compromiso Familiar: ",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "Nos mueve el vínculo de hermanos: trabajamos con dedicación y confianza, cuidando cada cliente como parte de nuestra propia casa.\n\n",
                             style=ft.TextStyle(color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "2.Responsabilidad: ",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "Cumplimos con lo que prometemos. Protegemos la salud, los espacios y el entorno con protocolos seguros y eficientes.\n\n",
                            style=ft.TextStyle(color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "3.Innovación: ",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "Aplicamos métodos modernos y tecnologías efectivas para prevenir y erradicar plagas con mínimo impacto ambiental.\n\n",
                            style=ft.TextStyle(color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "4.Transparencia: ",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "Informamos con claridad y actuamos con honestidad en cada paso del servicio.\n\n",
                            style=ft.TextStyle(color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "5.Cercanía con el Cliente: ",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "Ofrecemos atención personalizada, directa y humana. Escuchamos, entendemos y resolvemos.\n\n",
                            style=ft.TextStyle(color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "6. Sostenibilidad: ",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)
                        ),
                        ft.TextSpan(
                            "Utilizamos productos y técnicas que cuidan la salud y respetan el medio ambiente.",
                            style=ft.TextStyle(color=ft.Colors.BLACK)
                        ),
                        
                    ],
                    text_align=ft.TextAlign.JUSTIFY,
                    style=ft.TextStyle(size=TEXTO_SIZE, color=ft.Colors.BLACK87)
                )
            ],
            spacing=10
        )
    )

    # Fila contenedora (tres columnas)
    valores_row = ft.ResponsiveRow(
        controls=[
            ft.Column([columna1], col={"xs": 12, "md": 4}),
            ft.Column([columna2], col={"xs": 12, "md": 4}),
            ft.Column([columna3], col={"xs": 12, "md": 4}),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        run_spacing=10,
        spacing=10
    )

    return valores_row
