import re
from urllib.parse import quote

import flet as ft

from functions.asset_sources import SOCIAL_WHATSAPP
from functions.flet_actions import launch_url
from functions.resize_coordinator import register_resize_handler


def render_service_detail(
    page: ft.Page,
    contenedor: ft.Column,
    *,
    cache_key: str | None = None,
    title: str,
    lead_text: str,
    benefits: list[str],
    image_url: str,
    whatsapp_num: str,
    chips_textos: list[str],
    metricas: list[tuple[str, str]],
    proceso: list[tuple[str, str]],
    usos: list[str],
    highlight_text: str,
    title_sizes: tuple[int, int, int] = (26, 32, 48),
):
    if not hasattr(page, "_service_detail_cache"):
        page._service_detail_cache = {}

    cache_store = page._service_detail_cache
    cached = cache_store.get(cache_key) if cache_key else None
    if cached:
        try:
            cached["resize_fn"](None)
        except Exception:
            pass
        contenedor.controls.clear()
        contenedor.controls.append(cached["view"])
        contenedor.update()
        return

    def _sizes_for(p: ft.Page):
        w = p.width or 800
        if w < 420:
            return dict(
                title_sz=title_sizes[0],
                lead_sz=14,
                body_sz=14,
                image_h=180,
                cta_h=50,
                cta_radius=24,
                cta_icon=24,
                cta_sz=16,
                outer_pad=14,
                inner_gap=10,
                desktop=False,
            )
        if w < 768:
            return dict(
                title_sz=title_sizes[1],
                lead_sz=17,
                body_sz=16,
                image_h=300,
                cta_h=56,
                cta_radius=28,
                cta_icon=28,
                cta_sz=18,
                outer_pad=18,
                inner_gap=14,
                desktop=False,
            )
        return dict(
            title_sz=title_sizes[2],
            lead_sz=18,
            body_sz=17,
            image_h=380,
            cta_h=60,
            cta_radius=32,
            cta_icon=30,
            cta_sz=20,
            outer_pad=24,
            inner_gap=18,
            desktop=True,
        )

    SZ = _sizes_for(page)

    def _abrir_whatsapp(e):
        numero = re.sub(r"\D", "", whatsapp_num)
        msg = page.session.store.get("whatsapp_msg") or ""
        url = f"https://wa.me/{numero}"
        if msg:
            url += f"?text={quote(msg)}"
        launch_url(page, url)

    WHATSAPP_ICON = SOCIAL_WHATSAPP

    icono_whatsapp = ft.Image(
        src=WHATSAPP_ICON,
        width=SZ["cta_icon"] + 6,
        height=SZ["cta_icon"] + 6,
        fit=ft.BoxFit.CONTAIN,
    )

    boton_texto = ft.Text(
        "Contactanos hoy!",
        size=SZ["cta_sz"],
        weight=ft.FontWeight.W_600,
        color=ft.Colors.WHITE,
    )

    boton_whatsapp = ft.Container(
        on_click=_abrir_whatsapp,
        ink=True,
        bgcolor="#0F3D47",
        border_radius=SZ["cta_radius"],
        padding=ft.Padding.symmetric(horizontal=18, vertical=10),
        content=ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[icono_whatsapp, boton_texto],
        ),
        height=SZ["cta_h"],
    )

    fila_boton = ft.Row(
        controls=[boton_whatsapp],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    titulo_text = ft.Text(
        title,
        size=SZ["title_sz"],
        weight=ft.FontWeight.BOLD,
        color="#0F3D47",
        text_align=ft.TextAlign.CENTER,
    )
    titulo = ft.Stack(controls=[titulo_text], alignment=ft.alignment.center)

    lead = ft.Text(
        lead_text,
        size=SZ["lead_sz"],
        color=ft.Colors.BLACK_87,
        text_align=ft.TextAlign.JUSTIFY,
    )

    lead_box = ft.Container(
        bgcolor="#EEF6F7",
        border_radius=18,
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        content=lead,
    )

    benefit_texts: list[ft.Text] = []

    def _benefit_item(texto: str):
        txt = ft.Text(
            texto,
            size=SZ["body_sz"],
            color=ft.Colors.BLACK,
            text_align=ft.TextAlign.JUSTIFY,
        )
        benefit_texts.append(txt)
        return ft.Row(
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    width=28,
                    height=28,
                    border_radius=14,
                    bgcolor="#DCECEF",
                    alignment=ft.alignment.center,
                    content=ft.Icon(ft.Icons.CHECK, size=16, color="#0F3D47"),
                ),
                ft.Container(expand=True, content=txt),
            ],
        )

    desc = ft.Column(
        spacing=10,
        controls=[_benefit_item(texto) for texto in benefits],
    )

    metric_controls = []
    metric_value_texts: list[ft.Text] = []
    metric_detail_texts: list[ft.Text] = []
    for valor, texto in metricas:
        valor_txt = ft.Text(
            valor,
            size=SZ["body_sz"] + 8,
            color="#0F3D47",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        )
        detalle_txt = ft.Text(
            texto,
            size=SZ["body_sz"] - 2,
            color=ft.Colors.BLACK_87,
            text_align=ft.TextAlign.CENTER,
        )
        metric_value_texts.append(valor_txt)
        metric_detail_texts.append(detalle_txt)
        metric_controls.append(
            ft.Container(
                col={"xs": 12, "md": 4},
                bgcolor=ft.Colors.WHITE,
                border_radius=18,
                padding=ft.Padding.symmetric(horizontal=14, vertical=14),
                shadow=ft.BoxShadow(
                    blur_radius=12,
                    spread_radius=1,
                    color=ft.Colors.BLACK_12,
                    offset=ft.Offset(0, 4),
                ),
                content=ft.Column(
                    spacing=4,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[valor_txt, detalle_txt],
                ),
            )
        )

    metricas_grid = ft.ResponsiveRow(columns=12, spacing=12, run_spacing=12, controls=metric_controls)

    chip_controls = []
    chip_text_controls: list[ft.Text] = []
    for texto in chips_textos:
        chip_txt = ft.Text(
            texto,
            size=SZ["body_sz"] - 1,
            color="#0F3D47",
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.W_500,
        )
        chip_text_controls.append(chip_txt)
        chip_controls.append(
            ft.Container(
                col={"xs": 12, "md": 6},
                bgcolor="#EEF6F7",
                border_radius=14,
                padding=ft.Padding.symmetric(horizontal=12, vertical=10),
                content=chip_txt,
            )
        )
    chips = ft.ResponsiveRow(columns=12, spacing=10, run_spacing=10, controls=chip_controls)

    proceso_text_controls: list[ft.Text] = []
    proceso_items = []
    for numero, texto in proceso:
        paso_texto = ft.Text(
            texto,
            size=SZ["body_sz"] - 1,
            color=ft.Colors.BLACK_87,
            text_align=ft.TextAlign.LEFT,
        )
        proceso_text_controls.append(paso_texto)
        proceso_items.append(
            ft.Container(
                bgcolor="#F2F7F8",
                border_radius=18,
                padding=ft.Padding.symmetric(horizontal=14, vertical=12),
                content=ft.Row(
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=36,
                            height=36,
                            border_radius=18,
                            bgcolor="#123F49",
                            alignment=ft.alignment.center,
                            content=ft.Text(numero, size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                        ),
                        ft.Container(expand=True, content=paso_texto),
                    ],
                ),
            )
        )

    proceso_heading = ft.Text(
        "Como trabajamos",
        size=SZ["body_sz"] + 1,
        weight=ft.FontWeight.BOLD,
        color="#0F3D47",
    )
    proceso_box = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=24,
        padding=ft.Padding.symmetric(horizontal=20, vertical=18),
        shadow=ft.BoxShadow(
            blur_radius=14,
            spread_radius=1,
            color=ft.Colors.BLACK_12,
            offset=ft.Offset(0, 6),
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Row(
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.AUTO_AWESOME, size=20, color="#0F3D47"),
                        proceso_heading,
                    ],
                ),
                *proceso_items,
            ],
        ),
    )

    imagen_servicio = ft.Container(
        height=SZ["image_h"],
        alignment=ft.alignment.center,
        content=ft.Image(src=image_url, fit=ft.BoxFit.CONTAIN),
    )

    imagen_card = ft.Container(
        bgcolor="#F2F7F8",
        border_radius=26,
        padding=ft.Padding.symmetric(horizontal=24, vertical=24),
        content=imagen_servicio,
    )

    usos_heading = ft.Text(
        "Aplicaciones frecuentes",
        size=SZ["body_sz"] + 1,
        weight=ft.FontWeight.BOLD,
        color="#0F3D47",
    )
    uso_text_controls: list[ft.Text] = []
    usos_controls = []
    for texto in usos:
        uso_txt = ft.Text(
            texto,
            text_align=ft.TextAlign.CENTER,
            size=SZ["body_sz"] - 1,
            color="#0F3D47",
        )
        uso_text_controls.append(uso_txt)
        usos_controls.append(
            ft.Container(
                col={"xs": 6, "md": 6},
                bgcolor="#EEF6F7",
                border_radius=14,
                padding=ft.Padding.symmetric(horizontal=12, vertical=10),
                content=uso_txt,
            )
        )

    usos_card = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=24,
        padding=ft.Padding.symmetric(horizontal=18, vertical=18),
        shadow=ft.BoxShadow(
            blur_radius=14,
            spread_radius=1,
            color=ft.Colors.BLACK_12,
            offset=ft.Offset(0, 6),
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Row(
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.APARTMENT, size=20, color="#0F3D47"),
                        usos_heading,
                    ],
                ),
                ft.ResponsiveRow(columns=12, spacing=10, run_spacing=10, controls=usos_controls),
            ],
        ),
    )

    texto_destacado = ft.Text(
        highlight_text,
        size=SZ["body_sz"],
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_600,
    )

    destacada = ft.Container(
        bgcolor="#123F49",
        border_radius=22,
        padding=ft.Padding.symmetric(horizontal=18, vertical=16),
        content=ft.Column(
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[texto_destacado, fila_boton],
        ),
    )

    bloque_texto = ft.Container(
        expand=7,
        bgcolor=ft.Colors.WHITE,
        border_radius=28,
        padding=ft.Padding.symmetric(horizontal=30, vertical=28),
        shadow=ft.BoxShadow(
            blur_radius=18,
            spread_radius=1,
            color=ft.Colors.BLACK_12,
            offset=ft.Offset(0, 8),
        ),
        content=ft.Column(
            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            controls=[titulo, lead_box, metricas_grid, chips, desc, proceso_box],
        ),
    )

    bloque_visual = ft.Container(
        expand=5,
        content=ft.Column(
            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[imagen_card, usos_card, destacada],
        ),
    )

    desktop_layout = ft.Column(
        spacing=24,
        controls=[
            ft.Row(
                spacing=24,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[bloque_texto, bloque_visual],
            )
        ],
    )

    mobile_layout = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=SZ["inner_gap"],
        controls=[
            titulo,
            imagen_servicio,
            lead,
            metricas_grid,
            desc,
            chips,
            proceso_box,
            ft.Container(height=6),
            fila_boton,
        ],
    )

    card = ft.Container(
        bgcolor="#F9FBFB",
        padding=ft.Padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"] + 4),
        content=desktop_layout if SZ["desktop"] else mobile_layout,
    )

    list_view = ft.ListView(expand=True, controls=[card], padding=0)

    contenedor.controls.clear()
    contenedor.controls.append(list_view)
    contenedor.update()

    def _on_resize(e):
        nonlocal SZ
        if getattr(card, "page", None) is None:
            return

        SZ = _sizes_for(page)

        titulo_text.size = SZ["title_sz"]
        lead.size = SZ["lead_sz"]
        texto_destacado.size = SZ["body_sz"]
        proceso_heading.size = SZ["body_sz"] + 1
        usos_heading.size = SZ["body_sz"] + 1
        imagen_servicio.height = SZ["image_h"]

        icono_whatsapp.width = SZ["cta_icon"] + 6
        icono_whatsapp.height = SZ["cta_icon"] + 6
        boton_whatsapp.height = SZ["cta_h"]
        boton_whatsapp.border_radius = SZ["cta_radius"]
        boton_texto.size = SZ["cta_sz"]

        for txt in benefit_texts:
            txt.size = SZ["body_sz"]
        for txt in metric_value_texts:
            txt.size = SZ["body_sz"] + 8
        for txt in metric_detail_texts:
            txt.size = SZ["body_sz"] - 2
        for txt in chip_text_controls:
            txt.size = SZ["body_sz"] - 1
        for txt in proceso_text_controls:
            txt.size = SZ["body_sz"] - 1
        for txt in uso_text_controls:
            txt.size = SZ["body_sz"] - 1

        card.padding = ft.Padding.symmetric(horizontal=SZ["outer_pad"], vertical=SZ["outer_pad"] + 4)
        mobile_layout.spacing = SZ["inner_gap"]
        card.content = desktop_layout if SZ["desktop"] else mobile_layout
        card.update()

    resize_key = f"service_detail:{cache_key or title}"
    register_resize_handler(page, resize_key, _on_resize)

    if cache_key:
        cache_store[cache_key] = {
            "view": list_view,
            "resize_fn": _on_resize,
        }
