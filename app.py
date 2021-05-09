import gui
import steamRecord

class App:

    def __init__(self):
        window = gui.Window("Steam List")
        window.initialize()
        window.add_controls()
        window.show()
    

        



        



    def __del__(self):
        pass



app = App()

