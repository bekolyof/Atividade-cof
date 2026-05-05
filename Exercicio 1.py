nota1 = float(input("Digite a nota do 1º semestre: "))
nota2 = float(input("Digite a nota do 2º semestre: "))
nota3 = float(input("Digite a nota do 3º semestre: "))

media = (nota1 + nota2 + nota3) / 3
print(f"Média final: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 6:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")