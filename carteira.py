import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def analise_carteira(lista_carteira):

    start_date = input("Informe a data de início da consulta (YYYY-MM-DD): ")
    end_date = input("Informa a data final da consulta (YYYY-MM-DD): ")

    df = pd.DataFrame()

    for i in lista_carteira:
        cotacao = yf.download(i, start=start_date, end=end_date)
        df[i] = cotacao['Adj Close']

    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()


