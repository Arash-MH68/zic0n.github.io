# Quick Start Guide - Connect to GitHub

Your repository is pre-configured and ready to connect once Git is installed.

## Step 1: Install Git
Download and install from: https://git-scm.com/download/win
- Use default settings during installation
- **Important:** Restart PowerShell/terminal after installation

## Step 2: Connect to GitHub (First Time)

After installing Git and restarting PowerShell, run these commands in this directory:

```powershell
# Verify Git is installed
git --version

# Initialize the repository (if not already initialized)
git init

# Connect to your GitHub repository
git remote add origin https://github.com/Arash-MH68/zic0n.github.io.git

# Stage all files
git add .

# Create your first commit
git commit -m "Initial commit - connected to GitHub"

# Set main branch
git branch -M main

# Push to GitHub (you'll need to authenticate)
git push -u origin main
```

## Step 3: Authentication

When you run `git push`, you'll need to authenticate:
- **Option A:** Use a Personal Access Token (recommended)
  - Create one at: https://github.com/settings/tokens
  - Use it as the password when prompted
- **Option B:** Use GitHub Desktop (easier for beginners)
  - Download: https://desktop.github.com/

## Daily Workflow

Once connected, your daily workflow will be:

```powershell
# Make changes to files...

# Stage changes
git add .

# Commit changes
git commit -m "Description of your changes"

# Push to GitHub
git push origin main
```

## Current Files
- ✅ `index.html` - Your main website file
- ✅ `CNAME` - Custom domain configuration
- ✅ `.git/config` - Pre-configured with your repository URL

Everything is ready! Just install Git and run the commands above.

