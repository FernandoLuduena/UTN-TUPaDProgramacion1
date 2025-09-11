#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101, 1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un numero para saber cuantos digitos tiene: "))
contDigitos = 0

while numero > 0:
    numero //= 10
    contDigitos += 1

print(f"La cantidad de digitos que posee el numero es de {contDigitos}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0    

for i in range(valor1+1, valor2, 1):
    suma +=i

print(f"La suma del rango ingresado es {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
num = 1
while num != 0:
    num = int(input("Ingrese numeros enteros(corta con 0): "))
    suma += num

print(f"La suma de los numeros ingresados en secuencia es {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import randint

numeroRandom = randint(0,9)
intentos = 0 

numUsuario = 11

while numUsuario != numeroRandom:
    numUsuario = int(input("Ingrese un numero para adivinarlo: "))
    intentos += 1

print(f"El numero era el {numeroRandom}, la cantidad de intentos realizados es {intentos}")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100,0,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero positivo: "))
suma = 0

for i in range(0, num, 1):
    suma += i

print(f"Las suma de todos los numeros del rango es {suma}")

#Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0


for i in range(0,100):
    num = int(input("Ingrese un numero: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        print("El cero no se contabilizara porque es un numero neutro")

print(f"La cantidad de pares ingresados es de {pares}")
print(f"La cantidad de impares ingresados es de {impares}")
print(f"La cantidad de positivos ingresados es de {positivos}")
print(f"La cantidad de negativos ingresados es de {negativos}")

#Ejercicio 9

from statistics import mean
acumuladorMedia = 0

for i in range(0, 100):
    num = int(input("Ingrese los numeros para saber la media(puede ingresar hasta 100): "))
    acumuladorMedia += num

print(f"La media de los numeros ingresados es {mean(acumuladorMedia)}")

#Ejercicio 10

num = input("Ingrese un numero para darlo vuelta: ")
numInvertido = ""

for digito in num[::-1]:
    numInvertido += digito

print(f"Numero invertido: {numInvertido} ")