# components/servicios_detalle.py
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
    """

    def _sizes_for(p: ft.Page):
        w = p.width or 800
        if w < 420:    # móviles chicos
            return dict(
                title_sz=18, lead_sz=15, body_sz=14,
                rat_h=240, cta_h=50, cta_radius=24, cta_icon=24, cta_sz=16,
                outer_pad=14, inner_gap=10,
            )
        elif w < 768:  # móviles grandes / tablets
            return dict(
                title_sz=24, lead_sz=17, body_sz=16,
                rat_h=300, cta_h=56, cta_radius=28, cta_icon=28, cta_sz=18,
                outer_pad=18, inner_gap=14,
            )
        else:          # desktop
            return dict(
                title_sz=52, lead_sz=18, body_sz=17,
                rat_h=360, cta_h=60, cta_radius=32, cta_icon=30, cta_sz=20,
                outer_pad=22, inner_gap=16,
            )

    SZ = _sizes_for(page)

    # --- CTA WhatsApp ---
    def _abrir_whatsapp(e):
        numero = whatsapp_num.replace("+", "").strip()
        page.launch_url(f"https://wa.me/{numero}")

    WHATSAPP_ICON = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"

    boton_whatsapp = ft.Container(
        on_click=_abrir_whatsapp,
        ink=True,
        bgcolor="#0F3D47",   # mismo color que barra superior
        border_radius=SZ["cta_radius"],
        padding=ft.padding.symmetric(horizontal=18, vertical=10),
        content=ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(src=WHATSAPP_ICON, width=SZ["cta_icon"]+6, height=SZ["cta_icon"]+6, fit=ft.ImageFit.CONTAIN),
                ft.Text("Contáctanos hoy", size=SZ["cta_sz"], weight=ft.FontWeight.W_600, color=ft.Colors.WHITE),
            ],
        ),
        height=SZ["cta_h"],
    )

    # --- Textos ---
    titulo = ft.Text(
        "Desratización Profesional",  # 👈 una sola línea
        size=SZ["title_sz"],
        weight=ft.FontWeight.BOLD,
        color="#0F3D47",
        text_align=ft.TextAlign.CENTER,
    )

    lead = ft.Text(
        "Los roedores son una de las plagas más peligrosas por los daños estructurales que causan y las enfermedades que transmiten. "
        "Nuestro servicio de desratización incluye diagnóstico, control activo y sellado de accesos.",
        size=SZ["lead_sz"],
        color=ft.Colors.BLACK87,
        text_align=ft.TextAlign.JUSTIFY,  # 👈 justificado
    )

    desc = ft.Column(
        spacing=4,
        controls=[
            ft.Text("🔍 Inspección detallada para detectar nidos y rutas", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
            ft.Text("🧠 Estrategias inteligentes: cebos, trampas, estaciones seguras", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
            ft.Text("🚪 Recomendaciones de cierre y sellado estructural", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
            ft.Text("💡 Mantenemos tu propiedad libre de roedores con mínima interrupción.", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
        ],
    )

    imagen_rata = ft.Container(
        height=SZ["rat_h"],
        alignment=ft.alignment.center,
        content=ft.Image(src=rat_img_url, fit=ft.ImageFit.CONTAIN),
    )

    card = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"]+4),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=SZ["inner_gap"],
            controls=[titulo,imagen_rata, lead, desc, ft.Container(height=6), boton_whatsapp],
        ),
    )

    contenedor.controls.clear()
    contenedor.controls.append(ft.ListView(expand=True, controls=[card], padding=0))
    contenedor.update()

    # --- Responsivo ---
    def _on_resize(e):
        nonlocal SZ
        SZ = _sizes_for(page)
        titulo.size = SZ["title_sz"]
        lead.size = SZ["lead_sz"]
        imagen_rata.height = SZ["rat_h"]
        boton_whatsapp.height = SZ["cta_h"]
        boton_whatsapp.border_radius = SZ["cta_radius"]
        boton_whatsapp.content.controls[1].size = SZ["cta_sz"]  # texto dentro del botón
        card.padding = ft.padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"]+4)
        card.content.spacing = SZ["inner_gap"]
        card.update()

    page.on_resize = _on_resize
