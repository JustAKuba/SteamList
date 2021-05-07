from urllib.request import urlopen
from pathlib import Path
import re
import datetime
import time
import json

def monthToNumber(month):
    """Converts three char month to number"""
    return time.strptime(month, '%b').tm_mon 


class Game:
    
    def __init__(self,steam_id):
        "Represents data object of a game"
        self.steam_id = str(steam_id)
        self.name = ""
        self.price = 0.0
        self.publisher = ""
        self.developer = ""
        self.releaseDate = ""

    def update(self):
        "Updates information about the game"
        
        req = urlopen('https://store.steampowered.com/api/appdetails?appids=' + str(self.steam_id))
        rawData = json.load(req)
        gameData = rawData[self.steam_id]["data"]



        self.name = gameData["name"]
        self.price = gameData["package_groups"][0]["subs"][0]["price_in_cents_with_discount"]
        self.price = self.price/100
        self.publisher = gameData["publishers"][0]
        self.developer = gameData["developers"][0]
        tempReleaseDate = gameData["release_date"]["date"]
        tempReleaseDate = re.sub(r'[^\w]', ' ', tempReleaseDate).split(" ")
        numMonth = monthToNumber(tempReleaseDate[1])
        self.releaseDate = datetime.date(int (tempReleaseDate[3]), int (numMonth), int(tempReleaseDate[0]))

        print(self.name)
        print(self.price)
        print(self.publisher)
        print(self.developer)
        print(self.releaseDate)


deb = Game(107410)
deb.update()