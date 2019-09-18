from operator import mod, eq

def queijo(val: int) -> str:
	return 'queijo' if eq(mod(val, 3), 0) else val

# temos um problema. 15 é múltiplo de 3
def romeu_julieta(val: int):
	if queijo(val) == 'queijo':
		return 'queijo'
	
	if val == 5:
		return 'goiabada'

	return 'romeu e julieta'
