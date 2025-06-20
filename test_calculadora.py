import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        """
        Cria uma nova instância de Calculadora para cada teste.
        """
        self.calc = Calculadora()

    def test_somar_numeros_positivos(self):
        """Testa a soma de dois números positivos."""
        self.assertEqual(self.calc.somar(5, 3), 8)

    def test_subtrair_numeros_negativos(self):
        """Testa a subtração com números negativos."""
        self.assertEqual(self.calc.subtrair(10, -5), 15)

    def test_multiplicar_por_zero(self):
        """Testa a multiplicação por zero."""
        self.assertEqual(self.calc.multiplicar(7, 0), 0)

    def test_dividir_numeros_inteiros(self):
        """Testa a divisão de números inteiros."""
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero levanta um ValueError."""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()