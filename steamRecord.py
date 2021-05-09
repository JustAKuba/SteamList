from urllib.request import urlopen
import urllib
import re
import datetime
import time
import json
import gui

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

    def save(self):
        """Saves game into a file."""
        pass
            

    
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
        
         
        
