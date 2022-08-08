import PySimpleGUI as sg


class MainWindow:

    def __init__(self):
        sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
