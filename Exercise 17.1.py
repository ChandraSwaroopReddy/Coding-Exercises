import PySimpleGUI

def convert(feet, inches):
    meters = feet*0.3048 + inches*0.0254
    return meters

text1 = PySimpleGUI.Text("Enter feet:")
input1 = PySimpleGUI.Input(key="feet")

text2 = PySimpleGUI.Text("Enter inches:")
input2 = PySimpleGUI.Input(key="inches")

Convert_button = PySimpleGUI.Button("Convert")
output_label = PySimpleGUI.Text("", key="output")

window = PySimpleGUI.Window("Convertor", layout=[[text1, input1], [text2,input2],[Convert_button,output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")

window.close()