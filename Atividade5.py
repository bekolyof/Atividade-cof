pordutos = ["camiseta", "calça", "par meais", "boné", "toca", ]
precos = [40.00, 80.00, 16.00, 30.00, 17.00]
quantidades = [2, 1, 2, 1, 1]
subtotal = []


# Antes, Faria assim para pegar o produto e preço:

print:(f"O produto {produto[0]} custa R${precos[0]}.")

for indice, produto in enumerate(produtos):
    preco = precos[indice] # preco = precos[0]
    quantidade = quantidades[indice]
    subtotal = quantidade * preco
    subtotal.append(subtotal)
    
    mensagem = f"""
    ----------------------------------------------
    produto: {produto}
    Quantidade: {quantidade}
    Valor unitário: {preco}
    subtotal: {subtotal}
    print(f"O produto {produto} custa R${preco}.")

    print(mensagem)
