from functions import get_todos,write_todos
import time

while True:
    user_input = input('Choose to add, show or exit: ')
    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_input.startswith('show'):
        todos = get_todos('todos.txt')

        for index, i in enumerate(todos):
            i = i.strip('\n')
            print(index+1, i)
    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print('Your command is not valid')
            continue
    elif user_input.startswith('remove'):
        try:
            number = int(user_input[7:])

            todos = get_todos()

            todos.pop(number-1)

            write_todos(todos)
        except ValueError:
            print('Your command is invalid')
        except IndexError:
            print('Please give available index')
            continue
    elif 'exit' in user_input:
        break
    else:
        print('Wrong command')
print('Bye!')