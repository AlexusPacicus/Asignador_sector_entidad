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
OUT = BASE / f"cases_post_{TODAY}.csv"

def main():
    with open(IN, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in rows:
        result = app.invoke({"url": row["url"]})
        entity = result.get("entity") or {}
        row["detected_entity"] = entity.get("entity_id", "")

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
