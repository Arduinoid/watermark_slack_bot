if(-not (gps pythonw)) {
    Start-ScheduledTask -TaskPath \ -TaskName 'Slack Bot'
    Write-Output "Slack Bot restarted on: $(date)" >> 'C:\Scripts\slack_bot_log.txt'
}
else {
    Write-Output "Slack Bot is still running: $(date)" >> 'C:\Scripts\slack_bot_log.txt'
}