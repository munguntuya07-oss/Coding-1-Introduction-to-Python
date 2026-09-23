"""Validate course notebooks without executing every cell."""

from __future__ import annotations

import ast
import importlib
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOTS = (ROOT / "lectures", ROOT / "exercises")
EXPECTED_KERNEL = {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"}
DATA_REF_RE = re.compile(r'DATA_DIR\s*/\s*["\']([^"\']+)["\']')
CACHE_DIR = Path(tempfile.gettempdir()) / "coding1-notebook-check-cache"
os.environ.setdefault("MPLCONFIGDIR", str(CACHE_DIR / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE_DIR / "xdg"))
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def iter_notebooks() -> list[Path]:
    notebooks: list[Path] = []
    for root in NOTEBOOK_ROOTS:
        if root.exists():
            notebooks.extend(p for p in root.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts)
    return sorted(notebooks)


def imports_from_source(source: str) -> set[str]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set()
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module.split(".")[0])
    return modules


def check_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.relative_to(ROOT)}: invalid JSON: {exc}"]

    rel = path.relative_to(ROOT)
    kernel = notebook.get("metadata", {}).get("kernelspec")
    if kernel != EXPECTED_KERNEL:
        errors.append(f"{rel}: kernelspec is {kernel!r}, expected {EXPECTED_KERNEL!r}")

    modules: set[str] = set()
    data_refs: set[str] = set()
    for index, cell in enumerate(notebook.get("cells", []), start=1):
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code":
            modules.update(imports_from_source(source))
            data_refs.update(DATA_REF_RE.findall(source))
            try:
                ast.parse(source)
            except SyntaxError as exc:
                errors.append(f"{rel}: code cell {index} has syntax error: {exc}")

    for module in sorted(modules):
        if importlib.util.find_spec(module) is None:
            errors.append(f"{rel}: import not available: {module}")
            continue
        try:
            importlib.import_module(module)
        except Exception as exc:  # noqa: BLE001 - report any import-time failure.
            errors.append(f"{rel}: import failed for {module}: {exc}")

    for filename in sorted(data_refs):
        data_path = ROOT / "data" / "raw" / filename
        if not data_path.exists() or data_path.stat().st_size == 0:
            errors.append(f"{rel}: missing data file {data_path.relative_to(ROOT)}")
    return errors


def main() -> int:
    notebooks = iter_notebooks()
    if not notebooks:
        print("No notebooks found.")
        return 1

    errors: list[str] = []
    for path in notebooks:
        errors.extend(check_notebook(path))

    if errors:
        print("Notebook validation failed:")
        print("\n".join(errors))
        return 1
    print(f"Validated {len(notebooks)} notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
