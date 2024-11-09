import json
import os
from datetime import datetime

# File to store tasks data
TASKS_FILE = 'tasks.json'

# Helper function to load tasks from JSON file
def load_tasks():
    """Load tasks from the JSON file, or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Helper function to save tasks to the JSON file
def save_tasks(tasks):
    """Save the tasks list to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(tasks, description, due_date, priority):
    """Add a new task to the list."""
    task = {
        'id': len(tasks) + 1,  # Auto-increment task ID
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'status': 'pending'
    }
    tasks.append(task)
    save_tasks(tasks)

# Function to view all tasks
def view_tasks(tasks):
    """Display all tasks with their details."""
    if not tasks:
        print("There are no tasks in the list.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Due: {task['due_date']}, "
              f"Priority: {task['priority']}, Status: {task['status']}")

# Function to mark a task as completed
def mark_completed(tasks, task_id):
    """Mark a specific task as completed."""
    task = get_task_by_id(tasks, task_id)
    if task:
        task['status'] = 'completed'
        save_tasks(tasks)
        print(f"Task {task_id} has been marked as completed!")
    else:
        print(f"No task found with ID {task_id}.")

# Function to find a task by ID
def get_task_by_id(tasks, task_id):
    """Get a task by its ID."""
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# Function to delete a task
def delete_task(tasks, task_id):
    """Delete a task by its ID."""
    task = get_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task {task_id} has been deleted successfully.")
    else:
        print(f"No task found with ID {task_id}.")

# Function to edit an existing task
def edit_task(tasks, task_id, description=None, due_date=None, priority=None):
    """Edit a task's details."""
    task = get_task_by_id(tasks, task_id)
    if task:
        if description: task['description'] = description
        if due_date: task['due_date'] = due_date
        if priority: task['priority'] = priority
        save_tasks(tasks)
        print(f"Task {task_id} has been updated successfully.")
    else:
        print(f"No task found with ID {task_id}.")

# Function to filter tasks by status, priority, or due date
def filter_tasks(tasks, status=None, priority=None, due_date=None):
    """Filter tasks by status, priority, or due date."""
    filtered = tasks
    if status:
        filtered = [task for task in filtered if task['status'] == status]
    if priority:
        filtered = [task for task in filtered if task['priority'] == priority]
    if due_date:
        filtered = [task for task in filtered if task['due_date'] == due_date]

    if filtered:
        for task in filtered:
            print(f"ID: {task['id']}, Description: {task['description']}, Due: {task['due_date']}, "
                  f"Priority: {task['priority']}, Status: {task['status']}")
    else:
        print("No tasks match the provided filters.")

# Function to sort tasks based on a given criteria
def sort_tasks(tasks, criterion='due_date'):
    """Sort tasks by the selected criterion."""
    if criterion not in ['due_date', 'priority', 'description']:
        print("Invalid sort criterion.")
        return
    sorted_tasks = sorted(tasks, key=lambda x: x[criterion])
    for task in sorted_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Due: {task['due_date']}, "
              f"Priority: {task['priority']}, Status: {task['status']}")

# Function to search for tasks by a description keyword
def search_tasks(tasks, keyword):
    """Search tasks by a keyword in the description."""
    results = [task for task in tasks if keyword.lower() in task['description'].lower()]
    if results:
        for task in results:
            print(f"ID: {task['id']}, Description: {task['description']}, Due: {task['due_date']}, "
                  f"Priority: {task['priority']}, Status: {task['status']}")
    else:
        print(f"No tasks found matching '{keyword}'.")

# Function to get user input for task priority with validation
def get_priority_input():
    """Get priority input from the user, ensuring it's valid."""
    while True:
        priority = input("Enter priority (low, medium, high): ").lower()
        if priority in ['low', 'medium', 'high']:
            return priority
        else:
            print("Invalid priority. Please choose from 'low', 'medium', or 'high'.")

# Function to get valid date input from the user
def get_date_input(prompt):
    """Ensure that the user enters a valid date in the format YYYY-MM-DD."""
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please enter the date as YYYY-MM-DD.")

# Display the main menu
def display_menu():
    """Display the application's main menu."""
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Filter Tasks")
    print("7. Sort Tasks")
    print("8. Search Tasks")
    print("9. Exit")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = get_date_input("Enter due date (YYYY-MM-DD): ")
            priority = get_priority_input()
            add_task(tasks, description, due_date, priority)

        elif choice == '2':
            view_tasks(tasks)

        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(tasks, task_id)

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)

        elif choice == '5':
            task_id = int(input("Enter task ID to edit: "))
            description = input("New description (leave blank to skip): ")
            due_date = input("New due date (leave blank to skip): ")
            priority = input("New priority (leave blank to skip): ")
            edit_task(tasks, task_id, description, due_date, priority)

        elif choice == '6':
            status = input("Filter by status (pending/completed): ")
            priority = input("Filter by priority (low, medium, high): ")
            due_date = input("Filter by due date (YYYY-MM-DD): ")
            filter_tasks(tasks, status, priority, due_date)

        elif choice == '7':
            criterion = input("Sort tasks by (due_date/priority/description): ")
            sort_tasks(tasks, criterion)

        elif choice == '8':
            keyword = input("Enter search keyword: ")
            search_tasks(tasks, keyword)

        elif choice == '9':
            print("Exiting application...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
