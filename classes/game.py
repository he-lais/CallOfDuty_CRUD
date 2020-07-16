from classes.database import Database

class Game:
    def __init__(self):
        self.database = Database()
       # self.database.mostrar_tudo()
       #self.database.create('Fernanda', 666)
        #self.database.mostrar_tudo()
        #self.database.update_password('Layane', 0301, '12345')
        #player = self.database.read('Fernanda',666)
        #print(player)
        self.database.mostrar_tudo()