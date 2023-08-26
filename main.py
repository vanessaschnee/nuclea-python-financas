from utils.funcoes_auxiliares import return_menu_principal
from utils.menu_analise_carteira import menu_analise_carteira
from utils.menu_cliente import menu_cliente
from utils.menu_ordem import menu_ordem
from utils.menu_relatorio_carteira import menu_relatorio_carteira


def main():
    control = True
    while control:
        menu = int(input("\nSeja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. "
                         "Selecione uma as opções abaixo: \n "
                         "1 - Acessar Menu Clientes\n "
                         "2 - Cadastrar ação\n "
                         "3 - Realizar análise da carteira\n "
                         "4 - Imprimir relatório sobre ação específica e enviá-lo para o S3\n "
                         "5 - Sair\n "
                         "Digite a opção desejada: "))

        if menu == 1:
            menu_cliente()

        elif menu == 2:
            menu_ordem()

        elif menu == 3:
            menu_analise_carteira()

        elif menu == 4:
            menu_relatorio_carteira()

        elif menu == 5:
            print("Obrigada por utilizar nosso programa.")
            exit()

        else:
            print("Valor inválido, digite novamente.")

        return_menu = return_menu_principal()
        if return_menu:
            continue
        else:
            control = False

if __name__ == "__main__":
    main()