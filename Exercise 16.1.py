import PySimpleGUI

text1 = PySimpleGUI.Text("Enter feet: ")
input1 = PySimpleGUI.Input()

text2 = PySimpleGUI.Text("Enter inches: ")
input2 = PySimpleGUI.Input()

window = PySimpleGUI.Window("Convertor", layout=[[text1,input1], [text2,input2]])
window.read()
window.close()
