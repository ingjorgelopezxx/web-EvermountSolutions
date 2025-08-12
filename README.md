# Evermount App Modular (Flet)

Ejecuta con:

```bash
python main.py
# o
flet run main.py
```

Estructura:
- `main.py`: layout, menú, animaciones compartidas y motor de slides.
- `views/`: un archivo por opción del menú. Las vistas tipo "slides" llaman `ctx.start_slides(...)`.
