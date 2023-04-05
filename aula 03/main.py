from cidade import Cidade
from pessoa import Pessoa
from produto import Produto
from pedido import Pedido
from categoria import Categoria


poa = Cidade(1, "Porto Alegre")
cb = Cidade (2,"Campo Bom")
p1 = Pessoa("Saba","993838045", poa)
p2 = Pessoa("Pietro","996286120", cb)
print("Nome da cidade do", p2.nome, ":",p2.cidade.nome)
p1.imprimir()
print("------------------------------------------------29/03/2023----------------------------------------------------")
cat1 = Categoria(1, "Drinks")
cat2 = Categoria(2, "Foods")
prod1 = Produto("Coca-Cola", 6, cat1)
prod2 = Produto("Negroni", 12, cat1)
prod3 = Produto("Hamburguer", 8, cat2)

ped01 = Pedido("Rua A, 100", p1)
ped01.imprimir()

print("Soma: ", ped01.addProduto(prod1))
print("Soma: ", ped01.addProduto(prod3))
print("------------")
ped01.imprimir()
