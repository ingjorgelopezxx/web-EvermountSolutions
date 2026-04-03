import flet as ft


def create_dropdown_menu(menu_data, on_select, on_hover):
    menu_items = []
    for text, icon in menu_data:
        item = ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        width=30,
                        height=30,
                        border_radius=15,
                        bgcolor="#E5EEF2",
                        alignment=ft.alignment.center,
                        content=ft.Icon(icon, size=16, color="#123F49"),
                    ),
                    ft.Text(text, weight=ft.FontWeight.BOLD, color="#18343D"),
                    ft.Icon(ft.Icons.ARROW_OUTWARD, size=14, color="#6E8590"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=ft.Padding.symmetric(vertical=8, horizontal=12),
            bgcolor="#F8FBFC",
            border_radius=12,
            on_click=lambda e, t=text: on_select(t),
            ink=True,
        )
        menu_items.append(item)

    menu_column = ft.Column(controls=menu_items, spacing=8)

    dropdown = ft.Container(
        content=ft.Container(
            content=menu_column,
            bgcolor="rgba(255,255,255,0.98)",
            border_radius=20,
            border=ft.Border.all(1, "#DDE7EB"),
            padding=ft.Padding.all(10),
            shadow=ft.BoxShadow(blur_radius=22, spread_radius=0, color="rgba(15,32,39,0.18)", offset=ft.Offset(0, 10)),
            width=220,
            on_hover=on_hover,
        ),
        visible=False,
        top=52,
        right=10,
    )

    return menu_column, dropdown


def create_title_wrap():
    texto_titulo = ft.Stack(
        [
            ft.Text(
                "EvermountSolutions - Pest Defense",
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK_45,
                top=1,
                left=1,
            ),
            ft.Text(
                "EvermountSolutions - Pest Defense",
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
        ]
    )

    wrap_titulo = ft.Container(
        content=texto_titulo,
        expand=True,
        alignment=ft.alignment.center_left,
        visible=True,
    )
    return texto_titulo, wrap_titulo


def create_header(container_logo_empresa, wrap_titulo, slot_tabs_header, slot_iconos_header, container_boton_empresa):
    return ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#06151B", "#123743", "#275869"],
        ),
        border=ft.Border(bottom=ft.BorderSide(1, "rgba(255,255,255,0.08)")),
        shadow=ft.BoxShadow(blur_radius=18, spread_radius=0, color="rgba(4,18,24,0.20)", offset=ft.Offset(0, 4)),
        padding=ft.Padding.symmetric(horizontal=14, vertical=10),
        content=ft.Row(
            [
                container_logo_empresa,
                wrap_titulo,
                slot_tabs_header,
                slot_iconos_header,
                container_boton_empresa,
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def create_bottom_shell(button_controls: list[ft.Control]):
    promo_text = ft.Text(
        "Atención rápida | Insumos certificados | Respuesta inmediata | Técnicos especializados | Hogares y empresas",
        size=17,
        weight=ft.FontWeight.BOLD,
        color="#113842",
        no_wrap=True,
        text_align=ft.TextAlign.LEFT,
    )

    promo_flotante = ft.Container(
        content=promo_text,
        alignment=ft.alignment.center,
        padding=ft.Padding.only(left=10, right=10),
    )

    promo_items = [
        ("Atención rápida", ft.Icons.FLASH_ON),
        ("Insumos certificados", ft.Icons.VERIFIED),
        ("Respuesta inmediata", ft.Icons.SUPPORT_AGENT),
        ("Técnicos especializados", ft.Icons.HANDYMAN),
        ("Hogar y empresas", ft.Icons.HOME_WORK),
    ]
    promo_labels_text = " | ".join(label for label, _ in promo_items)

    promo_controls = []
    for idx, (label, icon_name) in enumerate(promo_items):
        promo_controls.append(
            ft.Row(
                [
                    ft.Icon(icon_name, size=18, color=ft.Colors.BLACK),
                    ft.Text(
                        label,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#113842",
                    ),
                ],
                spacing=6,
                tight=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        if idx < len(promo_items) - 1:
            promo_controls.append(
                ft.Text("|", size=18, weight=ft.FontWeight.BOLD, color="#7D97A1")
            )

    promo_text_row = ft.Row(
        promo_controls,
        spacing=10,
        tight=True,
        wrap=False,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    promo_flotante.content = promo_text_row

    promo_stack = ft.Stack(
        controls=[
            ft.Container(
                bgcolor="#ECF4F7",
                expand=True,
                border_radius=20,
            ),
            promo_flotante,
        ],
        height=46,
        expand=True,
        visible=False,
    )

    botones_agregar = ft.Row(
        button_controls,
        alignment=ft.MainAxisAlignment.END,
        vertical_alignment=ft.CrossAxisAlignment.END,
    )

    barra_inferior = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[promo_stack, botones_agregar],
    )

    zona_redes = ft.Container(
        content=barra_inferior,
        bgcolor="#F7FBFC",
        border=ft.Border(top=ft.BorderSide(1, "#DCE7EB")),
        padding=ft.Padding.symmetric(horizontal=14, vertical=10),
        alignment=ft.alignment.center,
    )

    return promo_items, promo_labels_text, promo_flotante, promo_stack, barra_inferior, zona_redes


def create_overlay(on_click):
    return ft.Container(
        left=0,
        top=0,
        right=0,
        bottom=0,
        bgcolor="rgba(0,0,0,0.001)",
        visible=False,
        on_click=on_click,
    )


def create_content_base(barra_superior, slot_contactos_bajo_header, contenido, zona_redes):
    return ft.Column(
        [
            barra_superior,
            slot_contactos_bajo_header,
            contenido,
            zona_redes,
        ],
        expand=True,
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


def create_root_stack(contenido_base, overlay_cierra_menu, dropdown, intro_modal):
    stack_raiz = ft.Stack(
        controls=[
            contenido_base,
            overlay_cierra_menu,
            dropdown,
        ],
        expand=True,
    )
    stack_raiz.controls.append(intro_modal)
    return stack_raiz
