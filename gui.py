from tkinter import font

import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter the To-do:")
input = sg.InputText(tooltip = "Type here", key = "todo")
add_button = sg.Button("Add")

window = sg.Window("My To-do app", layout=[[label], [input, add_button]], font=("Helvetica",20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()