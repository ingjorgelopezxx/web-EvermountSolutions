
import flet as ft

def build(page: ft.Page, ctx):
    # Delega al main para mostrar el carrusel y el contenido inicial
    ctx.show_inicio()
    # No devolvemos control porque ya actualizamos ctx.content desde el main
    return None
