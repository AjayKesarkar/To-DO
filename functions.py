def get_todos(filename='todos.txt'):
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)