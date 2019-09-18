# código-fonte: https://github.com/MeteHanC/Calculator-TDD-Python/blob/master/CalculatorTests.py
class Calculadora():

	TIPOS_NUMERICOS = (int, float, complex)

	@staticmethod
	def validar_numero(x, y):
		if not isinstance(x, Calculadora.TIPOS_NUMERICOS):
			raise ValueError
		if not isinstance(y, Calculadora.TIPOS_NUMERICOS):
			raise ValueError
	
	def somar(self, n1, n2):
		self.validar_numero(n1, n2)
		return n1 + n2

	def multiplicar(self, n1, n2):
		self.validar_numero(n1, n2)
		return n1 * n2

	def dividir(self, n1, n2):
		self.validar_numero(n1,n2)
		try:
			return n1 / n2
		except ZeroDivisionError as e:
		    raise ZeroDivisionError('Divisão por Zero não é permitida!') from e
		finally:
			pass