# Claude Code Remote Control — auto-start on login
# Keeps a background session named "Micro" running
# Connect from phone via Claude app > Sessions > "Micro"

$claudeExe = "C:\Users\User\.local\bin\claude.exe"
$logPath = "C:\Users\User\Dropbox\Nu micro\remote_control.log"

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
Add-Content $logPath "[$timestamp] Starting Remote Control session 'Micro'..."

# Start in background, log output
Start-Process -FilePath $claudeExe `
    -ArgumentList "--remote-control", "--name", "Micro" `
    -NoNewWindow `
    -RedirectStandardOutput $logPath `
    -RedirectStandardError $logPath
