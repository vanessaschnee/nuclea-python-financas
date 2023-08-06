from models.cliente import Cliente
from models.ordem import Ordem
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import return_menu_principal, format_text
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg
from utils.valida_endereco import valida_cep

list_client = []
cadastro_acao = []

def main():
    control = True
    while control:
        menu = int(input("\nSeja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. "
                         "Selecione uma as opções abaixo: \n "
                         "1 - Acessar Menu Clientes\n "
                         "2 - Cadastrar ação\n "
                         "3 = Realizar análise da carteira\n "
                         "4 - Imprimir relatório da carteira\n "
                         "5 - Sair\n "
                         "Digite a opção desejada: "))

        if menu == 1:
            control_menu_cliente = True

            while control_menu_cliente:
                opcao_menu_cliente = int(input("\nSelecione uma as opções abaixo: \n "
                                          "1 - Cadastrar Cliente\n "
                                          "2 - Consultar Cliente\n "
                                          "3 - Atualizar Cliente\n "
                                          "4 - Deletar Cliente\n "
                                          "5 - Voltar ao menu anterior\n "
                                          "Digite a opção desejada: "))

                if opcao_menu_cliente == 1:
                    client = {
                        "nome": format_text(),
                        "cpf": valida_cpf(),
                        "rg": valida_rg(),
                        "data_nascimento": valida_data_nascimento(),
                        "endereco": valida_cep(),
                        "num_casa": input("Número casa: "),
                    }

                    list_client.append(client)
                    conexao = Cliente()
                    conexao.cadastrar_cliente(list_client)
                    print(list_client)

                elif opcao_menu_cliente == 2:
                    cpf = input("\nDigite o CPF do cliente para consulta:")

                    conexao = Cliente()
                    conexao.consultar_cliente(cpf)

                elif opcao_menu_cliente == 3:
                    cpf = input("\nDigite o CPF do cliente que deseja alterar:")
                    conexao = Cliente()
                    conexao.alterar_cliente(cpf)

                elif opcao_menu_cliente == 4:
                    cpf = input("\nDigite o CPF do cliente que deseja excluir da base de dados:")
                    conexao = Cliente()
                    conexao.deletar_cliente(cpf)

                elif opcao_menu_cliente == 5:
                    control_menu_cliente = False

                else:
                    print("Opção inválida, digite novamente.")


        elif menu == 2:
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
                            "valor_compra": float(input("Valor da compra por ação: ").replace(",",".")),
                            "quantidade_compra": int(input("Quantidade de ações: ")),
                            "data_compra": input("Data da compra: ")
                        }

                        cadastro_acao.append(acao)
                        conexao = Ordem()
                        conexao.cadastrar_acao(cadastro_acao,consulta)
                        print(f"\nReveja o que foi inserido na conta de {consulta['Nome']}:\n "
                              f"{cadastro_acao} \n")

                        control_acao = False

                    else:
                        control_acao = False
                else:
                    pass


        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            print("Obrigada por utilizar nosso programa.")
            control = False
        else:
            print("Opção inválida, tente novamente.")

        return_menu = return_menu_principal()
        if return_menu:
            continue
        else:
            control = False

if __name__ == "__main__":
    main()