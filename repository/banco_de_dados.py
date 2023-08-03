import psycopg2
import os

def retorna_parametros_conexao_banco_de_dados():
    parametros_conexao = {
        "user": os.getenv("user"),
        "password": os.getenv("password"),
        "host": os.getenv("host"),
        "port": os.getenv("port"),
        "database": os.getenv("database"),
    }

    return parametros_conexao

def conexao_postgres():
    conecction = psycopg2.connect(**retorna_parametros_conexao_banco_de_dados())
    cursor = conecction.cursor()
    return cursor, conecction

def seleciona_cliente_banco_de_dados():
    print("Buscando os clientes no banco de dados.")
    select_query = "SELECT * FROM CLIENTE"
    cursor, connection = conexao_postgres()
    cursor.execute(select_query)
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)


def insert_cliente_banco_de_dados(list_client):
    insert_query = """
    INSERT INTO public.cliente(
        nome, cpf, rg, data_nascimento, cep, logradouro, bairro, cidade, estado, num_casa)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    values = list_client[0]["nome"],list_client[0]["cpf"],\
        list_client[0]["rg"],list_client[0]["data_nascimento"],\
        list_client[0]["endereco"]["CEP"],list_client[0]["endereco"]["Logradouro"], \
        list_client[0]["endereco"]["Bairro"], list_client[0]["endereco"]["Cidade"], \
        list_client[0]["endereco"]["Estado"], list_client[0]["num_casa"]

    cursor, connection = conexao_postgres()
    cursor.execute(insert_query,values)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    seleciona_cliente_banco_de_dados()