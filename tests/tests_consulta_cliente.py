import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMainFunction(unittest.TestCase):
    def test_consulta_cliente(self):

        inputs = [1, 2, "987.654.321-09", 5, 'nao']

        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new=StringIO()) as output:
            main()

        resultado_saida = output.getvalue()

        self.assertIn("Dados do cliente-", resultado_saida)
        self.assertIn("Nome: Maria Oliveira", resultado_saida)
        self.assertIn("CPF: 987.654.321-09", resultado_saida)
        self.assertIn("RG: 123456789", resultado_saida)
        self.assertIn("Data de Nascimento: 1982-02-28", resultado_saida)
        self.assertIn("Logradouro: Av. das Palmeiras, 456", resultado_saida)
        self.assertIn("Bairro: Jardim Botânico", resultado_saida)
        self.assertIn("Cidade: Rio de Janeiro", resultado_saida)
        self.assertIn("Estado: RJ", resultado_saida)
        self.assertIn("Num_casa: 456", resultado_saida)
        self.assertIn("CEP: 56789-321", resultado_saida)

if __name__ == '__main__':
    unittest.main()

