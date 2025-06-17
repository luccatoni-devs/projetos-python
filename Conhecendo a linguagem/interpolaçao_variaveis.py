nome = "Lucca"
idade = 18
profissao = "Desenvolvidor"
linguaguem = "Python"
saldo = 1000.399

dados = {"nome": "Lucca", "idade": 18}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome = nome, idade = idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")