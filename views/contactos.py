import flet as ft

def create_contactos_row(page: ft.Page) -> ft.Container:
    """
    Devuelve la fila de iconos de contacto con estilo adaptativo:
    - Mobile: texto negro y 'E-Mail'
    - Tablet/Desktop: texto blanco y correo completo
    - Tamaños de texto e iconos ligeramente mayores
    """

    # --- Datos de contacto ---
    numero_telefono = "+56999724454"
    enlace_llamada = f"tel:{numero_telefono}"
    enlace_correo = "mailto:operaciones@evermountsolutions.cl?subject=Consulta&body=Hola, quisiera más información"
    enlace_ubicacion = "https://maps.google.com/?q=EvermountSolutions+Chile"

    # --- Helper: clase de dispositivo ---
    def device_class() -> str:
        w = page.width or 0
        if w < 600:
            return "mobile"
        elif w < 1020:
            return "tablet"
        return "desktop"

    # --- Estilos base dinámicos ---
    cls = device_class()
    es_tablet_o_pc = cls in ("tablet", "desktop")
    color_texto = ft.Colors.WHITE if es_tablet_o_pc else ft.Colors.BLACK
    texto_mail = (
        "operaciones@evermountsolutions.cl" if es_tablet_o_pc else "E-Mail"
    )

    # 🔠 Tamaños más grandes
    size_text_mobile = 14
    size_text_tablet = 18
    size_text_pc = 16
    size_icon_mobile = 22
    size_icon_tablet = 30
    size_icon_pc = 26

    size_text = (
        size_text_mobile if cls == "mobile"
        else size_text_tablet if cls == "tablet"
        else size_text_pc
    )
    size_icon = (
        size_icon_mobile if cls == "mobile"
        else size_icon_tablet if cls == "tablet"
        else size_icon_pc
    )

    texto_style = dict(size=size_text, weight=ft.FontWeight.W_600, color=color_texto)

    # --- Acciones ---
    def abrir_llamada(e):
        page.launch_url(enlace_llamada)

    def abrir_correo(e):
        page.launch_url(enlace_correo)

    def abrir_maps(e):
        page.launch_url(enlace_ubicacion)

    # --- Textos dinámicos ---
    txt_tel = ft.Text(numero_telefono, **texto_style)
    txt_mail = ft.Text(texto_mail, **texto_style)
    txt_loc = ft.Text("Ubicación", **texto_style)

    # --- Fila de iconos con tamaño ajustado ---
    fila_iconos = ft.Row(
        [
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.PHONE, color=ft.Colors.BLUE, size=size_icon),
                        txt_tel,
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                ),
                on_click=abrir_llamada,
                ink=True,
                padding=2,
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREEN, size=size_icon),
                        txt_mail,
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                ),
                on_click=abrir_correo,
                ink=True,
                padding=2,
            ),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED, size=size_icon),
                        txt_loc,
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                ),
                on_click=abrir_maps,
                ink=True,
                padding=2,
            ),
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=15,
        key="fila_iconos",
    )

    # --- Función para actualizar dinámicamente color, texto y tamaños ---
    def _apply_style_adaptativo():
        cls_actual = device_class()
        es_tablet_pc_local = cls_actual in ("tablet", "desktop")
        color_local = ft.Colors.WHITE if es_tablet_pc_local else ft.Colors.BLACK
        txt_mail.value = (
            "operaciones@evermountsolutions.cl" if es_tablet_pc_local else "E-Mail"
        )

        # recalcular tamaños dinámicos
        size_text_local = (
            size_text_mobile if cls_actual == "mobile"
            else size_text_tablet if cls_actual == "tablet"
            else size_text_pc
        )
        size_icon_local = (
            size_icon_mobile if cls_actual == "mobile"
            else size_icon_tablet if cls_actual == "tablet"
            else size_icon_pc
        )

        for txt in [txt_tel, txt_mail, txt_loc]:
            txt.color = color_local
            txt.size = size_text_local

        # Actualizar íconos dentro de la fila
        for c in fila_iconos.controls:
            if isinstance(c, ft.Container) and isinstance(c.content, ft.Row):
                for item in c.content.controls:
                    if isinstance(item, ft.Icon):
                        item.size = size_icon_local

        fila_iconos.update()

    fila_iconos.data = {"apply_style_adaptativo": _apply_style_adaptativo}

    return fila_iconos
