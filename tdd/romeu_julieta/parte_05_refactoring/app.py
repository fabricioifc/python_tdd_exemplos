from operator import mod, eq

def queijo(val: int) -> str:
	return True if calcular_multiplo(val, 3) else False

def queijo_goiabada(val: int) -> str:
	is_multiplo_de_3 = calcular_multiplo(val, 3)
	is_multiplo_de_5 = calcular_multiplo(val, 5)
	return True if is_multiplo_de_3 and is_multiplo_de_5 else False

def goiabada(val: int) -> str:
	return True if calcular_multiplo(val, 5) else False

def calcular_multiplo(val: int, multiplo: int) -> bool:
	return eq(mod(val, multiplo), 0)

# temos um problema. 15 é múltiplo de 3
def romeu_julieta(val: int) -> str:
	if queijo_goiabada(val):
		return 'romeu e julieta'
	if queijo(val):
		return 'queijo'
	if goiabada(val):
		return 'goiabada'
	# raise Exception('x não é múltiplo válido para Romeu e Julieta: {}'.format(val))