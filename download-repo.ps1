# PowerShell script to download repository files without Git
# This downloads the main files from your GitHub repository

Write-Host "Downloading repository files from GitHub..." -ForegroundColor Yellow

$repoUrl = "https://raw.githubusercontent.com/Arash-MH68/zic0n.github.io/main"
$files = @("index.html", "CNAME")

# Create function to download file
function Download-File {
    param (
        [string]$Url,
        [string]$OutputPath
    )
    
    try {
        $response = Invoke-WebRequest -Uri $Url -UseBasicParsing
        $response.Content | Out-File -FilePath $OutputPath -Encoding UTF8
        Write-Host "Downloaded: $OutputPath" -ForegroundColor Green
        return $true
    } catch {
        Write-Host "Failed to download: $OutputPath" -ForegroundColor Red
        Write-Host "Error: $_" -ForegroundColor Red
        return $false
    }
}

# Download each file
$successCount = 0
foreach ($file in $files) {
    $fileUrl = "$repoUrl/$file"
    if (Download-File -Url $fileUrl -OutputPath $file) {
        $successCount++
    }
}

Write-Host "`nDownloaded $successCount of $($files.Count) files." -ForegroundColor $(if ($successCount -eq $files.Count) { "Green" } else { "Yellow" })
Write-Host "`nNote: This only downloads the main files. For full Git functionality," -ForegroundColor Yellow
Write-Host "install Git and use the connect-repo.ps1 script instead." -ForegroundColor Yellow

