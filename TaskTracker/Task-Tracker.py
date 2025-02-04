import argparse
import json
import os
import datetime

# Constants
JSON_FILE = "data.json"

def load():
    """
    Load tasks from the JSON file. If the file doesn't exist, create an empty one.
    """
    if not os.path.exists(JSON_FILE):
        save([])
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

def save(data):
    """
    Save tasks to the JSON file.
    """
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def add_task(task):
    """
    Add a new task to the list.
    """
    data = load()
    # Get the last used ID, or 0 if the list is empty
    last_id = data[-1]['id'] if data else 0
    
    new_task = {
        'id': last_id + 1,
        'description': task.desc,
        'status': 'todo',
        'createdAt': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updatedAt': "-",
        'isDeleted': False
    }
    data.append(new_task)
    save(data)
    print(f"Task added: [{new_task['id']}] {new_task['description']}")

def list_tasks(args):
    """
    List tasks, optionally filtered by status.
    """
    data = load()
    
    # Prepare the table header
    header = f'|{"Task Number":^13}|{"Description":^42}|{"Status":^13}|{"Created At":^21}|{"Updated At":^21}|'
    separator = '-' * len(header)

    print(separator)
    print(header)
    print(separator)

    for item in data:
        # Filter tasks based on status if provided
        if (not args.status or args.status == item['status']) and not item['isDeleted']:
            desc = item['description']
            if len(desc) > 37:
                desc = desc[:37] + "..."
            
            row = f'|{item["id"]:^13}| {desc:^41}|{item["status"]:^13}|{item["createdAt"]:^21}|{item["updatedAt"]:^21}|'
            print(row)
            print(separator)

def delete_task(task):
    """
    Mark a task as deleted.
    """
    data = load()
    for item in data:
        if item['id'] == task.num:
            if item['isDeleted']:
                print(f'Task number {task.num} doesn\'t exist or is already deleted!')
                return
            item['isDeleted'] = True
            save(data)
            print(f'Task number {task.num} deleted!')
            return
    print(f'Couldn\'t find task number {task.num}!')

def update_task(task):
    """
    Update the description of a task.
    """
    data = load()
    for item in data:
        if item['id'] == task.num:
            if item['isDeleted']:
                print(f'Task number {task.num} doesn\'t exist or is deleted!')
                return
            item['description'] = task.desc
            item['updatedAt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save(data)
            print(f'Task number {task.num} updated!')
            return
    print(f'Couldn\'t find task number {task.num}!')

def update_task_status(task, new_status):
    """
    Update the status of a task.
    """
    data = load()
    for item in data:
        if item['id'] == task.num:
            if item['isDeleted']:
                print(f'Task number {task.num} doesn\'t exist or is deleted!')
                return
            item['status'] = new_status
            item['updatedAt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save(data)
            print(f'Task number {task.num} updated, now {new_status}!')
            return
    print(f'Couldn\'t find task number {task.num}!')

def mark_in_progress(task):
    """
    Mark a task as in progress.
    """
    update_task_status(task, 'in-progress')

def mark_done(task):
    """
    Mark a task as done.
    """
    update_task_status(task, 'done')

def main():
    """
    Main function to set up the command-line interface and handle user commands.
    """
    parser = argparse.ArgumentParser(description="To-do List Manager")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    # Add task subparser
    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument('desc', type=str, help="Task description")
    add_parser.set_defaults(func=add_task)

    # Delete task subparser
    delete_parser = subparsers.add_parser('delete', help="Delete a task")
    delete_parser.add_argument('num', type=int, help="Task number to delete")
    delete_parser.set_defaults(func=delete_task)
    
    # Update task subparser
    update_parser = subparsers.add_parser('update', help="Update a task")
    update_parser.add_argument('num', type=int, help="Task number to update")
    update_parser.add_argument('desc', type=str, help="New task description")
    update_parser.set_defaults(func=update_task)

    # List tasks subparser
    list_parser = subparsers.add_parser('list', help="List tasks")
    list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'], help="Optional status filter")
    list_parser.set_defaults(func=list_tasks)

    # Mark in-progress task subparser
    progress_parser = subparsers.add_parser('mark-in-progress', help="Mark a task as in progress")
    progress_parser.add_argument('num', type=int, help="Task number to update")
    progress_parser.set_defaults(func=mark_in_progress)

    # Mark done task subparser
    done_parser = subparsers.add_parser('mark-done', help="Mark a task as done")
    done_parser.add_argument('num', type=int, help="Task number to update")
    done_parser.set_defaults(func=mark_done)
    
    # Parse arguments and call the appropriate function
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()