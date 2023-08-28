from utils.relatorio import obter_dados_acao
import datetime

def menu_relatorio_carteira():
    ticket = input("Digite o ticket da ação: ")

    # Obter a data, hora e segundo atual no formato "dia/mês/ano hora:minuto:segundo"
    data_hora_atual = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Criar o nome do arquivo combinando a data, hora e segundo atual com 'relatorio.txt'
    nome_arquivo = data_hora_atual.replace(":", "-").replace(" ", "_").replace("/", "-") + '_relatorio.txt'

    obter_dados_acao(ticket, nome_arquivo)

if __name__ == "__main__":
    menu_relatorio_carteira()

