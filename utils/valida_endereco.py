import requests
import json

def busca_cep(cep):
        url = f'http://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                return(data)

def valida_cep():
    while True:
        cep_input = input("CEP: ").replace("-", "")

        if cep_input.isdigit() and len(cep_input) == 8:
           return busca_cep(cep_input)

if __name__ == "__main__":
    print(valida_cep())