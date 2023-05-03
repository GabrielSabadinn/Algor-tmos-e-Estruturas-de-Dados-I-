from abc import ABC, abstractmethod
from carro import carro


class veiculo(ABC):
    def __init__(self, modelo =None, ano=None):
        self.modelo = modelo
        self.ano = ano


    def imprimir(self):
        print("Modelo: " + str(self.modelo))
        print("ano: " + str(self.ano))


    @abstractmethod
    def imprimirEspecifico(self):
        super().imprimir()
        print("Portas " +str(self.qntdportas))