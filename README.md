# Task Tracker (CLI & GUI)

This is a simple task management application built as a learning project. It was developed by following the [Python Developer roadmap](https://roadmap.sh/python) on roadmap.sh to practice fundamental programming skills.

The project includes two interfaces to manage tasks:

1.  A **Command-Line Interface (CLI)** for quick, terminal-based interactions.
2.  A **Graphical User Interface (GUI)** for a more visual, user-friendly experience.

## Features

  * ✅ Add, edit, and delete tasks.
  * 🔄 Update task status (`todo`, `in-progress`, `done`).
  * 📊 View all tasks, neatly grouped by status.
  * 💾 Task data is stored locally in a `todolist.json` file.
  * 🐍 Built with standard Python libraries only (no external dependencies).

## Setup

1.  Ensure you have Python 3 installed on your system.

2.  Clone this repository or download the files to a local directory.

    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

No further installation is needed.

## Usage

You can interact with the task tracker using either the CLI or the GUI.

### 1\. Command-Line Interface (`task_tracker.py`)

Run all commands from your terminal in the project directory.

  * **List all tasks (grouped by status):**

    ```bash
    python task_tracker.py list
    ```

  * **Add a new task:**

    ```bash
    python task_tracker.py add "Your new task description"
    ```

  * **Edit a task's description:**

    ```bash
    python task_tracker.py edit <ID> "Your updated description"
    ```

    *Example:* `python task_tracker.py edit 2 "Buy fresh milk and bread"`

  * **Delete a task:**

    ```bash
    python task_tracker.py delete <ID>
    ```

    *Example:* `python task_tracker.py delete 3`

  * **Update a task's status:**

    ```bash
    # Mark as in-progress
    python task_tracker.py mark-in-progress <ID>

    # Mark as done
    python task_tracker.py mark-done <ID>
    ```

    *Example:* `python task_tracker.py mark-done 1`

### 2\. Graphical User Interface (`task_gui.py`)

The GUI provides a more visual way to manage your tasks.

  * **Launch the application:**
    ```bash
    python task_gui.py
    ```
  * **How to Use:**
      * **Add:** Type a description in the input box and click "Add Task".
      * **Update/Delete:** First, click on a task in the list to select it. Then, click the "Mark Done" or "Delete Task" button.

## Learning Context

This project was built to practice core Python concepts, including:

  * File I/O with JSON for data persistence.
  * Handling command-line arguments with the `sys` module.
  * Structuring a program with functions and a `main` entry point.
  * Building a basic desktop GUI with the built-in `Tkinter` library.
  * Separating application logic (backend) from the user interface (frontend).
