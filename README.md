Task Tracker
============

Simple, console-based personal Task Tracker implemented in Python. It provides
basic task management operations you can run from a terminal using a menu-driven
interface.

Quick Features
--------------
- Create tasks (title + description)
- List all tasks with ID, title, description and status
- Update task title and description
- Delete tasks by ID
- Mark tasks as TODO, In Progress, or Completed

Files
-----
- [Task_Tracker/Task_Tracker.py](Task_Tracker/Task_Tracker.py): Main menu and
	task-management implementation (class-based).
- [Task_Tracker/Tasks.py](Task_Tracker/Tasks.py): Alternative, dictionary-style
	helper functions for a simpler task store.

Requirements
------------
- Python 3.8+

Installation
------------
No dependencies. Clone or copy the `Task_Tracker` folder and run with Python:

```bash
python Task_Tracker/Task_Tracker.py
```

Usage
-----
Run the script and follow the numbered menu. The menu options are:

1. Create Task - enter a title and description when prompted.
2. List Task - prints all tasks and their statuses.
3. Update Task - update title and description for an existing task ID.
4. Delete Task - remove a task by ID.
5. Mark Task as Complete - set status to Completed.
6. Mark Task as In Progress - set status to In Progress.
7. Mark Task as Done - sets status back to TODO.
8. Exit - quit the program.

Notes & Known Issues
--------------------
- The `Task_Tracker.py` implementation stores tasks in memory for the running
	session only (no persistence). Closing the program will lose all tasks.
- There is a minor bug in the `update` flow: the order of parameters when calling
	`update_task()` in the menu does not match the function signature. If you need
	to use update right away, open [Task_Tracker/Task_Tracker.py](Task_Tracker/Task_Tracker.py)
	and search for the `case 3` block to fix the argument order.

Contributing
------------
- Feel free to add file-backed persistence (JSON/SQLite), a CLI argument mode,
	or unit tests. Open a PR with small, focused commits.

License
-------
This repository does not include a license file. Add one if you plan to
redistribute or open-source the code.