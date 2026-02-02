"""Rellena detected_entity ejecutando el grafo."""
import csv
from pathlib import Path

from graph.graph import app

CSV_PATH = Path(__file__).parent.parent / "data/prueba_asignador_only_url.csv"


def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            url = row.get("url", "").strip()
            detected = ""
            if url:
                try:
                    result = app.invoke({"url": url})
                    detected = result.get("entity", {}).get("entity_id", "") or ""
                except Exception:
                    detected = ""
            row["detected_entity"] = detected
            rows.append(row)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
