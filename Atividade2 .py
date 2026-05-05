valor = float (input("Digite o valor do pedido: "))
""""
* Regra de negocio:
*se a venda for até 100 reais, de 5% de desconto 
*se o valor ser entre 100,1 e 299.99 reais, de 10% de desconto
* se o valor for acima de 300 reais,  de 15 de desconto
"""
if valor <=100:
    desconto = 0.95


elif valor > 100 and valor <= 299.99:
    desconto = 0.90 

else:
    desconto = 0.85
total = valor * desconto 
descontopercentual = (1 - desconto) * 100
descontopercentual = round(descontopercentual,0)

print("valor total foi de:", total, "seu desconto foi de:",)

print(f"sua compra deu r${valor}. voce ganhou {descontopercentual}%" f" de desconto. O tatal agora é R${total}")

