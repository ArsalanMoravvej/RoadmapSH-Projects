import argparse
import json
import os
import datetime

JSON_FILE = "data.json"


def load():
    if  not os.path.exists(JSON_FILE):
        save([])
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

def save(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=2)
        
def add_task(task):
    data = load()
    try:
        last_num = data[-1]['id']
    except:
        last_num = 0
    
    data.append({'id': last_num + 1,
                 'description': task.desc,
                 'status': 'todo',
                 'createdAt': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), 
                 'updatedAt': "-",
                 'isDeleted': False})
    save(data)

def list_tasks(args):

    data = load()
    
    header = f'|{"Task Number":^13}|{"Description":^42}|{"Status":^13}|{"Created At":^21}|{"Updated At":^21}|'
    seperator = '-' * len(header)

    print(seperator)
    print(header)
    print(seperator)

    for item in data:

        status = args.status

        if (not status or status == item['status']) and not item['isDeleted']:
            pass
        else:
            continue 

        desc = item['description']

        if len(desc) > 37:
            desc = desc[:37] + "..."
        
        
        row = f'|{item['id']:^13}| {desc:^41}| {item['status']:^12}|{item['createdAt']:^21}|{item['updatedAt']:^21}|'
        print(row)
        print(seperator)

def delete_task(task):
    data = load()

    for item in data:
        if item['id'] == task.num:
            if item['isDeleted'] == True:
                print (f'Task number {task.num} doesn\'t exist or already deleted!')
                return


            item['isDeleted'] = True
            save(data)
            print(f'Task number {task.num} deleted!')
            return
    
    print(f'could\'t find task number {task.num}!')

def main():
    parser = argparse.ArgumentParser(description="To-do Lister")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    # Add task subparser
    addTask_parser = subparsers.add_parser('add', help="Add a new task")
    addTask_parser.add_argument('desc', type=str, help="Task description")
    addTask_parser.set_defaults(func=add_task)

    # Delete task subparser
    deleteTask_parser = subparsers.add_parser('delete', help="Delete a task")
    deleteTask_parser.add_argument('num', type=int, help="Task number to delete")
    deleteTask_parser.set_defaults(func=delete_task)
    
    # Update task subparser
    # updateTask_parser = subparsers.add_parser('update', help="Update a task")
    # updateTask_parser.add_argument('num', type=int, help="Task number to update")
    # updateTask_parser.add_argument('desc', type=str, help="New task description")
    # updateTask_parser.set_defaults(func=update_task)

    # List tasks subparser
    listTasks_parser = subparsers.add_parser('list', help="List tasks")
    listTasks_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'], help="Optional status filter")
    listTasks_parser.set_defaults(func=list_tasks)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()