# Scrappykin Setup Instructions

## ✅ What's Been Created

Your Scrappykin website is ready to deploy! Here's what's been set up:

### File Structure
```
scrappykin/
├── public/
│   ├── index.html          ✅ Landing page (ready for your content)
│   ├── tos.html            ⏳ Placeholder (add your TOS content)
│   ├── privacy.html        ⏳ Placeholder (add your Privacy Policy)
│   ├── 404.html            ✅ Custom 404 page
│   ├── css/style.css       ✅ Custom CSS with animations
│   └── js/main.js          ✅ Vanilla JavaScript
├── docker-compose.yml      ✅ Docker configuration
├── nginx.conf              ✅ Web server config
├── Caddyfile.snippet       ✅ Reverse proxy config
├── deploy.sh               ✅ Automated deployment script
└── README.md               ✅ Complete documentation
```

### Features Included
- ✅ Responsive design (mobile-friendly)
- ✅ Tailwind CSS via CDN (no build step needed)
- ✅ Smooth animations and transitions
- ✅ Security headers configured
- ✅ Gzip compression enabled
- ✅ SEO-friendly structure
- ✅ Custom 404 page

## 🎯 Next Steps

### 1. Add Your Content

#### Update Legal Pages
Edit these files with your actual content:
- `public/tos.html` - Add your Terms of Service
- `public/privacy.html` - Add your Privacy Policy

The HTML structure is ready - just replace the placeholder text inside the `<div class="prose">` section.

#### Customize Home Page (Optional)
Edit `public/index.html` to:
- Update the tagline
- Add your feature descriptions
- Customize button links
- Add your branding

### 2. Configure DNS

Add these DNS records for `scrappykin.com`:

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

**Wait 5-15 minutes** for DNS propagation.

### 3. Deploy to VPS

Once DNS is configured and content is ready:

```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin
./deploy.sh
```

The script will:
1. Upload all files to the VPS
2. Prompt you to update the Caddyfile
3. Start the service
4. Show you the status

### 4. Update Caddyfile on VPS

When prompted during deployment, SSH into the VPS and add this to `/opt/services/caddy/Caddyfile`:

```
scrappykin.com, www.scrappykin.com {
    reverse_proxy scrappykin-web:80
    encode gzip
    
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    }
}
```

Then restart Caddy:
```bash
cd /opt/services/caddy && docker compose restart
```

## 🧪 Testing Locally

Before deploying, you can preview the site locally:

```bash
cd public
python3 -m http.server 8000
```

Then visit: http://localhost:8000

## 📝 Content Guidelines

### Terms of Service Page
Replace the placeholder in `tos.html` with sections like:
- Acceptance of Terms
- Use License
- User Responsibilities
- Disclaimer
- Limitations
- Governing Law
- Contact Information

### Privacy Policy Page
Replace the placeholder in `privacy.html` with sections like:
- Information Collection
- Use of Information
- Data Storage
- Third-Party Services
- Cookies
- User Rights
- Contact Information

### Home Page
The landing page has:
- Hero section with headline and CTA buttons
- 3-column feature section
- Navigation and footer with legal links

Customize the text and links to match your needs.

## 🎨 Customization Tips

### Colors
The site uses Tailwind's default palette:
- Primary: `blue-600` (buttons, accents)
- Background: `gray-50`
- Text: `gray-900`, `gray-600`

To change colors, replace the Tailwind classes in the HTML files.

### Fonts
Currently using system fonts. To add custom fonts:
1. Add Google Fonts link in `<head>`
2. Update CSS with `font-family`

### Layout
All pages use the same navigation and footer. To modify:
- Navigation: Top of each HTML file
- Footer: Bottom of each HTML file

## 🚀 After Deployment

### Verify Everything Works
1. Visit https://scrappykin.com
2. Check HTTPS certificate (should be automatic)
3. Test all navigation links
4. Test on mobile devices
5. Check legal pages load correctly

### Monitor the Service
```bash
# View logs
ssh vps-hetzner "docker logs scrappykin-web -f"

# Check status
ssh vps-hetzner "docker ps | grep scrappykin"

# Restart if needed
ssh vps-hetzner "cd /opt/services/scrappykin && docker compose restart"
```

## 🔄 Making Updates

After initial deployment, to update content:

1. Edit files locally
2. Run `./deploy.sh` again
3. Changes will be live immediately

No need to update Caddyfile again after the first deployment.

## 📚 Documentation

- **README.md** - Complete technical documentation
- **SETUP-INSTRUCTIONS.md** - This file (getting started guide)

## 🆘 Troubleshooting

### Site not loading
- Check DNS: `dig scrappykin.com`
- Check container: `ssh vps-hetzner "docker ps | grep scrappykin"`
- Check logs: `ssh vps-hetzner "docker logs scrappykin-web"`

### HTTPS not working
- Wait 5-10 minutes for Let's Encrypt
- Check Caddy logs: `ssh vps-hetzner "docker logs caddy"`

### Changes not appearing
- Clear browser cache (Cmd+Shift+R)
- Verify upload: `ssh vps-hetzner "ls -la /opt/services/scrappykin/public/"`
- Restart: `ssh vps-hetzner "cd /opt/services/scrappykin && docker compose restart"`

## ✨ You're Ready!

1. ✅ Website structure created
2. ⏳ Add your TOS and Privacy Policy content
3. ⏳ Configure DNS for scrappykin.com
4. ⏳ Run `./deploy.sh`
5. ⏳ Visit https://scrappykin.com

**Questions?** Check README.md for detailed technical information.
