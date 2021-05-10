import gui
import steamRecord
import tkinter as tk
from tkinter import messagebox
from urllib.request import urlopen
import urllib
import re
import datetime
import time
import json
from pathlib import Path

class App:

    def __init__(self):
        gui.activate()
        


        game = steamRecord.Game(1330460)
        game.load()
        gui.window.add_game(game.steam_id, game.name, game.price, game.publisher, game.developer, game.releaseDate)


app = App()

