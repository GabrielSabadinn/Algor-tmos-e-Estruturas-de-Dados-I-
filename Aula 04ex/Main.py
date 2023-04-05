class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Codigo :" + str(self.codigo))
        print("Nome :" + str(self.nome))
        print("Matricula :" + str(self.matricula))

class Aluno_ensino_medio:
    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        super().imprimir()
        print("Ano: " + str(self.ano))

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre
        
    def imprimir(self):
        super().imprimir()
        print("Semestre: " + str(self.semestre))



x = Aluno(1, "GABRIEL SABADIN", "0290712003333")
x.imprimir()
