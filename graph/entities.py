
import csv
from pathlib import Path

ENTITY_LOOKUP = {}
ENTITY_NAMES = {}

csv_path = Path(__file__).resolve().parent.parent / "data" / "entities.csv"

with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        entity_id = row["entity_id"]
        token = row["token"].lower()
        name = row["entity_name"]

        ENTITY_LOOKUP[token] = entity_id
        ENTITY_NAMES[entity_id] = name
