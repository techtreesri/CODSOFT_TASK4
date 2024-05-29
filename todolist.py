import json
import os

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = {'id': task_id, 'description': description, 'completed': False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task {task_id} added successfully.")

    def view_task(self, task_id):
        task = next((task for task in self.tasks if task['id'] == task_id), None)
        if task:
            print(f"ID: {task['id']}")
            print(f"Description: {task['description']}")
            print(f"Completed: {task['completed']}")
        else:
            print(f"No task found with ID {task_id}.")

    def update_task(self, task_id, description=None):
        task = next((task for task in self.tasks if task['id'] == task_id), None)
        if task:
            if description:
                task['description'] = description
            self.save_tasks()
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"No task found with ID {task_id}.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted successfully.")

    def list_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(f"ID: {task['id']}")
                print(f"Description: {task['description']}")
                print(f"Completed: {task['completed']}")
                print("-" * 20)
        else:
            print("No tasks found.")

    def mark_complete(self, task_id):
        task = next((task for task in self.tasks if task['id'] == task_id), None)
        if task:
            task['completed'] = True
            self.save_tasks()
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"No task found with ID {task_id}.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. List Tasks")
        print("6. Mark Task as Complete")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            task_id = int(input("Enter task ID to view: "))
            todo_list.view_task(task_id)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new task description (leave blank to keep current): ")
            todo_list.update_task(task_id, description if description else None)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.mark_complete(task_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
