import flet as ft

def main(page: ft.Page):
    page.title = "YouTube Video"
    page.scroll = "auto"

    youtube_webview = ft.WebView(
        url="https://www.youtube.com/embed/Q3Vb_DeChDM?autoplay=1&mute=1",
        expand=True
    )

    video_card = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        shadow=ft.BoxShadow(1, 4, ft.Colors.BLACK26, offset=ft.Offset(2, 2)),
        padding=10,
        width=300,
        height=500,
        content=youtube_webview
    )

    page.add(ft.Row([video_card], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main, view=ft.WEB_BROWSER)
