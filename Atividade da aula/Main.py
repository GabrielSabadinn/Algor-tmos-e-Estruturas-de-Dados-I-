from abc import ABC, abstractmethod

class computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo 
        self.cor = cor
        self.preco = preco 

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor:{self.cor}, Preço:{self.preco}"
    

    @abstractmethod 
    def cadastrar(self):
        pass 

class Desktop(computador):
    def __init__(self, modelo, cor, preco, potencia_da_fonte):
        super().__init__(modelo, cor, preco)        
        self._potenciadafonte = potencia_da_fonte

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Potencia da fonte:{self._potenciadafonte}"

class Notebook(computador):
    def __init__(self, modelo, cor, preco, tempo_batera):
        super().__init__(modelo, cor, preco)
        self.__tempo_batera = tempo_batera

    def getInformacoes(self):
        return f"{super().imprimir()}, Tempo da Bateria:{self.__tempo_batera}"



pc  = Desktop ("Msi", "Branco", 289789.00, "550W")

note = Notebook ("dell", "vermelho", 1431.00, "440")


print(pc.getInformacoes())
print(note.getInformacoes())