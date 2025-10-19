# Task Scheduler (Demo)

A Python automation script that runs tasks at scheduled intervals using data from a CSV file.

## Features
- Reads scheduled tasks from `tasks.csv`
- Executes actions automatically in a loop
- Logs task execution times to `logs.txt`
- Easy to customize for automation or monitoring

## Example `tasks.csv`
```
task_name,interval_seconds,action
Check Emails,5,print('📨 Checking inbox...')
Backup Files,10,print('💾 Backing up files...')
Send Report,15,print('📊 Generating daily report...')
```

## How to Run
```bash
python main.py
```

## Example Output
```
Loaded tasks:
- Check Emails (every 5s)
- Backup Files (every 10s)
- Send Report (every 15s)

Starting scheduler... Press Ctrl+C to stop.

Running task: Check Emails
📨 Checking inbox...
Running task: Backup Files
💾 Backing up files...
Running task: Send Report
📊 Generating daily report...
```
