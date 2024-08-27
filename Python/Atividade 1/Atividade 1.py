nome = input("Qual o nome do aluno?: ")
nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terceira nota:"))
nota4 = float(input("Quarta nota:"))
media = (nota1 + nota2 + nota3 + nota4)
nota_final = (media/4)
if nota_final >= 7:
    print(f"Parabéns o aluno {nome} foi aprovado.")

else:print(f"O aluno {nome} foi reprovado.")