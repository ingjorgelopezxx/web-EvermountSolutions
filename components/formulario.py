import flet as ft
import smtplib
from email.message import EmailMessage
import re
from email.header import Header
import asyncio

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "evermountsolutions@gmail.com"
EMAIL_PASS = "oiesfqyg afvluloa"
EMAIL_DESTINO = "operaciones@evermountsolutions.cl"

def validar_correo(email: str) -> bool:
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email) is not None

def create_formulario(page: ft.Page):

    # --- Overlay enviando ---
    enviando_overlay = ft.Container(
        visible=False,
        left=0, top=0, right=0, bottom=0,
        bgcolor="rgba(0,0,0,0.8)",  # semitransparente
        alignment=ft.alignment.center,
        content=ft.Container(
            width=300,
            height=200,
            border_radius=8,
            bgcolor=ft.Colors.BLACK87,
            padding=20,
            content=ft.Column(
                [
                    ft.ProgressRing(width=50, height=50, color=ft.Colors.WHITE),
                    ft.Text("Enviando información...", color=ft.Colors.WHITE, size=16)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        )
    )

    # --- Textos dinámicos del modal ---
    titulo_modal = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    mensaje_modal = ft.Text("", size=14, color=ft.Colors.WHITE)

    # --- Modal info ---
    modal_info = ft.Container(
        visible=False,
        bgcolor="rgba(0,0,0,0.8)",
        left=0, top=0, right=0, bottom=0,
        alignment=ft.alignment.center,
        content=ft.Container(
            width=300,
            height=200,
            border_radius=8,
            bgcolor=ft.Colors.BLACK87,
            padding=20,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e: cerrar_modal()
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                    titulo_modal,
                    mensaje_modal,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        )
    )

    def mostrar_modal(titulo: str, mensaje: str, color_titulo=ft.Colors.WHITE):
        titulo_modal.value = titulo
        titulo_modal.color = color_titulo
        mensaje_modal.value = mensaje
        modal_info.visible = True
        page.update()

    def cerrar_modal():
        modal_info.visible = False
        page.update()
        correo_tf.focus()

    ALTURA_CAMPOS = 56

    def on_warning_click(e):
        # 1) Forzar pérdida de foco cerrando el teclado
        correo_tf.disabled = True
        page.update()

        async def _restore():
            # dar un tick (o 50ms) y re-habilitar
            await asyncio.sleep(0.05)
            correo_tf.disabled = False
            # no re-enfocamos el campo para que el teclado NO vuelva
            page.update()

        page.run_task(_restore)

        # 2) Mostrar tu modal de aviso
        mostrar_modal(
            "Correo inválido",
            "Ingresa un correo con formato correcto (ejemplo: usuario@dominio.com).",
            ft.Colors.RED_400
        )

    # --- Icono alerta ---
    warning_icon = ft.IconButton(
        icon=ft.Icons.WARNING_AMBER_ROUNDED,
        icon_color=ft.Colors.RED,
        icon_size=20,               # tamaño del icono
        visible=False,
        tooltip="Correo electrónico inválido",
        style=ft.ButtonStyle(
            padding=ft.padding.all(0),            # 👈 sin padding interno
            shape=ft.RoundedRectangleBorder(radius=0)
        ),
        width=40, height=ALTURA_CAMPOS,        # 👈 alto y ancho fijo del botón
        on_click=on_warning_click,  # 👈 aquí
    )
    
    def ancho_responsivo():
        return page.width * 0.85

    def actualizar_estado_boton():
        campos_llenos = (
            (nombre.value or "").strip() != "" and
            (correo_tf.value or "").strip() != "" and
            (telefono.value or "").strip() != "" and
            (mensaje.value or "").strip() != ""
        )
        sin_alerta = not warning_icon.visible
        habilitar = campos_llenos and sin_alerta
        boton_enviar.disabled = not habilitar
        boton_con_gradiente.opacity = 1.0 if habilitar else 0.4
        boton_con_gradiente.update()
        boton_enviar.update()

    # --- Validaciones en vivo ---
    def on_mensaje_nombre_change(e):
        v = e.control.value or ""
        if v.startswith(" "):
            v = v.lstrip()
        while "  " in v:
            v = v.replace("  ", " ")
        if v != e.control.value:
            e.control.value = v
            e.control.update()
        actualizar_estado_boton()

    def solo_numeros_y_mas(e):
        v = (e.control.value or "")
        nuevo = re.sub(r"[^0-9+]", "", v)
        if nuevo != v:
            e.control.value = nuevo
            e.control.update()
        actualizar_estado_boton()

    def on_correo_change(e):
        v = (e.control.value or "")
        nuevo = v.replace(" ", "")
        if nuevo != v:
            e.control.value = nuevo
        warning_icon.visible = (nuevo != "" and not validar_correo(nuevo))
        e.control.update()
        warning_icon.update()
        actualizar_estado_boton()

    correo_tf = ft.TextField(
        label="Correo electrónico",
        color=ft.Colors.BLACK,
        width=ancho_responsivo(),
        height=ALTURA_CAMPOS,
        suffix=warning_icon,
        on_change=on_correo_change
    )

    nombre = ft.TextField(label="Nombre", width=ancho_responsivo(), height=ALTURA_CAMPOS,
                          color=ft.Colors.BLACK, on_change=on_mensaje_nombre_change)
    telefono = ft.TextField(label="Teléfono", width=ancho_responsivo(), height=ALTURA_CAMPOS,
                            color=ft.Colors.BLACK, on_change=solo_numeros_y_mas)
    mensaje = ft.TextField(label="Mensaje", multiline=True, min_lines=3,
                           width=ancho_responsivo(), color=ft.Colors.BLACK,
                           on_change=on_mensaje_nombre_change)

    status_text = ft.Text("", color=ft.Colors.GREEN)

    def ajustar_anchos(e=None):
        w = ancho_responsivo()
        nombre.width = w
        correo_tf.width = w
        telefono.width = w
        mensaje.width = w
        boton_enviar.width = w
        page.update()

    page.on_resize = ajustar_anchos

    async def proceso_envio():
        nombre_val = nombre.value.strip()
        correo_val = (correo_tf.value or "").strip()
        telefono_val = telefono.value.strip()
        mensaje_val = mensaje.value.strip()

        if not nombre_val or not correo_val or not mensaje_val:
            enviando_overlay.visible = False
            mostrar_modal(
            "Por favor completar todos los campos!",
            "asi se enviara la informacion correctamente",
            ft.Colors.RED_400
            )
            page.update()
            return

        if not validar_correo(correo_val):
            enviando_overlay.visible = False
            mostrar_modal(
            "Correo inválido",
            "Ingresa un correo con formato correcto (ejemplo: usuario@dominio.com).",
            ft.Colors.RED_400
            )
            page.update()
            return

        try:
            # enviar email en thread aparte
            def send_email():
                msg = EmailMessage()
                msg["Subject"] = str(Header(f"Nuevo mensaje de {nombre_val}", "utf-8"))
                msg["From"] = EMAIL_USER
                msg["To"] = EMAIL_DESTINO
                msg.set_content(
                    f"Nombre: {nombre_val}\n"
                    f"Correo: {correo_val}\n"
                    f"Teléfono: {telefono_val}\n\n"
                    f"Mensaje:\n{mensaje_val}",
                    charset="utf-8"
                )
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(EMAIL_USER, EMAIL_PASS)
                    server.send_message(msg)

            await asyncio.to_thread(send_email)

            # limpiar campos
            nombre.value = ""
            correo_tf.value = ""
            telefono.value = ""
            mensaje.value = ""
            enviando_overlay.visible = False
            actualizar_estado_boton()
            page.update()

            mostrar_modal(
                "¡Información enviada!",
                "Gracias por preferirnos. Nos pondremos en contacto pronto.",
                ft.Colors.BLUE
            )
        except Exception as ex:
            enviando_overlay.visible = False
            mostrar_modal(
            f"Error al enviar la información: {ex}",
            ft.Colors.RED_400
            )
            page.update()

    def enviar_formulario(e):
        enviando_overlay.visible = True
        page.update()
        # 👇 Correcto: pasar la función async sin ejecutarla
        page.run_task(proceso_envio)


    boton_enviar = ft.ElevatedButton(
        text="Enviar",
        disabled=True,
        color=ft.Colors.WHITE,
        bgcolor="transparent",
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
            overlay_color="rgba(255,255,255,0.1)",
            elevation=0,
            shape=ft.RoundedRectangleBorder(radius=8)
        ),
        on_click=enviar_formulario
    )

    boton_con_gradiente = ft.Container(
        content=boton_enviar,
        width=ancho_responsivo(),
        border_radius=8,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"]
        ),
        padding=0,
        opacity=0.4
    )

    formulario_con_modal = ft.Stack(
        [
            ft.Column(
                [
                    ft.Text("Contáctanos", size=28, weight=ft.FontWeight.BOLD, color="#090229"),
                    nombre,
                    correo_tf,
                    telefono,
                    mensaje,
                    boton_con_gradiente
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            modal_info,
            enviando_overlay
        ],
    )

    return formulario_con_modal
