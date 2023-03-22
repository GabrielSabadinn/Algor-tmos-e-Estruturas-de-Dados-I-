nome_produtos = ["Coca-cola", "Pepsi","Guarana",]
price = [5,6,3]
quantidade = [2,1,3]

def imprimir_lista(Nome,preco,quantidade):
    imprimir = f'Nome do produto; {nome_produtos}, preço do produto: {preco}, quantidade:{quantidade}'
    print(imprimir)

imprimir_lista(nome_produtos[1],price[1],quantidade[1])

imprimir_lista(nome_produtos.pop(1),price.pop(1),quantidade.pop(1))
print(nome_produtos)





