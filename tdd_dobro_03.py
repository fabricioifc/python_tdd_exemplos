# coding: utf-8
# Dobro de um número (com funções)
import unittest

class DobroTest(unittest.TestCase):
	
	def test_dobro(self):
		calculo = Calculo()
		self.assertEqual(16, calculo.calcular_dobro(8))

	def teste_valores_alfanumericos(self):
		calculo = Calculo()
		self.assertRaises(TypeError, calculo.calcular_dobro('1'))
		self.assertRaises(TypeError, calculo.calcular_dobro('F'))

class Calculo():

	def calcular_dobro(self, numero: int) -> int:
		return numero * 2

if __name__ == '__main__':
	unittest.main()