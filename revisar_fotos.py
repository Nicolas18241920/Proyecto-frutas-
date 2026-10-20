import unicodedata
from pathlib import Path
from PIL import Image

carpeta = Path("fotos")
salida = Path("fotos_ok")
salida.mkdir(exist_ok=True)

for f in sorted(carpeta.iterdir()):
    if not f.is_file():
        continue
    cabecera = f.read_bytes()[:16]
    try:
        im = Image.open(f)
        formato = im.format
        im = im.convert("RGB")
        nombre = unicodedata.normalize("NFKD", f.stem).encode("ascii", "ignore").decode()
        im.save(salida / f"{nombre}.jpg", "JPEG", quality=95)
        print("OK    ", f.name, formato)
    except Exception as e:
        print("FALLA ", f.name, f.stat().st_size, "bytes", cabecera)