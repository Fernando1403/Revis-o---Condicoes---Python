# Relembrando
"""Lista = ['a','b','c','d','e']

for k in Lista:
    if k == 'c':
        break
    print(k)"""

#1
# ax + b = 0   qual o valor de x

"""a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))

x = (-b / a)

print(f"O valor de x é : {x}")"""

"""
Base para os proximos exercicios
Voltage (V)
Potencia (P)
Resistencia (R)
Corrente (I)

V = I * R
I = V / R
P = V * I
P = R * I²
P = V² / R
"""

#2
# Crie um algoritimo que solicite potencia e voltagem e retorne corrente
# I = V / R

"""potencia = float(input("Insira a potencia: "))
voltagem = float(input("Insira a voltagem: "))

corrente = potencia / voltagem

print(f"O valor da corrente é: {corrente}")"""

#3
#Crie um alotirtimo que solicite resistencia e corrente e retorne voltage

"""resistencia = float(input("Insira a potencia: "))
corrente = float(input("Insira a voltagem: "))

voltagem = resistencia * corrente

print(f"A voltage é: {voltagem}")"""


#4
#Crie um algoritimo que solicite resistencia e corrente e retorne potencia

"""resistencia = float(input("Insira a potencia: "))
corrente = float(input("Insira a voltagem: "))

potencia = resistencia * (corrente ** 2)

print(f"A potencia é: {potencia}")"""

# Estruturas de condição

#5
# Crie um algoritimo para solicitar o clima para o usuario e retorna o que poderia ser
# feito em relação ao clima
# Ensolorado - dia de futebol e churrasco
# Chuvoso - Dia de netflix
# Nevando - Dia de tomar um chá ou chocolate quente
# Nublado - Dia de ler um livro

"""clima = input("Como está o clima: ")

while (clima != "Ensolarado" and clima != "Chuvoso" and clima != "Nevando" and clima != "Nublado"):
    print("Clima invalido! Tente : Ensolarado; Chuvoso; Nevando; Nublado;")
    clima = input("Como está o clima: ")

if(clima == "Ensolarado"):
    print("Dia de futebol e churrasco")
elif(clima == "Chuvoso"):
    print("Dia de Netflix")
elif(clima == "Nevando"):
    print("Dia de tomar um chá ou chocolate quente")
elif(clima == "Nublado"):
    print("Dia de ler um livro")"""

#6
# Crie um altoritimo para solicitar a forma geometrica e retorne o calculo da area
# e volume.
# Cilindro - area_cilindro pi * raio**2, volume_cilindro pi * raio**2 * altura
# Cubo - area_cubo base * altura, volume_cubo base * altura * comprimento

forma = input("Qual forma geometrica deseja: ")

while(forma != "Cilindro" and forma != "Cubo"):
    print("Forma invalida tente Cubo ou Cilindro")
    forma = input("Qual forma geometrica deseja: ")


if(forma == "Cilindro"):
    print("A formula é area_cilindro pi * raio**2, volume_cilindro pi * raio**2 * altura")
    raio = float(input("Qual é o raio: "))
    altura = float(input("Qual é a altura: "))
    areaCilindro = 3.14 * (raio**2)
    volumeCilindro = 3.14 * (raio**2) * altura
    print(f"A area é {areaCilindro} e o volume é {volumeCilindro}")
else:
    print("A forma é area_cubo base * altura, volume_cubo base * altura * comprimento")
    base = float(input("Qual é a base: "))
    altura = float(input("Qual é a altura: "))
    comprimento = float(input("Qual é o comprimento: "))
    areaCubo = base * altura
    volumeCubo = base * altura * comprimento
    print(f"A area é {areaCubo} e o volume é {volumeCubo}")
