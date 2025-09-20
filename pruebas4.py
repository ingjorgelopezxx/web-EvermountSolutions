# vertical_video.py
import flet as ft
from flet_video import Video

def create_vertical_video_card():
    """Tarjeta vertical con vídeo en autoplay"""
    return ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        padding=10,
        width=300,
        height=500,  # 👈 altura explícita del contenedor
        content=Video(
            "https://youtube.com/shorts/3zwD8ZUUx8o?si=LrHwb6jGc-EYeRXl",  # 👈 MP4 directo
            autoplay=True,
            muted=True,     # 👈 necesario para autoplay en navegadores
            # loop=True,    # 👈 quitar porque no existe en flet-video 0.1.1
            width=280,      # 👈 ancho del video
            height=480,     # 👈 alto del video
            fit=ft.ImageFit.COVER  # 👈 usar enum, no string
        ),
    )
