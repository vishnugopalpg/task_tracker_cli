
from datetime import datetime

class Task:
    def __init__(self, task_id, description, status="todo"):
        self.id = task_id
        self.description = description
        self.status = status
        self.created_at = self.current_time()
        self.updated_at = self.current_time()

    def current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Converts task object to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_At": self.updated_at
        }

    def update(self, description=None, status=None):
        """Updates the task description or status."""
        if description:
            self.description = description
        if status:
            self.status = status
        self.updated_at = self.current_time()