Python Intermediate Project 1 - Command-Based Task Management Application

The goal is to creat a simple console application that manages tasks through user commands.
Here is how I went about to making the application:
    First of all I decided to creat a function for each of the commands in order to make it easier to make changes to them later on. ALl the functions will be passed the list of tasks that we have, which will be empty at the start of the program. The tasks would be stored in a list of dictionaries that have the keys 'name' and 'description'.
Here are the commands and how I worked to realize the functions they were supposed to do:
1.  ADD
1.1 Prompts for the name of the task
1.2 Check if the task already exists, I have a boolean variable ' 'taskExists' that will be False initially, and if we find that the      task already exists 'taskExists' will change to True.
1.3 If 'taskExists' = False, meaning the task didn't exist in the list, we prompt for the description of the task and create a new dictionary  with the name and description given by the user.
1.4 We append the dictionary to the list. 

2.  UPDATE
1.1 Check if the list is empty or not, prints a warning if so, else prompts for the name of the task the user wants to update.
1.2 Loop through the list of tasks, if we find the needed task, we prompt for the new description, change the old one and exit the loop by using 'break'. Otherwise print that the task doesn't exist.

3.  LIST
Simply loop over the list and print each dictionary in a formatted way.

4.  REMOVE
1.1 Check if the list is empty or not, print a warning if so.
1.2 Prompt for the name of the task we want to remove.
1.3 Loop over the list, if we find the task with the given name, we remove it, otherwise we print an error messege that we couldn't find the task.
Here I also used a boolean variable to check if anythin was removed or not.

5.  MAIN()
I created an empty list, then prompted for a command from the user.
While the command wasn't 'EXIT' the program calls the function for each given command and then prompts for anothe command. 