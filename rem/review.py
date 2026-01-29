"""
Script offline para revisión LLM del repositorio.
Lee repo_snapshot.txt y cases.csv, envía a LLM, escribe review_output.md.
NO modifica el core ni ejecuta código automáticamente.
"""
from datetime import datetime, timezone
from pathlib import Path
from openai import OpenAI

REM_DIR = Path(__file__).parent
SNAPSHOT_PATH = REM_DIR / "repo_snapshot.txt"
CASES_PATH = REM_DIR / "cases.csv"
OUTPUT_PATH = REM_DIR / "review_output.md"

MODEL = "gpt-4.1-mini"

SYSTEM_PROMPT = """You are a code reviewer analyzing a Python codebase.
Review the provided repository snapshot and test cases.
Your output MUST follow this exact format:

OBSERVATIONS:
- ...

PATTERNS:
- ...

RISKS:
- ...

SUGGESTIONS (NON-EXECUTABLE):
- ...

Do NOT produce executable code. Only structured text observations."""


def load_file(path: Path) -> str:
    """Carga archivo como string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_user_prompt(snapshot: str, cases: str) -> str:
    """Construye el prompt de usuario con el contexto."""
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""## Metadata
- Timestamp: {utc_now}
- Snapshot file: {SNAPSHOT_PATH.name}
- Cases file: {CASES_PATH.name}

## Repository Snapshot

{snapshot}

## Test Cases (cases.csv)

{cases}

Analyze the codebase and test cases. Provide your review following the required format."""


def call_llm(system: str, user: str) -> str:
    """Llama al LLM via OpenAI SDK (Responses API)."""
    client = OpenAI()
    response = client.responses.create(
        model=MODEL,
        instructions=system,
        input=user,
        temperature=0.3,
    )
    return response.output_text


def validate_format(content: str) -> None:
    """Verifica que la respuesta contenga el formato requerido."""
    if "OBSERVATIONS:" not in content:
        raise ValueError("Respuesta LLM inválida: falta sección OBSERVATIONS:")


def write_output(content: str) -> None:
    """Escribe el output en review_output.md."""
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    snapshot = load_file(SNAPSHOT_PATH)
    cases = load_file(CASES_PATH)
    user_prompt = build_user_prompt(snapshot, cases)
    
    print("Enviando a LLM...")
    result = call_llm(SYSTEM_PROMPT, user_prompt)
    
    validate_format(result)
    write_output(result)
    print(f"Review escrito en: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
