import tkinter as tk

class Window:

    def __init__(self, title, ):
        "This class represents Graphical User Interface object"
        self.title = title
        pass

    def initialize(self):
        "Defines window itself"
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry("500x400+700+400")

        self.controls = tk.Frame(self.window)
        self.data = tk.Frame(self.window)
        self.controls.grid(column = 0)
        self.data.grid(column = 1)

    def add_game(self, name, price, publisher, developer, releaseDate):
        "Puts the game information into the UI"
        game = tk.Frame(self.data)

    def add_control(self):
        "Adds element to the control panel."
        pass






    def show(self):
        self.window.mainloop()





class Popup:

    def __init__(self):
        pass
    