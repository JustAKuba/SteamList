import tkinter as tk

class Window:


    def __init__(self, title, ):
        "This class represents Graphical User Interface object"
        self.title = title

        self.gameCount = 0 #Number of loaded games in a window


    def initialize(self):
        "Defines window itself"
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry("500x600")

        self.controls = tk.LabelFrame(self.window, text = "Control panel")
        self.data = tk.LabelFrame(self.window, text = "Games")



        self.controls.pack(fill = "both", expand = "yes", padx = 10, pady = 10, anchor = "w")
        self.data.pack(fill = "both", expand = "yes", padx = 10, pady = 10, anchor = "w")
        
        canvas = tk.Canvas(self.data)
        canvas.pack(side="left")

        yscrollbar = tk.Scrollbar(self.data, orient = "vertical", command = canvas.yview)
        yscrollbar.pack(side="right", fill="y")
        
        self.dataFrame = tk.Frame(canvas)
        self.dataFrame.pack()


    def add_game(self, name, price, publisher, developer, releaseDate):
        "Puts the game information into the UI"

        game = tk.LabelFrame(self.dataFrame)
        game.pack( fill = "both")
        self.gameCount += 1

        finName = tk.Label(game, text = name, anchor = "w")

        finPrice = tk.Label(game, text = "Price: " + str(price), font=("Courier", 9))
        finPublisher = tk.Label(game, text = "Publisher " + str(publisher), font=("Courier", 9))
        finDeveloper = tk.Label(game, text = "Developer: " + str(developer), font=("Courier", 9))
        finRelease = tk.Label(game, text = "Release date: " + str(releaseDate), font=("Courier", 9))

        constructionList = [
            finPrice,
            finPublisher,
            finDeveloper,
            finRelease
        ]

        finName.pack()

        segCount = 0
        for segment in constructionList:
            segment.pack(anchor = "w")


    def show(self):
        self.window.mainloop()



class Popup:

    def __init__(self):
        pass
    