# Scrappykin Deployment Checklist

This file is kept as a stable pointer for older links.

## Canonical docs

- Local editing and deploy script usage: `scrappykin/README.md`
- VPS operations and verification commands: `docs/services/scrappykin.md`

## Current deploy path

```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin
./scripts/deploy.sh
```

## Minimal verification

```bash
ssh vps-ops "sudo service-inspect ps scrappykin"
ssh vps-ops "sudo service-logs scrappykin 20"
```
