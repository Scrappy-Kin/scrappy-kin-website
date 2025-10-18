# 📂 Local vs Server: Workflow Explained

You asked: **"What's the deal with this folder? Shouldn't this content be on the server not local?"**

Great question! Here's how the workflow works:

## The Development → Deployment Model

```
┌─────────────────────────────────────┐
│  LOCAL MACHINE (Your Mac)           │
│  /Users/jonamar/Development/        │
│  generic-vps-hetzner/scrappykin/    │
│                                     │
│  - Edit files here                  │
│  - Version control (git)            │
│  - Test locally                     │
│  - Source of truth                  │
└──────────────┬──────────────────────┘
               │
               │ ./deploy.sh
               │ (rsync upload)
               ↓
┌─────────────────────────────────────┐
│  VPS SERVER (Hetzner)                │
│  /opt/services/scrappykin/          │
│                                     │
│  - Serves files to internet         │
│  - Nginx container                  │
│  - Production environment           │
│  - Don't edit directly!             │
└─────────────────────────────────────┘
```

## Why This Is The Right Way

### ✅ Advantages of Local Development

1. **Easy Editing**
   - Use your IDE (VS Code, etc.)
   - Syntax highlighting
   - Auto-completion
   - No SSH needed for every edit

2. **Version Control**
   - Can use git to track changes
   - Rollback if something breaks
   - See history of changes
   - Branch for experiments

3. **Testing**
   - Test locally before deploying
   - No risk to production
   - Faster iteration

4. **Backup**
   - Your local files are a backup
   - Server crash? No problem
   - Easy to redeploy

5. **Collaboration**
   - Multiple people can work
   - Push/pull changes
   - Code review possible

### ❌ Why NOT to Edit Directly on Server

1. **No version control** - Changes are lost if server dies
2. **No backup** - One mistake = gone forever
3. **Harder to edit** - SSH + nano/vim vs your IDE
4. **No testing** - Changes go live immediately
5. **Risky** - Typo = broken website

## How It Works

### Your Workflow

```bash
# 1. Edit files locally
code scrappykin/public/index.html

# 2. Test locally (optional)
cd scrappykin/public
python3 -m http.server 8000

# 3. Deploy to server
cd ..
./deploy.sh

# 4. Files are uploaded and served
```

### What deploy.sh Does

```bash
# Copies files from local → server
rsync -avz --delete ./public/ vps-hetzner:/opt/services/scrappykin/public/

# Server nginx container serves the files
# No restart needed (nginx serves static files)
```

## Comparison to Other Workflows

### Static Sites (What You're Using) ✅
```
Local → Deploy Script → Server → Nginx → Internet
```
- Simple
- Fast
- Reliable
- Industry standard

### Dynamic Sites (e.g., WordPress)
```
Edit in Browser → Database → Server → Internet
```
- No local copy
- Risky
- Hard to version control
- Not recommended for modern dev

### Git-Based Deployment (Advanced)
```
Local → Git Push → GitHub → CI/CD → Server → Internet
```
- Most professional
- Automated testing
- Can add later if needed

## Your Current Setup

**Local (Source)**
- `/Users/jonamar/Development/generic-vps-hetzner/scrappykin/`
- Edit here
- Version control here
- Test here

**Server (Production)**
- `/opt/services/scrappykin/`
- Files copied here by deploy.sh
- Nginx serves from here
- Don't edit here

## Best Practices

### ✅ DO
- Edit files locally
- Test before deploying
- Use git for version control
- Run `./deploy.sh` to publish changes
- Keep local folder as source of truth

### ❌ DON'T
- SSH into server to edit HTML
- Edit files directly in `/opt/services/scrappykin/`
- Delete local folder (it's your source!)
- Skip testing before deploying

## Adding Version Control (Optional)

Want to track changes with git?

```bash
cd /Users/jonamar/Development/generic-vps-hetzner/scrappykin

# Initialize git
git init

# Add .gitignore (already exists)
git add .gitignore

# Add all files
git add .

# First commit
git commit -m "Initial Scrappy Kin website"

# Optional: Push to GitHub
git remote add origin https://github.com/yourusername/scrappykin.git
git push -u origin main
```

## Summary

**Question**: "Shouldn't this content be on the server not local?"

**Answer**: It IS on the server (after you deploy), but you EDIT it locally. This is the standard, professional way to develop websites.

**Think of it like**:
- **Local folder** = Your workshop where you build things
- **Server folder** = The store where customers see the finished product
- **deploy.sh** = The delivery truck that moves things from workshop → store

---

**This is the correct workflow!** You're doing it right. 👍
