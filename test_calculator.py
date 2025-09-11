import pytest
from calculator import soma, subtracao, multiplicacao, divisao

def test_soma():
  assert soma(2, 3) == 5
  assert soma(-1, 1) == 0
  assert soma(0, 0) == 0

def test_subtracao():
  assert subtracao(5, 3) == 2
  assert subtracao(3, 5) == -2
  assert subtracao(0, 0) == 0

def test_multiplicacao():
  assert multiplicacao(4, 5) == 20
  assert multiplicacao(-2, 3) == -6
  assert multiplicacao(0, 100) == 0

def test_divisao():
  assert divisao(10, 2) == 5
  assert divisao(9, 3) == 3
  assert divisao(7, 2) == 3.5
  assert divisao(0, 5) == 0
  assert divisao(5, 0) == "Erro: Divisão por zero"
