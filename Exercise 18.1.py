import PySimpleGUI

PySimpleGUI.theme("Black")

def convert(feet, inches):
    meters = feet*0.3048 + inches*0.0254
    return meters

text1 = PySimpleGUI.Text("Enter feet:")
input1 = PySimpleGUI.Input(key="feet")

text2 = PySimpleGUI.Text("Enter inches:")
input2 = PySimpleGUI.Input(key="inches")

con_button = PySimpleGUI.Button("Convert")
exit_button = PySimpleGUI.Button("Exit")
output_label = PySimpleGUI.Text("", key="output")

window = PySimpleGUI.Window("Convertor", layout=[[text1, input1], [text2, input2],
                                                 [con_button, exit_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    match event:
        case "Convert":
            result = convert(feet, inches)
            window["output"].update(value=f"{result} m", text_color="white")

        case "Exit":
            break

window.close()
