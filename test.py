from Calc import somar
from Calc import subtrair
from Calc import multiplicar
from Calc import dividir



def test_somar():
    assert somar(2,4) == 6

def test_subtrair():
    assert subtrair(4,2) == 2

def test_multiplicar():
    assert multiplicar(4,2) == 8

def test_dividir():
    assert dividir(4,2) == 2


