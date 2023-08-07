from models.cliente import Cliente
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import format_text, return_menu_principal
from utils.valida_cpf import valida_cpf
from utils.valida_endereco import valida_cep
from utils.valida_rg import valida_rg

list_client = []


def menu_cliente():
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
            consulta = conexao.consultar_cliente(cpf)
            print(f'\nDados do cliente- \n'
                  f'Nome: {consulta["Nome"]}\n'
                  f'CPF: {consulta["CPF"]}\n'
                  f'RG: {consulta["RG"]}\n'
                  f'Data de Nascimento: {consulta["Data de Nascimento"]}\n'
                  f'Logradouro: {consulta["Logradouro"]}\n'
                  f'Bairro: {consulta["Bairro"]}\n'
                  f'Cidade: {consulta["Cidade"]}\n'
                  f'Estado: {consulta["Estado"]}\n'
                  f'Num_casa: {consulta["Num_casa"]}\n'
                  f'CEP: {consulta["CEP"]}')

        elif opcao_menu_cliente == 3:
            cpf = input("\nDigite o CPF do cliente que deseja alterar:")
            conexao = Cliente()
            conexao.alterar_cliente(cpf)

        elif opcao_menu_cliente == 4:
            cpf = input("\nDigite o CPF do cliente que deseja excluir da base de dados:")
            conexao = Cliente()
            resultado = conexao.deletar_cliente(cpf)
            if resultado == False:
                pass

        elif opcao_menu_cliente == 5:
            control_menu_cliente = False

        else:
            print("Opção inválida, digite novamente.")

if __name__ == "__main__":
    menu_cliente()