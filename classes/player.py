class Player:

    MAX_NUMBER_OF_LOADOUTS = 10

    def __init__(self, gamertag, password, total_wins, favorite_loadout, loadouts):
        self.gamertag = gamertag
        self.password = password
        self.total_wins = total_wins
        self.favorite_loadout = favorite_loadout
        self.loadouts = loadouts

    def create_loadout(self):
        pass

    def get_loadout(self, index): #le um loadout
        pass

    def update_loadout(self):
        pass

    def delete_loadout(self):
        pass

    #Descrição do meu objeto
    def __str__(self):
        return f'Jogador: [{self.gamertag}]\n' \
               f'Senha: {self.password} \n' \
               f'Vitórias: {self.total_wins} \n' \
               f'Loadout favorito: {self.favorite_loadout} \n' \
               f'Loadouts: {self.loadouts}'