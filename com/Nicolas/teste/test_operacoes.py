from unittest import TestCase
from com.Nicolas.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1,5]), 6, "Should be 6")

    def test_palavra(self):
        self.assertEqual(self.operacoes.numeroLetras('Nick'), 4, "Should be 4")