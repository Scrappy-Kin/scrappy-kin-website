# Scrappykin Setup Instructions

This file is kept as a stable pointer for older links.

## Canonical docs

- Local editing, file structure, and convenience deploy script: `scrappykin/README.md`
- VPS operations and wrapper commands: `docs/services/scrappykin.md`

## Current deploy path

```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin
./scripts/deploy.sh
```

`scripts/deploy.sh` uses the wrapper-based flow:

- `git push origin main`
- `ssh vps-ops "sudo service-deploy scrappykin"`
- `ssh vps-ops "sudo service-restart scrappykin"`

## Local preview

```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin/public
python3 -m http.server 8000
```
