import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen
import urllib
import re
import datetime
import time
import json
from pathlib import Path


thisFolderPath = Path(__file__).absolute().parent
parentFolderPath = thisFolderPath.parent
saveFilePath = Path(thisFolderPath)

global Labels
Labels = {
    'game_labels' : {

    }
}

def error(title, text):
    messagebox.showerror(title, text)

def info(title, text):
    messagebox.showinfo(title, text)

class Window:

    def __init__(self, title):
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
        self.controls.pack(fill = "both", padx = 10, anchor = "w")
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
        self.dataFrame.pack(fill = "both")
        


    def add_game(self, steam_id, name, price, publisher, developer, releaseDate):
        "Puts the game information into the UI"

        game = tk.LabelFrame(self.dataFrame)
        game.pack( fill = "both", expand = "yes")
        Labels['game_labels'][str(steam_id)] = game

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
        
        removeButton = tk.Button(game, text = "Remove from list", command = lambda:self.remove_game(steam_id)).pack(anchor='se')

    def remove_game(self, steam_id):
        try:
            Labels['game_labels'][str(steam_id)].destroy()
            GameList_.removeFromList(steam_id)
            return True
        except:
            return False

    def add_controls(self):
        "Fills the control section"
        addGameBut = tk.Button(self.controls, text = "Add game using ID", command= lambda: self.newGameWindow(reqGameWin, "Add Game")).grid(column=1, row=0)                 #pack(anchor="nw")
        addSaveBut = tk.Button(self.controls, text = "Save your selection", command = GameList_.saveToLocal).grid(column=0, row=0)                                           #pack(anchor="ne")
        addSearchBut = tk.Button(self.controls, text = "Add game using name", command = lambda: self.newGameWindow(searchWindow, "Add Game")).grid(column=2, row=0)          #pack(anchor="nw")
        pass

    def show(self):
        "Closes the window loop."
        self.window.mainloop()

    def newGameWindow(self, _class, title):
        new = tk.Toplevel(self.master)
        _class(new, title)
        

class reqGameWin:

    def __init__(self, master, title):
        self.master = master
        self.master.geometry("100x50")

        frame = tk.LabelFrame(self.master)
        frame.pack()

        self.entryString = tk.StringVar()
        entr = tk.Entry(frame, textvariable = self.entryString)
        
        submit = tk.Button(frame, text = "add", command =self.finishSubmit)
        
        entr.pack()
        submit.pack()
        

    def finishSubmit(self):
        submitString = self.entryString.get()
        
        submittedGame = Game(submitString)
        connectionSuccess = submittedGame.load()
        logSuccess = GameList_.addToList(submittedGame.steam_id)

        if connectionSuccess and logSuccess:
            Window_.add_game(submittedGame.steam_id, submittedGame.name, submittedGame.price, submittedGame.publisher, submittedGame.developer, submittedGame.releaseDate)
            info('Success', 'Game successfuly added.')
        else:
            error('Error', 'Game was not added. Try again.')
        self.master.destroy()

class searchWindow:
    def __init__(self, master, title):
       #Defining searchWindow
        self.master = master
        self.master.geometry("300x230")

        self.labelList = []

        self.frame = tk.LabelFrame(self.master, text = 'Search')
        self.frame.pack(fill = "both")

        self.result = tk.LabelFrame(self.master, text = "Result")
        self.result.pack(fill = "both", expand = "yes")

        self.entryString = tk.StringVar()
        entr = tk.Entry(self.frame, textvariable = self.entryString)
        
        entr.pack()
        submit = tk.Button(self.frame, text = "Search", command =self.submitGame).pack()
        


    def submitGame(self):
        submitString = self.entryString.get()

        if self.labelList:
            self.remove_game(self.labelList)
            self.labelList = []

        self.searchResult = Search_.search(submitString)
        if self.searchResult:
            self.add_game(self.searchResult)

    def add_game(self, steam_id):
        "Puts the game information into the UI"

        gameData = Game(steam_id)
        gameData.load()

        game = tk.Frame(self.result)
        game.pack( fill = "both", expand = "yes")
        self.labelList.append(game) 

        finName = tk.Label(game, text = gameData.name, anchor = "w")

        finPrice = tk.Label(game, text = "Price: " + str(gameData.price), font=("Courier", 9))
        finPublisher = tk.Label(game, text = "Publisher " + str(gameData.publisher), font=("Courier", 9))
        finDeveloper = tk.Label(game, text = "Developer: " + str(gameData.developer), font=("Courier", 9))
        finRelease = tk.Label(game, text = "Release date: " + str(gameData.releaseDate), font=("Courier", 9))

        constructionList = [
            finPrice,
            finPublisher,
            finDeveloper,
            finRelease
        ]

        finName.pack()
        for segment in constructionList:
            segment.pack(anchor = "w")

        addSaveBut = tk.Button(game, text = "Add", command = self.saveGame).pack(anchor='se')
        

    def remove_game(self, steam_id):
        try:
            self.labelList[0].destroy()
            GameList_.removeFromList(steam_id)
            return True
        except:
            return False

    def saveGame(self):
            
        submittedGame = Game(self.searchResult)
        connectionSuccess = submittedGame.load()
        logSuccess = GameList_.addToList(submittedGame.steam_id)

        if connectionSuccess and logSuccess:
            Window_.add_game(submittedGame.steam_id, submittedGame.name, submittedGame.price, submittedGame.publisher, submittedGame.developer, submittedGame.releaseDate)
            info('Success', 'Game successfuly added.')
        else:
            error('Error', 'Game was not added. Try again.')

        

class SteamSearchEngine:

    def __init__(self):
        req = urlopen('http://api.steampowered.com/ISteamApps/GetAppList/v0001/')
        
        self.appList = json.load(req)['applist']['apps']['app']

        self.gameDict = {}

        for game in self.appList:
            self.gameDict[game["name"]] = game["appid"]
        
    def search(self, entry):
        
        try:
            found_id = self.gameDict[entry]
        except:
            info('Not found', 'This game was not found, try again.')
            return False

        return found_id


class Game:
    
    def __init__(self,steam_id):
        "Represents data object of a game"

        self.steam_id = str(steam_id)
        self.name = ""
        self.price = 0.0
        self.publisher = ""
        self.developer = ""
        self.releaseDate = ""

    def load(self):
        "Updates information about the game"
        
        try:

            req = urlopen('https://store.steampowered.com/api/appdetails?appids=' + str(self.steam_id))
            rawData = json.load(req)
            gameData = rawData[self.steam_id]["data"]

            self.name = gameData["name"]
            self.price = gameData["package_groups"][0]["subs"][0]["price_in_cents_with_discount"]/100
            self.publisher = gameData["publishers"][0]
            self.developer = gameData["developers"][0]
            self.releaseDate = gameData["release_date"]["date"]

            return True

        except(urllib.error.URLError):
            error("Timeout", "Steam connection timed out. Try again.")
            return False

        except:
            error("Error", "Something went wront. Try again.")
            return False

    
    def params(self):
        data = {
            "steam_id" : self.steam_id,
            "name" : self.name,
            "price" : self.price,
            "publisher" : self.publisher,
            "developer" : self.developer,
            "release" : self.releaseDate
        }
        return data

class GameList:

    def __init__(self):
        
        self.list = []
        successfulLoad = self.loadFromLocal()
    
    def getGames(self):
        objectList = []
        for id in self.list:
            game = Game(id)
            game.load()
            objectList.append(game)
        return objectList

    def loadFromLocal(self):
        #try:
        with open(saveFilePath / 'data.json', 'r') as jsonFile:
            data = json.load(jsonFile)
        self.list = data['steam_ids'] 
        #except:
         #   info('Save file not found', 'Save file not found, new will be created once you save your files.')               
        
        return self.list

    def saveToLocal(self):
        """Saves games from list to json"""
        with open(saveFilePath / 'data.json', 'w') as jsonFile:
            dumpList = {'steam_ids' : self.list}
            data = json.dumps(dumpList)
            print(data, file=jsonFile)
       

    def addToList(self, steam_id):
        """Adds specific steam_id to the list"""
        #try:
        self.list.append(steam_id)
        return True


        #    return True
        #except:
        #    return False

    def removeFromList(self, steam_id):
        """Removes specific steam_id to the list"""
        count = 0
        for id in self.list:
            if id == steam_id:
                self.list.pop(count)
            count += 1
        return True

class App:

    def __init__(self):
        
        #Loading game list
        global GameList_
        GameList_= GameList()

        #Defining Window
        global Window_
        Window_ = Window("Steam List")
        
        global Search_
        Search_ = SteamSearchEngine()

        
        
        Window_.initialize()
        Window_.add_controls()

        savedGames = GameList_.getGames()
        for game in savedGames:
            Window_.add_game(game.steam_id, game.name, game.price, game.publisher, game.developer, game.releaseDate)
        


      


        Window_.show()


app = App()

