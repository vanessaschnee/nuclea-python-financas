from models.cliente import Cliente
from models.ordem import Ordem
from utils.data import valida_data

cadastro_acao = []
def menu_ordem():
    control_acao = True
    while control_acao:
        cpf_acao_cliente = input("Digite o CPF do cliente que irá ter ações adicionadas na carteira: ")

        conexao = Cliente()
        consulta = conexao.consultar_cliente(cpf_acao_cliente)
        print(f'\nDados do dono(a) da carteira- \n'
              f'Nome: {consulta["Nome"]}\n'
              f'CPF: {consulta["CPF"]}')

        if consulta:
            resposta_seguir = input("\nDeseja seguir? [sim/nao] \n").lower()

            if resposta_seguir == 'sim':
                print("\nInforme os dados da ação-")

                acao = {
                    "nome": input("Nome: "),
                    "ticket": input("Ticket: "),
                    "valor_compra": float(input("Valor da compra por ação: ").replace(",", ".")),
                    "quantidade_compra": int(input("Quantidade de ações: ")),
                    "data_compra": valida_data()
                }

                cadastro_acao.append(acao)
                conexao = Ordem()
                conexao.cadastrar_acao(cadastro_acao, consulta)
                print(f"\nReveja o que foi inserido na conta de {consulta['Nome']}:\n "
                      f"{cadastro_acao} \n")

                control_acao = False

            else:
                control_acao = False
        else:
            pass