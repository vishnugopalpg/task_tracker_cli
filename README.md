# Task Tracker CLI

A simple command line tool to track tasks.

## Usage

```bash
# Adding a new task
python task_cli.py add "Buy groceries"

# Updating a task
python task_tracker_cli.py update 1 "Buy groceries and cook dinner"

# Deleting a task
python task_tracker_cli.py delete 1

# Mark a task as in progress
python task_tracker_cli.py mark-in-progress 1

# Mark a task as done
python task_tracker_cli.py mark-done 1

# List all tasks
python task_tracker_cli.py list

# List tasks by status
python3 task_tracker_cli list done
python3 task_tracker_cli list todo
python3 task_tracker_cli list in-progress
