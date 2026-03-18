import flet as ft

from functions.flet_actions import launch_url


def create_contactos_row(page: ft.Page) -> ft.Container:
    numero_telefono = "+56967578823"
    enlace_llamada = f"tel:{numero_telefono}"
    enlace_correo = "mailto:operaciones@evermountsolutions.cl?subject=Consulta&body=Hola, quisiera más información"
    enlace_ubicacion = "https://maps.google.com/?q=EvermountSolutions+Chile"

    def abrir_llamada(e):
        launch_url(page, enlace_llamada)

    def abrir_correo(e):
        launch_url(page, enlace_correo)

    def abrir_maps(e):
        launch_url(page, enlace_ubicacion)

    txt_tel = ft.Text(numero_telefono)
    txt_mail = ft.Text("E-Mail")
    txt_loc = ft.Text("Ubicación")

    ic_tel = ft.Icon(ft.Icons.PHONE, color=ft.Colors.BLUE)
    ic_mail = ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREEN)
    ic_loc = ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED)

    def item(icono, texto, on_click):
        return ft.Container(
            content=ft.Row(
                [icono, texto],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            ),
            on_click=on_click,
            ink=True,
            padding=2,
        )

    c_tel = item(ic_tel, txt_tel, abrir_llamada)
    c_mail = item(ic_mail, txt_mail, abrir_correo)
    c_loc = item(ic_loc, txt_loc, abrir_maps)

    fila_iconos = ft.Row(
        [c_tel, c_mail, c_loc],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=12,
        key="fila_iconos",
    )

    def _apply_style_adaptativo():
        w = page.width or 0

        es_movil = w < 600
        ultra = 600 <= w < 805
        compact = w < 1300

        if es_movil:
            size_icon_local = 20
            size_text_local = 12
            fila_iconos.alignment = ft.MainAxisAlignment.CENTER
            fila_iconos.spacing = 10
        else:
            size_icon_local = 18 if compact else 26
            size_text_local = 13 if compact else 16
            fila_iconos.alignment = ft.MainAxisAlignment.END
            fila_iconos.spacing = 6 if ultra else 15

        color_local = ft.Colors.BLACK if es_movil else ft.Colors.WHITE

        if es_movil or w < 900:
            txt_mail.value = "E-Mail"
        else:
            txt_mail.value = "operaciones@evermountsolutions.cl"

        show_text = es_movil or (not ultra)

        txt_tel.visible = show_text
        txt_mail.visible = show_text
        txt_loc.visible = show_text

        for txt in [txt_tel, txt_mail, txt_loc]:
            txt.color = color_local
            txt.size = size_text_local

        for c in fila_iconos.controls:
            if isinstance(c, ft.Container) and isinstance(c.content, ft.Row):
                c.padding = 2 if es_movil else (1 if ultra else 2)
                c.content.spacing = 4 if es_movil else (2 if ultra else 4)
                for it in c.content.controls:
                    if isinstance(it, ft.Icon):
                        it.size = size_icon_local

        try:
            _ = fila_iconos.page
        except Exception:
            return

        fila_iconos.update()

    fila_iconos.data = {"apply_style_adaptativo": _apply_style_adaptativo}

    return fila_iconos
