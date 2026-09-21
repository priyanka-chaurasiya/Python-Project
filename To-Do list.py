# ==========================
# To-Do List in Python
# ==========================

# Simple To-Do List Application

tasks = []


# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    
    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully!")


# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\n----- Your Tasks -----")
        
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


# Function to update a task
def update_task():
    view_tasks()

    if len(tasks) > 0:
        try:
            number = int(input("Enter task number to update: "))

            if 1 <= number <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[number - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


# Function to delete a task
def delete_task():
    view_tasks()

    if len(tasks) > 0:
        try:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted_task = tasks.pop(number - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


# Main menu
while True:
    print("\n========================")
    print("       TO-DO LIST")
    print("========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
