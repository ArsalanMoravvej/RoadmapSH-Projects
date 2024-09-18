import argparse
import json
import os
import datetime

JSON_FILE = "data.json"
STATUS = ['todo', 'in-progress', 'done']


def load():
    if  not os.path.exists(JSON_FILE):
        save([])
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

def save(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=2)
        
def add_task(desc):
    data = load()
    try:
        last_num = data[-1]['id']
    except:
        last_num = 0
    
    data.append({'id': last_num + 1,
                 'description': desc,
                 'status': 0,
                 'createdAt': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), 
                 'updatedAt': "-",
                 'isDeleted': False})
    save(data)

def list_tasks(status=3):

    data = load()
    
    header = f'|{"Task Number":^13}|{"Description":^42}|{"Status":^13}|{"Created At":^21}|{"Updated At":^21}|'
    seperator = '-' * len(header)

    print(seperator)
    print(header)
    print(seperator)

    for item in data:

        item_status = item['status'] #0, 1, 2
        if status == item_status or status == 3:
            pass
        else:
            continue 

        desc = item['description']

        if len(desc) > 37:
            desc = desc[:37] + "..."
        
        
        row = f'|{item['id']:^13}| {desc:<41}| {STATUS[item_status]:<12}|{item['createdAt']:^21}|{item['updatedAt']:^21}|'
        print(row)
        print(seperator)



add_task('Task 3')