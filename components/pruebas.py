import flet as ft

# ------------------------------------------------------------
# Evermount Solutions - Banner 1024x512 (estilo del diseño)
# Reemplaza las rutas/URLs de imágenes por las tuyas.
# ------------------------------------------------------------

W, H = 1024, 512

# Coloca tus imágenes en una carpeta "assets/" junto a este script
LOGO_PATH = "assets/logo_pc_dark.png"

# Placeholders (cámbialos por tus fotos reales)
PEST_IMG_1 = "assets/pest_rodent.jpg"     # o URL
PEST_IMG_2 = "assets/pest_cockroach.jpg"  # o URL
PEST_IMG_3 = "assets/pest_wasp.jpg"       # o URL
TECH_IMG   = "assets/technician.png"      # ideal PNG con fondo transparente (o JPG)

def pest_card(src: str) -> ft.Control:
    return ft.Container(
        width=200,
        height=115,
        border_radius=10,
        clip_behavior=ft.ClipBehavior.NONE,
        bgcolor=ft.Colors.WHITE,
        content=ft.Image(src=src, fit=ft.ImageFit.COVER),
    )

def pill(label: str, icon: str = "✅") -> ft.Control:
    return ft.Container(
        padding=ft.padding.symmetric(horizontal=10, vertical=6),
        border_radius=999,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.BLACK)),
        content=ft.Row(
            spacing=6,
            tight=True,
            controls=[
                ft.Text(icon, size=14),
                ft.Text(label, size=12, weight=ft.FontWeight.W_600, color="#0B2D4A"),
            ],
        ),
    )

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.WHITE
    page.window_width = W
    page.window_height = H

    # Colores aproximados (ajusta si quieres)
    navy = "#0B2D4A"
    deep = "#0A2A45"
    mid  = "#1A5D9A"
    light = "#BFD9F2"

    # Fondo con degradado hacia la derecha (como pediste)
    background = ft.Container(
        width=W,
        height=H,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[
                ft.Colors.WHITE,
                ft.Colors.WHITE,
                ft.Colors.with_opacity(1, light),
                ft.Colors.with_opacity(1, mid),
                ft.Colors.with_opacity(1, deep),
            ],
            stops=[0.0, 0.55, 0.70, 0.85, 1.0],
        ),
    )

    # Panel izquierdo (contenido)
    left_panel = ft.Container(
        width=720,
        height=H,
        padding=ft.padding.only(left=26, right=18, top=18, bottom=18),
        content=ft.Column(
            spacing=12,
            controls=[
                # Header: logo + texto
                ft.Row(
                    spacing=16,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=140,
                            height=90,
                            alignment=ft.alignment.center,
                            content=ft.Image(src=LOGO_PATH, fit=ft.ImageFit.CONTAIN),
                        ),
                        ft.Column(
                            spacing=2,
                            controls=[
                                ft.Text("Evermount\nSolutions", size=34, weight=ft.FontWeight.W_800, color=navy),
                                ft.Text("CONTROL DE PLAGAS", size=14, weight=ft.FontWeight.W_700, color=navy),
                            ],
                        ),
                    ],
                ),

                # Banda azul "EXPERTOS..."
                ft.Container(
                    height=58,
                    border_radius=12,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=[deep, "#123E63", deep],
                    ),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        "EXPERTOS EN CONTROL DE PLAGAS",
                        size=22,
                        weight=ft.FontWeight.W_800,
                        color=ft.Colors.WHITE,
                    ),
                ),

                # Imágenes de plagas
                ft.Row(
                    spacing=12,
                    controls=[
                        pest_card(PEST_IMG_1),
                        pest_card(PEST_IMG_2),
                        pest_card(PEST_IMG_3),
                    ],
                ),

                # Etiquetas / servicios
                ft.Row(
                    spacing=10,
                    wrap=True,
                    controls=[
                        pill("ROEDORES", "🐭"),
                        pill("INSECTOS", "🪳"),
                        pill("TERMITAS", "🐜"),
                        pill("PROTECCIÓN DEL HOGAR", "🛡️"),
                    ],
                ),

                # Banda inferior (azul)
                ft.Container(
                    height=86,
                    border_radius=14,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=[deep, "#0E3B66", deep],
                    ),
                    padding=ft.padding.symmetric(horizontal=18, vertical=14),
                    content=ft.Column(
                        spacing=6,
                        controls=[
                            ft.Text(
                                "SEGURIDAD • EFICACIA • CONFIANZA",
                                size=18,
                                weight=ft.FontWeight.W_800,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "CUIDAMOS SU HOGAR Y NEGOCIO",
                                size=14,
                                weight=ft.FontWeight.W_700,
                                color=ft.Colors.with_opacity(0.95, ft.Colors.WHITE),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    # Panel derecho: “espacio” con degradado y técnico (opcional)
    right_panel = ft.Container(
        expand=True,
        height=H,
        alignment=ft.alignment.bottom_right,
        padding=ft.padding.only(right=18, bottom=10),
        content=ft.Stack(
            controls=[
                # Silueta casa (simple, opcional)
                ft.Container(
                    alignment=ft.alignment.center_right,
                    padding=ft.padding.only(right=65, bottom=60),
                    content=ft.Icon(ft.Icons.HOUSE_ROUNDED, size=170, color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE)),
                ),
                # Técnico
                ft.Image(
                    src=TECH_IMG,
                    fit=ft.ImageFit.CONTAIN,
                    width=320,
                    height=360,
                    opacity=1.0,
                ),
            ]
        ),
    )

    banner = ft.Container(
        width=W,
        height=H,
        content=ft.Stack(
            controls=[
                background,
                ft.Row(
                    spacing=0,
                    controls=[
                        left_panel,
                        right_panel,
                    ],
                ),
            ]
        ),
    )

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            padding=0,
            content=banner,
        )
    )

# IMPORTANTE:
# - assets_dir="assets" hace que Flet sirva archivos locales de /assets
# - Crea carpeta "assets" y coloca las imágenes con esos nombres
ft.app(target=main, view=ft.WEB_BROWSER)