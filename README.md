# tunefinder-skill

A portable Codex/Hermes skill for running [TuneFinder](https://github.com/christophechang/TuneFinder) with a simple interactive flow.

This repo does not contain TuneFinder itself. It contains:

- a reusable skill
- a small runner script
- setup instructions

## Credit

TuneFinder was created by [Christophe Chang](https://github.com/christophechang).

- Original repo: [christophechang/TuneFinder](https://github.com/christophechang/TuneFinder)

This repo is only a companion skill layer for running a local TuneFinder install from Codex or Hermes.

## What this skill does

- lets you say `Run TuneFinder`
- asks `weekly run or mix-prep?` if needed
- asks for a genre only when `mix-prep` needs one
- runs your local TuneFinder install with the right command

## Prerequisites

You need your own local TuneFinder install with its own `.env`, Python environment, and Discord/API setup.

## Install the skill

Install from GitHub by pointing your skill installer at the `tunefinder-skill/` folder in this repo.

After installing, restart Codex or Hermes if your client requires it to pick up new skills.

## Configure your local TuneFinder path

Create a local config file at:

`~/.tunefinder-skill/config.env`

Example:

```bash
TUNEFINDER_PATH=/absolute/path/to/TuneFinder
TUNEFINDER_PYTHON=./venv/bin/python
```

### Two supported setup styles

1. Hard-code your local path

Set `TUNEFINDER_PATH` in `~/.tunefinder-skill/config.env`.

2. Point to your own clone of the original TuneFinder repo

Clone `christophechang/TuneFinder` wherever you want, set `TUNEFINDER_PATH` to that clone, and keep using the same skill.

## Usage

Examples:

```text
Run TuneFinder
Run TuneFinder weekly
Run TuneFinder house
Run TuneFinder mix-prep
```

Valid mix-prep genres:

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

## Security

- Do not commit your TuneFinder `.env`
- Do not commit your `~/.tunefinder-skill/config.env`
- This repo is designed so your secrets stay inside your local TuneFinder install

## Files

- `tunefinder-skill/SKILL.md`: skill instructions
- `tunefinder-skill/scripts/run_tunefinder.py`: portable command runner
- `tunefinder-skill/references/setup.md`: setup and troubleshooting notes
