# To-Do List CLI App
# CodeOrbit Tech - Python Programming Internship

tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\n===== YOUR TASKS =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter a task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def remove_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice. Please try again.")


main()