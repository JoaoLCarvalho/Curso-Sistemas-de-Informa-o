#nome do aluno.
nome = input("Nome do aluno: ")

#variavel para notas.
notas = []

#mecânismo para que a quantidade de notas não seja pré-definida.
while True:
    pergunta = input("Digíte as notas(ou 'ok' para parar): ")
    if pergunta.lower() == 'ok':
        break
    try:
        nota = float(pergunta)
        notas.append(nota)
    except ValueError:
        print("Digíte um número válido.")

#setor onde as notas recebidas serão somadas.
soma_0 = notas
soma_1 = sum(soma_0)

#setor onde serão divididas.
divisao_0 = len(notas)
d = divisao_0

#cálculo da média.
media = (soma_1 / d)

#setor que calcula e verifica se o aluno foi aprovado.
if media >= 7:
    print (f"Parabéns o aluno {nome} passou com a média {media}")
else:
    print(f"O aluno {nome} foi reprovado com a média {media}.")