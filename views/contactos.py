import flet as ft

def create_contactos_row(page: ft.Page) -> ft.Container:
    numero_telefono = "+56999724454"
    enlace_llamada = f"tel:{numero_telefono}"
    enlace_correo = "mailto:operaciones@evermountsolutions.cl?subject=Consulta&body=Hola, quisiera más información"
    enlace_ubicacion = "https://maps.google.com/?q=EvermountSolutions+Chile"

    def abrir_llamada(e): page.launch_url(enlace_llamada)
    def abrir_correo(e): page.launch_url(enlace_correo)
    def abrir_maps(e):   page.launch_url(enlace_ubicacion)

    # Textos (se actualizan en apply)
    txt_tel  = ft.Text(numero_telefono)
    txt_mail = ft.Text("E-Mail")
    txt_loc  = ft.Text("Ubicación")

    # Íconos (se actualizan en apply)
    ic_tel  = ft.Icon(ft.Icons.PHONE,        color=ft.Colors.BLUE)
    ic_mail = ft.Icon(ft.Icons.EMAIL,        color=ft.Colors.GREEN)
    ic_loc  = ft.Icon(ft.Icons.LOCATION_ON,  color=ft.Colors.RED)

    def item(icono, texto, on_click):
        return ft.Container(
            content=ft.Row(
                [icono, texto],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            ),
            on_click=on_click,
            ink=True,
            padding=2,  # se ajusta en apply
        )

    c_tel  = item(ic_tel,  txt_tel,  abrir_llamada)
    c_mail = item(ic_mail, txt_mail, abrir_correo)
    c_loc  = item(ic_loc,  txt_loc,  abrir_maps)

    fila_iconos = ft.Row(
        [c_tel, c_mail, c_loc],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=12,   # se ajusta en apply
        key="fila_iconos",
    )

    def _apply_style_adaptativo():
        w = page.width or 0

        es_movil = w < 600
        ultra = 600 <= w < 805        # ✅ “ultra compacto” SOLO para header/tablet angosto
        compact = w < 1300

        # tamaños base
        if es_movil:
            size_icon_local = 20
            size_text_local = 12
            fila_iconos.alignment = ft.MainAxisAlignment.CENTER
            fila_iconos.spacing = 10
        else:
            size_icon_local = 18 if compact else 26
            size_text_local = 13 if compact else 16
            fila_iconos.alignment = ft.MainAxisAlignment.END   # ✅ header derecha
            fila_iconos.spacing = 6 if ultra else 15

        # color texto según fondo
        # en tu app móvil normalmente fondo claro → negro
        # en header (>=600) fondo azul → blanco
        color_local = ft.Colors.BLACK if es_movil else ft.Colors.WHITE

        # mail corto en móvil/compact; largo en grande
        if es_movil or w < 900:
            txt_mail.value = "E-Mail"
        else:
            txt_mail.value = "operaciones@evermountsolutions.cl"

        # ✅ reglas de visibilidad:
        # - móvil <600: SIEMPRE textos
        # - ultra (600-780): SOLO iconos
        show_text = es_movil or (not ultra)

        txt_tel.visible = show_text
        txt_mail.visible = show_text
        txt_loc.visible = show_text

        for txt in [txt_tel, txt_mail, txt_loc]:
            txt.color = color_local
            txt.size = size_text_local

        # ajustar íconos + paddings internos
        for c in fila_iconos.controls:
            if isinstance(c, ft.Container) and isinstance(c.content, ft.Row):
                c.padding = 2 if es_movil else (1 if ultra else 2)
                c.content.spacing = 4 if es_movil else (2 if ultra else 4)
                for it in c.content.controls:
                    if isinstance(it, ft.Icon):
                        it.size = size_icon_local

        if getattr(fila_iconos, "page", None) is not None:
            fila_iconos.update()



    fila_iconos.data = {"apply_style_adaptativo": _apply_style_adaptativo}

    return fila_iconos
