#!/bin/bash
set -e

# Scrappykin Deployment Script
# This script deploys the Scrappykin website to the VPS

echo "🚀 Deploying Scrappykin to VPS..."
echo "� Pushing current branch to origin/main..."
git push origin main

echo "📁 Deploying service files via vps-ops wrapper..."
ssh vps-ops "sudo service-deploy scrappykin"

echo "🔄 Restarting Scrappykin service..."
ssh vps-ops "sudo service-restart scrappykin"

echo "📊 Container status:"
ssh vps-ops "sudo service-inspect ps scrappykin"

echo ""
echo "✅ Deployment complete!"
echo "🌐 Your site should be available at:"
echo "   https://scrappykin.com"
echo "   https://www.scrappykin.com"
echo ""
echo "📝 To view logs:"
echo "   ssh vps-ops \"sudo service-logs scrappykin 50\""
