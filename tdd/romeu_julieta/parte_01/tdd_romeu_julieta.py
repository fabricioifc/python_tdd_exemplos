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
	def teste_existe_romeu_e_julieta(self):
		romeu_julieta()

main()