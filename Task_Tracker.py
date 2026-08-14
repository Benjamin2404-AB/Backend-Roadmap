tasks = []
from enum import Enum

next_id = 1
class Status(Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"


class Task():
    def __init__ (self,title:str ,description:str):
        self.title = title
        self.status =  Status.TODO.value
        self.id = 0
        self.description = description
        
    def __str__ (self):
        return(f"{self.title} \t\t {self.description} \t\t {self.status}")
        
    def complete_task(self):
        self.status = Status.COMPLETED.value
    def setas_todo_task(self):
            self.status = Status.TODO.value
    def setas_inprogress_task(self):
                self.status = Status.IN_PROGRESS.value
        
    def set_id(self,id):
        self.id = id
        
    def set_status(self,eval):
        self.status = eval
        
    def get_id(self):
        return self.id
    def set_title(self,newTitle:str):
        self.title = newTitle
    def get_title(self):
        return self.title
        
    def set_description(self,text):
        self.description = text
        
    def get_description(self):
        return self.description
        
        
def create_task(title:str,description:str):
    task = Task(title,description)
    global next_id
    task.set_id(next_id)
    next_id+=1
    # task.set_description(description)
    tasks.append(task)
    
    print(f"Successfully added task: {title}")
    


def list_tasks():
    print(" Task \t\t Description \t\t Status")
    for t in tasks:
        print(f"{t.get_id()}  {t}")
    
    
def complete_task(id):
    for t in tasks:
        if t.get_id() == id:
            t.complete_task()
            print(f"Task {t.get_title()} is now completed")
        
    return ("No valid task with ID found")
    
def inProgress_task(id):
    for t in tasks:
        if t.get_id() == id:
            t.setas_inprogress_task()
            print(f"Task {t.get_title()} is now IN PROGRESS")
            return
    
    return ("No valid task with ID found")
        
            
def todo_task(id):
    for t in tasks:
        if t.get_id() == id:
            t.setas_todo_task()
            print(f"Task {t.get_title()} is now marked as TODO")
            return
            
      
    return ("No valid task with ID found")
            
    
    
    

def update_task(id,title:str,description:str):
    for t in tasks:
        if t.get_id() == id:
            t.set_title(title)
            t.set_description(description)
            
            


def delete_task(id):
    for t in tasks:
        if t.get_id() == id:
            tasks.remove(t)


def main():
    is_running = True
    while is_running:
   
        commands = [1,2,3,4,5,6,7,8]

        print("WELCOME TO PERSONAL TASK TRACKER")
        print("""

               1. Create Task
               2. List Task
               3. Update Task
               4. Delete Task
               5. Mark Task as Complete
               6. Mark Task as In Progress
               7. Mark Task as Done
               8. Exit


               """)

        user_command = int(input("Enter command to begin : "))
        while user_command not in commands:
            try:
                print("WELCOME TO PERSONAL TASK TRACKER")
                print("""

                            1. Create Task
                            2. List Task
                            3. Update Task
                            4. Delete Task
                            5. Mark Task as Complete
                            6. Mark Task as In Progress
                            7. Mark Task as Done
                            8. Exit


                            """)

                user_command = int(input("Enter command to begin : "))

            except:
                print("Enter valid value between 1-4 ")

        match user_command:
            case 1:
                try:
                    task_title = input("Enter a task name :\n")
                    task_descr = input("Enter a task description :\n")

                except:
                    print("Enter a valid input")

                create_task(task_title,task_descr)
            case 2:
                list_tasks()
            case 3:
                try:
                    task_id =  int(input("Enter a valid id of task to update: \n"))
                    task_title = input("Enter new title: \n")
                    task_desc =  input("Enter a new description: \n")
                    update_task(task_id,task_desc,task_title)
                except:
                    print("Please enter a valid input. Must be a number")
            case 4:
                task_to_delete =  int(input("Enter a valid id of task to delete: \n"))
                delete_task(task_to_delete)

            case 5:
                task_id =  int(input("Enter a valid id of task to complete: \n"))
                complete_task(task_id)
                
            case 6:
                    task_id =  int(input("Enter a valid id of task to make IN PROGRESS: \n"))
                    inProgress_task(task_id)
            case 7:
                    task_id =  int(input("Enter a valid id of task to TODO: \n"))
                    todo_task(task_id)
                
            case 8:
                print("Goodbye")
                is_running = False
    
    
    
if __name__ == "__main__":
    main()