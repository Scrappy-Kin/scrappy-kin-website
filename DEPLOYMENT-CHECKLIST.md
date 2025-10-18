# Scrappykin Deployment Checklist

Use this checklist to deploy your Scrappykin website.

## Pre-Deployment

### ✅ Files Ready
- [x] Website structure created
- [x] Home page (index.html) - ready for customization
- [x] Terms of Service page (tos.html) - **needs your content**
- [x] Privacy Policy page (privacy.html) - **needs your content**
- [x] 404 page created
- [x] CSS and JS files ready
- [x] Docker configuration complete
- [x] Deployment script ready

### 📝 Content Tasks
- [x] Add your Terms of Service content to `public/tos.html` ✅
- [x] Add your Privacy Policy content to `public/privacy.html` ✅
- [x] Customize home page headline and features in `public/index.html` ✅
- [ ] Update email signup form action (when backend is ready)

### 🌐 DNS Configuration
- [ ] Add A record: `@` → `46.224.23.202`
- [ ] Add A record: `www` → `46.224.23.202`
- [ ] Wait 5-15 minutes for propagation
- [ ] Verify with: `dig scrappykin.com`

## Deployment Steps

### 1. Test Locally (Optional)
```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin/public
python3 -m http.server 8000
# Visit http://localhost:8000
```
- [ ] Home page looks good
- [ ] Navigation works
- [ ] Legal pages load
- [ ] Mobile responsive

### 2. Run Deployment Script
```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin
./deploy.sh
```
- [ ] Files uploaded successfully
- [ ] No errors during upload

### 3. Update Caddyfile on VPS
When prompted by the script:

```bash
ssh vps-hetzner
nano /opt/services/caddy/Caddyfile
```

Add this at the end:
```
scrappykin.com, www.scrappykin.com {
    reverse_proxy scrappykin-web:80
    encode gzip
    
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    }
}
```

- [ ] Caddyfile updated
- [ ] Saved changes (Ctrl+O, Enter, Ctrl+X)
- [ ] Press Enter in deployment script to continue

### 4. Verify Deployment
The script will show container status. Then:

```bash
# Check container is running
ssh vps-hetzner "docker ps | grep scrappykin"
```
- [ ] Container shows as "Up"
- [ ] No restart loops

```bash
# Check logs
ssh vps-hetzner "docker logs scrappykin-web --tail 20"
```
- [ ] No error messages
- [ ] Nginx started successfully

## Post-Deployment

### 5. Test the Website
- [ ] Visit https://scrappykin.com
- [ ] HTTPS works (green padlock)
- [ ] Home page loads correctly
- [ ] Click "Terms of Service" link
- [ ] Click "Privacy Policy" link
- [ ] Test www.scrappykin.com redirect
- [ ] Test 404 page: https://scrappykin.com/nonexistent

### 6. Mobile Testing
- [ ] Test on mobile device
- [ ] Navigation works
- [ ] Text is readable
- [ ] Buttons are tappable

### 7. Browser Testing
- [ ] Chrome/Brave
- [ ] Safari
- [ ] Firefox
- [ ] Mobile Safari/Chrome

## Troubleshooting

### DNS not resolving
```bash
# Check propagation
dig scrappykin.com
dig www.scrappykin.com

# Should show: 46.224.23.202
```
**Solution**: Wait longer (up to 1 hour) or check DNS provider settings

### HTTPS not working
```bash
# Check Caddy logs
ssh vps-hetzner "docker logs caddy --tail 50"
```
**Solution**: Wait 5-10 minutes for Let's Encrypt certificate

### Site shows 502 Bad Gateway
```bash
# Check if container is running
ssh vps-hetzner "docker ps | grep scrappykin"

# Check container logs
ssh vps-hetzner "docker logs scrappykin-web"
```
**Solution**: Restart container if needed

### Changes not appearing
```bash
# Verify files on VPS
ssh vps-hetzner "ls -la /opt/services/scrappykin/public/"

# Check file timestamps
ssh vps-hetzner "ls -lt /opt/services/scrappykin/public/"
```
**Solution**: Clear browser cache (Cmd+Shift+R) or restart container

## Maintenance

### Update Content
1. Edit files in `scrappykin/public/` locally
2. Run `./deploy.sh`
3. Verify changes live

### View Logs
```bash
ssh vps-hetzner "docker logs scrappykin-web -f"
```

### Restart Service
```bash
ssh vps-hetzner "cd /opt/services/scrappykin && docker compose restart"
```

## Success Criteria

✅ All items checked above
✅ https://scrappykin.com loads with HTTPS
✅ All pages accessible
✅ No console errors
✅ Mobile responsive
✅ Legal pages have content

## Next Steps After Launch

- [ ] Set up analytics (if needed)
- [ ] Submit to search engines
- [ ] Set up monitoring/uptime checks
- [ ] Add to VPS documentation
- [ ] Test backups

---

**Ready to deploy?** Start with the DNS configuration, then run `./deploy.sh`!

**Questions?** Check `SETUP-INSTRUCTIONS.md` or `README.md`
