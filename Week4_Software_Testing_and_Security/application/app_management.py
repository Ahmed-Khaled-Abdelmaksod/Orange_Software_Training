
from task import Task
import time
class app_management:
    def __init__(self):
        self.tasks = []

    
    def add_task(self,title,description,due_date):
        if title == "":
            print("Title is mandatory")
            return False
        if len(title) < 10 or len(title) > 30:
            print("Title's length must be greater than 10 and lower than 30 ")
            return False
        task = Task(title=title,description=description,due_date=due_date)
        self.tasks.append(task)
        return True 
    
    
    def get_tasks(self):
        return self.tasks
    
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks avilable")
        else:
            for task in self.tasks:
                title_status = "incomplete"
                if task.status == True:
                    title_status = "Complete"
                print('%'*50)
                print(f"{task.title}"+f" '{title_status}'")
                print("   "+task.description)
                print(f"Due Date : {task.due_date}")
                print('%'*50)
        time.sleep(1)
    
    
    def complete_task(self,title):
        temp_flag = False
        for task in self.tasks:
            if task.title == title:
                temp_flag = True
                task.status = True
                break
        if temp_flag:
            print("Well Done!! Task finished sucessfully")
        else:
            print("Can't find the task :(")
        time.sleep(1)
    
    
    def delete_task(self,title):
        task_wanted  = None
        temp_flag = False
        no_flag = False
        for task in self.tasks:
            if task.title == title:
                task_wanted = task
                temp_flag = True
                # choice = input('Are you sure? Y/N : ')
                # choice = choice.capitalize()
                # if choice == 'Y':
                #     temp_flag = True
                #     no_flag = False
                # else:
                #     no_flag = True
                break
        if no_flag:
            print("Can't delete task")
        else:
            if temp_flag:
                self.tasks.remove(task_wanted)
                print("Task Deleted Successfully . . .")
            else:
                print("Can't find the task :(")
        time.sleep(1)
