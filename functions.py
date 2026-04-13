def get_todos(filepath="files/Todos.txt"):
    """ Read a text file and return a list of to-do items """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath="files/Todos.txt"):
    """ Write a to-do items list to a text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__=="__main__":
    print("Hello")
    print(get_todos())