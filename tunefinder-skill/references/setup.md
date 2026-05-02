# Setup

## Overview

This skill is an onboarding and launcher layer for a separate local TuneFinder install.

Original TuneFinder repo:

- https://github.com/christophechang/TuneFinder

## What this skill expects

This skill expects a separate local TuneFinder install.

It does not bundle:

- TuneFinder source code
- TuneFinder `.env`
- API keys
- Discord bot setup

## First-time onboarding

For a new user, do setup in this order:

1. Clone TuneFinder from Christophe Chang's repo.
2. Create TuneFinder's virtualenv and install its dependencies.
3. Copy TuneFinder's `.env.example` to `.env`.
4. Fill TuneFinder's required API keys and Discord values.
5. Run TuneFinder's own config check.
6. Create this skill's local config file at `~/.tunefinder-skill/config.env`.
7. Run this skill's wrapper with `--mode check-config`.
8. Then run a dry-run or live TuneFinder command.

## Install TuneFinder

Example:

```bash
git clone https://github.com/christophechang/TuneFinder.git
cd TuneFinder
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .env.example .env
```

Then fill TuneFinder's `.env` with that user's own keys and Discord values.

## Verify TuneFinder itself

Run inside the TuneFinder repo:

```bash
./venv/bin/python -m tunefinder check-config
```

That must pass before this skill can run live commands reliably.

## Local config

Create:

`~/.tunefinder-skill/config.env`

Example:

```bash
TUNEFINDER_PATH=/absolute/path/to/TuneFinder
TUNEFINDER_PYTHON=./venv/bin/python
```

## Variables

- `TUNEFINDER_PATH`
  Absolute path to the local TuneFinder repo.

- `TUNEFINDER_PYTHON`
  Optional. Defaults to `./venv/bin/python` relative to `TUNEFINDER_PATH`.

## Examples

If you cloned TuneFinder here:

```bash
TUNEFINDER_PATH=/Users/you/Documents/TuneFinder
TUNEFINDER_PYTHON=./venv/bin/python
```

If you want to override config for one run only:

```bash
TUNEFINDER_PATH=/Users/you/Documents/TuneFinder \
python3 scripts/run_tunefinder.py --mode weekly
```

## Troubleshooting

### TuneFinder path missing

Set `TUNEFINDER_PATH` in `~/.tunefinder-skill/config.env`.

### TuneFinder not installed yet

Clone and configure TuneFinder first, then return to this skill wrapper.

### Python executable missing

Make sure TuneFinder has a working virtualenv, or set `TUNEFINDER_PYTHON` to the correct executable.

### TuneFinder config errors

Run:

```bash
python3 scripts/run_tunefinder.py --mode check-config
```

Then fix the underlying TuneFinder install.
