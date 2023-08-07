import unittest
from unittest.mock import patch
from faker import Faker
from main import main
from utils.menu_cliente import list_client
from utils.valida_cpf import gera_cpf

class TestStringMethods(unittest.TestCase):
    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def test_cliente(self):

        nome = self.gerar_nome_fake()
        cpf = gera_cpf()

        inputs = [1, 1, nome, cpf, "387071489", "23/12/1993", "20520050", "79", 5, "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            "nome": nome,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "38.707.148-9",
            "data_nascimento": "23/12/1993",
            "endereco": {'CEP': '20520-050', 'Logradouro': 'Rua Conde de Bonfim',
                         'Bairro': 'Tijuca', 'Cidade': 'Rio de Janeiro', 'Estado': 'RJ'},
            "num_casa": '79'
        }

        self.assertIn(cliente_esperado, list_client)
