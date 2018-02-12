$log_file = 'C:\Scripts\slack_bot_log.txt'
if (-not (test-path $log_file)) {  New-Item $log_file}
if(-not (gps pythonw)) {
    Start-ScheduledTask -TaskPath \ -TaskName 'Slack Bot'
    Write-Output "Slack Bot restarted on: $(date)" >> $log_file
}
else {
    Write-Output "Slack Bot is still running: $(date)" >> $log_file
}