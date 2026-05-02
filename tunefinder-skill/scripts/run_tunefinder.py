#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from pathlib import Path


VALID_GENRES = {
    "dnb",
    "breaks",
    "house",
    "ukg",
    "uk-bass",
    "electronica",
    "downtempo",
    "techno",
    "funk-soul-jazz",
    "hip-hop",
}


def load_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def resolve_settings() -> tuple[Path, str]:
    config_path = Path(
        os.environ.get(
            "TUNEFINDER_SKILL_CONFIG",
            str(Path.home() / ".tunefinder-skill" / "config.env"),
        )
    )
    file_values = load_env_file(config_path)

    tunefinder_path = os.environ.get("TUNEFINDER_PATH") or file_values.get("TUNEFINDER_PATH")
    python_rel = os.environ.get("TUNEFINDER_PYTHON") or file_values.get("TUNEFINDER_PYTHON") or "./venv/bin/python"

    if not tunefinder_path:
        raise SystemExit(
            "TUNEFINDER_PATH is not set. Add it to ~/.tunefinder-skill/config.env "
            "or export it in your shell."
        )

    repo_path = Path(tunefinder_path).expanduser().resolve()
    if not repo_path.exists():
        raise SystemExit(f"TUNEFINDER_PATH does not exist: {repo_path}")
    if not (repo_path / "tunefinder").exists():
        raise SystemExit(f"TUNEFINDER_PATH does not look like a TuneFinder repo: {repo_path}")

    return repo_path, python_rel


def build_command(mode: str, genre: str | None, dry_run: bool) -> list[str]:
    cmd = ["-m", "tunefinder"]

    if mode == "weekly":
        cmd.append("run")
    elif mode == "mix-prep":
        if not genre:
            raise SystemExit("mix-prep mode requires --genre")
        if genre not in VALID_GENRES:
            raise SystemExit(f"Invalid genre '{genre}'. Valid genres: {', '.join(sorted(VALID_GENRES))}")
        cmd.extend(["mix-prep", genre])
    elif mode == "check-config":
        cmd.append("check-config")
    else:
        raise SystemExit(f"Unsupported mode: {mode}")

    if dry_run and mode != "check-config":
        cmd.append("--dry-run")

    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(description="Portable TuneFinder runner")
    parser.add_argument("--mode", required=True, choices=["weekly", "mix-prep", "check-config"])
    parser.add_argument("--genre")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repo_path, python_rel = resolve_settings()
    python_path = (repo_path / python_rel) if python_rel.startswith(".") else Path(python_rel).expanduser()

    if not python_path.exists():
        raise SystemExit(
            f"TuneFinder Python executable not found: {python_path}\n"
            "Set TUNEFINDER_PYTHON in ~/.tunefinder-skill/config.env if needed."
        )

    cmd = [str(python_path), *build_command(args.mode, args.genre, args.dry_run)]
    completed = subprocess.run(cmd, cwd=repo_path)
    return completed.returncode


if __name__ == "__main__":
    sys.exit(main())
