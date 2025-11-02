## Purpose

This repository is a very small Selenium web-browsing exercise. It currently contains an empty `main.py` and a minimal `README.md` header. These instructions help an AI coding agent be productive quickly by describing the expected entrypoints, environment, and common patterns to follow when adding features or tests.

## Quick summary (what you'll find)
- `main.py` — repository entrypoint (currently empty). Implement new behaviour here.
- `README.md` — placeholder; use it for high-level run/install notes if you add dependencies.

## When making changes
- Preserve a single script entrypoint: implement a `main()` and standard CLI guard:

  Example pattern to create in `main.py`:

  - def main(args):
  - if __name__ == "__main__":
  -     main(sys.argv[1:])

- Keep I/O minimal and explicit. Return structured results or write to files when creating demos.

## Environment & runtime notes (Linux dev container)
- This workspace runs on Linux in the dev container. Assume bash shell for commands.
- Typical workflow to prepare a local environment (add a `requirements.txt` when adding packages):

  - python -m venv .venv
  - source .venv/bin/activate
  - pip install selenium webdriver-manager

- Prefer `webdriver-manager` to reduce friction when setting up browser drivers.

## Testing & quick verification
- Add a small script or pytest test that launches a headless browser and visits a stable page (example: `https://example.com`) to validate Selenium wiring.
- Keep tests fast: run headless and avoid heavy waits. Use explicit short timeouts and element checks.

## Conventions / patterns to follow
- One small, focused script per task. If the feature grows, factor into `src/` with clear module boundaries.
- Logging: use Python `logging` module rather than print for diagnosable output.
- Configuration: prefer CLI args or environment variables over hard-coded values for URLs and timeouts.

## Integration & external points
- Selenium-driven browser interactions are the expected integration point. Use `webdriver-manager` or clearly document driver requirements in `README.md`.
- If you add cloud or external services, update `README.md` with any credentials/ENV requirements and add a `requirements.txt`.

## What NOT to change without asking
- Don't add large, opinionated frameworks (e.g., full Django/Flask) unless the task explicitly requires it.

## Examples from this repo
- `main.py` — start here. If it's empty, create a minimal, well-documented entrypoint and accompanying tests as described above.

## When in doubt
- Keep changes small and self-contained. Add a `README.md` section documenting how to run any new script or tests.

Please review these instructions and tell me if you want more strict conventions (packaging, CI, linters) or example implementations added.
