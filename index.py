class pessoa:
	def __init__(self, name,vida, age, city,luckyNumber, helthy, eating = False,running = False, exercising 
=False):
		self.nome = name
		self.age = age
		self.luckyNumber = luckyNumber
		self.helthy = helthy
		self.running = running
		self.eating = eating
		self.exercising = exercising 

	def runningStart(self):
		self.running = True

	def runningStop(self):
		self.running = False


p1 = pessoa("mario", 19,3, 'manaus',89,'good')

print("=====BEM VINDO ==========")
print("==ESTE JOGO SE CHAMA=====")
print("====JOGO DA VIDA=========")
input("pressione enter")
print("Você tem a incrivel missão de salvar sua familia")
print("Você conseguirá se achar o tesouro escondido no calabouço")
input("Se quiser arriscar tudo, pressione ENTER!!!")

print("=====O COMEÇO =========")
print("Para passar pelos desafio do calabouço")
print("É necessário que você escolha entre duas opções")
print("Uma é boa e outra é a ruim!")
input("pressiona enter")

while level < 10: #aqui é onde tem que rolar todo o negocio tlgd
	



