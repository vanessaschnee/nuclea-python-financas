import yfinance as yf
def obter_dados_acao(ticket, nome_arquivo):

    try:

        print("Coletando dados da ação: " + ticket + '\n')

        acao = yf.download(ticket + '.SA', progress=False)

        print(acao)

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatório da ação: " + ticket)
            arquivo.write(str(acao.tail()))

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique se o nome está correto.")