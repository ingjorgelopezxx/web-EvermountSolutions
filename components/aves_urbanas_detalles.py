# components/servicios_detalle.py
import flet as ft
import re
from urllib.parse import quote

def render_servicio_aves_urbanas(
    page: ft.Page,
    contenedor: ft.Column,
    *,
    aves_img_url: str = "https://i.postimg.cc/MGBy5SXS/avesurbanas.png",
    whatsapp_num: str = "+56999724454",
):
    """
    Pinta el detalle del servicio 'aves urbanas' con estilo tipo flyer.
    """

    def _sizes_for(p: ft.Page):
        w = p.width or 800
        if w < 420:    # móviles chicos
            return dict(
                title_sz=22, lead_sz=14, body_sz=14,
                aves_h=180, cta_h=50, cta_radius=24, cta_icon=24, cta_sz=16,
                outer_pad=14, inner_gap=10,
            )
        elif w < 768:  # móviles grandes / tablets
            return dict(
                title_sz=32, lead_sz=17, body_sz=16,
                aves_h=300, cta_h=56, cta_radius=28, cta_icon=28, cta_sz=18,
                outer_pad=18, inner_gap=14,
            )
        else:          # desktop
            return dict(
                title_sz=46, lead_sz=18, body_sz=17,
                aves_h=360, cta_h=60, cta_radius=32, cta_icon=30, cta_sz=20,
                outer_pad=22, inner_gap=16,
            )

    SZ = _sizes_for(page)

    # --- CTA WhatsApp ---
    def _abrir_whatsapp(e):
        # número en solo dígitos
        numero = re.sub(r"\D", "", whatsapp_num)

        # lee el mensaje que guardaste en main con page.client_storage.set("whatsapp_msg", "...")
        msg = page.client_storage.get("whatsapp_msg") or ""

        # arma la URL con text solo si hay mensaje
        url = f"https://wa.me/{numero}"
        if msg:
            url += f"?text={quote(msg)}"

        page.launch_url(url)
    WHATSAPP_ICON = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"

    icono_whatsapp = ft.Image(
        src=WHATSAPP_ICON,
        width=SZ["cta_icon"] + 6,
        height=SZ["cta_icon"] + 6,
        fit=ft.ImageFit.CONTAIN,
    )

    # Botón que se ajusta a su contenido (sin expand, sin width)
    boton_whatsapp = ft.Container(
        on_click=_abrir_whatsapp,
        ink=True,
        bgcolor="#0F3D47",   # mismo color que la barra superior
        border_radius=SZ["cta_radius"],
        padding=ft.padding.symmetric(horizontal=18, vertical=10),
        content=ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                icono_whatsapp,
                ft.Text(
                    "Contáctanos hoy!",
                    size=SZ["cta_sz"],
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.WHITE,
                ),
            ],
        ),
        height=SZ["cta_h"],
    )

    # Fila para centrar el botón y evitar que se estire
    fila_boton = ft.Row(
        controls=[boton_whatsapp],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # --- Textos ---
    titulo_text = ft.Text(
        "Control de Aves Urbanas"
        "\n(Palomas, tórtolas, gorriones u otras especies invasoras)",
        size=SZ["title_sz"],
        weight=ft.FontWeight.BOLD,
        color="#0F3D47",           # color principal
        text_align=ft.TextAlign.CENTER,
    )

    # stack por si luego quieres agregar glow/sombra compuesta
    titulo = ft.Stack(controls=[titulo_text], alignment=ft.alignment.center)

    lead = ft.Text(
        "Las aves pueden convertirse en una plaga cuando anidan en techos, cornisas, galpones o equipos "
        "de ventilación, generando suciedad, malos olores y riesgos sanitarios. Nuestro servicio de control "
        "de aves está diseñado para alejar sin dañar, utilizando métodos seguros y autorizados.",
        size=SZ["lead_sz"],
        color=ft.Colors.BLACK87,
        text_align=ft.TextAlign.JUSTIFY,  # 👈 justificado
    )

    desc = ft.Column(
        spacing=4,
        controls=[
            ft.Text("⚙️ Instalación de sistemas anti-posamiento (pinchos, redes, tensores, gel repelente).", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
            ft.Text("🚫 Prevención de anidación y acumulación de excrementos.", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
            ft.Text("📋 Inspección técnica y asesoría personalizada.", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
            ft.Text("🌿 Soluciones éticas y respetuosas con la fauna.", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
            ft.Text("🛠️ Recomendado para: industrias, iglesias, colegios, techos de viviendas, galpones, restaurantes y edificios públicos.", size=SZ["body_sz"], text_align=ft.TextAlign.JUSTIFY,color=ft.Colors.BLACK),
        ],
    )

    imagen_aves = ft.Container(
        height=SZ["aves_h"],
        alignment=ft.alignment.center,
        content=ft.Image(src=aves_img_url, fit=ft.ImageFit.CONTAIN),
    )

    card = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"]+4),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=SZ["inner_gap"],
            controls=[titulo,imagen_aves, lead, desc, ft.Container(height=6), fila_boton],
        ),
    )

    contenedor.controls.clear()
    contenedor.controls.append(ft.ListView(expand=True, controls=[card], padding=0))
    contenedor.update()

     # --- Responsivo ---
    def _on_resize(e):
        nonlocal SZ
        SZ = _sizes_for(page)

        titulo_text.size = SZ["title_sz"]
        lead.size = SZ["lead_sz"]
        imagen_aves.height = SZ["rat_h"]

        # CTA
        icono_whatsapp.width = SZ["cta_icon"] + 6
        icono_whatsapp.height = SZ["cta_icon"] + 6
        boton_whatsapp.height = SZ["cta_h"]
        boton_whatsapp.border_radius = SZ["cta_radius"]
        # texto del botón
        if isinstance(boton_whatsapp.content, ft.Row) and len(boton_whatsapp.content.controls) >= 2:
            btn_text = boton_whatsapp.content.controls[1]
            if isinstance(btn_text, ft.Text):
                btn_text.size = SZ["cta_sz"]

        # paddings y spacing
        card.padding = ft.padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"] + 4)
        card.content.spacing = SZ["inner_gap"]
        card.update()

    page.on_resize = _on_resize
