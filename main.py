import csv
import time
from datetime import datetime

def load_tasks(file_path):
    tasks = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tasks.append({
                "task_name": row["task_name"],
                "interval_seconds": int(row["interval_seconds"]),
                "action": row["action"]
            })
    return tasks


def execute_action(action_text):
    try:
        exec(action_text)
    except Exception as e:
        print(f"⚠️ Error executing action: {e}")


def log_task(task_name):
    with open("logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Task executed: {task_name}\n")


def main():
    tasks = load_tasks("tasks.csv")
    print("Loaded tasks:")
    for t in tasks:
        print(f"- {t['task_name']} (every {t['interval_seconds']}s)")

    print("\nStarting scheduler... Press Ctrl+C to stop.\n")

    last_run = {task["task_name"]: 0 for task in tasks}

    try:
        while True:
            current_time = time.time()
            for task in tasks:
                if current_time - last_run[task["task_name"]] >= task["interval_seconds"]:
                    print(f"Running task: {task['task_name']}")
                    execute_action(task["action"])
                    log_task(task["task_name"])
                    last_run[task["task_name"]] = current_time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


if __name__ == "__main__":
    main()
