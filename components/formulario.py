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

    correo_tf = ft.TextField(
        label="Correo electrónico",
        color=ft.Colors.BLACK,
        width=ancho_responsivo(),
        height=ALTURA_CAMPOS,
        suffix=warning_icon
    )

    # --- Campos de texto ---
    nombre = ft.TextField(label="Nombre", width=ancho_responsivo(),height=ALTURA_CAMPOS, color=ft.Colors.BLACK)
    telefono = ft.TextField(label="Teléfono", width=ancho_responsivo(), height=ALTURA_CAMPOS,color=ft.Colors.BLACK)
    mensaje = ft.TextField(label="Mensaje", multiline=True, min_lines=3,
                           width=ancho_responsivo(), color=ft.Colors.BLACK)

    # 5) Validación en vivo que muestra/oculta el icono
    def validar_correo_en_tiempo_real(e):
        v = (correo_tf.value or "").strip()
        warning_icon.visible = (v != "" and not validar_correo(v))
        page.update()

    correo_tf.on_change = validar_correo_en_tiempo_real
    
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
        nombre_val = nombre.value.strip()
        correo_val = (correo_tf.value or "").strip()
        telefono_val = telefono.value.strip()
        mensaje_val = mensaje.value.strip()

        if not nombre_val or not correo_val or not mensaje_val:
            status_text.value = "Por favor completa todos los campos obligatorios."
            status_text.color = ft.Colors.RED
            page.update()
            return

        if not validar_correo(correo_val):
            status_text.value = "Por favor ingresa un correo electrónico válido."
            status_text.color = ft.Colors.RED
            page.update()
            return

        # --- Crear email ---
        try:
            msg = EmailMessage()
            # 👇 Forzar UTF-8 en el asunto
            msg["Subject"] = str(Header(f"Nuevo mensaje de {nombre_val}", "utf-8"))
            msg["From"] = EMAIL_USER
            msg["To"] = EMAIL_DESTINO

            # 👇 Forzar UTF-8 en el cuerpo
            msg.set_content(
                f"Nombre: {nombre_val}\n"
                f"Correo: {correo_val}\n"
                f"Teléfono: {telefono_val}\n\n"
                f"Mensaje:\n{mensaje_val}",
                charset="utf-8"
            )

            # --- Enviar ---
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASS)
                server.send_message(msg)

            # en lugar de status_text → mostrar modal
           
            nombre.value = ""
            correo_tf.value = ""
            telefono.value = ""
            mensaje.value = ""
            mostrar_modal(
                "¡Información enviada!",
                "Gracias por preferirnos. Nos pondremos en contacto pronto.",
                ft.Colors.BLUE
            )
        except Exception as ex:
            status_text.value = f"Error al enviar la información: {ex}"
            status_text.color = ft.Colors.RED

        page.update()

    # --- Botón enviar transparente con estilo ---
    boton_enviar = ft.ElevatedButton(
        text="Enviar",
        color=ft.Colors.WHITE,
        bgcolor="transparent",  # transparente para mostrar gradiente del container
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(
                size=20,
                weight=ft.FontWeight.BOLD,
            ),
            overlay_color="rgba(255,255,255,0.1)",  # color al presionar
            elevation=0,
            shape=ft.RoundedRectangleBorder(radius=8)
        ),
        on_click=enviar_formulario
    )

    # --- Contenedor con fondo degradado ---
    boton_con_gradiente = ft.Container(
        content=boton_enviar,
        width=ancho_responsivo(),
        border_radius=8,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"]  # 👈 tus colores degradado
        ),
        padding=0
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
        modal_info  # modal arriba
    ],
    )

    return formulario_con_modal
