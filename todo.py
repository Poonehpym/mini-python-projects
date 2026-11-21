FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


tasks = load_tasks()

while True:
    print("\n=== My To-Do List ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        task = input("New task: ")
        tasks.append(task)
        save_tasks(tasks)
        print(f"Added: {task}")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to remove!")
        else:
            show_tasks(tasks)
            try:
                num = int(input("Task number to remove: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            except ValueError:
                print("Please enter a number.")
            except IndexError:
                print("No task with that number.")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Please choose 1 to 4")