import tkinter as tk

class Window:

    def __init__(self, title, ):
        "This class represents Graphical User Interface object"
        self.title = title

        self.gameCount = 0 #Number of loaded games in a window

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
        self.gameCount += 1

        truName = tk.Label(text = name)

        tagPrice = tk.Label(text = "Price:")
        truPrice = tk.Label(text = price)

        tagPublisher = tk.Label(text = "Publisher:")
        truPublisher = tk.Label(text = publisher)

        tagDeveloper = tk.Label(text = "Developer:")
        truDeveloper = tk.Label(text = developer)

        tagRelease = tk.Label(text = "Release:")
        truRelease = tk.Label(text = releaseDate)

        constructionList = [
            [tagPrice, truPrice],
            [tagDeveloper, truDeveloper],
            [tagPublisher, truPublisher],
            [tagRelease, truRelease]
        ]

        truName.grid(column = 0, row = 0, columnspan = 3)

        elRow = 0
        for segment in constructionList:
            elRow += 1
            elColumn = 0
            for element in segment:
                secondSpan = 1
                if elColumn % 2 == 0:
                    secondSpan = 2
               
                element.grid(row = elRow, column = elColumn, columnspan = secondSpan, sticky = "w")
                elColumn += 1
                




    def add_control(self):
        "Adds element to the control panel."
        pass






    def show(self):
        self.window.mainloop()





class Popup:

    def __init__(self):
        pass
    