def display_function(todos):
    # list comprehension: new_todos = [item.strip('\n') for item in todos]
    todos.sort()
    for index, item in enumerate(todos):
        item = item.strip('\n')
        print(f"{str(index + 1)}. {item.title()}")

def file_function(path, cmd, todos):
    #global todos
    with open(path, cmd) as file:
        #don't need to close with with
        if cmd == 'r':
            readline = file.readlines()
            return readline
        elif cmd == 'w':
            file.writelines(todos)

