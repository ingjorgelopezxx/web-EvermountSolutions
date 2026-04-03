import flet as ft


COLOR_SEPARADOR_PC = "#203a43"
COLOR_SEPARADOR_MOBILE = "#0D2943"


def safe_remove(control, controls_list):
    try:
        while control in controls_list:
            controls_list.remove(control)
    except Exception:
        pass


def safe_update(ctrl):
    try:
        if getattr(ctrl, "page", None) is not None:
            ctrl.update()
    except Exception:
        pass


def resize_video_card(card: ft.Container, w: int, h: int):
    card.width = w
    card.height = h

    data = card.data or {}
    stack = data.get("stack")
    img = data.get("img")
    overlay = data.get("overlay")

    if stack:
        stack.width = w
        stack.height = h
    if img:
        img.width = w
        img.height = h
    if overlay:
        overlay.width = w
        overlay.height = h

    safe_update(card)


def build_video_card(page: ft.Page, youtube_id: str, w: int, h: int, launch_url):
    watch_url = f"https://www.youtube.com/watch?v={youtube_id}"
    thumb_url = f"https://img.youtube.com/vi/{youtube_id}/hqdefault.jpg"

    img = ft.Image(
        src=thumb_url,
        width=w,
        height=h,
        fit=ft.BoxFit.COVER,
    )

    overlay = ft.Container(
        width=w,
        height=h,
        alignment=ft.alignment.center,
        content=ft.Container(
            bgcolor="rgba(0,0,0,0.16)",
            border_radius=999,
            padding=10,
            content=ft.Icon(
                ft.Icons.PLAY_CIRCLE_FILL,
                size=58,
                color=ft.Colors.WHITE,
            ),
        ),
    )

    stack = ft.Stack(
        width=w,
        height=h,
        controls=[img, overlay],
    )

    card = ft.Container(
        width=w,
        height=h,
        border_radius=24,
        bgcolor="#FDFEFE",
        border=ft.Border.all(1, "#D7E4E9"),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        shadow=ft.BoxShadow(
            blur_radius=18,
            spread_radius=0,
            color="rgba(11,38,47,0.16)",
            offset=ft.Offset(0, 10),
        ),
        content=stack,
        ink=True,
        on_click=lambda e: launch_url(page, watch_url),
    )

    card.data = {"img": img, "overlay": overlay, "stack": stack}
    return card


def create_separator(page: ft.Page, texto: str, icono=None) -> ft.Container:
    tx = None
    ic = None

    if isinstance(icono, list) and icono and isinstance(icono[0], tuple):
        bloques = []
        for idx, (label, icn) in enumerate(icono):
            bloques.append(
                ft.Row(
                    [
                        ft.Icon(icn, color=ft.Colors.WHITE, size=20),
                        ft.Text(
                            label,
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ],
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
            if idx < len(icono) - 1:
                bloques.append(
                    ft.Text(
                        "|",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    )
                )
        contenido_row = ft.Row(
            bloques,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
            wrap=False,
        )
    elif isinstance(icono, (list, tuple)):
        iconos = [
            ft.Icon(icn, color=ft.Colors.WHITE, size=22)
            for icn in icono
        ]
        ic = ft.Row(
            iconos,
            spacing=6,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        contenido_row = ic
    else:
        ic = ft.Icon(icono, color=ft.Colors.WHITE, size=24) if icono else None
        tx = ft.Text(
            texto,
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        )
        contenido_row = ft.Row(
            [ic if ic else ft.Container(), tx],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        )

    inner = ft.Container(
        content=contenido_row,
        border_radius=999,
        border=ft.Border.all(1, "rgba(255,255,255,0.16)"),
        bgcolor="rgba(255,255,255,0.06)",
        padding=ft.Padding.symmetric(horizontal=18, vertical=10),
        shadow=ft.BoxShadow(
            blur_radius=12,
            spread_radius=0,
            color="rgba(0,0,0,0.10)",
            offset=ft.Offset(0, 4),
        ),
    )

    sep = ft.Container(
        bgcolor=COLOR_SEPARADOR_MOBILE,
        margin=ft.Margin.only(top=14),
        content=inner,
        alignment=ft.alignment.center,
        width=float("inf"),
        padding=ft.Padding.symmetric(vertical=12, horizontal=10),
    )

    sep.data = sep.data or {}
    sep.data.update(
        {
            "bg_mobile": COLOR_SEPARADOR_MOBILE,
            "txt": tx,
            "icon": ic,
            "inner": inner,
        }
    )
    return sep


def create_signature(page: ft.Page, texto: str) -> ft.Container:
    txt = ft.Text(
        texto,
        size=12,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    cont = ft.Container(
        bgcolor=COLOR_SEPARADOR_MOBILE,
        content=txt,
        alignment=ft.alignment.center,
        width=None,
    )

    cont.data = {
        "mobile_bg": COLOR_SEPARADOR_MOBILE,
        "raw_text": texto,
        "oneline_text": " ".join(texto.split()),
    }
    return cont


def create_signature_with_icons() -> tuple[ft.Control, ft.Control, ft.Control]:
    def _inline_item(icon_name, label, size=12):
        return ft.Row(
            [
                ft.Icon(icon_name, size=size + 2, color="#202325"),
                ft.Text(label, size=size, weight=ft.FontWeight.BOLD, color="#202325"),
            ],
            spacing=4,
            tight=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    footer_inline = ft.Row(
        [
            ft.Text("Desarrollo por Ing. Jorge Lopez con tecnologia", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
            ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.WEB, "Flet"),
            ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.CODE, "Python"),
            ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.PHONE, "+56937539304"),
            ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.CAMERA_ALT, "jorgelopezsilva"),
            ft.Text("|", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
            ft.Text("2025 (c) Todos los derechos reservados", size=12, weight=ft.FontWeight.BOLD, color="#202325"),
        ],
        spacing=8,
        wrap=True,
        run_spacing=6,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    footer_tablet = ft.Row(
        [
            ft.Text("Desarrollo Ing. Jorge Lopez", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
            ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.WEB, "Flet", 9),
            ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.CODE, "Python", 9),
            ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.PHONE, "+56937539304", 9),
            ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
            _inline_item(ft.Icons.CAMERA_ALT, "jorgelopezsilva", 9),
            ft.Text("|", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
            ft.Text("2025 (c)", size=9, weight=ft.FontWeight.BOLD, color="#202325"),
        ],
        spacing=4,
        wrap=False,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    footer_mobile = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("Desarrollo Ing. Jorge Lopez", size=10, weight=ft.FontWeight.BOLD, color="#202325"),
                    ft.Text("|", size=10, weight=ft.FontWeight.BOLD, color="#202325"),
                    _inline_item(ft.Icons.WEB, "Flet", 11),
                    ft.Text("|", size=11, weight=ft.FontWeight.BOLD, color="#202325"),
                    _inline_item(ft.Icons.CODE, "Python", 11),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    _inline_item(ft.Icons.PHONE, "+56937539304", 11),
                    ft.Text("|", size=11, weight=ft.FontWeight.BOLD, color="#202325"),
                    _inline_item(ft.Icons.CAMERA_ALT, "jorgelopezsilva", 11),
                    ft.Text("|", size=11, weight=ft.FontWeight.BOLD, color="#202325"),
                    ft.Text("2025 (c)", size=10, weight=ft.FontWeight.BOLD, color="#202325"),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=4,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return footer_mobile, footer_tablet, footer_inline

