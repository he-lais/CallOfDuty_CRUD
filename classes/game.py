from classes.database import Database

class Game:
    def __init__(self):
        self.database = Database()
        self.database.mostrar_tudo()