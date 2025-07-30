texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # Adiciona uma quebra de linha

# Utilizando else no for
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()

# Exemplo utilizando a função built-in range
print(list(range(4)))

# Tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")