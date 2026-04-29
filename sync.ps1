# Nu Micro — Auto sync to GitHub
# Runs on schedule via Windows Task Scheduler
# Pushes: scripts/, source_text/, NU_Micro_Study_Method.md, README.md, sync.ps1
# Does NOT push: PDFs, pptx, docx (synced via Dropbox instead — see .gitignore)

$repo = "C:\Users\User\Dropbox\Nu micro"
$logFile = "$repo\sync_log.txt"

Set-Location $repo

# Check if there's anything new in tracked/trackable files only
$status = git status --porcelain 2>&1

if ($status) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    # Add only text files and scripts — .gitignore blocks PDFs/pptx/docx automatically
    git add -A
    git commit -m "Auto-sync: $timestamp"
    git push origin master
    Add-Content $logFile "[$timestamp] Synced"
    Write-Host "Synced at $timestamp"
} else {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    Add-Content $logFile "[$timestamp] Nothing to sync"
    Write-Host "Nothing new to sync."
}
