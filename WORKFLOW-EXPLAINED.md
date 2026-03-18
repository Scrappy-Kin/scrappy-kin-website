# Scrappykin Workflow Explained

This file is kept as a stable pointer for older links.

## Canonical docs

- Local editing and file layout: `scrappykin/README.md`
- VPS operations and deploy commands: `docs/services/scrappykin.md`

## Current workflow

- Edit files locally under `scrappykin/public/`
- Preview locally if needed
- Deploy with `./scripts/deploy.sh`
- Verify on the VPS with `service-inspect` or `service-logs`

## Current deploy path

```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin
./scripts/deploy.sh
```
