def get_todos(filepath = "../files/todos.txt"):
    """
    Read the text file and returns the list of to-do items
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg , filepath = "../files/todos.txt"):
    """
    Writes the to-do item in the text file.
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

print(__name__)

if(__name__ == "__main__"):
    print("Hello")