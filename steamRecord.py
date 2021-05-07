from urllib.request import urlopen  
from pathlib import Path
import re
import datetime
import time

def monthToNumber(month):
#Converts three char month to number
	try:
		return time.strptime(month, '%b').tm_mon 
	except:
		return 0


class Game:
    
    def __init__(self,steam_id):
        "Represents data object of a game"
        self.steam_id = steam_id
        self.name = ""
        self.price = 0.0
        self.publisher = ""
        self.developer = ""
        self.releaseDate = ""

    def update(self):
        "Updates information about the game"
        
        
        
        
        
        
        
        
        
        
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

