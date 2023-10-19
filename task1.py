to_do_list = []
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


def display_list():
    if to_do_list:
        print("To-Do List:")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display the to-do list")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
