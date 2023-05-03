from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}"

    @abstractmethod
    def cadastrar(self):
        pass

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Potência da Fonte: {self._potenciaDaFonte}"

    def cadastrar(self):
        print("Cadastrando Desktop...")

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
   
    def getInformacoes(self):
        return f"{super().getInformacoes()}, Tempo de Bateria: {self.__tempoDeBateria}"
   
    def cadastrar(self):
        print("Cadastrando  o Notebook...")


pc  = Desktop ("Msi", "Branco", 289789.00, "550W")

note = Notebook ("dell", "vermelho", 1431.00, "440")


pc.cadastrar()
note.cadastrar()
print(pc.getInformacoes())
print(note.getInformacoes())