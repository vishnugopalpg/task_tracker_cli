import json
import os
from task import Task

class TaskManager:
    TASKS_FILE = "tasks.json"

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.TASKS_FILE):
            return []
        with open(self.TASKS_FILE, 'r') as file:
            try:
                return [Task(**task) for task in json.load(file)]
            except json.JSONDecodeError:
                print("Error loading tasks from file.")
                return []

    def save_tasks(self):
        """Writes the tasks to the JSON file."""
        with open(self.TASKS_FILE, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        """Adds a new task."""
        task_id = (self.tasks[-1].id + 1) if self.tasks else 1  # Safely get new ID
        new_task = Task(task_id, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully (ID: {new_task.id})")

    def update_task(self, task_id, description):
        """Updates an existing task's description."""
        task = self.get_task_by_id(task_id)
        if task:
            task.update(description=description)
            self.save_tasks()
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Deletes a task by ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted successfully.")

    def mark_in_progress(self, task_id):
        """Marks a task as in-progress."""
        task = self.get_task_by_id(task_id)
        if task:
            task.update(status="in-progress")
            self.save_tasks()
            print(f"Task {task_id} marked as in-progress.")
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_done(self, task_id):
        """Marks a task as done."""
        task = self.get_task_by_id(task_id)
        if task:
            task.update(status="done")
            self.save_tasks()
            print(f"Task {task_id} marked as done.")
        else:
            print(f"Task with ID {task_id} not found.")

    def list_tasks(self, status=None):
        """Lists all tasks, optionally filtered by status."""
        if not self.tasks:
            print("No tasks found.")
            return

        filtered_tasks = self.tasks if status is None else [task for task in self.tasks if task.status == status]

        for task in filtered_tasks:
            print(f"ID: {task.id}, Description: {task.description}, Status: {task.status}, Updated At: {task.updated_at}")

    def get_task_by_id(self, task_id):
        """Finds a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
