import requests
import json

def busca_cep(cep):
        url = f'http://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:

                #tratar caso tenha algo em branco/vazio

                endereco = {
                    "CEP": data["cep"],
                    "Logradouro": data["logradouro"],
                    "Bairro": data["bairro"],
                    "Cidade": data["localidade"],
                    "Estado": data["uf"]
                }

                for chave, valor in endereco.items():
                    if valor in chave == "":
                        endereco.remove(chave)

                return(endereco)

def valida_cep():
    while True:
        cep_input = input("CEP: ").replace("-", "").replace(".", "")

        if cep_input.isdigit() and len(cep_input) == 8:
            retorno_cep = busca_cep(cep_input)
            if retorno_cep:
                return retorno_cep
            else:
                print("CEP não encontrado ou inválido.")
        else:
            print("CEP não encontrado ou inválido.")


if __name__ == "__main__":
    print(valida_cep())