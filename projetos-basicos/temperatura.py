
celsius = 0.0
kelvin = 0.0
farenheit = 0.0
unimed = ""
print("\033c", end="")

while celsius == 0.0:
    celsius = (input("Digite a temperatura em graus: "))
    try:
        celsius = float(celsius)
    except:
        print("Temperatura deve ser informada corretamente!")
        celsius = 0.0

while unimed == "":
    unimed = input("Digite K para Kelvin, ou F para Farenheit: ")
    if unimed != "K" and unimed != "F":
        print("Outra unidade de medida deve ser informada corretamente!")
        unimed = ""

if unimed == "K":
    kelvin = celsius + 273
    print("Temperatura em Celsius: ", celsius)
    print("Temperatura em Kelvin: ", kelvin)
elif unimed == "F":
    farenheit = ((celsius * 9) / 5 + 32)
    print("Temperatura em Celsius: ", celsius)
    print("Temperatura em Farenheit: ", farenheit)

print ("Fim do algoritmo!")
