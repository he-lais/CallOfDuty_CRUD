import pickle
import os

from classes import exception_messages
from classes.file_manager import file_exists, create_file
from classes.my_exception import MyException
from classes.player import Player

class Database:
    CAMINHO_ARQUIVO = os.path.join(os.getcwd(), 'players.pkl') #vou precisar de um arquivo

    def __init__(self):
        # Variavel de instancia -> salva os dados dos jogadores
        #cria a tabela hash para que cada objeto do banco de dados tenha um valor diferente

        self.players= {}

    def create(self, gamertag, password):
        #Analogia ao INSERT INTO do banco de dados

        if not gamertag.strip(): #senão for valida
            raise MyException (exception_messages.INVALID_GAMERTAG)

        player = Player (gamertag, password, 0, None, [None] * 10)
        self.players[gamertag] = player #mapeia o jogador por gamertag na tabela hash (tabela players)

    def salvar_dados(self): #Vai salvar a tabela hash 'players' dentro do HD, antes só ficava na memória RAM
        try:
            # Abrindo o arquivo em forma de escrita binaria
            with open(self.CAMINHO_ARQUIVO, 'wb') as file:
                pickle.dump(self.players, file, pickle.HIGHEST_PROTOCOL) #Salva tabela hash dentro do arquivo
            print('Dados salvos com sucesso!')
            return True
        except Exception as e:
            print('Erro ao salvar os dados')
            print(str(e))
            return False

    def carregar_dados(self):

        if not file_exists (self.CAMINHO_ARQUIVO):
            create_file(self.CAMINHO_ARQUIVO)

        # Abrindo o arquivo em modo de leitura binario
        with open(self.CAMINHO_ARQUIVO, 'rb') as file:
            try:
                self.players = pickle.load(file)
                return True
            except EOFError as e:
                print(str(e))
                return False


