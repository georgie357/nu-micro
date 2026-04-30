# Claude Code Remote Control — launch from desktop shortcut
# Starts a named session accessible from phone via Claude app > Sessions > "Micro"

$claudeExe = "C:\Users\User\.local\bin\claude.exe"
$logPath = "C:\Users\User\Dropbox\Nu micro\remote_control.log"

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
Add-Content $logPath "[$timestamp] Starting session 'Micro'..."

# Start minimized console window (Hidden breaks interactive TUI)
Start-Process -FilePath $claudeExe `
    -ArgumentList "--name", "Micro" `
    -WindowStyle Minimized
