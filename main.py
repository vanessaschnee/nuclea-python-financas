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
            "nome": input("Nome: "),
            "cpf": input("CPF: "),
            "rg": input("RG: "),
            "data_nascimento": input("Data de nascimento: "),
            "cep": input("CEP: "),
            "num_casa": int(input("Número casa: ")),
        }

        list_client.append(client)
        print(list_client)

        return_menu = input("Deseja retornar ao menu principal [sim/nao]? ")

        if return_menu == 'sim':
            control = True
        else:
            print("Obrigada por utilizar nosso programa.")
            control = False

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