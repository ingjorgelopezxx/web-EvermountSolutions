import flet as ft
import smtplib
from email.message import EmailMessage
import re
from email.header import Header
import asyncio

# --- CONFIGURA AQUÍ TU CORREO ---
SMTP_SERVER = "smtp.gmail.com"      # Servidor SMTP (Gmail)
SMTP_PORT = 587                     # Puerto TLS para Gmail
EMAIL_USER = "evermountsolutions@gmail.com"   # Cambia por tu correo remitente
EMAIL_PASS = "oiesfqyg afvluloa"  # Cambia por tu contraseña o App Password Gmail
EMAIL_DESTINO = "operaciones@evermountsolutions.cl"  # Cambia por el correo de destino



# --- Validar correo electrónico ---
def validar_correo(email: str) -> bool:
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(patron, email) is not None

def create_formulario(page: ft.Page):
    """
    Crea un formulario con campos:
    Nombre, Correo electrónico, Teléfono, Mensaje y un botón Enviar.
    Al presionar Enviar, envía un correo electrónico con la información.
    """
    enviando_overlay = ft.Container(
        visible=False,
        left=0, top=0, right=0, bottom=0,
        bgcolor="rgba(0,0,0,0.5)",  # semitransparente
        alignment=ft.alignment.center,
        content=ft.Column(
            [
                ft.ProgressRing(width=50, height=50, color=ft.Colors.WHITE),
                ft.Text("Enviando información...", color=ft.Colors.WHITE, size=16)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

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

        # 👇 cambiar opacidad del container gradiente
        boton_con_gradiente.opacity = 1.0 if habilitar else 0.4

        boton_con_gradiente.update()
        boton_enviar.update()


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

     # --- Textos dinámicos del modal ---
    titulo_modal = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    mensaje_modal = ft.Text("", size=14, color=ft.Colors.WHITE)
    # --- Modal de éxito ---
    modal_info = ft.Container(
        visible=False,
        bgcolor="rgba(0,0,0,0.8)",  # fondo semitransparente
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
                    ft.Row(  # fila con la X a la derecha
                        [
                            ft.Container(),  # espacio a la izquierda
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

    # --- función para calcular ancho dinámico ---
    def ancho_responsivo():
        return page.width * 0.85  # 👈 15% menos que el ancho de pantalla
    
    ALTURA_CAMPOS = 56  # altura estándar de TextField

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
    def on_mensaje_nombre_change(e):
        v = e.control.value or ""

        # 1) Eliminar espacios al inicio
        if v.startswith(" "):
            v = v.lstrip()

        # 2) Reemplazar espacios dobles o más por un solo espacio
        while "  " in v:
            v = v.replace("  ", " ")

        # 3) Actualizar el campo si cambió
        if v != e.control.value:
            e.control.value = v
            e.control.update()

        # (opcional) actualizar estado del botón
        actualizar_estado_boton()

    def solo_numeros_y_mas(e):
        v = (e.control.value or "")
        # ^ Filtra todo lo que NO sea dígito o +
        nuevo = re.sub(r"[^0-9+]", "", v)
        if nuevo != v:
            e.control.value = nuevo
            e.control.update()
        actualizar_estado_boton()

    def on_correo_change(e):
        # 1) Quitar espacios
        v = (e.control.value or "")
        nuevo = v.replace(" ", "")
        if nuevo != v:
            e.control.value = nuevo

        # 2) Validar correo y mostrar/ocultar icono
        warning_icon.visible = (nuevo != "" and not validar_correo(nuevo))

        # 3) Actualizar solo ese control e icono
        e.control.update()
        warning_icon.update()

        # 4) Actualizar estado del botón
        actualizar_estado_boton()
    
    correo_tf = ft.TextField(
        label="Correo electrónico",
        color=ft.Colors.BLACK,
        width=ancho_responsivo(),
        height=ALTURA_CAMPOS,
        suffix=warning_icon,
        on_change=on_correo_change  
    )
  
    # --- Campos de texto ---
    nombre = ft.TextField(label="Nombre", width=ancho_responsivo(),height=ALTURA_CAMPOS, color=ft.Colors.BLACK,on_change=on_mensaje_nombre_change)
    telefono = ft.TextField(label="Teléfono", width=ancho_responsivo(), height=ALTURA_CAMPOS,color=ft.Colors.BLACK,on_change=solo_numeros_y_mas)
    mensaje = ft.TextField(label="Mensaje", multiline=True, min_lines=3,
                           width=ancho_responsivo(), color=ft.Colors.BLACK,on_change=on_mensaje_nombre_change)
    
    status_text = ft.Text("", color=ft.Colors.GREEN)

    # --- Ajustar anchos al redimensionar ---
    def ajustar_anchos(e=None):
        w = ancho_responsivo()
        nombre.width = w
        correo_tf.width = w
        telefono.width = w
        mensaje.width = w
        boton_enviar.width = w
        page.update()

    page.on_resize = ajustar_anchos  # se dispara cuando cambia tamaño pantalla

    # --- Función de envío ---
    def enviar_formulario(e):
        # Mostrar overlay de envío
        enviando_overlay.visible = True
        page.update()

        async def proceso_envio():
            nombre_val = nombre.value.strip()
            correo_val = (correo_tf.value or "").strip()
            telefono_val = telefono.value.strip()
            mensaje_val = mensaje.value.strip()

            if not nombre_val or not correo_val or not mensaje_val:
                enviando_overlay.visible = False
                status_text.value = "Por favor completa todos los campos obligatorios."
                status_text.color = ft.Colors.RED
                page.update()
                return

            if not validar_correo(correo_val):
                enviando_overlay.visible = False
                status_text.value = "Por favor ingresa un correo electrónico válido."
                status_text.color = ft.Colors.RED
                page.update()
                return

            try:
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

                # --- Enviar (bloqueante) ---
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(EMAIL_USER, EMAIL_PASS)
                    server.send_message(msg)

                # Limpiar campos
                nombre.value = ""
                correo_tf.value = ""
                telefono.value = ""
                mensaje.value = ""

                # Ocultar overlay de envío
                enviando_overlay.visible = False
                page.update()

                # Mostrar modal de éxito
                mostrar_modal(
                    "¡Información enviada!",
                    "Gracias por preferirnos. Nos pondremos en contacto pronto.",
                    ft.Colors.BLUE
                )
            except Exception as ex:
                enviando_overlay.visible = False
                status_text.value = f"Error al enviar la información: {ex}"
                status_text.color = ft.Colors.RED
                page.update()

        page.run_task(proceso_envio())


    # --- Botón enviar transparente con estilo ---
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
        opacity=0.4  # 👈 arranca opaco porque disabled=True
    )

    # --- Columna del formulario ---
    formulario_con_modal = ft.Stack(
    [
        ft.Column(  # formulario normal
            [
                ft.Text("Contáctanos", size=28, weight=ft.FontWeight.BOLD, color="#090229"),
                nombre,
                correo_tf,
                telefono,
                mensaje,
                boton_con_gradiente,
                status_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        modal_info,  # modal arriba
        enviando_overlay  # overlay de “enviando…”
    ],
    )
    return formulario_con_modal
