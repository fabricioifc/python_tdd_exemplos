from operator import mod, eq

def queijo(val: int) -> str:
	return 'queijo' if eq(mod(val, 3), 0) else val

def queijo_goiabada(val: int) -> str:
	return 'romeu e julieta' if eq(mod(val, 3), 0) and eq(mod(val, 5), 0) else val

def goiabada(val: int) -> str:
	return 'goiabada' if eq(mod(val, 5), 0) else val

# temos um problema. 15 é múltiplo de 3
def romeu_julieta(val: int):
	if queijo_goiabada(val) == 'romeu e julieta':
		return 'romeu e julieta'
	if queijo(val) == 'queijo':
		return 'queijo'
	if goiabada(val) == 'goiabada':
		return 'goiabada'
