import unittest
from unittest.mock import patch
from main import main


class TestStringMethods(unittest.TestCase):
    def test_consulta_cliente(self):

        inputs = [1, 2, "123.456.789-01", 5, 'nao']

        with patch("builtins.input", side_effect=inputs):
            main()

        self.assertIn()
