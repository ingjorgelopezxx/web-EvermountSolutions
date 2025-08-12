# components/botones.py
import flet as ft
import asyncio

def create_boton_empresa(page: ft.Page, on_click_toggle):
    """
    Devuelve:
      container_boton_empresa, start_pulse, stop_pulse
    """
    imagen_boton_empresa = ft.Image(
        src= "https://i.postimg.cc/rFxRRS5D/logo-72x72.png", fit=ft.ImageFit.CONTAIN,
        scale=1.0, animate_scale=200, tooltip="Menú Empresa"
    )

    container_boton_empresa = ft.Container(
        content=ft.Container(
            content=imagen_boton_empresa,
            width=50,
            height=50,
            border_radius=25,
            bgcolor=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#ffffff", "#dcdcdc"],
            ),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=10,
                color=ft.Colors.BLACK38,
                offset=ft.Offset(3, 3),
            ),
            on_click=on_click_toggle,
            ink=True,
            alignment=ft.alignment.center,
        ),
        width=64,
        height=64,
        bgcolor=ft.Colors.BLACK12,
        border_radius=32,
        padding=7,
        scale=1.0,
        animate_scale=200,
    )

    async def _pulso():
        try:
            while True:
                container_boton_empresa.scale = 1.18
                container_boton_empresa.update()
                await asyncio.sleep(0.7)
                container_boton_empresa.scale = 1.0
                container_boton_empresa.update()
                await asyncio.sleep(0.7)
        except Exception:
            pass

    task_ref = [None]

    def start_pulse():
        if task_ref[0] is None:
            task_ref[0] = page.run_task(_pulso)
        return task_ref[0]

    def stop_pulse():
        if task_ref[0]:
            task_ref[0].cancel()
            task_ref[0] = None

    return container_boton_empresa, start_pulse, stop_pulse


def create_botones_redes(page: ft.Page, url_whatsapp: str, url_instagram: str, url_facebook: str, on_sabiasque_click=None ):
    """
    Devuelve:
      boton_facebook, boton_instagram, boton_whatsapp, start_bounce, stop_bounce
    (En ese orden para que puedas reusar tu Row)
    """
    img_whatsapp = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
        fit=ft.ImageFit.COVER,
        scale=1.0,
        animate_scale=200,
        tooltip="Contáctanos por WhatsApp",
    )
    img_instagram = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg",
        fit=ft.ImageFit.CONTAIN,
        scale=1.0,
        animate_scale=200,
        tooltip="Síguenos en Instagram",
    )
    img_facebook = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/b/b9/2023_Facebook_icon.svg",
        width=60,
        height=60,
        fit=ft.ImageFit.CONTAIN,
        scale=1.0,
        animate_scale=200,
        tooltip="Síguenos en Facebook",
    )
    img_sabiasque = ft.Image(
        src="https://i.postimg.cc/hj0qRQwn/white-Photoroom-1.jpg",
        fit=ft.ImageFit.CONTAIN,
        scale=1.0,
        animate_scale=200,
        tooltip="Sabías que...",
    )

    def _hover(img: ft.Image):
        def handler(e: ft.HoverEvent):
            img.scale = 1.1 if e.data == "true" else 1.0
            img.update()
        return handler

    boton_whatsapp = ft.Container(
        content=img_whatsapp,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        on_click=lambda _: page.launch_url(url_whatsapp),
        on_hover=_hover(img_whatsapp),
        ink=True,
    )
    boton_instagram = ft.Container(
        content=img_instagram,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        on_click=lambda _: page.launch_url(url_instagram),
        on_hover=_hover(img_instagram),
        ink=True,
    )
    boton_facebook = ft.Container(
        content=img_facebook,
        width=60,
        height=60,
        border_radius=30,
        bgcolor=None,
        shadow=None,
        on_click=lambda _: page.launch_url(url_facebook),
        on_hover=_hover(img_facebook),
        ink=False,
    )
    boton_sabiasque = ft.Container(
        content=img_sabiasque,
        width=60, height=60,
        border_radius=30,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(1, 8, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        on_click=on_sabiasque_click or (lambda _: None),  # <-- aquí
        on_hover=_hover(img_sabiasque),
        ink=True,
    )
    async def _bounce():
        try:
            imgs = [img_whatsapp, img_instagram, img_facebook,img_sabiasque]
            while True:
                for img in imgs:
                    img.scale = 1.2
                    img.update()
                    await asyncio.sleep(0.4)
                    img.scale = 1.0
                    img.update()
                    await asyncio.sleep(0.4)
        except Exception:
            pass

    task_ref = [None]

    def start_bounce():
        if task_ref[0] is None:
            task_ref[0] = page.run_task(_bounce)
        return task_ref[0]

    def stop_bounce():
        if task_ref[0]:
            task_ref[0].cancel()
            task_ref[0] = None

    # orden: facebook, instagram, whatsapp (para tu Row actual)
    return boton_facebook, boton_instagram, boton_whatsapp, boton_sabiasque, start_bounce, stop_bounce
