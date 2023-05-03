class Veiculo():
    def __init__(self, marca, qntrodas, modelo) -> None:
        self.marca = marca 
        self.qntrodas = qntrodas
        self.modelo = modelo 
        self.velocidade = 0

    def imprimir(self):
        print(f" Marca: {self.marca}")
        print(f" Quantidade de rodas: {self.qntrodas}")
        print(f" Modelo: {self.modelo}")
        print(f" Velocidade: {self.velocidade}")

class Bicicleta(Veiculo):
    def __init__(self, marca, qntrodas, modelo, nummarchas, bagageiro):
        super().__init__(marca, qntrodas, modelo)
        self.nummarchas = nummarchas
        self.bagageiro = False
        
    def imprimir(self):
        super().imprimir()
        print(f"Numero de marchas:{self.nummarchas}")
    
class Automovel(Veiculo):
    def __init__(self, marca, qntrodas, modelo, potencia_motor):
        super().__init__(marca, qntrodas, modelo)
        self.potenciamotor = potencia_motor

    def imprimir(self):
        super().imprimir()
        print(f"Potencia do motor:{self.potencia_motor}")

class Moto(Automovel):
    def __init__(self, marca, qntrodas, modelo, potencia_motor, partida_eletrica):
        super().__init__(marca, qntrodas, modelo, potencia_motor)
        self.partida_eletrica = partida_eletrica

    def imprimir(self):
        super().imprimir()
        print(f"Partida Eletrica:{self.partida_eletrica}")

class Carro(Automovel):
    def __init__(self, marca, qntrodas, modelo, potencia_motor,qntdportas):
        super().__init__(marca, qntrodas, modelo, potencia_motor)
        self.qntdportas = qntdportas
    
    def imprimir(self):
        super().imprimir()
        print(f"Quantidade de porta:{self.qntdportas}")