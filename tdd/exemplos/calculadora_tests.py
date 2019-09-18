# código-fonte: https://github.com/MeteHanC/Calculator-TDD-Python/blob/master/CalculatorTests.py
from unittest import TestCase, main
import calculadora

class CalculadoraTests(TestCase):
	
	def setUp(self):
		self.calculadora = calculadora.Calculadora()

	def test_somar_dois_numeros(self):
		numero_um = 4
		numero_dois = 2
		resultado = self.calculadora.somar(numero_um, numero_dois)
		self.assertEqual(resultado, 6)

	def test_valores_invalidos(self):
		numero_um = 'quatro'
		numero_dois = 'dois'
		self.assertRaises(ValueError, self.calculadora.somar, numero_um, numero_dois)

	def test_multiplicar(self):
		numero_um = 4
		numero_dois = 2
		resultado = self.calculadora.multiplicar(numero_um, numero_dois)
		self.assertEqual(resultado, 8)

	def test_dividir(self):
		numero_um = 4
		numero_dois = 2
		resultado = self.calculadora.dividir(numero_um, numero_dois)
		self.assertEqual(resultado, 2)

	def test_divisao_por_zero(self):
		numero_um = 5
		numero_dois = 0
		self.assertRaises(ZeroDivisionError, self.calculadora.dividir, numero_um, numero_dois)

	def tearDown(self):
		self.calculadora = None
		

main()