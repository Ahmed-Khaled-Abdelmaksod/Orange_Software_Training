from app_management import app_management
from user_management import user_management
import time


choice = 0 # Global variable to store user choice

# Function to get the choice of the user to determind the operation 
def main_menu():
    global choice
    print("choose one of the following:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. complete Task")
    print("4. delete Task")
    print("5. Log out")
    # handle value error
    try:
        choice = int(input("Choose one option: "))
        if 1 <= choice <= 5: # choice must be 1 or 2 or 3 or 4 or 5
            pass
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# used to create animation ....... 
def animation():
    for i in range(15):
        time.sleep(0.1)
        print(".", end='', flush=True)  # flush=True ensures the print happens immediately
    print()  # Move to the next line after the animation finishes


# used to create animation at the start of the project 
def start_animation():
    print("Application Starting", end=' ')
    animation()

# used to create animation at the end of the project
def end_animation():
    print("Application Closing", end=' ')
    animation()

# main logic of the program
def app_start():
    # Initialize the task management and user management systems
    app = app_management()
    users = user_management()
    
    # Start a visual animation indicating the application is loading
    start_animation()
    
    # Add a default admin user with username 'admin' and password '123'
    users.add_user("admin", '123')
    
    login_flag = False
    
    # Prompt the user to log in until successful
    while not login_flag:
        username = input("Enter your username: ")  # Prompt for username
        password = input("Enter your password: ")  # Prompt for password
        
        # Validate login, loop continues until the login is successful
        login_flag = users.login(username, password)
    
    # Main application loop, runs continuously until the user chooses to exit
    while True:
        # Display the main menu
        main_menu()
        
        # Add a new task
        if choice == 1:
            title = input('Title: ')  # Prompt for task title
            description = input('Description: ')  # Prompt for task description
            due_date = input('Due Date: ')  # Prompt for task due date
            
            # Add the task via app_management and check if it was successfully added
            status = app.add_task(title, description, due_date)
            if status:
                print("Task added successfully!!")
                time.sleep(1)  # Pause for a second to confirm task added
            
        # View all tasks
        elif choice == 2:
            app.view_tasks()  # Call the method to display all tasks
        
        # Mark a task as complete
        elif choice == 3:
            title = input('Enter the title of the task to complete: ')  # Prompt for task title
            app.complete_task(title)  # Mark the task as completed by its title
        
        # Delete a task
        elif choice == 4:
            title = input('Enter the title of the task to delete: ')  # Prompt for task title
            app.delete_task(title)  # Delete the task by its title
        
        # Exit the application
        elif choice == 5:
            break  # Break out of the loop, ending the application
        
        # Print a separator for better UI experience
        print('-' * 50)
    
    # End visual animation indicating the application is closing
    end_animation()


if __name__ == '__main__':
    app_start()