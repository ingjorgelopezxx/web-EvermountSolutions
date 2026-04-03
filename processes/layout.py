import flet as ft


def clamp(v, mn, mx):
    return max(mn, min(mx, v))


def get_content_widths(w: int):
    if w < 600:
        return None, None
    if w < 900:
        base = min(int(w * 0.96), 860)
        return base, base
    if w < 1280:
        base = min(int(w * 0.94), 1120)
        return base, min(base, 1040)
    if w < 1600:
        base = min(int(w * 0.92), 1320)
        return base, min(base, 1180)
    base = min(int(w * 0.90), 1480)
    return base, min(base, 1240)


def apply_separator_sizes(page: ft.Page, separadores: list[ft.Container]):
    w = page.width or 0

    if w < 600:
        txt_size, icon_size, pad_v = 16, 18, 8
        inner_pad_x, inner_pad_y = 14, 8
    elif w < 1300:
        txt_size, icon_size, pad_v = 18, 20, 10
        inner_pad_x, inner_pad_y = 18, 10
    else:
        txt_size, icon_size, pad_v = 20, 24, 12
        inner_pad_x, inner_pad_y = 22, 11

    for sep in separadores:
        data = sep.data or {}
        tx = data.get("txt")
        ic = data.get("icon")
        inner = data.get("inner")

        if tx:
            tx.size = txt_size
        if ic:
            ic.size = icon_size
        if inner:
            inner.padding = ft.Padding.symmetric(horizontal=inner_pad_x, vertical=inner_pad_y)

        sep.padding = ft.Padding.symmetric(vertical=pad_v, horizontal=10)
        sep.width = float("inf")

        if getattr(sep, "page", None) is not None:
            sep.update()


def adjust_multimedia_zone(
    page: ft.Page,
    *,
    bloque_programas: ft.Container,
    carrusel_vertical: ft.Container,
    zona_multimedia: ft.Container,
    video_cards: list[ft.Container],
    resize_video_card,
    safe_update,
):
    w = page.width or 0

    program_data = bloque_programas.data or {}
    top_card = program_data.get("top_card")
    bottom_card = program_data.get("bottom_card")
    gap_cards = program_data.get("gap", 14)
    section_base_w, _ = get_content_widths(w)
    section_w = section_base_w or int(w * 0.94)
    if w >= 1100:
        section_w = min(int(w * 0.97), 1760)

    if 700 <= w < 1020:
        left_w = clamp(int(section_w * 0.31), 335, 380)
        top_h = 372
        bottom_h = 245
        side_pad = 0
    elif 1020 <= w < 1400:
        left_w = clamp(int(section_w * 0.26), 350, 390)
        top_h = 340
        bottom_h = 245
        side_pad = 0
    else:
        left_w = clamp(int(section_w * 0.24), 340, 390)
        top_h = 340
        bottom_h = 245
        side_pad = 0

    if top_card:
        top_card.height = top_h
        safe_update(top_card)
    if bottom_card:
        bottom_card.height = bottom_h
        safe_update(bottom_card)

    bloque_programas.width = left_w
    target_h = top_h + bottom_h + gap_cards

    media_count = 1
    if w >= 1120:
        media_count += 1
    if w >= 1500:
        media_count += 1
    if w >= 1820:
        media_count += 1
    if w >= 2140:
        media_count += 1

    controls_count = 1 + media_count
    total_gap = 18 * max(0, controls_count - 1)
    available_media_w = max(
        220,
        int((section_w - left_w - total_gap) / media_count),
    )
    if w < 1020:
        target_w = clamp(available_media_w, 280, 460)
    elif w < 1600:
        proportional_w = int(target_h * 0.72)
        target_w = clamp(max(available_media_w, proportional_w), 300, 500)
    else:
        proportional_w = int(target_h * 0.78)
        target_w = clamp(max(available_media_w, proportional_w), 320, 540)

    for card in video_cards:
        resize_video_card(card, target_w, target_h)

    try:
        data = carrusel_vertical.data or {}
        tarjeta = data.get("tarjeta")
        imagen = data.get("imagen")

        if tarjeta:
            tarjeta.width = target_w
            tarjeta.height = target_h
            safe_update(tarjeta)

        if imagen:
            imagen.width = target_w
            imagen.height = target_h
            safe_update(imagen)

        carrusel_vertical.width = target_w
        carrusel_vertical.height = target_h
        safe_update(carrusel_vertical)
    except Exception as ex:
        print("resize carrusel_vertical error:", ex)

    def box_auto(ctrl, width_value):
        return ft.Container(
            content=ctrl,
            width=width_value,
            padding=0,
            margin=0,
            alignment=ft.alignment.center,
        )

    def box_fixed(ctrl):
        return ft.Container(
            content=ctrl,
            width=target_w,
            height=target_h,
            padding=0,
            margin=0,
            alignment=ft.alignment.center,
        )

    controls_row = [
        box_auto(bloque_programas, left_w),
        box_fixed(carrusel_vertical),
    ]
    if w >= 1120:
        controls_row.append(box_fixed(video_cards[0]))
    if w >= 1500:
        controls_row.append(box_fixed(video_cards[1]))
    if w >= 1820:
        controls_row.append(box_fixed(video_cards[2]))
    if w >= 2140:
        controls_row.append(box_fixed(video_cards[3]))

    content_total_w = left_w + (target_w * media_count) + (18 * max(0, len(controls_row) - 1))

    contenido_programas = ft.Row(
        controls=controls_row,
        spacing=18,
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        wrap=False,
    )

    if w >= 1020:
        zona_multimedia.padding = ft.Padding.symmetric(horizontal=side_pad, vertical=14)
        zona_multimedia.content = ft.Container(
            width=section_w,
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[ft.Container(width=content_total_w, content=contenido_programas)],
                scroll=ft.ScrollMode.AUTO,
                spacing=0,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )
    else:
        zona_multimedia.padding = ft.Padding.symmetric(horizontal=side_pad, vertical=14)
        zona_multimedia.content = ft.Container(
            width=section_w,
            alignment=ft.alignment.center,
            content=contenido_programas,
        )

    safe_update(zona_multimedia)


def adjust_banner_pc(
    page: ft.Page,
    *,
    banner_pc: ft.Container,
    hero_text_block: ft.Column,
    titulo1: ft.Text,
    titulo2: ft.Text,
    desc_banner: ft.Text,
    logo_box: ft.Container,
    banner_img_box: ft.Container,
    form_card: ft.Container,
    form_card_host: ft.Column,
    ancho_form_min: int,
    ancho_form_max: int,
    safe_update,
):
    w = page.width or 1200

    t = clamp((w - 600) / (800 - 600), 0.0, 1.0)
    f_800_600 = 0.68 + 0.32 * t

    t1 = int(w * 0.035)
    t2 = int(w * 0.032)
    td = int(w * 0.015)
    logo = int(w * 0.10)

    if w < 1300:
        factor = clamp((w - 900) / (1300 - 900), 0.7, 1.0)
        t1 = int(t1 * factor)
        t2 = int(t2 * factor)
        td = int(td * factor)
        logo = int(logo * factor)

    if w < 800:
        t1 = int(t1 * f_800_600)
        t2 = int(t2 * f_800_600)
        td = int(td * f_800_600)
        logo = int(logo * f_800_600)

    if w < 800:
        t1 = clamp(t1, 18, 52)
        t2 = clamp(t2, 16, 48)
        td = clamp(td, 10, 20)
        logo = clamp(logo, 70, 140)
    elif w < 1020:
        t1 = clamp(int(w * 0.024), 18, 28)
        t2 = clamp(int(w * 0.021), 16, 24)
        td = clamp(int(w * 0.0105), 10, 13)
        logo = clamp(int(w * 0.075), 58, 82)
    else:
        t1 = clamp(t1, 22, 64)
        t2 = clamp(t2, 20, 58)
        td = clamp(td, 12, 28)
        logo = clamp(logo, 90, 200)

    titulo1.size = t1
    titulo2.size = t2
    desc_banner.size = td
    logo_box.width = logo
    logo_box.height = logo

    if w < 1020:
        img_w = clamp(int(w * 0.16), 125, 165)
    else:
        img_w = clamp(int(w * (0.18 if w < 1260 else 0.14)), 180 if w < 1260 else 150, 280 if w < 1260 else 250)
    base_h = int(w * 0.18)

    if w < 1600:
        tt = (1600 - w) / (1600 - 1200)
        factor_h = 1.0 + 0.30 * clamp(tt, 0, 1)
    else:
        factor_h = 1.0

    img_h = int(base_h * factor_h)

    if w < 800:
        img_h = int(img_h * (0.70 + 0.30 * t))

    if w < 1020:
        img_h = clamp(int(img_h * 0.76), 170, 235)
    else:
        img_h = clamp(img_h, 180 if w < 800 else 220, 420)

    banner_img_box.width = img_w
    banner_img_box.height = img_h

    if w < 800:
        form_w = int(220 + 60 * t)
        form_w = clamp(form_w, 210, 300)
        form_card.padding = 8 if w < 700 else 10
    elif w < 1020:
        form_w = clamp(int(w * 0.26), 220, 250)
        form_card.padding = 8
    elif w < 1260:
        form_w = clamp(int(w * 0.21), 245, 295)
        form_card.padding = 10
    else:
        form_w = clamp(int(w * 0.17), 250, 305)
        form_card.padding = 12

    if w < 1020:
        text_w = clamp(int(w * 0.40), 260, 360)
    elif w < 1260:
        text_w = clamp(int(w * 0.38), 360, 430)
    elif w < 1600:
        text_w = clamp(int(w * 0.42), 430, 560)
    else:
        text_w = clamp(int(w * 0.45), 520, 680)

    hero_text_block.width = text_w
    form_card.width = form_w
    form_card_host.width = form_card.width
    safe_update(banner_pc)
