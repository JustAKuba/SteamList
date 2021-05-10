from urllib.request import urlopen
import urllib
import re
import datetime
import time
import json
import gui
from pathlib import Path

thisFolderPath = Path(__file__).absolute().parent
parentFolderPath = thisFolderPath.parent

saveFilePath = Path(thisFolderPath / 'userData')




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
            gui.error("Timeout", "Steam connection timed out. Try again.")
            return False

        except:
            gui.error("Error", "Something went wront. Try again.")
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
        self.list = self.loadFromLocal()
    
    def getGames(self):
        objectList = []
        for id in self.list:
            game = Game(steam_id)
            game.load()
            objectList.append(game)
        return objectList

    def loadFromLocal(self):
        try:
            with open(saveFilePath / 'data.json', 'r') as jsonFile:
                data = json.load(jsonFile)
                self.list = data['steam_ids']
            return True
        except:
            return False
        
        return self.list

    def saveToLocal(self):
        try:
            with open(saveFilePath / 'data.json', 'w') as jsonFile:
                dumpList = {'steam_ids' : self.list}
                data = json.dump(jsonFile, dumpList)
            return True
        except:
            return False

       

    def addToList(self, steam_id):
        """Adds specific steam_id to the list"""
        try:
            self.list.append(steam_id)


            return True
        except:
            return False

    def removeFromList(self, steam_id):
        """Removes specific steam_id to the list"""
        count = 0
        for id in self.list:
            if id == steam_id:
                self.list.pop(count)
            count += 1
            

global Game_List
Game_List = GameList()
        


        
         
        
