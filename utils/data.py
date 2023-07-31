from datetime import datetime
def valida_data_nascimento():
    while True:
        data_nascimento = input("Data Nascimento: ")

        try:
            data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("Data inválida, digite novamente.")
        except ValueError as e:
            print(f'Erro: {e}, digite novamente.')

if __name__ == "__main__":
    valida_data_nascimento()