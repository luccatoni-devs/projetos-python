def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("retire seu dinheiro na boca do caixa")
    else:
        print("Valor inválido")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)