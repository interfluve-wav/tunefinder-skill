---
name: tunefinder-skill
description: Use when the user asks to install, configure, onboard, or run TuneFinder locally, including weekly music reports and genre-specific mix-prep reports.
---

# TuneFinder Skill

Use this skill when the user wants to install, configure, or run a local TuneFinder install.

## When to use

- The user says `Run TuneFinder`
- The user wants help installing or setting up TuneFinder
- The user wants help connecting this skill to a local TuneFinder clone
- The user wants a weekly music discovery run
- The user wants `mix-prep` for a genre like `house`, `ukg`, or `dnb`

## Onboarding flow

If the user is not set up yet, do onboarding before trying to run TuneFinder:

1. Confirm whether they already have a local TuneFinder clone.
2. If not, point them to Christophe Chang's original repo:
   `https://github.com/christophechang/TuneFinder`
3. Have them configure:
   - TuneFinder's `.env`
   - TuneFinder's Python environment
   - `~/.tunefinder-skill/config.env`
4. Run the helper script with `--mode check-config`.
5. Only move to `weekly` or `mix-prep` after config passes.

Read [references/setup.md](references/setup.md) for onboarding, install, and troubleshooting steps.

## Interactive flow

When the user asks to run TuneFinder without enough detail:

1. Ask: `Do you want a weekly run or mix-prep?`
2. If they choose `mix-prep` and did not provide a genre, ask for one valid genre.
3. Then run the command with the helper script in `scripts/run_tunefinder.py`.

When the user already provides enough detail:

- Weekly run: run it directly
- TuneFinder plus genre: run `mix-prep <genre>` directly

Do not ask unnecessary follow-up questions once mode and genre are clear.

## Valid mix-prep genres

- `dnb`
- `breaks`
- `house`
- `ukg`
- `uk-bass`
- `electronica`
- `downtempo`
- `techno`
- `funk-soul-jazz`
- `hip-hop`

## Commands

Run from this skill directory with:

```bash
python3 scripts/run_tunefinder.py --mode weekly
python3 scripts/run_tunefinder.py --mode mix-prep --genre house
python3 scripts/run_tunefinder.py --mode weekly --dry-run
python3 scripts/run_tunefinder.py --mode mix-prep --genre ukg --dry-run
python3 scripts/run_tunefinder.py --mode check-config
```

## Configuration

The helper script reads local user config from:

`~/.tunefinder-skill/config.env`

Read [references/setup.md](references/setup.md) when:

- TuneFinder path is not configured yet
- TuneFinder is not installed yet
- the user needs onboarding from zero
- the local repo path changed
- the Python executable inside TuneFinder is different
- the user needs install or troubleshooting help

## Execution rules

- Prefer live runs unless the user explicitly asks for a dry run.
- If setup is incomplete, help the user finish setup before trying to run live commands.
- If the helper script reports a missing path or invalid config, surface that exact problem.
- If the run succeeds, tell the user whether it completed and posted successfully.
- Do not assume this repo contains TuneFinder itself.
