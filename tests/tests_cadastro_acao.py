import unittest
from unittest.mock import patch
from main import main
from utils.menu_ordem import cadastro_acao


class TestStringMethods(unittest.TestCase):
    def test_cadastro_acao(self):
        inputs = [2, "987.654.321-09", "sim", "Itausa", "ITSA4", 9.80, 10, '01/08/2023', "não"]

        with patch("builtins.input", side_effect=inputs):
            main()

        nova_acao = {
            "nome": "Itausa",
            "ticket": "ITSA4",
            "valor_compra": 9.80,
            "quantidade_compra": 10,
            "data_compra": '01/08/2023',
        }

        self.assertIn(nova_acao, cadastro_acao)
