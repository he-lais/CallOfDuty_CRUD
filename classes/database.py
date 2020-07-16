import os
import pickle
from classes import exception_messages,file_manager
from classes.file_manager import file_exists, create_file
from classes.my_exception import MyException
from classes.player import Player


class Database:

    CAMINHO_ARQUIVO = os.path.join(os.getcwd(), 'players.pkl')

    def __init__(self):

        # Tabela hash que mapeia a gamertag para um objeto Player
        # Fazendo uma analogia, isso aqui seria uma TABLE no banco de dados MySQL
        self.players = {}
        self.carregar_dados()

    def create(self, gamertag, password):
        """
        Analogia ao INSERT INTO ...

        INSERT INTO Players (Gamertag, Password, TotalWins, FavoriteLoadout, Loadouts) VALUES
                                ('20_matar_70_correr', '123456', '0', NULL, NULL);
        """
        if not gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)

        if self.player_exists(gamertag):
            raise MyException(exception_messages.PLAYER_ALREADY_REGISTERED)

        player = Player(gamertag, password, 0, None, [None] * 10)
        self.players[gamertag] = player

        # Salvando os dados no HDD
        self.salvar_dados()

    def read(self, gamertag, password):
        """
        Analogia ao SELECT * FROM ...
        """
        if not gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)

        if not self.player_exists(gamertag):
            raise MyException(exception_messages.PLAYER_NOT_FOUND)

        player = self.players.get(gamertag)

        if player.password != password:
            raise MyException(exception_messages.WRONG_PASSWORD)

        return player

    def update_gamertag(self, gamertag, password, new_gamertag):
        """
        Analogia ao UPDATE no MySQL ...
        SET Gamertag = new_gamertag WHERE Gamertag = gamertag_atual AND Password = senha_atual;
        """
        if not new_gamertag.strip():
            raise MyException(exception_messages.INVALID_GAMERTAG)

        try:
            # Buscando o jogador na tabela
            player = self.read(gamertag, password)

            # Excluindo o jogador da tabela hash
            # A ENTRADA DA HASH É EXCLUÍDA, MAS O OBJETO CONTINUA EXISTINDO!!!
            del self.players[gamertag]

            # Atualizando a gamertag do jogador
            player.gamertag = new_gamertag

            self.players[new_gamertag] = player

            # Salvando os dados no HDD
            self.salvar_dados()
            return True

        except MyException as e:
            raise e

    def update_password(self, gamertag, password, new_password):
        """
        Analogia ao UPDATE no MySQL ...
        SET Password = nova_senha WHERE Gamertag = gamertag_atual AND Password = senha_atual;
        """
        if not new_password.strip():
            raise MyException(exception_messages.INVALID_PASSWORD)

        try:
            # Buscando o jogador na tabela
            player = self.read(gamertag, password)

            # Atualizando a senha do jogador
            player.password = new_password

            # Salvando os dados no HDD
            self.salvar_dados()
            return True

        except MyException as e:
            raise e

    def delete(self, gamertag, password):
        """
        Analogia ao DELETE FROM no MySQL ...

        DELETE FROM Players WHERE Gamertag = gamertag AND Password = senha;
        """
        try:
            # Buscando o jogador na tabela
            player = self.read(gamertag, password)

            # Removendo a referencia do objeto da tabela hash
            del self.players[gamertag]

            # Removendo o objeto em si da memoria RAM (nao eh necessario, visto que
            # a coleta de lixo ja faz a coleta automatica quando nao tem mais nenhuma
            # referencia do objeto)
            del player

            # Salvando as mudancas no HDD
            self.salvar_dados()

            return True

        except MyException as e:
            raise e

    def player_exists(self, gamertag):
        return False if not self.players or self.players.get(gamertag) is None else True

    def mostrar_tudo(self):
        if not self.players:
            print(exception_messages.EMPTY_DATABASE)
        else:
            print('-=' * 50)
            for player in self.players.values():
                print(player)
                print('-=' * 50)

    def salvar_dados(self):
        """
        Salva os dados da memoria RAM no HDD

        return: True se deu tudo certo, False caso contrario
        """
        try:
            # Abrindo o arquivo em forma de escrita binaria
            with open(self.CAMINHO_ARQUIVO, 'wb') as file:
                pickle.dump(self.players, file, pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(str(e))
            return False

    def carregar_dados(self):
        """
        Carrega os dados do HDD para a memoria RAM

        return: True se deu tudo certo, False caso contrario
        """
        if not file_exists(self.CAMINHO_ARQUIVO):
            file_manager.create_file(self.CAMINHO_ARQUIVO)
            return True

        # Abrindo o arquivo em modo de leitura binario
        with open(self.CAMINHO_ARQUIVO, 'rb') as file:
            try:
                self.players = pickle.load(file)
                return True
            except EOFError as eof:
                print(str(eof))
                return False

'''
db = Database()
db.create('Laís Helena', 123)
'''
