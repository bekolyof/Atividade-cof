nota1 = float(input("Digite a nota do 1 primeiro semestre: "))
nota2 = float(input("Digite a nota do 2 segundo semestr: "))
nota3= float(input("Digite a nota do 3 triceiro semestre: "))

media = (nota1 + nota2 + nota3/3)
print(f"Media final:{media :.2f}")


if media>= 7:
    print("situação: Aprovado")
if media>= 6:
    print("situação: recuperação")
if media>= 5: 
    print("setução: reprovado")

