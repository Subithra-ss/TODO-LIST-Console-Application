import os

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = {
            'title': title,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        print("\nTask added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
            return
        print("\n--- To-Do List ---")
        for idx, task in enumerate(self.tasks, 1):
            status = "✔️" if task['completed'] else "❌"
            print(f"{idx}. [{status}] {task['title']} - {task['description']}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print("\nTask marked as completed!\n")
        else:
            print("\nInvalid task number.\n")

    def edit_task(self, task_number, new_title, new_description):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['title'] = new_title
            self.tasks[task_number - 1]['description'] = new_description
            print("\nTask updated successfully!\n")
        else:
            print("\nInvalid task number.\n")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            print("\nTask deleted successfully!\n")
        else:
            print("\nInvalid task number.\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    manager = TaskManager()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-6): "))
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
            continue

        if choice == 1:
            title = input("\nEnter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)
        elif choice == 2:
            manager.view_tasks()
        elif choice == 3:
            manager.view_tasks()
            try:
                task_number = int(input("\nEnter task number to mark as completed: "))
                manager.mark_task_completed(task_number)
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        elif choice == 4:
            manager.view_tasks()
            try:
                task_number = int(input("\nEnter task number to edit: "))
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                manager.edit_task(task_number, new_title, new_description)
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        elif choice == 5:
            manager.view_tasks()
            try:
                task_number = int(input("\nEnter task number to delete: "))
                manager.delete_task(task_number)
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        elif choice == 6:
            print("\nExiting application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1-6.\n")
        
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()
