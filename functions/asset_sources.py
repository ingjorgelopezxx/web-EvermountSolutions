from pathlib import Path


ASSETS_ROOT = Path(__file__).resolve().parent.parent / "assets"


def asset_or_remote(local_relative_path: str, remote_url: str) -> str:
    local_path = ASSETS_ROOT / local_relative_path
    if local_path.exists():
        return local_relative_path.replace("\\", "/")
    return remote_url


HOME_HERO_LOGO = asset_or_remote(
    "brand/logo-72x72.png",
    "https://i.postimg.cc/GhQhHVCX/logo-empresa-Photoroom.png",
)
HOME_HERO_BADGE_LOGO = asset_or_remote(
    "brand/logo-round.jpg",
    "https://i.postimg.cc/sDPWTSk5/lll.jpg",
)
HOME_HERO_IMAGE = asset_or_remote(
    "home/hero-banner.png",
    "https://i.postimg.cc/htB3zLB6/Imagen7.png",
)
INTRO_LOGO = asset_or_remote(
    "brand/logo-mobile-dark.png",
    "https://i.postimg.cc/8PvSgg5x/logo-mobile-dark.png",
)

SOCIAL_WHATSAPP = asset_or_remote(
    "icons/whatsapp.svg",
    "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
)
SOCIAL_INSTAGRAM = asset_or_remote(
    "icons/instagram.svg",
    "https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg",
)
SOCIAL_FACEBOOK = asset_or_remote(
    "icons/facebook.svg",
    "https://upload.wikimedia.org/wikipedia/commons/b/b9/2023_Facebook_icon.svg",
)
SOCIAL_SABIAS = asset_or_remote(
    "icons/sabias-que.jpg",
    "https://i.postimg.cc/hj0qRQwn/white-Photoroom-1.jpg",
)

CARRUSEL_HOME_IMAGES = [
    asset_or_remote("home/carrusel/slide-01.png", "https://i.postimg.cc/nzZ8YggY/Chat-GPT-Image-16-sept-2025-11-00-13-p-m.png"),
    asset_or_remote("home/carrusel/slide-02.png", "https://i.postimg.cc/D0XY9c9y/roedores.png"),
    asset_or_remote("home/carrusel/slide-03.png", "https://i.postimg.cc/QdbnZCy5/voladores-insectos.png"),
    asset_or_remote("home/carrusel/slide-04.png", "https://i.postimg.cc/bJ2Trw3m/termitas.png"),
    asset_or_remote("home/carrusel/slide-05.png", "https://i.postimg.cc/hGQxb3Tj/voladores-aves.png"),
    asset_or_remote("home/carrusel/slide-06.png", "https://i.postimg.cc/C13hWvW5/insectos-rastreros.png"),
    asset_or_remote("home/carrusel/slide-07.png", "https://i.postimg.cc/g0bcQM1r/programas-mensuales.png"),
]

PROGRAM_IMAGES = [
    asset_or_remote("home/programas/programa-01.jpg", "https://i.postimg.cc/15nLZNp7/imagen1.jpg"),
    asset_or_remote("home/programas/programa-02.jpg", "https://i.postimg.cc/RZwyW5pc/imagen2.jpg"),
    asset_or_remote("home/programas/programa-03.jpg", "https://i.postimg.cc/BvgzC50b/imagen3.jpg"),
    asset_or_remote("home/programas/programa-04.jpg", "https://i.postimg.cc/FRCnM91Q/imagen4.jpg"),
    asset_or_remote("home/programas/programa-05.jpg", "https://i.postimg.cc/9FN0WFkY/Whats-App-Image-2025-11-17-at-5-58-09-PM.jpg"),
    asset_or_remote("home/programas/programa-06.jpg", "https://i.postimg.cc/Xq5W44BD/Whats-App-Image-2025-11-17-at-5-58-10-PM.jpg"),
]

SERVICE_MENU_IMAGES = {
    "roedores": asset_or_remote("services/menu/roedores.png", "https://i.postimg.cc/cLvXDbLz/Chat-GPT-Image-26-ago-2025-03-08-53-p-m-Photoroom.png"),
    "sanitizacion": asset_or_remote("services/menu/sanitizacion.png", "https://i.postimg.cc/zGfdKtvL/desinfeccion-Photoroom-Photoroom.png"),
    "voladores": asset_or_remote("services/menu/voladores.png", "https://i.postimg.cc/V6hZkjmS/white-Photoroom-Photoroom.png"),
    "rastreros": asset_or_remote("services/menu/rastreros.png", "https://i.postimg.cc/Kzx7yqmM/Chat-GPT-Image-26-ago-2025-03-18-37-p-m-Photoroom.png"),
    "termitas": asset_or_remote("services/menu/termitas.png", "https://i.postimg.cc/rpLxSn0R/Chat-GPT-Image-26-ago-2025-03-13-04-p-m-Photoroom.png"),
    "aves": asset_or_remote("services/menu/aves.png", "https://i.postimg.cc/wjzDN4sJ/Chat-GPT-Image-26-ago-2025-03-09-31-p-m-Photoroom.png"),
}

SABIASQUE_IMAGES = {
    "cucarachas": asset_or_remote("sabiasque/cucarachas.png", "https://www.gardentech.com/-/media/project/oneweb/gardentech/images/pest-id/bug-pest/cockroach.png"),
    "ratas": asset_or_remote("sabiasque/ratas.png", "https://i.postimg.cc/yNKpkNv3/istockphoto-1413873422-612x612-Photoroom.png"),
    "ratones": asset_or_remote("sabiasque/ratones.png", "https://i.postimg.cc/Xqgd1VwZ/raton-campo-mus-musculus-768x576-Photoroom.png"),
    "termitas": asset_or_remote("sabiasque/termitas.png", "https://i.postimg.cc/wjVRQRQ1/termitas-1.png"),
    "hormigas": asset_or_remote("sabiasque/hormigas.png", "https://i.postimg.cc/Yq95H8Sg/hormiga-eliminar-plaga-Photoroom.png"),
    "palomas": asset_or_remote("sabiasque/palomas.png", "https://i.postimg.cc/qBZm8rkj/151120130815-paloma2-624x351-thinkstock-nocredit-Photoroom.png"),
    "chinches": asset_or_remote("sabiasque/chinches.png", "https://i.postimg.cc/MHcmscWv/chinche-cimex-lectularius-Photoroom.png"),
    "pulgas": asset_or_remote("sabiasque/pulgas.png", "https://i.postimg.cc/C12jfFjF/flea-Photoroom.png"),
    "moscas": asset_or_remote("sabiasque/moscas.png", "https://i.postimg.cc/3wZN2kmt/white-Photoroom-1.png"),
}

INSECT_ICON_IMAGES = {
    "cucarachas": asset_or_remote("insectos/cucarachas.png", "https://cdn-icons-png.flaticon.com/512/8005/8005026.png"),
    "hormigas": asset_or_remote("insectos/hormigas.jpg", "https://static.vecteezy.com/system/resources/previews/015/211/725/non_2x/ant-icon-cartoon-style-vector.jpg"),
    "chinches": asset_or_remote("insectos/chinches.png", "https://cdn-icons-png.flaticon.com/512/1850/1850155.png"),
    "pulgas": asset_or_remote("insectos/pulgas.png", "https://cdn-icons-png.flaticon.com/512/2295/2295144.png"),
    "moscas": asset_or_remote("insectos/moscas.png", "https://cdn-icons-png.flaticon.com/512/1357/1357476.png"),
    "zancudos": asset_or_remote("insectos/zancudos.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR29MlAGMA1uNdMVEQtGxDEuh_gLjc_vf1H4w&s"),
    "avispas": asset_or_remote("insectos/avispas.jpg", "https://static.vecteezy.com/system/resources/previews/014/285/415/non_2x/agression-wasp-icon-outline-style-vector.jpg"),
    "raton": asset_or_remote("insectos/raton.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_KKIyhsZpTWOzWNYwJLRLKheBjk4EAPefqw&s"),
    "rata": asset_or_remote("insectos/rata.jpg", "https://static.vecteezy.com/system/resources/previews/014/986/360/non_2x/rat-icon-cartoon-style-vector.jpg"),
    "termita_subterranea": asset_or_remote("insectos/termita-subterranea.png", "https://cdn-icons-png.freepik.com/512/4982/4982504.png"),
    "termita_madera_seca": asset_or_remote("insectos/termita-madera-seca.jpg", "https://thumbs.dreamstime.com/b/icono-vectorial-de-color-plano-%C3%BAnico-la-madera-los-insectos-termite-157353067.jpg"),
    "termita_otros": asset_or_remote("insectos/termita-otros.png", "https://i.postimg.cc/85r8Fs7m/trt.png"),
    "palomas": asset_or_remote("insectos/palomas.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM-8j_vQCe1wXK-otbgAAlnYQIynlY9rampQ&s"),
    "tortolas": asset_or_remote("insectos/tortolas.png", "https://png.pngtree.com/png-vector/20230315/ourmid/pngtree-vector-turtledove-png-image_6650452.png"),
    "gorriones": asset_or_remote("insectos/gorriones.jpg", "https://st3.depositphotos.com/4233957/34474/v/450/depositphotos_344748232-stock-illustration-sparrow-small-city-bird-illustration.jpg"),
    "aves_otros": asset_or_remote("insectos/aves-otros.png", "https://i.postimg.cc/KYBwFww0/aves-urbanas.png"),
}

SERVICE_DETAIL_IMAGES = {
    "roedores": asset_or_remote("services/detail/roedores.png", "https://i.postimg.cc/Xqgd1VwZ/raton-campo-mus-musculus-768x576-Photoroom.png"),
    "sanitizacion": asset_or_remote("services/detail/sanitizacion.png", "https://i.postimg.cc/zGfdKtvL/desinfeccion-Photoroom-Photoroom.png"),
    "voladores": asset_or_remote("services/detail/voladores.png", "https://i.postimg.cc/fLk0j6KP/voladores-Photoroom-Photoroom.png"),
    "rastreros": asset_or_remote("services/detail/rastreros.png", "https://i.postimg.cc/Z5ZVmx43/rastreros-Photoroom-Photoroom.png"),
    "termitas": asset_or_remote("services/detail/termitas.png", "https://i.postimg.cc/CK2jHKwJ/termitas-detalle.png"),
    "aves": asset_or_remote("services/detail/aves.png", "https://i.postimg.cc/MGBy5SXS/avesurbanas.png"),
}
