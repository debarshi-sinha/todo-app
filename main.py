# prompt = "Enter Todo :"
# # user_text = input(prompt)
# # print(user_text)
# todo1 = input()
# todo2 = input()
# todo3 = input()
# todo = [todo1,todo2,todo3,"Hello"]
# print(todo)
#
# print(type(prompt))
# print(type(todo))
from pyexpat.errors import messages
# def get_todos():
#     with open("files/Todos.txt", "r") as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
#import functions
from functions import get_todos,write_todos
import  time
now = time.strftime("%b %d %Y %H:%M:%S")
print("It is ",now)
while True:
    user_action = input("Type add, show, edit ,exit or complete: ")
    user_action = user_action.strip()
    #match user_action:
        #case "add":
    #if "add" in user_action or "new" in user_action:
    if user_action.startswith("add"):
            # todo = input("Enter a Todo: ") + "\n"
            todo = '\n'+ user_action[4:]

            # file = open("files/Todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            # with open(f"files/Todos.txt", "r") as file:
            #     todos = file.readlines()

            todos = get_todos()

            todos.append(todo)

            # file = open("files/Todos.txt", "w")
            # file.writelines(todos)
            # file.close()
            # with open("files/Todos.txt", "w") as file:
            #     file.writelines(todos)
            write_todos(todos)

        #case "show" | "display":
    #elif "show" in user_action:
    elif user_action.startswith("show"):
            # file = open("files/Todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            # with open(f"files/Todos.txt", "r") as file:
            #     todos = file.readlines()

            todos = get_todos()
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            # new_todos = [item.strip("\n") for item in todos]

            for index,item in enumerate(todos):
                item = item.strip("\n")
                #print(index+1, item) print(index+1,"-",item)
                print(f"{index+1}-{item}")
        #case "edit":
    #elif "edit" in user_action:
    elif user_action.startswith("edit"):
        try :
            # number = int(input("Number of the todo to edit: "))
            number = int(user_action[5:])
            number -= 1

            # with open(f"files/Todos.txt", "r") as file:
            #     todos = file.readlines()

            todos = get_todos()

            new_todo = input("Enter new todo :")
            todos[number] = new_todo+'\n'

            # with open("files/Todos.txt", "w") as file:
            #     file.writelines(todos)

            write_todos(todos)
        except ValueError:
            print("Your command is not Valid.")
            # user_action = input("Type add, show, edit ,exit or complete: ")
            # user_action = user_action.strip()
            continue
        #case "complete":
    #elif "complete" in user_action:
    elif user_action.startswith("complete"):
        try:
            #number = int(input("Number of the todo to complete: "))
            number = int(user_action[9:])

            # with open(f"files/Todos.txt", "r") as file:
            #     todos = file.readlines()

            todos = get_todos()

            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)

            # with open("files/Todos.txt", "w") as file:
            #     file.writelines(todos)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        #case "exit":
    #elif "exit" in user_action:
    elif user_action.startswith("exit"):
            break
        #case _:
    else:
        print("Hey , you entered a wrong keyword")

print("bye!")
