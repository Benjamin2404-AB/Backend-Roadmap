# tasks -> add, update, delte, mark as in progress
# List tasks , list in progress , list done 




tasks = []

def create_task(id:int,title:str, description:str,completed:str):
    task={
        'id':id,
        'title': title,
        'description': description,
        'completed':completed,
    }
    tasks.append(task)


def delete_task(id:int):
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
        return
        

def update_task(id:int,title:str,description:str):
    for task in tasks:
        if task['id'] == id:
            task['title'] = title
            task['description'] = description
        return
        
    

def list_tasks():
    for task in tasks:
        print(task)
        
        


