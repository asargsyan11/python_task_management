
#Function to add a task, as a parameter i'm passing the list of commands we already have 
def addTask(tasks):
    
    #1.prompts for the name of the task
    nameTask = input("Enter the name of the task you want to add: ")
    #2.check if the task exists already, if so, display an error message instead
    taskExists = False
    if tasks:
        for task in tasks:
            if task['name'] == nameTask:
                print("The task already exists.")
                taskExists = True

    #3.promt for the description otherwise
    if taskExists == False:
        descTask = input("Enter the description of the task: ")
        newTask = {
                    "name" : nameTask,
                    "description" : descTask
                    }
        tasks.append(newTask)


#Function to update a task that already exists
def updateTask(tasks):
    
    if not tasks:
        print("Warning: the list is empty.")
    #prompt for the name of the task
    else:
        nameUpdated = input("Enter the name for the command you want to update: ")
        taskUpdated = False
    #loop the tasks in the list, if we find we prompt for a new description and change the previous one 
        if tasks:
            for task in tasks:
                if task["name"] == nameUpdated:
                    descUpdated = input("Enter the new description: ")
                    task["description"] = descUpdated
                    taskUpdated = True
                    break 
            if taskUpdated == False:
                    print("The task doesn't exist")


#Function to list the tasks
def listTasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"Task {i}:")
        print(f"Name: {task['name']}")
        print(f"Description: {task['description']}")
        print()    

#Function to remove a task that's on the list
def removeTask(tasks):

    #check if the list is empty
    if not tasks:
        print("Warning: the list is empty")
    #prompt for the name of the task, check if it exists and remove
    else:
        taskRemoved = input("Enter the name of the task you want to remove: ")
        removed = False
        if tasks:
            for task in tasks:
                if task["name"] == taskRemoved:
                    tasks.remove(task)
                    print("The task has been removed")
                    removed = True
                    break ; 
            if removed == False:
                print("Error: the task doesn't exist.")
    #i used a bool variable to check if the task was removed or not, in order to handle the error

def main():
    tasks = []
    
    command = input("Enter the command: ")
    while not command.upper() == "EXIT":
        if command.upper() == "ADD":
            addTask(tasks)
            command = input("Enter the command: ")
        elif command.upper() == "UPDATE":
            updateTask(tasks)
            command = input("Enter the command: ") 
        elif command.upper() == "LIST":
            listTasks(tasks)
            command = input("Enter the command: ")
        elif command.upper() == "REMOVE":
            removeTask(tasks)
            command = input("Enter the command: ")
        else:
            print("Error: Unknown task")
            command = input("Enter the command: ")  


if __name__ == "__main__":
    main()
