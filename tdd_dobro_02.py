# coding: utf-8
# Dobro de um número (com funções)

def calcular_dobro(numero: int) -> int:
	return int(numero * int(numero))

assert 1 == calcular_dobro('1')
assert 4 == calcular_dobro(2)