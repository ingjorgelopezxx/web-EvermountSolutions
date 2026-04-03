Asset migration guide

This project now supports local-first image loading with remote fallback through [asset_sources.py](/C:/Users/jorge/Music/APPEVERMOUNT/functions/asset_sources.py).

Recommended first migration set
- `assets/brand/logo-72x72.png`
- `assets/brand/logo-round.jpg`
- `assets/brand/logo-mobile-dark.png`
- `assets/home/hero-banner.png`
- `assets/icons/whatsapp.svg`
- `assets/icons/instagram.svg`
- `assets/icons/facebook.svg`
- `assets/icons/sabias-que.jpg`

Home carousel
- `assets/home/carrusel/slide-01.png`
- `assets/home/carrusel/slide-02.png`
- `assets/home/carrusel/slide-03.png`
- `assets/home/carrusel/slide-04.png`
- `assets/home/carrusel/slide-05.png`
- `assets/home/carrusel/slide-06.png`
- `assets/home/carrusel/slide-07.png`

Program images
- `assets/home/programas/programa-01.jpg`
- `assets/home/programas/programa-02.jpg`
- `assets/home/programas/programa-03.jpg`
- `assets/home/programas/programa-04.jpg`
- `assets/home/programas/programa-05.jpg`
- `assets/home/programas/programa-06.jpg`

Service menu
- `assets/services/menu/roedores.png`
- `assets/services/menu/sanitizacion.png`
- `assets/services/menu/voladores.png`
- `assets/services/menu/rastreros.png`
- `assets/services/menu/termitas.png`
- `assets/services/menu/aves.png`

Service detail
- `assets/services/detail/roedores.png`
- `assets/services/detail/sanitizacion.png`
- `assets/services/detail/voladores.png`
- `assets/services/detail/rastreros.png`
- `assets/services/detail/termitas.png`
- `assets/services/detail/aves.png`

Sabias que
- `assets/sabiasque/cucarachas.png`
- `assets/sabiasque/ratas.png`
- `assets/sabiasque/ratones.png`
- `assets/sabiasque/termitas.png`
- `assets/sabiasque/hormigas.png`
- `assets/sabiasque/palomas.png`
- `assets/sabiasque/chinches.png`
- `assets/sabiasque/pulgas.png`
- `assets/sabiasque/moscas.png`

Insectos y aves
- `assets/insectos/cucarachas.png`
- `assets/insectos/hormigas.jpg`
- `assets/insectos/chinches.png`
- `assets/insectos/pulgas.png`
- `assets/insectos/moscas.png`
- `assets/insectos/zancudos.png`
- `assets/insectos/avispas.jpg`
- `assets/insectos/raton.png`
- `assets/insectos/rata.jpg`
- `assets/insectos/termita-subterranea.png`
- `assets/insectos/termita-madera-seca.jpg`
- `assets/insectos/termita-otros.png`
- `assets/insectos/palomas.png`
- `assets/insectos/tortolas.png`
- `assets/insectos/gorriones.jpg`
- `assets/insectos/aves-otros.png`

Remaining remote dependencies

These are still expected to stay remote because they are functional links or dynamic resources rather than static design assets.

- `https://wa.me/...` for WhatsApp launch
- `https://www.instagram.com/...` for Instagram profile
- `https://maps.app.goo.gl/...` for location link
- `https://www.youtube.com/watch?...` for video launch
- `https://img.youtube.com/vi/.../hqdefault.jpg` for dynamic YouTube thumbnails
- `https://api.resend.com/emails` for email delivery API
