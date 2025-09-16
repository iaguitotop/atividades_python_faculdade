class Aluno:
  def __init__(self): 
    self._nome = []
    self._notas = []

  def get_nome(self): #método para solicitar o nome do aluno e armazenar na lista "nome"
    self.nome = str(input("Coloque seu nome:"))

  def get_notas (self): #solicita quantas notas tem e as notas delas, depois adiciona na lista "notas"
    quantidade = int(input("Digite o número de notas: "))
    for i in range(quantidade):
      nota = float(input(f"Digite a nota {i+1}:"))
      self._notas.append(nota)
  def calcular_media(self): #método para pegar as notas da lista "self._notas" e fazer a média delas
    if len(self._notas) == 0: #verifica se a lista "self._notas" tá vazia
      return 0 #se a lista estiver vazia, a função para aqui
    return sum(self._notas) / len(self._notas) # o "sum" serve pra somar os itens da lista e o "len" pega a quantidade de notas
  def verificar_aprovacao(self):
    media = self.calcular_media()
    print(f"Média final: {media:.2f}")
    if media >= 7:
      print("Você foi aprovado")
    else:
      print("Você foi reprovado")

aluno = Aluno()
aluno.get_nome()
aluno.get_notas()
aluno.verificar_aprovacao()