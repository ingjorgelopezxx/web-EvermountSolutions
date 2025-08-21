# components/servicio_desratizacion.py
import flet as ft

def render_servicio_desratizacion(
    page: ft.Page,
    contenedor: ft.Column,
    *,
    rat_img_url: str = "https://i.postimg.cc/FsrS6xC9/raton-campo-mus-musculus-768x576.jpg",
    whatsapp_num: str = "+56937539304",
):
    """
    Pinta el detalle del servicio 'Desratización' con estilo tipo flyer.
    - page: ft.Page
    - contenedor: columna donde quieres renderizar el contenido
    """

    # Usa el mismo color que tu barra superior
    COLOR_PRINCIPAL = "#0F4D4A"  # cámbialo si tu barra usa otro

    def _sizes_for(p: ft.Page):
        w = p.width or 800
        if w < 420:  # móviles chicos
            return dict(
                logo_w=120, logo_h=60,
                title_sz=38, lead_sz=16, body_sz=15,
                rat_h=260,
                cta_h=52, cta_radius=28, cta_icon=26, cta_sz=18,
                outer_pad=16, inner_gap=12,
            )
        elif w < 768:  # móviles grandes / tablets chicas
            return dict(
                logo_w=150, logo_h=72,
                title_sz=46, lead_sz=18, body_sz=16,
                rat_h=320,
                cta_h=56, cta_radius=30, cta_icon=28, cta_sz=20,
                outer_pad=18, inner_gap=14,
            )
        else:  # tablet / desktop
            return dict(
                logo_w=190, logo_h=90,
                title_sz=56, lead_sz=20, body_sz=18,
                rat_h=380,
                cta_h=60, cta_radius=34, cta_icon=30, cta_sz=22,
                outer_pad=22, inner_gap=16,
            )

    SZ = _sizes_for(page)

    # --- CTA WhatsApp ---
    def _abrir_whatsapp(e):
        numero = whatsapp_num.replace("+", "").strip()
        page.launch_url(f"https://wa.me/{numero}")

    # PNG para máxima compatibilidad
    WHATSAPP_ICON = "https://upload.wikimedia.org/wikipedia/commons/5/5e/WhatsApp_icon.png"

    icono_whatsapp = ft.Image(
        src=WHATSAPP_ICON,
        width=SZ["cta_icon"] + 6,
        height=SZ["cta_icon"] + 6,
        fit=ft.ImageFit.CONTAIN,
    )

    boton_whatsapp = ft.Container(
        on_click=_abrir_whatsapp,
        ink=True,
        bgcolor=COLOR_PRINCIPAL,            # ← mismo color que la barra
        border_radius=SZ["cta_radius"],
        padding=ft.padding.symmetric(horizontal=18, vertical=10),
        content=ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                icono_whatsapp,
                ft.Text(
                    "Contáctanos hoy",
                    size=SZ["cta_sz"],
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.WHITE,
                ),
            ],
        ),
        height=SZ["cta_h"],
    )

    # --- Estructura principal ---

    titulo = ft.Text(
        "Desratización\nProfesional",
        size=SZ["title_sz"],
        weight=ft.FontWeight.BOLD,
        color=COLOR_PRINCIPAL,              # ← mismo color que la barra
        text_align=ft.TextAlign.CENTER,
    )

    # Texto principal + bullets (sustituyen al subtexto anterior)
    descripcion = ft.Text(
        "Los roedores son una de las plagas más peligrosas por los daños estructurales "
        "que causan y las enfermedades que transmiten. Nuestro servicio de desratización "
        "incluye diagnóstico, control activo y sellado de accesos.",
        size=SZ["lead_sz"],
        color=ft.Colors.BLACK87,
        text_align=ft.TextAlign.CENTER,
    )

    bullet_textos = [
        "🔍 Inspección detallada para detectar nidos y rutas",
        "🧠 Estrategias inteligentes: cebos, trampas, estaciones seguras",
        "🚪 Recomendaciones de cierre y sellado estructural",
        "💡 Mantenemos tu propiedad libre de roedores con mínima interrupción.",
    ]
    bullets = [ft.Text(t, size=SZ["body_sz"], color=ft.Colors.BLACK87) for t in bullet_textos]

    lista = ft.Column(
        controls=bullets,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=6,
    )

    imagen_rata = ft.Container(
        height=SZ["rat_h"],
        alignment=ft.alignment.center,
        content=ft.Image(src=rat_img_url, fit=ft.ImageFit.CONTAIN),
    )

    card = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"] + 4),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=SZ["inner_gap"],
            controls=[
                titulo,
                descripcion,
                lista,
                imagen_rata,
                ft.Container(height=6),
                boton_whatsapp,
            ],
        ),
    )

    # Render en el contenedor destino
    contenedor.controls.clear()
    contenedor.controls.append(
        ft.ListView(expand=True, controls=[card], padding=0)
    )
    contenedor.update()

    # --- Responsivo en runtime ---
    def _on_resize(e):
        nonlocal SZ
        SZ = _sizes_for(page)

        titulo.size = SZ["title_sz"]
        descripcion.size = SZ["lead_sz"]
        for t in bullets:
            t.size = SZ["body_sz"]

        imagen_rata.height = SZ["rat_h"]
        icono_whatsapp.width = SZ["cta_icon"] + 6
        icono_whatsapp.height = SZ["cta_icon"] + 6
        boton_whatsapp.height = SZ["cta_h"]
        boton_whatsapp.border_radius = SZ["cta_radius"]

        # actualizar paddings y gaps del card
        card.padding = ft.padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"] + 4)
        card.content.spacing = SZ["inner_gap"]
        card.update()

    page.on_resize = _on_resize
