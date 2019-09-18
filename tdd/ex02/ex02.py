# ex02.py
import unittest
from helloworld import get_greetings

class SegundoTeste(unittest.TestCase):
	
	def test_ola_mundo(self):
		self.assertEqual(get_greetings(), 'Hello World!')

if __name__ == '__main__':
	unittest.main()