"""
Recalcula detected_entity para todas las URLs usando el grafo LangGraph.
"""
import csv
from graph.graph import app
from datetime import date
from pathlib import Path

BASE = Path("rem/cases")
TODAY = date.today().isoformat()

IN = BASE / "cases.csv"
OUT_BASE = BASE / f"cases_post_{TODAY}.csv"

OUT = OUT_BASE
counter = 1
while OUT.exists():
    OUT = BASE / f"cases_post_{TODAY}_{counter}.csv"
    counter += 1

def main():
    with open(IN, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        base_fields = list(reader.fieldnames)
        extra_fields = ["detected_entity", "human_entity", "error_type", "reviewed"]

        fieldnames = base_fields + [f for f in extra_fields if f not in base_fields]

        rows = list(reader)

    for row in rows:
        result = app.invoke({"url": row["url"]})
        entity = result.get("entity") or {}
        row["detected_entity"] = entity.get("entity_id", "")
        row["human_entity"] = ""
        row["error_type"] = ""
        row["reviewed"] = "false"

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
