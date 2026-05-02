# Setup

## What this skill expects

This skill expects a separate local TuneFinder install.

It does not bundle:

- TuneFinder source code
- TuneFinder `.env`
- API keys
- Discord bot setup

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

### Python executable missing

Make sure TuneFinder has a working virtualenv, or set `TUNEFINDER_PYTHON` to the correct executable.

### TuneFinder config errors

Run:

```bash
python3 scripts/run_tunefinder.py --mode check-config
```

Then fix the underlying TuneFinder install.
