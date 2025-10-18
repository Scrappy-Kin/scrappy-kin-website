# Scrappykin Website

Simple static marketing website for scrappykin.com built with Tailwind CSS, vanilla JavaScript, and HTML.

## Structure

```
scrappykin/
├── public/
│   ├── index.html          # Home page (landing page)
│   ├── tos.html            # Terms of Service
│   ├── privacy.html        # Privacy Policy
│   ├── css/
│   │   └── style.css       # Custom CSS styles
│   └── js/
│       └── main.js         # Vanilla JavaScript
├── docker-compose.yml      # Docker configuration
├── nginx.conf              # Nginx web server config
├── Caddyfile.snippet       # Caddy reverse proxy config
├── deploy.sh               # Deployment script
└── README.md               # This file
```

## Technology Stack

- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework (via CDN)
- **Vanilla JavaScript** - No frameworks, just plain JS
- **Nginx Alpine** - Lightweight web server
- **Docker** - Containerization
- **Caddy** - Reverse proxy with automatic HTTPS

## Local Development

To preview locally, you can use any static file server:

```bash
# Using Python
cd public
python3 -m http.server 8000

# Using Node.js (if you have npx)
cd public
npx serve

# Using PHP
cd public
php -S localhost:8000
```

Then visit http://localhost:8000

## Deployment

### Prerequisites

1. DNS configured: A records for `scrappykin.com` and `www.scrappykin.com` pointing to `46.224.23.202`
2. SSH access to VPS configured as `vps-hetzner`

### Deploy to VPS

```bash
chmod +x deploy.sh
./deploy.sh
```

The script will:
1. Create the service directory on the VPS
2. Upload all files
3. Prompt you to update the Caddyfile
4. Restart Caddy
5. Start the Scrappykin container

### Manual Deployment Steps

If you prefer to deploy manually:

1. **Copy files to VPS:**
   ```bash
   ssh vps-hetzner "mkdir -p /opt/services/scrappykin"
   rsync -avz ./public/ vps-hetzner:/opt/services/scrappykin/public/
   rsync -avz ./docker-compose.yml ./nginx.conf vps-hetzner:/opt/services/scrappykin/
   ```

2. **Update Caddyfile:**
   ```bash
   ssh vps-hetzner "nano /opt/services/caddy/Caddyfile"
   ```
   
   Add the content from `Caddyfile.snippet`

3. **Restart Caddy:**
   ```bash
   ssh vps-hetzner "cd /opt/services/caddy && docker compose restart"
   ```

4. **Start Scrappykin:**
   ```bash
   ssh vps-hetzner "cd /opt/services/scrappykin && docker compose up -d"
   ```

## Updating Content

### Update Legal Pages

1. Edit `public/tos.html` or `public/privacy.html` locally
2. Run `./deploy.sh` to push changes

### Update Home Page

1. Edit `public/index.html` locally
2. Run `./deploy.sh` to push changes

### Update Styles

1. Edit `public/css/style.css` for custom CSS
2. Modify Tailwind classes directly in HTML files
3. Run `./deploy.sh` to push changes

## Management Commands

```bash
# View logs
ssh vps-hetzner "docker logs scrappykin-web -f"

# Restart service
ssh vps-hetzner "cd /opt/services/scrappykin && docker compose restart"

# Stop service
ssh vps-hetzner "cd /opt/services/scrappykin && docker compose down"

# Start service
ssh vps-hetzner "cd /opt/services/scrappykin && docker compose up -d"

# Check status
ssh vps-hetzner "docker ps | grep scrappykin"
```

## Features

- ✅ Responsive design (mobile-friendly)
- ✅ Modern UI with Tailwind CSS
- ✅ Fast loading (static files, gzip compression)
- ✅ Automatic HTTPS via Caddy
- ✅ Security headers configured
- ✅ SEO-friendly HTML structure
- ✅ Smooth animations and transitions
- ✅ Accessible navigation

## Customization

### Colors

The site uses Tailwind's default color palette. To customize:
- Edit the Tailwind classes in HTML files
- Or add custom CSS in `public/css/style.css`

### Fonts

Currently using system fonts. To add custom fonts:
1. Add font link in `<head>` of HTML files
2. Update CSS with font-family

### Content

- **Home page**: Edit `public/index.html`
- **Terms**: Edit `public/tos.html`
- **Privacy**: Edit `public/privacy.html`

## DNS Configuration

Required DNS records:

```
Type: A
Name: @
Value: 46.224.23.202
TTL: 300

Type: A
Name: www
Value: 46.224.23.202
TTL: 300
```

## Troubleshooting

### Site not loading
- Check DNS propagation: `dig scrappykin.com`
- Check container status: `ssh vps-hetzner "docker ps | grep scrappykin"`
- Check logs: `ssh vps-hetzner "docker logs scrappykin-web"`

### HTTPS not working
- Wait 5-10 minutes for Let's Encrypt certificate
- Check Caddy logs: `ssh vps-hetzner "docker logs caddy"`
- Verify DNS is pointing to correct IP

### Changes not appearing
- Clear browser cache
- Verify files were uploaded: `ssh vps-hetzner "ls -la /opt/services/scrappykin/public/"`
- Restart container: `ssh vps-hetzner "cd /opt/services/scrappykin && docker compose restart"`

## License

All rights reserved.
