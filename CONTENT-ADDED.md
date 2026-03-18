# Scrappykin Content Added

This file is kept as a stable pointer for older links.

## Canonical docs

- Current site structure and editing workflow: `scrappykin/README.md`
- VPS deploy and verification commands: `docs/services/scrappykin.md`

## Current editing flow

- Edit HTML under `scrappykin/public/`
- Optionally preview locally from `scrappykin/public/`
- Deploy with `./scripts/deploy.sh`

## Local preview

```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin/public
python3 -m http.server 8000
```
