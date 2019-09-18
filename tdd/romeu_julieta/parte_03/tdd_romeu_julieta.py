'''
Uma entrada de valores numéricos

Quando for:
3x			->	Queijo
5x			->	Goiabada
3x e 5x		->	Romeu e Julieta
'''
from unittest import TestCase, main
from app import romeu_julieta

class TesteRomeuEJulieta(TestCase):
	# def teste_existe_romeu_e_julieta(self):
	# 	romeu_julieta()

	def teste_rej_deve_retornar_queijo_quando_for_multiplos_de_3(self):
		valores_entrada = [3, 6, 9]
		valor_experado = 'queijo'
		for valor in valores_entrada:
			with self.subTest(valor=valor):
				self.assertEqual(romeu_julieta(valor), valor_experado)

	def teste_rej_deve_retornar_queijo_quando_for_5(self):
		valor_entrada = 5
		valor_experado = 'goiabada'
		self.assertEqual(romeu_julieta(valor_entrada), valor_experado)

	def teste_rej_deve_retornar_romeu_e_julieta_quando_for_15(self):
		valor_entrada = 15
		valor_experado = 'romeu e julieta'
		self.assertEqual(romeu_julieta(valor_entrada), valor_experado)

main()