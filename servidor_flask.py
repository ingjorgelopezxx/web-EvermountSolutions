import flet as ft
import os

def main(page: ft.Page):
    page.title = "Botón WhatsApp Flotante"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.window_resizable = True

    # Número de WhatsApp y mensaje
    numero_whatsapp = "56912345678"
    mensaje = "Hola, estoy interesado en tus productos"
    mensaje_encoded = mensaje.replace("Hola, deseo recibir mas informacion... ", "%20")
    url_whatsapp = f"https://wa.me/{+56937539304}?text={mensaje_encoded}"

    # URL del logo (formato PNG o SVG público)
    logo_url = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"

    # Imagen como botón con efectos
    imagen_logo = ft.Image(
        src=logo_url,
        width=60,
        height=60,
        fit=ft.ImageFit.CONTAIN,
        tooltip="Contáctanos por WhatsApp",
    )

    # Contenedor con estilo y efecto hover
    boton_contenedor = ft.Container(
        content=imagen_logo,
        alignment=ft.alignment.center,
        width=65,
        height=65,
        border_radius=100,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.BLACK26,
            offset=ft.Offset(2, 2),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        ),
        on_click=lambda _: page.launch_url(url_whatsapp),
        on_hover=lambda e: imagen_logo.scale.update(1.1 if e.data == "true" else 1.0),
        ink=True,
    )

    # Activar escala animada al pasar el mouse
    imagen_logo.scale = 1.0
    imagen_logo.animate_scale = 200

    # Botón flotante alineado abajo a la derecha
    boton_flotante = ft.Container(
        content=boton_contenedor,
        alignment=ft.alignment.bottom_right,
        padding=20,
        expand=True
    )

    # Agrega el botón como superposición
    page.overlay.append(boton_flotante)

    # Ejemplo de contenido de la página
    page.add(
        ft.Column([
            ft.Text("Página de ejemplo con botón flotante de WhatsApp", size=22),
            ft.Text("Puedes contactarnos fácilmente desde cualquier dispositivo."),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

# Ejecutar en navegador
ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))

