def get_todos(filepath = "pavdev.txt"):
    file = open(filepath, 'r')
    todos = file.readlines()
    file.close()
    return todos


def write_todos(todos,filepath = "pavdev.txt"):
    file = open(filepath, 'w')
    file.writelines(todos)
    file.close()

