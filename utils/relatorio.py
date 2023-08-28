import yfinance as yf
from s3.upload_success import upload_success

def obter_dados_acao(ticket, nome_arquivo):

    try:

        print("Coletando dados da ação: " + ticket + '\n')

        acao = yf.download(ticket + '.SA', progress=False)

        print(acao)

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatório da ação: " + ticket)
            arquivo.write(str(acao.tail()))

        upload_success(nome_arquivo)

    except Exception as e:
        print("Erro ao obter dados da ação. Verifique se o nome está correto.")




