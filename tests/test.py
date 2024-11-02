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

        input("\nPressione ENTER para continuar os testes.")

        self.assertNotEqual(func.main("1",2), 40)
        print("20 é diferente de 40!")


    def test_letrasErro(self):
        self.assertRaises(TypeError, func.multiplicar("x",9))
        print("Erro bem sucedido!")

    def test_saida(self):
        self.assertIsNone(func.main("2",8))
        print("Saindo corretamente!")



        