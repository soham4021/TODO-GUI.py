FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """Reads a text file and returns the list of to-do items from it"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos, filepath=FILEPATH):
    """Writes the desired todo items to a text file"""
    with open(filepath, "w") as file:
            file.writelines(todos)


if __name__ == "__main__":
    print("Hello from functions.py")

