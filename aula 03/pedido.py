class Pedido:
    def __init__(self,endereco,cliente):
     self.id = None
     self.end = endereco
     self.produtos = []
     self.cliente =  cliente

    def addProduto(self, produto):
        self.produtos.append(produto)
        soma = 0
        for prod in self.produtos:
            soma += prod.preco
        return soma


    def imprimir(self):
        print("Pedido:")
        print("Endereço:", self.end)
        print("Cliente:", self.cliente.nome)
        print("Cidade: ", self.cliente.cidade.nome)
        print("Produtos do Pedido:")
        if len(self.produtos) == 0:
            print("Pedido vazio")
        else:
            soma = 0
            for prod in self.produtos:
                soma += prod.preco
                print("Produto: ", prod.nome)
                print("Preço: ", prod.preco)
                print("Categoria: ", prod.cat.nome)
            print("total: ", soma)
            print("-----------------------------------------------")