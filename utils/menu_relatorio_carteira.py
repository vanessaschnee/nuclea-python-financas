from relatorio import obter_dados_acao
def menu_relorio_carteira():
    ticket = input("Digite o ticket da ação: ")
    nome_arquivo = input("Digite o nome do arquivo: ")
    obter_dados_acao(ticket, nome_arquivo)