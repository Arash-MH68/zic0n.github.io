# Connecting to Your GitHub Repository

## Option 1: Install Git and Clone (Recommended)

1. **Install Git for Windows:**
   - Download from: https://git-scm.com/download/win
   - Run the installer with default settings
   - Restart your terminal/PowerShell after installation

2. **Clone your repository:**
   ```bash
   git clone https://github.com/Arash-MH68/zic0n.github.io.git .
   ```

3. **Verify connection:**
   ```bash
   git remote -v
   ```

## Option 2: Manual Setup (If Git is already installed but not in PATH)

If Git is installed but not recognized, add it to your PATH:
- Git is typically installed at: `C:\Program Files\Git\cmd\git.exe`
- Add this to your system PATH environment variable

## Option 3: Use GitHub Desktop

1. Download GitHub Desktop from: https://desktop.github.com/
2. Sign in with your GitHub account
3. Clone the repository: `https://github.com/Arash-MH68/zic0n.github.io`

## After Connecting:

Once connected, you can:
- Edit files locally
- Commit changes: `git add .` then `git commit -m "your message"`
- Push changes: `git push origin main`

