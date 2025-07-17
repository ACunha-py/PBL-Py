import tkinter as tk
from tkinter import messagebox
from task_tracker import get_tasks, add_task, delete_task, update_status


# Functions
## Helper function
def get_selected_task_id():
    try:
        selected_item = task_listbox.get(task_listbox.curselection()) # Gets the selected item
        task_id = int(selected_item.split(" | ")[0].replace("ID ", ""))
        return task_id
    except:
        messagebox.showwarning("⚠️ Selection error!⚠️","Please select a task from the list.")
        return None


## Callback Function
def refresh_task_list():
    task_listbox.delete(0,tk.END) # Clear the listbox
    tasks = get_tasks() #Get the tasks
    for task in tasks: #for loop
        display_text = f"ID {task['id']} | {task['status']} | {task['description']}"
        task_listbox.insert(tk.END, display_text)


## Button logic
def add_task_gui():
    description = task_entry.get() #entry widget adds description
    if description:
        add_task(description)
        task_entry.delete(0, tk.END)
        refresh_task_list()

def delete_task_gui():
    task_id = get_selected_task_id()
    if task_id is not None:
        if delete_task(task_id):
            refresh_task_list()

def mark_done_gui():
    task_id = get_selected_task_id()
    if task_id is not None:
        update_status(task_id, "done")
        refresh_task_list()


# GUI Setup
## Program Window
root_window = tk.Tk()


## Program Information
### Title Bar text
root_window.title("Task Tracker")


## Frame to hold widgets
### This frame will hold the entry box and button
entry_frame = tk.Frame(root_window)


## Widgets
task_listbox = tk.Listbox(root_window, height=15)
task_listbox.pack(pady=10, padx=10, fill="x")
action_frame = tk.Frame(root_window)
action_frame.pack(pady = 10)


## Pack the frame so it and its contents become visible
entry_frame.pack(pady=5)


## Widget creation
task_entry = tk.Entry(entry_frame, width=40)
task_entry.pack(side="left", padx=5)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task_gui)
add_button.pack(side="left")

done_button = tk.Button(action_frame, text= "Mark Done", command = mark_done_gui)
done_button.pack(side="left", padx=5)

delete_button = tk.Button(action_frame, text="Delete Task", command=delete_task_gui)
delete_button.pack(side="left")


# Run application
refresh_task_list() # retrieve initial load
root_window.mainloop() # start the main event loop