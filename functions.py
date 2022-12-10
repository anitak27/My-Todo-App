FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def save_todos(todos_local, filepath=FILEPATH):
    """ Saves a list to a text file """
    todos_local = [todo.capitalize() for todo in todos_local]
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == '__main__':  # Executes only if this file is directly executed
    print(get_todos())
