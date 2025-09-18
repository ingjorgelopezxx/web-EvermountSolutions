import flet as ft
import smtplib
from email.message import EmailMessage
import re
from email.header import Header

# --- CONFIGURA AQUÍ TU CORREO ---
SMTP_SERVER = "smtp.gmail.com"      # Servidor SMTP (Gmail)
SMTP_PORT = 587                     # Puerto TLS para Gmail
EMAIL_USER = "evermountsolutions@gmail.com"   # Cambia por tu correo remitente
EMAIL_PASS = "oiesfqyg afvluloa"  # Cambia por tu contraseña o App Password Gmail
EMAIL_DESTINO = "Operaciones@evermountsolutions.cl"  # Cambia por el correo de destino

def create_formulario(page: ft.Page):
    """
    Crea un formulario con campos:
    Nombre, Correo electrónico, Teléfono, Mensaje y un botón Enviar.
    Al presionar Enviar, envía un correo electrónico con la información.
    """

    # --- Validar correo electrónico ---
    def validar_correo(email: str) -> bool:
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(patron, email) is not None

    status_text = ft.Text("", color=ft.Colors.GREEN)

    # --- función para calcular ancho dinámico ---
    def ancho_responsivo():
        return page.width * 0.85  # 👈 15% menos que el ancho de pantalla

    # --- Campos de texto ---
    nombre = ft.TextField(label="Nombre", width=ancho_responsivo(), color=ft.Colors.BLACK)
    correo = ft.TextField(label="Correo electrónico", width=ancho_responsivo(), color=ft.Colors.BLACK)
    telefono = ft.TextField(label="Teléfono", width=ancho_responsivo(), color=ft.Colors.BLACK)
    mensaje = ft.TextField(label="Mensaje", multiline=True, min_lines=3,
                           width=ancho_responsivo(), color=ft.Colors.BLACK)

    # --- Ajustar anchos al redimensionar ---
    def ajustar_anchos(e=None):
        w = ancho_responsivo()
        nombre.width = w
        correo.width = w
        telefono.width = w
        mensaje.width = w
        boton_enviar.width = w
        page.update()

    page.on_resize = ajustar_anchos  # se dispara cuando cambia tamaño pantalla

    # --- Función de envío ---
    def enviar_formulario(e):
        nombre_val = nombre.value.strip()
        correo_val = correo.value.strip()
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

            status_text.value = "¡Formulario enviado correctamente!"
            status_text.color = ft.Colors.GREEN
            nombre.value = ""
            correo.value = ""
            telefono.value = ""
            mensaje.value = ""

        except Exception as ex:
            status_text.value = f"Error al enviar el formulario: {ex}"
            status_text.color = ft.Colors.RED

        page.update()

    # --- Botón Enviar ---
    boton_enviar = ft.ElevatedButton(
        text="Enviar",
        width=ancho_responsivo(),
        on_click=enviar_formulario,
        bgcolor="#090229",
        color=ft.Colors.WHITE
    )

    # --- Columna del formulario ---
    formulario = ft.Column(
        [
            ft.Text("Contáctanos", size=20, weight=ft.FontWeight.BOLD, color="#090229"),  # Azul oscuro
            nombre,
            correo,
            telefono,
            mensaje,
            boton_enviar,
            status_text
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    return formulario
