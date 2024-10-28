import unittest
import src.funcoes as func

class TestCAlculadora(unittest. TestCase):

    def test_multiplicar(self):
        self.assertEqual(func.multiplicar(4, 2), 8)
        self.assertEqual(func.multiplicar(8, 8), 64)
        print("Multiplicação OK!")

    def test_dividir(self):
        self.assertEqual(func.multiplicar(2, 0.5), 1)
        self.assertEqual(func.multiplicar(4, 0.5), 2)
        print("Divisão OK!")

    def test_completo(self):
        self.assertEqual(func.main("1",2), 20)
        print("Funcionando corretamente!")

    def test_erro(self):
        self.assertEqual(func.main("b",6), None)
        print("Ocorreu um erro!")

    def test_saida(self):
        self.assertEqual(func.main("2",8), None)
        print("Saindo corretamente!")



        