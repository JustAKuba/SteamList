from urllib.request import urlopen
from pathlib import Path
import re
import datetime
import time
import json

def monthToNumber(month):
    """Converts three char month to number"""
    try:
        return time.strptime(month, '%b').tm_mon 
    except:
        return 0


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

        """
        data = requests.get('https://store.steampowered.com/api/appdetails?appids=' + str(self.steam_id))
        gameData = data[self.steam_id]["data"]
        """

        self.name = gameData["name"]
        self.price = gameData["package_groups"][0]["subs"][0]["price_in_cents_with_discount"]
        self.price = self.price/100
        self.publisher = gameData["publishers"][0]
        self.developer = gameData["developers"][0]
        tempReleaseDate = gameData["release_date"]["date"]
        tempReleaseDate = re.sub(r'[^\w]', ' ', tempReleaseDate).split(" ")
        numMonth = monthToNumber(tempReleaseDate[1])
        self.releaseDate = datetime.date(int (tempReleaseDate[3], numMonth, tempReleaseDate[0]))

        print(self.name)
        print(self.price)
        print(self.publisher)
        print(self.developer)
        print(self.releaseDate)



        
        
        
        
        
        
        
        
        """
        with urlopen("https://steamcommunity.com/app/" + str(self.steam_id)) as html:
            data = str(html.read())
        self.name = re.findall('<div class="apphub_AppName">(.*?)</div>', data)
        
        if '<div class="discount_final_price">' in data:
            self.price = re.findall('<div class="discount_final_price">(.*?)</div>', data)
        elif '<div class="game_purchase_price price">' in data:
            self.price = re.findall('<div class="discount_final_price">(.*?)</div>', data)

        tempDev = re.findall('<div class="summary column" id="developers_list"><a href="https://store.steampowered.com/developer/(.*?)</div>', data)
        self.developer = re.findall('>(.*?</a>)', tempPub)

        tempPub = re.findall('<div class="summary column"><a href="https://store.steampowered.com/publisher/(.*?)</div>', data)
        self.publisher = re.findall('>(.*?)</a>', tempPub)

        if '<b>Release Date:</b>' in data:
            tempDate = re.findall('<b>Release Date:</b>(.*?)<br>', data)
        elif '<b>Early Access Release Date:</b>' in data:
            tempDate = re.findall('<b>Early Access Release Date:</b>(.*?)</b>', date)
            
        updateTime = re.sub(r'[^\w]', ' ', tempDate).split(" ")
        self.releaseDate = datetime.date(int (updateTime[3], int (monthToNumber(updateTime[1])), int (updateTime[0]))
        """



deb = Game(107410)
deb.update()