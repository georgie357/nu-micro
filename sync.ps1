# Nu Micro — Auto sync to GitHub
# Runs on schedule, pushes any new files from instructor

$repo = "C:\Users\User\Dropbox\Nu micro"
$logFile = "$repo\sync_log.txt"

Set-Location $repo

# Check if there's anything new
$status = git status --porcelain 2>&1

if ($status) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    git add -A
    git commit -m "Auto-sync: new files added $timestamp"
    git push origin master
    Add-Content $logFile "[$timestamp] Synced: $status"
    Write-Host "Synced new files at $timestamp"
} else {
    Write-Host "Nothing new to sync."
}
