import psycopg2
import os

class BancoDeDados:

    def __init__(self):
        self.conexao = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.conexao.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()

    def retorna_parametros_conexao_banco_de_dados(self):
        parametros_conexao = {
            "user": os.getenv("user"),
            "password": os.getenv("password"),
            "host": os.getenv("host"),
            "port": os.getenv("port"),
            "database": os.getenv("database"),
        }
        return parametros_conexao