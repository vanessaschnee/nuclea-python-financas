import psycopg2
import os

from carteira import analise_carteira
from repository.BancoDeDados import BancoDeDados


class Ordem (BancoDeDados):
    def __init__(self):

        super().__init__()

        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None
        self.conexao = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.conexao.cursor()

    def __del__(self):
        super().__del__()

    def retorna_parametros_conexao_banco_de_dados_em_ordem(self):
        parametros_conexao = super().retorna_parametros_conexao_banco_de_dados()
        return parametros_conexao

    def cadastrar_acao(self, acao, cliente_id):
        self.nome = acao[0]["nome"]
        self.ticket = (acao[0]["ticket"] + '.SA').replace(" ","")
        self.valor_compra = acao[0]["valor_compra"]
        self.quantidade_compra = acao[0]["quantidade_compra"]
        self.data_compra = acao[0]["data_compra"]
        self.cliente_id = cliente_id["Id"]

        insert_query = f"""
                INSERT INTO public.ordem (nome, ticket, valor_compra, quantidade_compra,
                data_compra, cliente_id)
                VALUES(%s, %s, %s, %s, %s, %s);
                """

        values = (
            self.nome, self.ticket, self.valor_compra, self.quantidade_compra, self.data_compra,
            self.cliente_id
        )

        try:
            self.cursor.execute(insert_query, values)
            self.conexao.commit()
            print("Ordem cadastrada com sucesso!")
        except psycopg2.Error as e:
            self.conexao.rollback()
            print("Erro ao cadastrar ordem:", e)

    def consultar_acoes_carteira(self, cliente_id):
        self.cliente_id = cliente_id

        select_query = """
                        SELECT ticket 
                        FROM public.ordem 
                        WHERE cliente_id = %s;
                """

        try:
            self.cursor.execute(select_query, cliente_id)
            carteira_encontrada = self.cursor.fetchall()

            if carteira_encontrada:
                analise_carteira(carteira_encontrada)
            else:
                print("Carteira não encontrada.")

        except psycopg2.Error as e:
            self.conexao.rollback()
            print("\nErro ao encontrar carteira:", e)




