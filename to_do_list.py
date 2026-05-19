# Simple To-Do List Program
# This program allows users to add tasks, view tasks, and exit

# Create an empty list to store all tasks
tasks = []

# Create a loop that runs until the user exits
while True:
    # Display menu options to the user
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Exit")
    
    # Ask user to choose an option
    choice = input("Choose an option (1, 2, or 3): ")
    
    # If user chooses 1, add a new task
    if choice == "1":
        # Ask user to enter a task
        task = input("Enter a task: ")
        # Add the task to the tasks list
        tasks.append(task)
        # Confirm that the task was added
        print(f"Task '{task}' added successfully!")
    
    # If user chooses 2, display all tasks
    elif choice == "2":
        # Check if there are any tasks in the list
        if len(tasks) == 0:
            # If list is empty, tell the user
            print("No tasks yet! Add one to get started.")
        else:
            # If there are tasks, display them all
            print("\n--- Your Tasks ---")
            # Use a loop to print each task with a number
            for i in range(len(tasks)):
                # Print task number and the task name
                print(f"{i + 1}. {tasks[i]}")
    
    # If user chooses 3, exit the program
    elif choice == "3":
        # Display goodbye message
        print("Goodbye! Thank you for using To-Do List.")
        # Exit the while loop and end the program
        break
    
    # If user enters something other than 1, 2, or 3
    else:
        # Tell the user to enter a valid option
        print("Invalid choice! Please enter 1, 2, or 3.")