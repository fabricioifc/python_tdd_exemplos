import unittest

class PrimeiroTeste(unittest.TestCase):
	
	def test_uppercase(self):
		self.assertEqual('ola mundo'.upper(), 'OLA MUNDO')

if __name__ == '__main__':
	unittest.main()