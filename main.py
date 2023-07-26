from utils.funcoes_auxiliares import *
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg

control = True
list_client = []

while control:
    menu = int(input("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. "
                     "Selecione uma as opções abaixo: \n "
                     "1 - Cadastrar Cliente\n "
                     "2 - Cadastrar ação\n "
                     "3 = Realizar análise da carteira\n "
                     "4 - Imprimir relatório da carteira\n "
                     "5 - Sair\n "
                     "Digite a opção desejada: "))

    if menu == 1:
        print("informe os dados do cliente:")
        client = {
            "nome": format_text(input("Nome: ")),
            "cpf": valida_cpf(input("CPF: ").replace(".","").replace("-","")),
            "rg": valida_rg(input("RG: ").replace(".","").replace("-","")),
            "data_nascimento": input("Data de nascimento: "),
            "cep": input("CEP: "),
            "num_casa": input("Número casa: "),
        }

        list_client.append(client)
        print(list_client)
        validador = return_menu_principal()

    elif menu == '2':
        pass
    elif menu == '3':
        pass
    elif menu == '4':
        pass
    elif menu == '5':
        print("Obrigada por utilizar nosso programa.")
        control = False
    else:
        print("Opção inválida, tente novamente.")
