import tkinter as tk
from tkinter import messagebox
import steamRecord



class Window:


    def __init__(self, title, ):
        "This class represents Graphical User Interface object"
        self.title = title


    def initialize(self):
        "Defines window itself"
        #Configuring master window
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry("500x600")

        self.master = self.window

        #Preparing main sections
        self.controls = tk.LabelFrame(self.window)
        self.data = tk.LabelFrame(self.window, text = "Games")
       
       
        #Packing main sections
        self.controls.pack(fill = "both", expand = "yes", padx = 10, pady = 10, anchor = "w")
        self.data.pack(fill = "both", expand = "yes", padx = 10, pady = 10, anchor = "w")
        
        #Creating canvas for scrolling frame feature
        canvas = tk.Canvas(self.data)
        canvas.pack(side="left",fill = "both", expand = "yes")

        #Configuring scrollbar
        yscrollbar = tk.Scrollbar(self.data, orient = "vertical", command = canvas.yview)
        yscrollbar.pack(side="right", fill="y")

        #Attaching scrollbar to the canvas
        canvas.configure(yscrollcommand = yscrollbar.set)   
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

        #Creating frame inside the canvas
        self.dataFrame = tk.Frame(canvas)
        canvas.create_window((0,0), window=self.dataFrame, anchor = "nw")


    def add_game(self, name, price, publisher, developer, releaseDate):
        "Puts the game information into the UI"

        game = tk.LabelFrame(self.dataFrame)
        game.pack( fill = "both", expand = "yes")
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

    def add_controls(self):
        "Fills the control section"
        addGameBut = tk.Button(self.controls, text = "Add game using ID", command= lambda: self.newGameWindow(reqGameWin, "Add Game")).pack()
        
        pass



    def show(self):
        "Closes the window loop."
        self.window.mainloop()

    def newGameWindow(self, _class, title):
        self.new = tk.Toplevel(self.master)
        _class(self.new, title)
        

class reqGameWin:

    def __init__(self, master, title):
        self.master = master
        self.master.geometry("400x400+200+200")
        self.frame = tk.LabelFrame(self.master)
        self.frame.pack()

        self.entryString = tk.StringVar()
        self.entr = tk.Entry(self.frame, textvariable = self.entryString)
        
        self.submit = tk.Button(self.frame, text = "Save", command =self.finishSubmit)
        
        self.entr.pack()
        self.submit.pack()
        

    def finishSubmit(self):
        submitString = self.entryString.get()
        
        submittedGame = steamRecord.Game(submitString)
        submittedGame.save()

        self.master.destroy()





        
def error(title, text):
    messagebox.showerror(title, text)
    


def win():
    """Open window"""
    