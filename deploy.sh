#!/bin/bash
set -e

# Scrappykin Deployment Script
# This script deploys the Scrappykin website to the VPS

VPS_HOST="vps-hetzner"
SERVICE_DIR="/opt/services/scrappykin"
CADDY_DIR="/opt/services/caddy"

echo "🚀 Deploying Scrappykin to VPS..."

# Create service directory on VPS if it doesn't exist
echo "📁 Creating service directory..."
ssh $VPS_HOST "mkdir -p $SERVICE_DIR"

# Copy files to VPS
echo "📤 Uploading files..."
rsync -avz --delete \
    --exclude='.git' \
    --exclude='deploy.sh' \
    --exclude='Caddyfile.snippet' \
    --exclude='README.md' \
    ./public/ \
    $VPS_HOST:$SERVICE_DIR/public/

rsync -avz \
    ./docker-compose.yml \
    ./nginx.conf \
    $VPS_HOST:$SERVICE_DIR/

# Update Caddyfile (manual step reminder)
echo ""
echo "⚠️  MANUAL STEP REQUIRED:"
echo "Add the following to $CADDY_DIR/Caddyfile on the VPS:"
echo ""
cat Caddyfile.snippet
echo ""
read -p "Press Enter after you've updated the Caddyfile..."

# Restart Caddy
echo "🔄 Restarting Caddy..."
ssh $VPS_HOST "cd $CADDY_DIR && docker compose restart"

# Start or restart Scrappykin service
echo "🔄 Starting Scrappykin service..."
ssh $VPS_HOST "cd $SERVICE_DIR && docker compose up -d"

# Wait a moment for container to start
sleep 3

# Check status
echo ""
echo "✅ Deployment complete!"
echo ""
echo "📊 Container status:"
ssh $VPS_HOST "docker ps | grep scrappykin"
echo ""
echo "🌐 Your site should be available at:"
echo "   https://scrappykin.com"
echo "   https://www.scrappykin.com"
echo ""
echo "📝 To view logs:"
echo "   ssh $VPS_HOST \"docker logs scrappykin-web -f\""
