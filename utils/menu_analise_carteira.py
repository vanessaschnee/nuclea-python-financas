from models.cliente import Cliente
from models.ordem import Ordem

def menu_analise_carteira():
    control_consulta_carteira = True
    while control_consulta_carteira:

        cpf_acao_cliente = input("Digite o CPF do cliente que deseja ter sua carteira analisada: ")

        conexao = Cliente()
        consulta = conexao.consultar_cliente(cpf_acao_cliente)
        print(f'\nDados do dono(a) da carteira- \n'
              f'Nome: {consulta["Nome"]}\n'
              f'CPF: {consulta["CPF"]}')

        if consulta:
            resposta_seguir = input("\nDeseja seguir? [sim/nao] \n").lower()

            if resposta_seguir == "sim":
                consulta_id = str(consulta["Id"])
                conexao = Ordem()
                conexao.consultar_acoes_carteira(consulta_id)
                control_consulta_carteira = False

            else:
                control_consulta_carteira = False

        else:
            pass