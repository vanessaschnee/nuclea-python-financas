from repository.banco_de_dados import insert_cliente_banco_de_dados
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
        menu = int(input("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. "
                         "Selecione uma as opções abaixo: \n "
                         "1 - Acessar Menu Clientes\n "
                         "2 - Cadastrar ação\n "
                         "3 = Realizar análise da carteira\n "
                         "4 - Imprimir relatório da carteira\n "
                         "5 - Sair\n "
                         "Digite a opção desejada: "))

        if menu == 1:
            opcao_menu_um = int(input("Selecione uma as opções abaixo: \n "
                                      "1 - Cadastrar Cliente\n "
                                      "2 - Consultar Cliente\n "
                                      "3 - Atualizar Cliente\n "
                                      "4 - Deletar Cliente\n "
                                      "5 - Voltar ao menu anterior\n "
                                      "Digite a opção desejada: "))

            if opcao_menu_um == 1:
                client = {
                    "nome": format_text(),
                    "cpf": valida_cpf(),
                    "rg": valida_rg(),
                    "data_nascimento": valida_data_nascimento(),
                    "endereco": valida_cep(),
                    "num_casa": input("Número casa: "),
                }

                list_client.append(client)
                insert_cliente_banco_de_dados(list_client)
                print(list_client)

        elif menu == 2:
            print("Informe os dados da ação: ")
            acao = {
                "nome": input("Nome: "),
                "ticket": input("Ticket: "),
                "valor_compra": float(input("Valor da compra por ação: ")),
                "quantidade_compra": int(input("Quantidade de ações: ")),
                "data_compra": input("Data da compra: ")
            }

            cadastro_acao.append(acao)
            print(cadastro_acao)

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