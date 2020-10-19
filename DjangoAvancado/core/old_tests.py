from django.test import TestCase


def add_num(num):
    return num + 1


class SimplesTestCase(TestCase):
    """
    1. Qual função de teste sempre começa com "test_", pois o Django vai procurar métodos que começam dessa forma.
    2. Caso os testes precisem do BD, o DJango cria um novo BD para testes, e no final destroi ele.
    3. No console, cada ponto "." representa um teste que foi rodado. Se aparecer um "F", o teste falhou.
    """
    # Esta função serve para roda toda vez que o teste é iniciado
    def setUp(self):
        print('Iniciando o TestCase')
        self.numero = 41

    # Testa a unidade de código
    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 42)
