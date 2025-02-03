# Todo List Application

A simple command-line todo list manager written in Python. This application allows you to manage your tasks efficiently through various commands.

This project is inspired by and follows some concepts from the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker).

## Features

- Add new tasks
- List all tasks (with optional status filter)
- Update existing tasks
- Mark tasks as in-progress or done
- Delete tasks

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the `Task-Tracker.py` file.
2. Ensure you have Python 3.6 or higher installed on your system.

## Usage

Run the script using Python from the command line:

```
python Task-Tracker.py <command> [options]
```

### Available Commands

1. **Add a new task**
   ```
   python Task-Tracker.py add "Task description"
   ```

2. **List tasks**
   - List all tasks:
     ```
     python Task-Tracker.py list
     ```
   - List tasks with a specific status:
     ```
     python Task-Tracker.py list [todo|in-progress|done]
     ```

3. **Update a task**
   ```
   python Task-Tracker.py update <task_id> "New task description"
   ```

4. **Mark a task as in-progress**
   ```
   python Task-Tracker.py mark-in-progress <task_id>
   ```

5. **Mark a task as done**
   ```
   python Task-Tracker.py mark-done <task_id>
   ```

6. **Delete a task**
   ```
   python Task-Tracker.py delete <task_id>
   ```

## Data Storage

The application stores tasks in a JSON file named `data.json` in the same directory as the script. This file is created automatically when you add your first task.

## Example Usage

1. Add a new task:
   ```
   python Task-Tracker.py add "Complete the project proposal"
   ```

2. List all tasks:
   ```
   python Task-Tracker.py list
   ```

3. Mark a task as in-progress:
   ```
   python Task-Tracker.py mark-in-progress 1
   ```

4. Update a task description:
   ```
   python Task-Tracker.py update 1 "Complete and submit the project proposal"
   ```

5. Mark a task as done:
   ```
   python Task-Tracker.py mark-done 1
   ```

6. List only completed tasks:
   ```
   python Task-Tracker.py list done
   ```

7. Delete a task:
   ```
   python Task-Tracker.py delete 1
   ```

## Contributing

Feel free to fork this project and submit pull requests with any improvements or bug fixes. For ideas on how to extend this project, check out the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker).

## License

This project is open source and available under the [MIT License](LICENSE).
