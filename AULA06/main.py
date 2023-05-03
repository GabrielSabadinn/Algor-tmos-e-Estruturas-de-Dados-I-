from Cidade import Cidade
from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(2, "Capão da Canoa")

joao = Fisica("João", "2233-4455", c1 , "000.111.222-33")
maria = Fisica("Maria", "3344-5566", c2 , "111.222.333-44")
jose = Fisica("Jose", "3344-5566", c2 , "222.333.444-55")

dosul = Juridica("Supermercado Dosul", "234-4321", c1, "01.234.567/0001-00")

dosul.imprimir()
dosul.addFuncionario(joao)
dosul.addFuncionario(maria)
print(" ------------\n\n")
dosul.imprimir()
