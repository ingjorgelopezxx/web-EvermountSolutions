import flet as ft
import re
import asyncio
import os
import requests
import inspect
from functions.resize_coordinator import register_resize_handler
# =========================
#  ENV (Render)
# =========================
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")
EMAIL_FROM = os.getenv("EMAIL_FROM")

RESEND_ENDPOINT = "https://api.resend.com/emails"


def validar_correo(email: str) -> bool:
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, email) is not None


def correo_parece_valido(email: str) -> bool:
    if " " in email or "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    local, dominio = partes
    if not local or not dominio or "." not in dominio:
        return False
    if dominio.startswith(".") or dominio.endswith("."):
        return False
    secciones = [s for s in dominio.split(".") if s]
    return len(secciones) >= 2


def validar_telefono(telefono: str) -> bool:
    limpio = re.sub(r"[^\d]", "", telefono)
    return 8 <= len(limpio) <= 15


def create_formulario(page: ft.Page):
    estado_boton = {"habilitado": True}
    form_root_ref = {"control": None}
    status_modal_ref = {"control": None}

    def safe_update(ctrl: ft.Control):
        try:
            if getattr(ctrl, "page", None) is not None:
                ctrl.update()
        except Exception:
            pass

    def safe_page_update():
        try:
            form_root = form_root_ref["control"]
            if getattr(form_root, "page", None) is not None:
                form_root.update()
            else:
                page.update()
        except Exception:
            pass

    def safe_status_update():
        try:
            status_modal_ctrl = status_modal_ref["control"]
            if getattr(status_modal_ctrl, "page", None) is not None:
                status_modal_ctrl.update()
            else:
                safe_page_update()
        except Exception:
            pass

    def focus_control(ctrl: ft.Control):
        try:
            result = ctrl.focus()
            if inspect.isawaitable(result):
                async def _focus():
                    await result
                page.run_task(_focus)
        except Exception:
            pass

    # --- Textos dinámicos del modal de estado ---
    titulo_modal = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
    mensaje_modal = ft.Text("", size=14, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
    status_ring = ft.ProgressRing(width=46, height=46, color=ft.Colors.WHITE, visible=False)
    close_status_btn = ft.IconButton(
        icon=ft.Icons.CLOSE,
        icon_color=ft.Colors.WHITE,
        visible=False,
        on_click=lambda e: cerrar_modal(),
    )

    # --- Modal único de estado ---
    status_modal = ft.Container(
        visible=False,
        bgcolor="rgba(0,0,0,0.8)",
        left=0, top=0, right=0, bottom=0,
        alignment=ft.alignment.center,
        content=ft.Container(
            width=320,
            border_radius=12,
            bgcolor=ft.Colors.BLACK_87,
            padding=22,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(expand=True),
                            close_status_btn,
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                    status_ring,
                    titulo_modal,
                    mensaje_modal,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
                tight=True,
            )
        )
    )

    def mostrar_estado(
        titulo: str,
        mensaje: str,
        *,
        color_titulo=ft.Colors.WHITE,
        loading: bool = False,
        closable: bool = True,
    ):
        titulo_modal.value = titulo
        titulo_modal.color = color_titulo
        mensaje_modal.value = mensaje
        status_ring.visible = loading
        close_status_btn.visible = closable and not loading
        status_modal.visible = True
        safe_status_update()

    def ocultar_estado():
        status_modal.visible = False
        safe_status_update()

    def set_loading(loading: bool, texto: str | None = None):
        estado_boton["habilitado"] = not loading
        boton_enviar.disabled = loading
        safe_update(boton_enviar)
        safe_update(boton_con_gradiente)
        if loading:
            mostrar_estado(
                "Validando información",
                texto or "Espera un momento mientras revisamos y preparamos tu solicitud.",
                loading=True,
                closable=False,
            )

    def cerrar_modal():
        ocultar_estado()
        focus_control(correo_tf)

    def limpiar_alertas():
        return
    
    # Ã¢Å“â€¦ Compacto solo cuando ancho < 700
    BREAKPOINT_COMPACT = 800

    def es_compacto():
        return (page.width or 0) < BREAKPOINT_COMPACT

    def es_tablet_hero():
        w = page.width or 0
        return 700 <= w < 1020

    def altura_campos_actual():
        if es_tablet_hero():
            return 48
        return 52 if es_compacto() else 68

    def titulo_size_actual():
        if es_tablet_hero():
            return 16
        return 22 if es_compacto() else 28

    def spacing_actual():
        if es_tablet_hero():
            return 4
        return 6 if es_compacto() else 10

    def min_lines_mensaje_actual():
        if es_tablet_hero():
            return 1
        return 2 if es_compacto() else 3

    def boton_text_size_actual():
        if es_tablet_hero():
            return 14
        return 16 if es_compacto() else 20

    def textfield_text_size_actual():
        if es_tablet_hero():
            return 13
        return 14 if es_compacto() else 16

    def label_size_actual():
        if es_tablet_hero():
            return 11
        return 11 if es_compacto() else 12

    def textfield_content_padding_actual():
        if es_tablet_hero():
            return ft.Padding.only(left=12, right=10, top=14, bottom=10)
        if es_compacto():
            return ft.Padding.only(left=12, right=10, top=15, bottom=11)
        return ft.Padding.only(left=14, right=12, top=18, bottom=14)


    ALTURA_CAMPOS = altura_campos_actual()

    MAX_FORM_WIDTH = 320
    MIN_FORM_WIDTH = 220

    def ancho_responsivo():
        w = page.width or 360  # fallback seguro si aún no existe
        # En desktop el formulario vive dentro de una tarjeta lateral,
        # así que no podemos dimensionarlo contra todo el viewport.
        if es_tablet_hero():
            return max(220, min(255, w * 0.23))
        if es_pc_o_tablet():
            return max(240, min(340, w * 0.24))
        return max(MIN_FORM_WIDTH, min(w * 0.92, MAX_FORM_WIDTH))


    def actualizar_estado_boton():
        estado_boton["habilitado"] = True
        boton_enviar.disabled = False
        safe_update(boton_enviar)
        safe_update(boton_con_gradiente)

    # --- Validaciones en vivo ---
    def on_mensaje_nombre_change(e):
        limpiar_alertas()
        actualizar_estado_boton()

    def solo_numeros_y_mas(e):
        limpiar_alertas()
        actualizar_estado_boton()

    def on_correo_change(e):
        v = (e.control.value or "")
        nuevo = v.replace(" ", "")
        if nuevo != v:
            e.control.value = nuevo
            safe_update(e.control)

        limpiar_alertas()
        actualizar_estado_boton()

    def on_correo_blur(e):
        actualizar_estado_boton()

    BREAKPOINT_TABLET = 700

    def es_pc_o_tablet():
        return (page.width or 0) >= BREAKPOINT_TABLET

    def label_color_actual():
        return ft.Colors.WHITE if es_pc_o_tablet() else "#E5EEF1"

    def padding_horizontal_actual():
        return 0 if es_pc_o_tablet() else 0

    async def _start_submit_flow():
        set_loading(True, "Validando información...")
        # Devolvemos el control al loop para que el modal se pinte
        # y recién luego arrancamos la validación/envío.
        await asyncio.sleep(0.03)
        page.run_task(proceso_envio)

    def enviar_formulario(e):
        if not estado_boton["habilitado"]:
            return
        boton_enviar.disabled = True
        estado_boton["habilitado"] = False
        safe_update(boton_enviar)
        safe_update(boton_con_gradiente)
        page.run_task(_start_submit_flow)

    boton_enviar_text = ft.Text(
        "Solicitar contacto",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
    )

    boton_enviar = ft.Button(
        content=boton_enviar_text,
        disabled=False,
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
        hint_text="Correo electrónico",
        hint_style=ft.TextStyle(color="#6B7F88", size=label_size_actual()),
        color=ft.Colors.BLACK,
        width=ancho_responsivo(),
        height=None,
        bgcolor=ft.Colors.WHITE,
        border_color="#D7E3E8",
        focused_border_color="#123F49",
        border_radius=14,
        text_vertical_align=ft.VerticalAlignment.CENTER,
        on_change=on_correo_change,
        on_blur=on_correo_blur
    )

    nombre_real = ft.TextField(
        hint_text="Nombre",
        hint_style=ft.TextStyle(color="#6B7F88", size=label_size_actual()),
        width=ancho_responsivo(),
        height=None,
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        border_color="#D7E3E8",
        focused_border_color="#123F49",
        border_radius=14,
        text_vertical_align=ft.VerticalAlignment.CENTER,
        on_change=on_mensaje_nombre_change
    )

    telefono_real = ft.TextField(
        hint_text="Teléfono",
        hint_style=ft.TextStyle(color="#6B7F88", size=label_size_actual()),
        width=ancho_responsivo(),
        height=None,
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        border_color="#D7E3E8",
        focused_border_color="#123F49",
        border_radius=14,
        text_vertical_align=ft.VerticalAlignment.CENTER,
        on_change=solo_numeros_y_mas
    )

    mensaje_real = ft.TextField(
        hint_text="Mensaje",
        hint_style=ft.TextStyle(color="#6B7F88", size=label_size_actual()),
        multiline=True,
        min_lines=min_lines_mensaje_actual(),
        width=ancho_responsivo(),
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        border_color="#D7E3E8",
        focused_border_color="#123F49",
        border_radius=16,
        on_change=on_mensaje_nombre_change
    )

    for tf in (nombre_real, correo_tf_real, telefono_real, mensaje_real):
        tf.text_size = textfield_text_size_actual()
        tf.content_padding = textfield_content_padding_actual()

    correo_tf = correo_tf_real

    def wrap_con_padding(tf, label_text: str):
        return ft.Container(
            content=tf,
            padding=ft.Padding.symmetric(horizontal=padding_horizontal_actual()),
            alignment=ft.alignment.center,
            data={},
        )

    nombre = wrap_con_padding(nombre_real, "Nombre")
    correo_w = wrap_con_padding(correo_tf_real, "Correo electrónico")
    telefono = wrap_con_padding(telefono_real, "Teléfono")
    mensaje = wrap_con_padding(mensaje_real, "Mensaje")

    boton_con_gradiente = ft.Container(
        content=boton_enviar,
        width=ancho_responsivo(),
        border_radius=8,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#0B222A", "#144857", "#1E6B7B"]
        ),
        opacity=1.0
    )

    boton_wrapper = ft.Container(
        content=boton_con_gradiente,
        padding=ft.Padding.symmetric(horizontal=padding_horizontal_actual()),
        margin=ft.Margin.only(top=0)
    )

    ESPACIO_BOTON_PC = 32

    def ajustar_responsivo(e=None):
        w = ancho_responsivo()

        # menos margen arriba del botón en compacto
        if es_tablet_hero():
            boton_wrapper.margin = ft.Margin.only(top=6)
        elif es_compacto():
            boton_wrapper.margin = ft.Margin.only(top=8)
        else:
            boton_wrapper.margin = ft.Margin.only(top=ESPACIO_BOTON_PC) if es_pc_o_tablet() else ft.Margin.only(top=0)

        for tf in (nombre_real, correo_tf_real, telefono_real, mensaje_real):
            tf.width = w

        # En campos simples dejamos que Flet calcule la altura real del label flotante.
        for tf in (nombre_real, correo_tf_real, telefono_real):
            tf.height = None

        # líneas del mensaje dinámicas
        mensaje_real.min_lines = min_lines_mensaje_actual()
        mensaje_real.max_lines = 2 if es_tablet_hero() else None

        # tamaño del texto del botón dinámico
        boton_enviar_text.size = boton_text_size_actual()

        boton_enviar.style = ft.ButtonStyle(
            text_style=ft.TextStyle(size=boton_text_size_actual(), weight=ft.FontWeight.BOLD),
            overlay_color="rgba(255,255,255,0.1)",
            elevation=0,
            shape=ft.RoundedRectangleBorder(radius=8)
        )

        lc = label_color_actual()
        ph = padding_horizontal_actual()

        for tf in (nombre_real, correo_tf_real, telefono_real, mensaje_real):
            tf.hint_style = ft.TextStyle(color="#6B7F88", size=label_size_actual())
            tf.text_size = textfield_text_size_actual()
            tf.content_padding = textfield_content_padding_actual()

        for cont in (nombre, correo_w, telefono, mensaje):
            cont.padding = ft.Padding.symmetric(horizontal=ph)

        boton_con_gradiente.width = w
        boton_con_gradiente.height = 34 if es_tablet_hero() else None
        boton_wrapper.padding = ft.Padding.symmetric(horizontal=ph)

        form_root = form_root_ref["control"]
        if getattr(form_root, "page", None) is not None:
            form_root.update()
        elif getattr(page, "session_id", None) is not None:
            page.update()

    register_resize_handler(page, "contact_form", ajustar_responsivo)

    # =========================
    #  SENDGRID - envío (API)
    # =========================
    def send_via_resend(subject: str, content: str):
        if not RESEND_API_KEY:
            raise RuntimeError("Falta RESEND_API_KEY en variables de entorno.")
        if not EMAIL_DESTINO:
            raise RuntimeError("Falta EMAIL_DESTINO en variables de entorno.")
        if not EMAIL_FROM:
            raise RuntimeError("Falta EMAIL_FROM en variables de entorno.")

        payload = {
            "from": f"Evermount Solutions <{EMAIL_FROM}>",
            "to": [EMAIL_DESTINO],
            "subject": subject,
            "text": content,
            "reply_to": EMAIL_FROM,
        }

        headers = {
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        }

        try:
            resp = requests.post(
                RESEND_ENDPOINT,
                json=payload,
                headers=headers,
                timeout=20,
            )

            print("Resend status:", resp.status_code)
            print("Resend body:", resp.text)

            if resp.status_code not in (200, 201):
                raise RuntimeError(f"Resend respondió {resp.status_code}: {resp.text}")

        except Exception as e:
            raise RuntimeError(f"Resend error: {e}")

    async def proceso_envio():
        nombre_val = (nombre_real.value or "").strip()
        correo_val = (correo_tf_real.value or "").strip()
        telefono_val = (telefono_real.value or "").strip()
        mensaje_val = (mensaje_real.value or "").strip()

        if not nombre_val or not correo_val or not telefono_val or not mensaje_val:
            set_loading(False)
            mostrar_estado(
                "Por favor completar todos los campos!",
                "Así se enviará la información correctamente.",
                color_titulo=ft.Colors.RED_400,
                loading=False,
                closable=True,
            )
            return

        if not validar_correo(correo_val):
            set_loading(False)
            focus_control(correo_tf_real)
            mostrar_estado(
                "Correo inválido",
                "Ingresa un correo con formato correcto (ejemplo: usuario@dominio.com).",
                color_titulo=ft.Colors.RED_400,
                loading=False,
                closable=True,
            )
            return

        if not validar_telefono(telefono_val):
            set_loading(False)
            focus_control(telefono_real)
            mostrar_estado(
                "Teléfono inválido",
                "Ingresa un teléfono con formato correcto (ejemplo: +56912345678).",
                color_titulo=ft.Colors.RED_400,
                loading=False,
                closable=True,
            )
            return

        try:
            mostrar_estado(
                "Enviando información",
                "Estamos enviando tu solicitud. Esto puede tardar unos segundos.",
                loading=True,
                closable=False,
            )

            subject = f"Nuevo mensaje de {nombre_val}"
            body = (
                f"Nombre: {nombre_val}\n"
                f"Correo: {correo_val}\n"
                f"Teléfono: {telefono_val}\n\n"
                f"Mensaje:\n{mensaje_val}"
            )

            # Logs útiles para Render (aparecen en Logs)
            print("Formulario recibido:", {"nombre": nombre_val, "correo": correo_val})
            print("Enviando con Resend...")
            await asyncio.to_thread(send_via_resend, subject, body)

            print("Enviado OK")

            # limpiar campos
            nombre_real.value = ""
            correo_tf_real.value = ""
            telefono_real.value = ""
            mensaje_real.value = ""

            set_loading(False)
            actualizar_estado_boton()
            mostrar_estado(
                "¡Información enviada!",
                "Gracias por preferirnos. Nos pondremos en contacto pronto.",
                color_titulo=ft.Colors.BLUE,
                loading=False,
                closable=True,
            )

        except Exception as ex:
            print("ERROR al enviar:", str(ex))
            set_loading(False)
            mostrar_estado(
                "Error al enviar la información",
                str(ex),
                color_titulo=ft.Colors.RED_400,
                loading=False,
                closable=True,
            )

    formulario_con_modal = ft.Container(
        alignment=ft.alignment.center,
        bgcolor="rgba(245,250,252,0.92)",
        border_radius=24,
        border=ft.Border.all(1, "#DCE7EB"),
        padding=ft.Padding.symmetric(horizontal=18, vertical=18),
        shadow=ft.BoxShadow(blur_radius=24, spread_radius=0, color="rgba(14,38,46,0.14)", offset=ft.Offset(0, 12)),
        content=ft.Column(
            tight=True,
            controls=[
                ft.Text(
                    "Cuéntanos tu necesidad y te responderemos con orientación técnica y una propuesta clara.",
                    size=13,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                nombre,
                correo_w,
                telefono,
                mensaje,
                boton_wrapper
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=spacing_actual()
        ),
    )

    form_root_ref["control"] = formulario_con_modal
    formulario_con_modal.data = {
        "status_modal": status_modal,
        "status_modal_ref": status_modal_ref,
    }
    status_modal_ref["control"] = status_modal

    return formulario_con_modal


