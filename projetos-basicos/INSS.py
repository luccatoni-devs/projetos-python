descinss = 0.0
salarioliq = 0.0
salario = 0.0
nome = ""
print("\033c", end="")

while nome == "":
    nome = str(input("Digite o nome do funcionário: "))
    if nome == "":
        print("O nome deve ser informado")

while salario == 0.0:
    salario = (input("Digite o salário: "))
    try: 
        salario = float(salario)
    except:
        print("O salário deve ser informado corretamente!")
        salario = 0.0

if salario <= 1693.72:
    descinss = salario * 0.08
    salarioliq = salario - descinss
    print("Olá ",nome,"você vai ser descontado de INSS R$",descinss, "e o salário líquido será de R$",salarioliq)
elif salario <= 2822.90:
    descinss = salario * 0.09
    salarioliq = salario - descinss
    print("Olá ",nome,"você vai ser descontado de INSS R$",descinss, "e o salário líquido será de R$",salarioliq)
elif salario <= 5645.90:
    descinss = salario * 0.11
    salarioliq = salario - descinss
    print("Olá ",nome,"você vai ser descontado de INSS R$",descinss, "e o salário líquido será de R$",salarioliq)
else:
    descinss = salario * 0.15
    salarioliq = salario - descinss
    print("Olá ",nome,"você vai ser descontado de INSS R$",descinss, "e o salário líquido será de R$",salarioliq)