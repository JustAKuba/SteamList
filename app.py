import gui
import steamRecord

class App:

    def __init__(self):
        
        window = gui.Window("Steam List")
        window.initialize()

        debugGame = steamRecord.Game(1239080)
        debugGame.load()

        window.add_game(debugGame.name, debugGame.price, debugGame.publisher, debugGame.developer, debugGame.releaseDate)

        window.show()



    def __del__(self):
        pass



app = App()