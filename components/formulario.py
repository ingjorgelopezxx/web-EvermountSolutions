import flet as ft
import re
import asyncio
import os
import json
import urllib.request
from email.header import Header

# =========================
#  ENV (Render)
# =========================
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO", "operaciones@evermountsolutions.cl")
EMAIL_FROM = os.getenv("EMAIL_FROM", "evermountsolutions@gmail.com")  # puede ser tu gmail mientras completas verificación/dominio

SENDGRID_ENDPOINT = "https://api.sendgrid.com/v3/mail/send"


def validar_correo(email: str) -> bool:
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email) is not None


def create_formulario(page: ft.Page):
    def safe_update(ctrl: ft.Control):
        if getattr(ctrl, "page", None) is not None:
            ctrl.update()

    # --- Overlay enviando ---
    enviando_overlay = ft.Container(
        visible=False,
        left=0, top=0, right=0, bottom=0,
        bgcolor="rgba(0,0,0,0.8)",
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
        if getattr(correo_tf, "page", None) is not None:
            try:
                correo_tf.focus()
            except Exception:
                pass
        if getattr(page, "session_id", None) is not None:
            page.update()

    ALTURA_CAMPOS = 56

    def on_warning_click(e):
        correo_tf.disabled = True
        page.update()

        async def _restore():
            await asyncio.sleep(0.05)
            correo_tf.disabled = False
            page.update()

        page.run_task(_restore)

        mostrar_modal(
            "Correo inválido",
            "Ingresa un correo con formato correcto (ejemplo: usuario@dominio.com).",
            ft.Colors.RED_400
        )

    warning_icon = ft.IconButton(
        icon=ft.Icons.WARNING_AMBER_ROUNDED,
        icon_color=ft.Colors.RED,
        icon_size=20,
        visible=False,
        tooltip="Correo electrónico inválido",
        style=ft.ButtonStyle(
            padding=ft.padding.all(0),
            shape=ft.RoundedRectangleBorder(radius=0)
        ),
        width=40, height=ALTURA_CAMPOS,
        on_click=on_warning_click,
    )

    def ancho_responsivo():
        return page.width * 0.85

    def actualizar_estado_boton():
        campos_llenos = (
            (nombre_real.value or "").strip() != "" and
            (correo_tf_real.value or "").strip() != "" and
            (telefono_real.value or "").strip() != "" and
            (mensaje_real.value or "").strip() != ""
        )
        sin_alerta = not warning_icon.visible
        habilitar = campos_llenos and sin_alerta

        boton_enviar.disabled = not habilitar
        boton_con_gradiente.opacity = 1.0 if habilitar else 0.4

        safe_update(boton_con_gradiente)
        safe_update(boton_enviar)

    # --- Validaciones en vivo ---
    def on_mensaje_nombre_change(e):
        v = e.control.value or ""
        if v.startswith(" "):
            v = v.lstrip()
        while "  " in v:
            v = v.replace("  ", " ")
        if v != e.control.value:
            e.control.value = v
            safe_update(e.control)
        actualizar_estado_boton()

    def solo_numeros_y_mas(e):
        v = (e.control.value or "")
        nuevo = re.sub(r"[^0-9+]", "", v)
        if nuevo != v:
            e.control.value = nuevo
            safe_update(e.control)
        actualizar_estado_boton()

    def on_correo_change(e):
        v = (e.control.value or "")
        nuevo = v.replace(" ", "")
        if nuevo != v:
            e.control.value = nuevo

        warning_icon.visible = (nuevo != "" and not validar_correo(nuevo))
        safe_update(e.control)
        safe_update(warning_icon)
        actualizar_estado_boton()

    BREAKPOINT_TABLET = 700

    def es_pc_o_tablet():
        return (page.width or 0) >= BREAKPOINT_TABLET

    def label_color_actual():
        return ft.Colors.BLACK if es_pc_o_tablet() else ft.Colors.BLACK54

    def padding_horizontal_actual():
        return 20 if es_pc_o_tablet() else 0

    def enviar_formulario(e):
        enviando_overlay.visible = True
        page.update()
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

    correo_tf_real = ft.TextField(
        label="Correo electrónico",
        label_style=ft.TextStyle(color=label_color_actual()),
        color=ft.Colors.BLACK,
        width=ancho_responsivo(),
        height=ALTURA_CAMPOS,
        suffix=warning_icon,
        on_change=on_correo_change
    )

    nombre_real = ft.TextField(
        label="Nombre",
        label_style=ft.TextStyle(color=label_color_actual()),
        width=ancho_responsivo(),
        height=ALTURA_CAMPOS,
        color=ft.Colors.BLACK,
        on_change=on_mensaje_nombre_change
    )

    telefono_real = ft.TextField(
        label="Teléfono",
        label_style=ft.TextStyle(color=label_color_actual()),
        width=ancho_responsivo(),
        height=ALTURA_CAMPOS,
        color=ft.Colors.BLACK,
        on_change=solo_numeros_y_mas
    )

    mensaje_real = ft.TextField(
        label="Mensaje",
        label_style=ft.TextStyle(color=label_color_actual()),
        multiline=True,
        min_lines=3,
        width=ancho_responsivo(),
        color=ft.Colors.BLACK,
        on_change=on_mensaje_nombre_change
    )

    correo_tf = correo_tf_real

    def wrap_con_padding(tf):
        return ft.Container(
            content=tf,
            padding=ft.padding.symmetric(horizontal=padding_horizontal_actual()),
            alignment=ft.alignment.center,
        )

    nombre = wrap_con_padding(nombre_real)
    correo_w = wrap_con_padding(correo_tf_real)
    telefono = wrap_con_padding(telefono_real)
    mensaje = wrap_con_padding(mensaje_real)

    boton_con_gradiente = ft.Container(
        content=boton_enviar,
        width=ancho_responsivo(),
        border_radius=8,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#0f2027", "#203a43", "#2c5364"]
        ),
        opacity=0.4
    )

    boton_wrapper = ft.Container(
        content=boton_con_gradiente,
        padding=ft.padding.symmetric(horizontal=padding_horizontal_actual()),
        margin=ft.margin.only(top=0)
    )

    ESPACIO_BOTON_PC = 32

    def ajustar_responsivo(e=None):
        w = ancho_responsivo()

        boton_wrapper.margin = ft.margin.only(top=ESPACIO_BOTON_PC) if es_pc_o_tablet() else ft.margin.only(top=0)

        for tf in (nombre_real, correo_tf_real, telefono_real, mensaje_real):
            tf.width = w

        lc = label_color_actual()
        ph = padding_horizontal_actual()

        for tf in (nombre_real, correo_tf_real, telefono_real, mensaje_real):
            tf.label_style = ft.TextStyle(color=lc)

        for cont in (nombre, correo_w, telefono, mensaje):
            cont.padding = ft.padding.symmetric(horizontal=ph)

        boton_con_gradiente.width = w
        boton_wrapper.padding = ft.padding.symmetric(horizontal=ph)

        page.update()

    ajustar_responsivo()

    prev_on_resized = page.on_resized

    def _chain_resized(e):
        try:
            if prev_on_resized:
                prev_on_resized(e)
        except Exception:
            pass
        ajustar_responsivo(e)

    page.on_resized = _chain_resized

    # =========================
    #  SENDGRID - envío (API)
    # =========================
    def send_via_sendgrid(subject: str, content: str):
        if not SENDGRID_API_KEY:
            raise RuntimeError("Falta SENDGRID_API_KEY en variables de entorno (Render).")
        if not EMAIL_DESTINO:
            raise RuntimeError("Falta EMAIL_DESTINO en variables de entorno (Render).")
        if not EMAIL_FROM:
            raise RuntimeError("Falta EMAIL_FROM en variables de entorno (Render).")

        payload = {
            "personalizations": [{"to": [{"email": EMAIL_DESTINO}]}],
            "from": {"email": EMAIL_FROM, "name": "Evermount Solutions"},
            "subject": subject,
            "content": [{"type": "text/plain", "value": content}],
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            SENDGRID_ENDPOINT,
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {SENDGRID_API_KEY}",
                "Content-Type": "application/json",
            },
        )

        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                # SendGrid normalmente responde 202 Accepted
                status = resp.status
        except Exception as e:
            raise RuntimeError(f"SendGrid error: {e}")

        if status not in (200, 202):
            raise RuntimeError(f"SendGrid respondió status {status}")

    async def proceso_envio():
        nombre_val = (nombre_real.value or "").strip()
        correo_val = (correo_tf_real.value or "").strip()
        telefono_val = (telefono_real.value or "").strip()
        mensaje_val = (mensaje_real.value or "").strip()

        # ✅ requerimos todos, porque tu botón también lo exige
        if not nombre_val or not correo_val or not telefono_val or not mensaje_val:
            enviando_overlay.visible = False
            mostrar_modal(
                "Por favor completar todos los campos!",
                "Así se enviará la información correctamente.",
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
            subject = str(Header(f"Nuevo mensaje de {nombre_val}", "utf-8"))
            body = (
                f"Nombre: {nombre_val}\n"
                f"Correo: {correo_val}\n"
                f"Teléfono: {telefono_val}\n\n"
                f"Mensaje:\n{mensaje_val}"
            )

            # Logs útiles para Render (aparecen en Logs)
            print("📩 Formulario recibido:", {"nombre": nombre_val, "correo": correo_val})
            print("✉️ Enviando con SendGrid...")

            await asyncio.to_thread(send_via_sendgrid, subject, body)

            print("✅ Enviado OK")

            # limpiar campos
            nombre_real.value = ""
            correo_tf_real.value = ""
            telefono_real.value = ""
            mensaje_real.value = ""

            enviando_overlay.visible = False
            actualizar_estado_boton()
            page.update()

            mostrar_modal(
                "¡Información enviada!",
                "Gracias por preferirnos. Nos pondremos en contacto pronto.",
                ft.Colors.BLUE
            )

        except Exception as ex:
            print("🔥 ERROR al enviar:", str(ex))
            enviando_overlay.visible = False
            mostrar_modal(
                "Error al enviar la información",
                str(ex),
                ft.Colors.RED_400
            )
            page.update()

    formulario_con_modal = ft.Stack(
        [
            ft.Column(
                [
                    ft.Text("Contáctanos", size=28, weight=ft.FontWeight.BOLD, color="#090229"),
                    nombre,
                    correo_w,
                    telefono,
                    mensaje,
                    boton_wrapper
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            modal_info,
            enviando_overlay
        ],
        alignment=ft.alignment.center,
    )

    return formulario_con_modal
