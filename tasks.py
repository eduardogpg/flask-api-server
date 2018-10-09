__TASKS = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description' : 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done' : False,
        'priority': 1
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False,
        'priority': 2
    }
]

def tasks():
    return __TASKS

def last():
    return None if len(__TASKS) == 0 else __TASKS[-1]

def get(id=1):
    tasks = [task for task in __TASKS if task['id'] == id]
    if len(tasks) == 0:
        return None
    else:
        return tasks[0]

def generate_id():
    return  last()['id'] + 1 if last() is not None else 1

def create(title='', description='', done=False):
    task = {
        'id' : generate_id(),
        'title' : title,
        'description': description,
        'done': done
    }

    __TASKS.append(task)
    return task

def update(id, title, description, done):
    task = get(id)
    print("\n\n")
    print(id)
    print(title)


    print(description)

    if task is None:
        return False

    task['title'] = title if title != '' else task['title']
    task['description'] = description if description != '' else task['description']
    task['done'] = done

    return task

def delete(id):
    task = get(id)
    if task is None:
        return False

    __TASKS.remove(task)
    return True
