def get_todos():
    """ reads a text file and returns the list of the to-do items"""
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(filepath, todos_arg):
    """writes the to-do items in the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
