#!/usr/bin/env python3
"""
Auditor offline v0 - ejecuta análisis de URLs con Ollama.
"""

import csv
import subprocess
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

CASES_CSV = BASE_DIR / "cases" / "cases_post_R1_2026-01-29.csv"

RULES_FILE = BASE_DIR / "auditor" / "RULES_PASSIVE.txt"
PROMPT_FILE = BASE_DIR / "auditor" / "PROMPT_v0.txt"

OUTPUT_DIR = BASE_DIR / "auditor" / "outputs"

rules_text = RULES_FILE.read_text(encoding="utf-8")
prompt_template = PROMPT_FILE.read_text(encoding="utf-8")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

today = date.today().isoformat()
output_base = OUTPUT_DIR / f"auditor_outputs_raw_{today}.md"

output_file = output_base
counter = 1
while output_file.exists():
    output_file = OUTPUT_DIR / f"auditor_outputs_raw_{today}_{counter}.md"
    counter += 1

with open(CASES_CSV, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(f"# Auditor Output - {today}\n\n")
        out.write(f"**CSV:** {CASES_CSV.name}\n\n")
        
        for row in reader:
            url = row["url"]
            detected_entity = row["detected_entity"]
            
            full_prompt = f"""{rules_text}

{prompt_template}

INPUT:
- url: {url}
- detected_entity: {detected_entity}
"""
            print(f"Auditing: {url}", flush=True)

            result = subprocess.run(
                ["ollama", "run", "gemma3:4b"],
                input=full_prompt,
                capture_output=True,
                text=True
            )
            
            model_output = result.stdout.strip() or result.stderr.strip()

            
            out.write("---\n\n")
            out.write(f"## URL: {url}\n\n")
            out.write(f"**detected_entity:** {detected_entity if detected_entity else '(vacío)'}\n\n")
            out.write("### Output del modelo:\n\n")
            out.write(model_output)
            out.write("\n\n")
