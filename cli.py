from functions import get_todos, write_todos
import time

now = time.strftime("%b %d %Y %H-%M-%S")
print("It is", now)

print("For edit or complete case, provide the todo number as well")
while True:
    prompt = input("Type add, show, edit, complete or exit: ")
    prompt = prompt.strip()
    
    if prompt.startswith("add"):
        todo = prompt[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif prompt.startswith("show"):
        todos = get_todos()
        
        for index,item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index+1}-{item}"
            print(row)

    elif prompt.startswith("edit"):
        try:
            number = int(prompt[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Invalid command entered. Enter a number along with edit.")
            continue

        except IndexError:
            print("Invalid index entered.")
            continue

    elif prompt.startswith("complete"):
        try:
            todos = get_todos()

            number = int(prompt[9:])

            todos.pop(number - 1)

            write_todos(todos)

        except ValueError:
            print("Invalid command entered. Enter a number along with edit.")
            continue

        except IndexError:
            print("Invalid index entered")
            continue

    elif prompt.startswith("exit"):
        break

    else:
        print("Invalid command")
        

print("Bye!")