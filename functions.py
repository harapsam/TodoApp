import time


def read_todos():
    with open("todolist.txt", "r") as file:
        contents = file.readlines()
    return contents


def write_todos(todos):
    with open("todolist.txt", "w") as file:
        for todo in todos:
            file.write(todo)


def get_date():
    date = time.strftime('%B %d, %Y')
    return date
