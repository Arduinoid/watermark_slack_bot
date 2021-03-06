function Deploy-SlackBot ([switch]$Start, [switch]$NoCopy) {
    $source = '\\JON-T3600\C$\Deployment\watermark_slack_bot'
    $destination = '\\NAS-R510\C$\Users\Jon\Documents\watermark_slack_bot'
    if (Test-Path $destination) {
        $destination = '\\NAS-R510\C$\Users\Jon\Documents'
    }
    $server = 'NAS-R510'
    if ((Test-Path $source) -and -not $NoCopy) {
        Write-Host "Beginning to copy files to server..." -ForegroundColor Cyan
        Copy-Item -Path $source -Destination $destination -Force -Recurse -Confirm
        Write-Host "Finished copy process" -ForegroundColor Cyan
    }
    if ($Start) {
        if ((Get-Process -ComputerName $server -Name pythonw -ErrorAction SilentlyContinue)) {
            Write-Host 'Slack Bot was running and will now be stopped...' -ForegroundColor Yellow
            Invoke-Command $server {
                Stop-Process -Name pythonw
                Start-Sleep -Seconds 1
                Start-ScheduledTask -TaskPath \ -TaskName 'Slack Bot'
            }
        }
        else {
            Invoke-Command $server {
                Start-ScheduledTask -TaskPath \ -TaskName 'Slack Bot'
            }
        }
        if (Test-Path "$destination\pid.txt") {
            $process = Get-Content "$destination\pid.txt"
            Write-Host "Slack Bot should now be running on the following process: $process" -ForegroundColor Green
        }
        
    }
}
