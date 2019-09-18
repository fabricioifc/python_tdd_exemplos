from unittest import TestCase, main
from roma import add

class test_adicionar_numeros_romanos(TestCase):

    def test_adicionando_is(self):
        self.assertEqual(add('I', 'I'), 'II')
        self.assertEqual(add('I', 'II'), 'III')

main()