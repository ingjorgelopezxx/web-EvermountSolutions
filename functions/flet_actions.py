def launch_url(page, url: str) -> None:
    async def _launch():
        from flet.controls.services.url_launcher import UrlLauncher

        launcher = UrlLauncher()
        await launcher.launch_url(url)

    page.run_task(_launch)
