def view_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\n No tasks found!\n")
            else:
                print("\n Your To-Do List:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("\n No tasks found!\n")


# Function to add a new task
def add_task():
    task = input(" Enter new task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!\n")


# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{removed.strip()}' deleted!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")
    except FileNotFoundError:
        print(" No tasks to delete!\n")


# Main program loop
while True:
    print("====== TO-DO APP ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter between 1-4.\n")