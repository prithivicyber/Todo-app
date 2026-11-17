from tkinter import font
import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text(" ", key = "clock")
label = sg.Text("Enter the To-do:")
input = sg.InputText(tooltip = "Type here", key = "todo")
add_button = sg.Button("Add", size = 10)
list_box = sg.Listbox(values= functions.get_todos(), key = "todos", enable_events = True, size= [45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button =sg.Button("Exit")

layout = [[clock],
          [label],
          [input, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("My To-do app", layout=layout, font=("Helvetica",20))
while True:
    event, values = window.read(timeout = 200)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo =  values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values = todos)
            except IndexError:
                sg.popup("Select an item first", font =("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values = todos)
                window["todo"].update(value = "")
            except IndexError:
                sg.popup("Select an item first", font=("Helvetica", 20))
        case "Exit":
            break

        case "todos":
            window["todo"].update(value = values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()