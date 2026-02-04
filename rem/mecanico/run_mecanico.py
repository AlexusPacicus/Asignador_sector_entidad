#!/usr/bin/env python3
"""
Auditor mecánico v1 - ejecuta análisis de patrones en URLs con Ollama.
Asigna mecánicamente un único patrón P0–P8 conforme a la taxonomía.
"""

import csv
import subprocess
import sys
from datetime import date
from pathlib import Path

# Directorios base
MECANICO_DIR = Path(__file__).parent
REM_DIR = MECANICO_DIR.parent
INPUTS_DIR = REM_DIR / "inputs"

# Archivos de entrada
CASES_CSV = Path(sys.argv[1]) if len(sys.argv) > 1 else INPUTS_DIR / "cases.csv"

# Artefactos
PROMPT_FILE = MECANICO_DIR / "PROMPT.txt"
TAXONOMIA_FILE = INPUTS_DIR / "auditor_v1_taxonomia.md"
CHECKLIST_FILE = INPUTS_DIR / "auditor_v1_checklist.md"
PATRONES_HUMANO_FILE = INPUTS_DIR / "patrones_humano.md"

# Directorio de salida
OUTPUT_DIR = MECANICO_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Modelo a usar
MODEL = sys.argv[2] if len(sys.argv) > 2 else "gemma3:4b"


def load_artifacts() -> dict[str, str]:
    """Carga todos los artefactos necesarios."""
    return {
        "prompt": PROMPT_FILE.read_text(encoding="utf-8"),
        "taxonomia": TAXONOMIA_FILE.read_text(encoding="utf-8"),
        "checklist": CHECKLIST_FILE.read_text(encoding="utf-8"),
        "patrones_humano": PATRONES_HUMANO_FILE.read_text(encoding="utf-8"),
    }


def build_full_prompt(artifacts: dict[str, str], row: dict[str, str]) -> str:
    """Construye el prompt completo para una URL."""
    url = row.get("url", "")
    detected_entity = row.get("detected_entity", "")
    human_entity = row.get("human_entity", row.get("expected_entity", ""))
    reviewed = row.get("reviewed", "true")

    return f"""{artifacts["prompt"]}

---
TAXONOMÍA P0–P8:
{artifacts["taxonomia"]}

---
CHECKLIST OPERATIVA:
{artifacts["checklist"]}

---
PATRONES HUMANOS (contexto pasivo):
{artifacts["patrones_humano"]}

---
INPUT:
- url: {url}
- detected_entity: {detected_entity}
- human_entity: {human_entity}
- reviewed: {reviewed}
"""


def run_model(prompt: str, model: str) -> str:
    """Ejecuta el modelo y retorna la salida."""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        capture_output=True,
        text=True
    )
    return result.stdout.strip() or result.stderr.strip()


def get_output_file() -> Path:
    """Genera nombre de archivo de salida único para hoy."""
    today = date.today().isoformat()
    output_base = OUTPUT_DIR / f"mecanico_outputs_{today}.md"

    output_file = output_base
    counter = 1
    while output_file.exists():
        output_file = OUTPUT_DIR / f"mecanico_outputs_{today}_{counter}.md"
        counter += 1

    return output_file


def main():
    print(f"Cargando artefactos...", flush=True)
    artifacts = load_artifacts()

    print(f"CSV: {CASES_CSV}", flush=True)
    print(f"Modelo: {MODEL}", flush=True)

    output_file = get_output_file()
    today = date.today().isoformat()

    with open(CASES_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        with open(output_file, "w", encoding="utf-8") as out:
            out.write(f"# Auditor Mecánico Output - {today}\n\n")
            out.write(f"**CSV:** {CASES_CSV.name}\n")
            out.write(f"**Modelo:** {MODEL}\n\n")

            for i, row in enumerate(reader, 1):
                url = row.get("url", "")

                # Skip si url vacía o reviewed != true
                reviewed = row.get("reviewed", "true").lower()
                if not url or (reviewed != "true" and reviewed != ""):
                    print(f"[{i}] Saltando (reviewed={reviewed}): {url[:50]}...", flush=True)
                    continue

                print(f"[{i}] Auditando: {url[:80]}...", flush=True)

                full_prompt = build_full_prompt(artifacts, row)
                model_output = run_model(full_prompt, MODEL)

                detected = row.get("detected_entity", "")
                human = row.get("human_entity", row.get("expected_entity", ""))

                out.write("---\n\n")
                out.write(f"## [{i}] URL\n\n")
                out.write(f"```\n{url}\n```\n\n")
                out.write(f"**detected_entity:** {detected if detected else '(vacío)'}\n\n")
                out.write(f"**human_entity:** {human if human else '(vacío)'}\n\n")
                out.write("### Output:\n\n")
                out.write(f"```json\n{model_output}\n```\n\n")

    print(f"\nOutput guardado en: {output_file}", flush=True)


if __name__ == "__main__":
    main()
