from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,id ,nome, telefone):
        self.id = id
        self.nome = nome 
        self._telefone = telefone 


    @abstractmethod
    def marcarpresenca(self):
        pass

    @abstractmethod
    def matricular(self):
        pass 

class AlunoGraduacao(Pessoa):
    def __init__(self, id, nome, telefone, matricula, presencas):
        super().__init__(id, nome, telefone)
        self.__matricula = matricula
        self.__presencas = 0

    def marcarpresenca(self):
        self.__presencas +=1

    def matricular(self):
        pass 

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def imprimirDados(self):
            print("ID:", self.id)
            print("Nome:", self.nome)
            print("Telefone:", self._telefone)
            print("Matrícula:", self.__matricula)
            print("Presenças:", self.__presencas)

alunooo = AlunoGraduacao(1, "Gabriel Sabadin", "99999999", "8448", 0)
print (alunooo.getMatricula())
alunooo.imprimirDados()

