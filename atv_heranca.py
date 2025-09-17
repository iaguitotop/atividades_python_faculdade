class Empregado:
  def __init__ (self, nome, salario_base):
    self.nome = nome
    self.salario_base = salario_base

#Criando a classe gerente
class Gerente(Empregado):
  def __init__ (self, nome, salario_base, bonus):
    super().__init__(nome, salario_base)
    self.bonus = bonus
  def saldo (self):
    return f"Saldo base: {self.salario_base}"
  def bonus_fx (self):
    bonus = 500
    return f"Bônus: {bonus} "
  def saldo_total (self):
    soma = self.salario_base + self.bonus

gerente = Gerente("carlos", 3000, 500)
print(gerente.saldo)
print(gerente.bonus_fx)
print(gerente.saldo_total)