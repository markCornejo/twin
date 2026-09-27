from pathlib import Path
from pypdf import PdfReader
import json

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# Leer PDF de LinkedIn
try:
    reader = PdfReader(DATA_DIR / "linkedin.pdf")
    linkedin = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            linkedin += text

except FileNotFoundError:
    linkedin = "Perfil de LinkedIn no disponible"

# Leer resumen
with open(DATA_DIR / "summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

# Leer estilo
with open(DATA_DIR / "style.txt", "r", encoding="utf-8") as f:
    style = f.read()

# Leer hechos
with open(DATA_DIR / "facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)