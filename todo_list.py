# Define an empty list to store tasks
tasks = []

# Function to add a new task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")


# Function to display all tasks in the list
def show_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("The to-do list is empty.")

# Function to remove a task from the list
def remove_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index.")

# Main function that runs the program
def main():
    print("Welcome to the To-Do List!")

    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Option: ")

        if choice == '1':
            task = input("Enter the new task: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number to be removed: "))
            remove_task(task_index)
        elif choice == '4':
            print("Thank you for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

# Check if this script is the main script to be executed
if __name__ == "__main__":
    main()
