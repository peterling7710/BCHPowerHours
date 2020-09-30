# Create a todo class - parameters name, date and complete
# You can put all your methods for what the app should do (from the spec) here as well!
from datetime import datetime

class Todo():
    def __init__(self,name,date):
        self.name = name
        self.date = date
        self.complete = False
    def description(self):
        s = 'complete' if self.complete else 'incomplete'
        print(f'{self.name}, due {self.date}, currently {s}')
    def is_complete(self):
        return self.complete
    def is_overdue(self):
        if self.complete:
            return False
        today = datetime.now()
        due = self.date + ' 2020'
        due = datetime.strptime(due,'%b %d %Y')
        if today > due:
            return True
        else:
            return False
    
todos = []
print('TODO LIST')
print('Use this app to track your upcoming todos!')
prompt_str = """Press 0 to close the app
Press 1 to add a new todo
Press 2 to mark a todo as complete
Press 3 to mark a todo as incomplete
Press 4 to list all todos
Press 5 to print all complete todos
Press 6 to print all incomplete todos
Press 7 to print all overdue todos
Press 8 to delete a todo\n"""
# Have an infinite loop
while True:
# Read user input
    read = int(input(prompt_str))
# Decision structure based on input
# Close app
    if read == 0:
        break
# Add a new todo - use input again
    elif read == 1:
        new_todo = input('Enter the name, and completion date of the task, separated by a comma\n')
        params = [s.strip() for s in new_todo.split(',')]
        new_todo = Todo(params[0],params[1])
        todos.append(new_todo)
# Mark todo as complete - need input 
    elif read == 2:
        target = input('enter name of todo that got completed\n')
        for todo in todos:
            if target == todo.name:
                todo.complete = True
# Mark todo as incomplete - need input 
    elif read == 3:
        target = input('enter name of todo that is incomplete\n')
        for todo in todos:
            if target == todo.name:
                todo.complete = False
# Print out todos
    elif read == 4:
        for todo in todos:
            todo.description()
        print('\n')
# Print completed todos
    elif read == 5:
        count = 0
        for todo in todos:
            if todo.is_complete():
                todo.description()
                count += 1
        print(f'There are currently {count} completed todos\n')
# Print incompleted todos
    elif read == 6:
        count = 0
        for todo in todos:
            if not todo.is_complete():
                todo.description()
                count += 1
        print(f'There are currently {count} incomplete todos\n')
# Print overdue
    elif read == 7:
        count = 0
        for todo in todos:
            if todo.is_overdue():
                todo.description()
                count += 1
        print(f'There are currently {count} overdue todos\n')
# Delete a todo - takes input as well
    elif read == 8:
        target = input('enter name of todo to delete\n')
        for i, todo in enumerate(todos):
            if target == todo.name:
                to_del = i
        del todos[to_del]
                