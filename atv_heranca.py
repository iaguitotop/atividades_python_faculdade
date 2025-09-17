class Empregado:
  def __init__ (self, nome, salario_base):
    self.nome = nome
    self.salario_base = salario_base

#Criando a classe gerente
class Gerente(Empregado):
  def __init__ (self, nome, salario_base, bonus):
    super().__init__(nome, salario_base)
    self.bonus = bonus
  def saldo_g (self):
    return f"Saldo base: {self.salario_base}"
  
  def bonus_fx (self):
    bonus = 500
    return f"Bônus: {bonus} "
  def saldo_total (self):
    soma = self.bonus + self.salario_base
    return f"Valor total: {soma}"

gerente = Gerente("carlos", 3000, 500)
print(gerente.nome)
print(gerente.saldo_g())
print(gerente.bonus_fx())
print(gerente.saldo_total())

class Vendedor(Empregado):
  def __init__ (self, nome, salario_base, comissao):
    super().__init__(nome, salario_base)
    self.comissao = comissao
  
  def saldo_v (self):
    return f"Saldo base: {self.salario_base}"
  
  def comissao_v (self):
    return f"sua comissão é: {self.comissao}%"
  
  def saldo_total_v (self):
    multi = self.salario_base * self.comissao
    return f"Saldo total: {multi :.2f} "

vendedor = Vendedor("Gustavo", 3000, 1.1)
print(vendedor.nome)
print(vendedor.saldo_v())
print(vendedor.comissao_v())
print(vendedor.saldo_total_v())