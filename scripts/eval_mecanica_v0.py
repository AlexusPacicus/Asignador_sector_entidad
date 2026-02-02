#!/usr/bin/env python3
"""Evaluación mecánica v0: asigna bucket y exporta casos FN/MISMATCH."""

import pandas as pd


def assign_bucket(row: pd.Series) -> str:
    """Asigna bucket según reglas cerradas."""
    human = str(row["human_entity"]).strip() if pd.notna(row["human_entity"]) else ""
    detected = str(row["detected_entity"]).strip() if pd.notna(row["detected_entity"]) else ""

    if human == "" and detected == "":
        return "TN"
    elif human == "" and detected != "":
        return "FP"
    elif human != "" and detected == "":
        return "FN"
    elif human == detected:
        return "TP"
    else:
        return "MISMATCH"


def main():
    # 1) Leer CSV
    input_path = "data/eval/urls_eval_v0.csv"
    df = pd.read_csv(input_path)

    # 2) Añadir columna bucket
    df["bucket"] = df.apply(assign_bucket, axis=1)

    # 3) Guardar CSV actualizado
    df.to_csv(input_path, index=False)
    print(f"CSV actualizado: {input_path}")

    # 4) Imprimir conteo por bucket
    print("\nConteo por bucket:")
    print(df["bucket"].value_counts().to_string())

    # 5) Exportar casos FN y MISMATCH
    cases_df = df[df["bucket"].isin(["FN", "MISMATCH"])][
        ["url", "detected_entity", "human_entity", "bucket"]
    ]
    output_path = "rem/cases/cases_eval_v0.csv"
    cases_df.to_csv(output_path, index=False)
    print(f"\nCasos FN/MISMATCH exportados: {output_path} ({len(cases_df)} filas)")


if __name__ == "__main__":
    main()
