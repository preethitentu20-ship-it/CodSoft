# To-Do List Application
tasks = []
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
while True:
    show_menu()
    choice = input("Enter your choice: ")
    # Add Task
    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    # View Tasks
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Update Task
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = int(input("Enter task number to update: "))

            if 1 <= task_num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == '4':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1): 
                print(f"{i}. {task}")

            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == '5':
        print("Exiting To-Do List Application.")
        break

    else:
        print("Invalid choice. Please try again.")