# Import datetime module to handle date-related operations for the current date.
import datetime

# Open and read user data from the file.
with open("user.txt", "r") as file_passwords:
    dict_users = {}  # Dictionary to store usernames and passwords.

    # Loop through each line in the text file,
    # splitting each line into username and password,
    # and adding them as key-value pairs to the dictionary.
    for line in file_passwords:
        username, password = line.strip().split(", ")
        dict_users[username] = password


# Prompt the user to log in.
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in dict_users and dict_users[username] == password:
        print("Login Successful!")
        break  # Exit the loop once valid credentials are provided.
    else:
        print("Invalid username or password. Please try again.")


# Initialize main menu loop for user interaction.
while True:
    menu = input(
        '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics (admin only)
e - exit
: '''
    ).lower()

    # Option to register a new user.
    if menu == 'r':
        if username == "admin":  # Only admin can register new users.
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            confirm_password = input("Renter new password: ")

            if new_password == confirm_password:  # Checking if passwords match.
                with open("user.txt", "a") as user_file:
                    user_file.write(f"\n{new_username}, {new_password}")
            else:
                print("Passwords do not match, please re-enter passwords.")
        else:
            print("You cannot register a new user because you are not admin.")

    # Option to add a new task.
    elif menu == 'a':
        user_task = input("Enter the username of the user the task is assigned to: ")
        title_of_task = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (e.g., 20 Dec 2020): ")
        current_date = datetime.datetime.now().strftime("%d-%b-%Y")

        with open("tasks.txt", "a") as task_file:
            task_file.write(
                f"\n{user_task}, {title_of_task}, {task_description}, "
                f"{current_date}, {due_date}, No"
            )
        print("Task added successfully.")

    # Option to view all tasks.
    elif menu == 'va':
        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                task_data = line.strip().split(", ")

                print("-----------------------")
                print(f"Task: {task_data[1]}")
                print(f"Assigned to: {task_data[0]}")
                print(f"Date assigned: {task_data[3]}")
                print(f"Due date: {task_data[4]}")
                print(f"Task complete? {task_data[5]}")
                print(f"Task description:\n{task_data[2]}")
                print("------------------------")

    # Option to view tasks assigned to the logged-in user.
    elif menu == 'vm':
        with open("tasks.txt", "r") as task_file:
            user_tasks_found = False

            for line in task_file:
                task_data = line.strip().split(", ")

                if task_data[0] == username:
                    user_tasks_found = True

                    print('---------------------')
                    print(f"Task: {task_data[1]}")
                    print(f"Assigned to: {task_data[0]}")
                    print(f"Date assigned: {task_data[3]}")
                    print(f"Due date: {task_data[4]}")
                    print(f"Task complete? {task_data[5]}")
                    print(f"Task description:\n{task_data[2]}")
                    print('---------------------')
            if not user_tasks_found:
                print("No tasks found for your username.")

    # Option to display statistics (admin only).
    elif menu == 'ds':
        if username == "admin":
            with open("tasks.txt") as task_file:
                total_tasks = len(task_file.readlines())

            with open("user.txt", "r") as user_file:
                total_users = len(user_file.readlines())

            print("\nStatistics:")
            print(f"Total number of tasks: {total_tasks}")
            print(f"Total number of users: {total_users}\n")
        else:
            print("Only the admin can display the statistics.")

    # Option to exit the program.
    elif menu == 'e':
        print("Goodbye!")
        exit()

    # Handle invalid input.
    else:
        print("You have entered an invalid input. Please try again.")