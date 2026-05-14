import random

numero_secreto = random.randint(1, 10)
palpite = 0
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1 a 10): "))

    tentativas += 1

    if palpite != numero_secreto:
        print("Errou! Tente novamente.")

# verifica singular/plural
if tentativas == 1:
    palavra = "vez"
else:
    palavra = "vezes"

print(f"Acertou! Parabéns! Você tentou {tentativas} {palavra}.")
