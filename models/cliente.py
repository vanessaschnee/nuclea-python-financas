import psycopg2
import os


class Cliente:

    def __init__(self):
        self.id = None
        self.cpf = None
        self.nome = None
        self.rg = None
        self.data_nascimento = None
        self.cep = None
        self.logradouro = None
        self.numero_residencia = None
        self.bairro = None
        self.cidade = None
        self.estado = None
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

    def cadastrar_cliente(self, cliente):
        self.nome = cliente[0]["nome"]
        self.cpf = cliente[0]["cpf"]
        self.rg = cliente[0]["rg"]
        self.data_nascimento = cliente[0]["data_nascimento"]
        self.cep = cliente[0]["endereco"]["CEP"]
        self.logradouro = cliente[0]["endereco"]["Logradouro"]
        self.numero_residencia = cliente[0]["num_casa"]
        self.bairro = cliente[0]["endereco"]["Bairro"]
        self.cidade = cliente[0]["endereco"]["Cidade"]
        self.estado = cliente[0]["endereco"]["Estado"]

        insert_query = """
        INSERT INTO public.cliente (nome, cpf, rg, data_nascimento,
        cep, logradouro, bairro, cidade, estado, num_casa)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        values = (
            self.nome, self.cpf, self.rg, self.data_nascimento, self.cep,
            self.logradouro, self.bairro, self.cidade, self.estado, self.numero_residencia
        )

        try:
            self.cursor.execute(insert_query, values)
            self.conexao.commit()
            print("Cliente cadastrado com sucesso!")
        except psycopg2.Error as e:
            self.conexao.rollback()
            print("Erro ao cadastrar cliente:", e)

    def consultar_cliente(self, cpf, cliente=None):
        self.cpf = cpf

        select_query = """
                SELECT * FROM public.cliente WHERE cpf = %s;
        """

        try:
            self.cursor.execute(select_query, (self.cpf,))
            cliente_encontrado = self.cursor.fetchone()

            if cliente_encontrado:
                dict_cliente_encontrado = {
                    "Nome": cliente_encontrado[1],
                    "CPF": cliente_encontrado[2],
                    "RG": cliente_encontrado[3],
                    "Data de Nascimento": cliente_encontrado[4],
                    "Logradouro": cliente_encontrado[6],
                    "Bairro": cliente_encontrado[7],
                    "Cidade": cliente_encontrado[8],
                    "Estado": cliente_encontrado[9],
                    "Num_casa": cliente_encontrado[10],
                    "CEP": cliente_encontrado[5]
                }

                return dict_cliente_encontrado

            else:
                print("Cliente não encontrado.")

        except psycopg2.Error as e:
            self.conexao.rollback()
            print("Erro ao encontrar cliente:", e)

    def alterar_cliente(self, cpf):
        cliente_encontrado = self.consultar_cliente(cpf)
        print(cliente_encontrado)

        if not cliente_encontrado:
            return

        campo_de_alteracao = int(input("\nDigite o número da alteração que deseja realizar:\n"
                                       "[1] Nome\n"
                                       "[2] CPF\n"
                                       "[3] RG\n"
                                       "[4] Data de Nascimento\n"
                                       "[5] Logradouro \n"
                                       "[6] Bairro \n"
                                       "[7] Cidade \n"
                                       "[8] Estado \n"
                                       "[9] Número da casa \n"
                                       "[10] CEP\n"
                                       "\nQual campo você deseja alterar? "))

        campos_para_alterar = {
            1: "nome",
            2: "cpf",
            3: "rg",
            4: "data_nascimento",
            5: "logradouro",
            6: "bairro",
            7: "cidade",
            8: "estado",
            9: "numero_residencia",
            10: "cep",
        }

        campo = campos_para_alterar.get(campo_de_alteracao)

        if not campo:
            print("Opção inválida.")
            return

        novo_valor = input(f"\nDigite o novo valor para '{campo}': ")

        setattr(self, campo, novo_valor)

        update_query = f"""
            UPDATE public.cliente SET {campo} = %s WHERE cpf = %s;
        """
        values = (novo_valor, cpf)

        try:
            self.cursor.execute(update_query, values)
            self.conexao.commit()
            print(f"{campo.title()} do cliente foi alterado com sucesso!")

            cliente_atualizado = self.consultar_cliente(cpf)
            if cliente_atualizado:
                print("\nDados atualizados do cliente:")
                for chave, valor in cliente_atualizado.items():
                    print(f"{chave}: {valor}")

        except psycopg2.Error as e:
            self.conexao.rollback()
            print(f"Erro ao alterar {campo} do cliente:", e)

    def deletar_cliente(self, cpf):
        cliente_encontrado = self.consultar_cliente(cpf)

        if not cliente_encontrado:
            return

        delete_query = """
            DELETE FROM public.cliente WHERE cpf = %s;
        """
        values = (cpf,)

        try:
            self.cursor.execute(delete_query, values)
            self.conexao.commit()
            print("Cliente deletado da base de dados com sucesso!")
        except psycopg2.Error as e:
            self.conexao.rollback()
            print("Erro ao deletar cliente:", e)


if __name__ == "__main__":
    cpf = "873.797.470-02"
    conexao = Cliente()
    resultado_consulta = conexao.deletar_cliente(cpf)

