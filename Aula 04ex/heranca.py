

class Pessoa:
    def __init__(self, name, fone, city=None ):
        self.id = None 
        self.nome = name 
        self.fone = fone 
        self.cidade = city

    def imprimir(self):
        print("---------------------------------------------")
        print("Nome: ", self.nome)
        print("Telefone: ", self.fone)
        print("Cidade: ", self.cidade.nome)

class Cidade:
    def __init__(self, id, name):
        self.id = id 
        self.nome = name 

class Fisica(Pessoa):
    def __init__(self):
        super().__init__()