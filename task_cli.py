import sys
from task_manager import TaskManager

class TaskCLI:
    def __init__(self):
        self.manager = TaskManager()

    def run(self):
        if len(sys.argv) < 2:
            print("Usage: task-cli [command] [arguments]")
            return

        command = sys.argv[1]

        if command == "add":
            if len(sys.argv) < 3:
                print("Usage: task-cli add [description]")
                return
            description = sys.argv[2]
            self.manager.add_task(description)
        elif command == "list":
            status = sys.argv[2] if len(sys.argv) > 2 else None
            self.manager.list_tasks(status)
        elif command == "update":
            if len(sys.argv) < 4:
                print("Usage: task-cli update [task_id] [new_description]")
                return
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            self.manager.update_task(task_id, new_description)
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Usage: task-cli delete [task_id]")
                return
            task_id = int(sys.argv[2])
            self.manager.delete_task(task_id)
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Usage: task-cli mark-in-progress [task_id]")
                return
            task_id = int(sys.argv[2])
            self.manager.mark_in_progress(task_id)
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Usage: task-cli mark-done [task_id]")
                return
            task_id = int(sys.argv[2])
            self.manager.mark_done(task_id)
        else:
            print("Unknown command")

if __name__ == "__main__":
    cli = TaskCLI()
    cli.run()
