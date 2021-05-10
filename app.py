import gui
import steamRecord

class App:

    def __init__(self):
        gui.activate()
        


        game = steamRecord.Game(1330460)
        game.load()
        gui.window.add_game(game.steam_id, game.name, game.price, game.publisher, game.developer, game.releaseDate)


app = App()

