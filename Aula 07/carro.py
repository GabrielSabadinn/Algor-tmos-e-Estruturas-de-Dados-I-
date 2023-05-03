from veiculo import veiculo


class carro(veiculo):
    def __init__(self, modelo=None, ano=None, qtdportas = 4):
        super().__init__(modelo, ano)
        self.qntportas = qtdportas


    def imprimir(self):
        return super().imprimir()

    def imprimirEspecifico(self):
        super().imprimir()
        print("Portas " +str(self.qntdportas))