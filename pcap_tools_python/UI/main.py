import PySimpleGUI as sg


class MainWindow:

    def __init__(self):
        layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-"), sg.Button("OK")]]



        # Create the window
        window = sg.Window("Demo", layout)

        # Create an event loop
        while True:
            event, values = window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "OK" or event == sg.WIN_CLOSED:
                print(values["-IN-"])
                break



        window.close()
