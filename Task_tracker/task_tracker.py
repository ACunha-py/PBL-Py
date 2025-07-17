import sys  # command-line arguments
import json  # read and write JSON - database
from datetime import datetime

#create constant for filename - if it needs changing, this is the place.
task_file = "todolist.json"

# Creating a [helper] grouping function
def print_task_group(title, tasks_in_group):
    """Prints a formatted group of tasks"""
    print(f"------------------------------ {title.upper()} ------------------------------")
    if not tasks_in_group:
        print("No tasks found in this category.")
    else:
        tasks_in_group.sort(key=lambda x: x['id']) # Sorts tasks by ID
        print(f"{'ID':<4} | {'Status':<12} | {'Last Updated':<20} | {'Description'}")


        for task in tasks_in_group:
            updated_time = task['updatedAt'][:16].replace('T', ' ')
            print(f"{task['id']:<4} | {task['status']:<12} | {updated_time:<20} | {task['description']}")

# Creating a [helper] display function
def get_tasks():
    """ Shows a list of all tasks """
    try:
        with open(task_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Creating the display function
def display_tasks():
    """loads and displays all tasks."""
    try:
        with open(task_file, 'r') as f:  # If you find the task, then load the file
            tasks = json.load(f)
    except FileNotFoundError:  # otherwise, give me a blank list.
        tasks = []
## Create separate lists for each status
    todo_tasks = [task for task in tasks if task['status'] == 'todo']
    in_progress_tasks = [task for task in tasks if task['status'] == 'in-progress']
    done_tasks = [task for task in tasks if task ['status'] == 'done']

## Call the helper function to print each group.
    print_task_group("To do", todo_tasks)
    print(" ")
    print_task_group("In Progress", in_progress_tasks)
    print(" ")
    print_task_group("Done", done_tasks)

    print("-"*70)

# Creating the add_task function
def add_task(description: str):
    """ Deals with the logic for loading, updating and saving tasks. """
    # Let's try to load existing tasks from the JSON File.
    ## Let's create a 'try...except' as a failsafe in case the file doesn't exist yet.
    try:
        with open(task_file, "r") as f:  # "r" stands for read-mode.
            tasks = json.load(f)  # Creates a list in Python.
    except FileNotFoundError:
        tasks = []  # If the file isn't found, create an empty list.

    ## ID the new task - new_id
    ### Find the highest existing ID and +1
    #### If the task list is empty we'll use +[0]
    if tasks:
        new_id = max(task['id'] for task in tasks) + 1
    else:
        new_id = 1

    ## Create a dictionary
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),  # format type YYYY-MM-DD HH:MM:SS
        "updatedAt": datetime.now().isoformat()
    }
    ## Let's add the new task to the list.
    tasks.append(new_task)

    ## Rewrite the file with the updated list.
    with open(task_file, "w") as f:  ### w = write mode
        json.dump(tasks, f, indent=4)  ### json.dump converts from .py to .json. // indent=4 was a recommendation I saw.
    print(f"✅ Task added successfully (Id: {new_id})")
    return True


# Creating the delete task function
def delete_task(task_id: int):
    """ Deletes a task using its ID. """
    ## Let's load the existing tasks
    try:
        with open(task_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("❌: No tasks found. The task file does not exist.")
        return False

    ## Now let's create a new list without the task to be deleted.
    tasks_after_deletion = [task for task in tasks if task["id"] != task_id]

    ## Is the task actually deleted?
    if len(tasks) == len(tasks_after_deletion):
        print(f"❌: Task with ID {task_id} not found.")
        return False
    else:  ### Rewrite the list in the file.
        with open(task_file, 'w') as f:
            json.dump(tasks_after_deletion, f, indent=4)
        print(f"✅ Task with ID {task_id} deleted successfully.")
        return True


# Creating the edit function
def update_description(task_id: int, new_description: str):
    """ Updates a task's description and it's 'updatedAt' timestamp."""
    ## Let's load the existing tasks
    try:
        with open(task_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("❌: No tasks found. The task file does not exist.")
        return False

    ## Let's find the task and update it
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            task_found = True
            break  #After the task is found and updated, break the loop.

    ## Once that's done, save the file or report an error.
    if task_found:
        with open(task_file, "w") as f:
            json.dump(tasks, f, indent=4)
        print(f"✅ Task with ID {task_id} updated successfully.")
        return True
    else:
        print(f"❌: Task with ID {task_id} not found.")
        return False
def update_status(task_id: int, new_status: str):
    """ Finds a task using ID and updates the status. """
    try:
        with open(task_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("❌: No tasks found.")
        return False

    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            task_found = True
            break

    if task_found:
        with open(task_file, "w") as f:
            json.dump(tasks, f, indent=4)
        print(f"✅ Task {task_id} status updated to '{new_status}'.")
        return True
    else:
        print(f"❌: Task with ID {task_id} not found.")
        return False


# Main function of the program.
def main():
    """Main function that controls the script's flow."""
    if len(sys.argv) < 2:
        print("Expected: python task_tracker.py <command> [arguments]")
        display_tasks()
        return
    ## sys.argv is a list of words the user typed.
    ### If len is >2 then the user didn't type a command.

    command = sys.argv[1]  # The command is the first word after the script's name.
    action_successful = False

    # Structure for commands:
    ## Add command
    if command.lower() == "add":
        if len(sys.argv) < 3:  ## This checks if they provided a description for the task
            print("❌: Task description is missing!")
            print("Example: python task_tracker.py add 'Buy Milk'")
        else:
            description = sys.argv[2]  # The description is the [2] word after the script's name.
            action_successful = add_task(description)

    ## Delete command
    elif command.lower() == "delete":
        if len(sys.argv) < 3:  ## This checks if they provided a viable ID
            print("❌: Missing Task ID for deleting!")
            print("Example: python task_tracker.py delete [ID]")
        else:
            try:  ## If the ID is valid, then it can call the function to delete the task.
                task_id = int(sys.argv[2])
                action_successful = delete_task(task_id)
            except ValueError:
                print("❌: Invalid task ID! The ID must be a number.")

    ## Edit command
    elif command.lower() == "edit":
        if len(sys.argv) < 4:  #This assumes the 4th argument is the new description.
            print("❌: Missing arguments for 'edit' command.")
            print("Example: pythong task_tracker.py edit [id] [New Description]")
        else:
            try:
                task_id = int(sys.argv[2])
                new_description = sys.argv[3]
                action_successful = update_description(task_id, new_description)
            except ValueError:
                print("❌: Invalid ID. The ID must be a number.")


    ## Mark-in-progress function
    elif command.lower() == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("❌: Missing task ID.")
        else:
            try:
                task_id = int(sys.argv[2])
                action_successful = update_status(task_id, "in-progress")
            except ValueError:
                print("❌: Invalid ID. The ID must be a number.")
    ## Mark-done function
    elif command.lower() == 'mark-done':
        if len(sys.argv) < 3:
            print("❌: Missing task ID.")
        else:
            try:
                task_id = int(sys.argv[2])
                action_successful = update_status(task_id, "done")
            except ValueError:
                print("❌: Invalid ID. The ID must be a number.")


    ## Lists command
    elif command.lower() == "list":
        display_tasks()
        return
    ## Unknown command:
    else:
        print(f"❌: Unknown command '{command}'")

    # Display the list after a successful action
    if action_successful:
        display_tasks()


# If the script is being run, then call main() function.
if __name__ == "__main__":
    main()
