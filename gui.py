import functions
import FreeSimpleGUI as sg

label = sg.Text("Enter the To-do:")
input = sg.InputText(tooltip = "Type here")
add_button = sg.Button("Add")

window = sg.Window("My To-do app", layout=[[label], [input, add_button]])
window.read()
window.close()