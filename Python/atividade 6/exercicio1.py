class empregado():
    def __init__(self, nome, salario,lucro_mensal, vendas):
        self.nome = nome
        self.salario = salario
        self.lucro_mensal = lucro_mensal
        self.vendas = vendas

    def calc():
        ...
class Gerente(empregado):
    def calc(self):
        return (f"{self.nome} recebe {self.salario + (self.lucro_mensal * 0.1)}")
class vendedor(empregado):
   def calc(self):
       return (f"{self.nome} recebe {self.salario + (self.vendas * 0.02)}")
    
G = Gerente("Fábio", 1412, 100000, 0)
V = vendedor("João", 1412, 100000, 5000)

print(G.calc())
print(V.calc())