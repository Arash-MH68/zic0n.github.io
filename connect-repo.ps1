# PowerShell script to connect to your GitHub repository
# Run this script after installing Git

Write-Host "Checking for Git installation..." -ForegroundColor Yellow

# Check if git is available
try {
    $gitVersion = git --version 2>&1
    Write-Host "Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "Git is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "Then restart PowerShell and run this script again." -ForegroundColor Yellow
    exit 1
}

Write-Host "`nSetting up repository connection..." -ForegroundColor Yellow

# Check if .git directory exists
if (Test-Path .git) {
    Write-Host "Repository already initialized." -ForegroundColor Green
    git remote -v
} else {
    Write-Host "Initializing repository and connecting to remote..." -ForegroundColor Yellow
    
    # Check if directory is empty
    $files = Get-ChildItem -Force | Where-Object { $_.Name -ne ".git" }
    if ($files.Count -gt 0) {
        Write-Host "Warning: Directory is not empty. Files may be overwritten." -ForegroundColor Yellow
        $response = Read-Host "Continue? (y/n)"
        if ($response -ne "y") {
            Write-Host "Cancelled." -ForegroundColor Red
            exit 1
        }
    }
    
    # Clone the repository
    Write-Host "Cloning repository..." -ForegroundColor Yellow
    git clone https://github.com/Arash-MH68/zic0n.github.io.git temp_repo
    
    if ($LASTEXITCODE -eq 0) {
        # Move files from temp_repo to current directory
        Move-Item -Path "temp_repo\*" -Destination "." -Force
        Move-Item -Path "temp_repo\.git" -Destination "." -Force -ErrorAction SilentlyContinue
        Remove-Item -Path "temp_repo" -Recurse -Force
        
        Write-Host "`nRepository connected successfully!" -ForegroundColor Green
        Write-Host "Your repository files are now in this directory." -ForegroundColor Green
        
        git remote -v
    } else {
        Write-Host "Failed to clone repository. Please check your internet connection and try again." -ForegroundColor Red
        exit 1
    }
}

Write-Host "`nSetup complete!" -ForegroundColor Green

