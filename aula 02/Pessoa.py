class Pessoa:
    idade = None

    def __init__(self,nome,idade):
        print("objeto instanciado")
        #self.nome = "Sabadin"
        self.nome = nome 
        self.idade = idade
        self.fone = input("Seu celular por favo: ")

    def imprimit(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Celular: ", self.fone)
