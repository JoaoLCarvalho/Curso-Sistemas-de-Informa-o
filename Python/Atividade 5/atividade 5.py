class aluno:
    def __init__(self, nome, nota1, nota2):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def get_nota1(self):
        return self.__nota1 

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def get_nota2(self):
        return self.__nota2 

def criar_aluno():
    nome = input("Digíte o nome do aluno: ")
    nota1 = float(input("Digíte a primeira nota: "))
    nota2 = float(input("Digíte a segunda nota: "))
    return aluno(nome, nota1, nota2)

aluno = criar_aluno()
print(f"Nome: {aluno.get_nome()}")
print(f"Nota 1: {aluno.get_nota1()}") 
print(f"Nota 2: {aluno.get_nota2()}")