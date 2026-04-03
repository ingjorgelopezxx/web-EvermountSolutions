import asyncio

import flet as ft


def create_navigation(page: ft.Page, contenido: ft.Column, scroll_keys: dict[str, ft.ScrollKey]):
    async def _push_route_async(route: str):
        await page.push_route(route)

    def push_route(route: str):
        page.run_task(_push_route_async, route)

    async def _scroll_to_async(scroll_key_name: str, duration: int = 0):
        if (page.route or "/") != "/":
            await page.push_route("/")
            await asyncio.sleep(0.08)

        for wait_time, target_duration in ((0.0, duration), (0.08, 0), (0.18, 0), (0.32, 0)):
            if wait_time:
                await asyncio.sleep(wait_time)
            try:
                await contenido.scroll_to(
                    scroll_key=scroll_keys[scroll_key_name],
                    duration=target_duration,
                )
                return
            except RuntimeError:
                continue
            except Exception:
                break

    def scroll_to_key(scroll_key: str, duration: int = 0):
        page.run_task(_scroll_to_async, scroll_key, duration)

    async def _scroll_content_top_async():
        for wait_time in (0.0, 0.12, 0.28):
            if wait_time:
                await asyncio.sleep(wait_time)
            try:
                await contenido.scroll_to(offset=0, duration=0)
                return
            except RuntimeError:
                continue
            except Exception:
                break

    def scroll_content_top():
        page.run_task(_scroll_content_top_async)

    return push_route, scroll_to_key, scroll_content_top
