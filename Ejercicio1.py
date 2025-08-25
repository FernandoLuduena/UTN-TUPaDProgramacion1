from math import pi

#Ejercicio 1

print("Hola Mundo")

#Ejercicio 2

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}")

#Ejercicio 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar =input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

#Ejercicio 4

radio = float(input("Ingrese el radio de un circulo: "))

perimetro = 2 * pi * radio
area = pi * pow(radio, 2)

print(f"El perimetro de su circulo es {round(perimetro,2)} y el area {round(area,2)}")

#Ejercicio 5

segundos = int(input("Ingrese la cantidad de segundos a convertir en horas: "))

horas = segundos / 3600

print(f"La cantidad de segundos en hs es {horas} hs.")

#Ejercicio 6

numero = int(input("Ingrese un numero para saber su tabla de multiplicar: "))

for item in range(1,11,1):
    n = numero * item
    print(n)
    
#Ejercicio 7

num1 = int(input("Ingrese el primer numero(distinto de 0): "))
num2 = int(input("Ingrese el segundo numero(distinto de 0): "))

print(f"Suma: {num1+num2} \n Resta: {num1 - num2} \n Multiplicacion: {num1 * num2} \n Division: {num1 / num2}")

#Ejercicio 8

peso = int(input("Ingrese su peso(KG): "))
altura = float(input("Ingrese su altura(Mts): "))

imc = peso / pow(altura, 2)

print(f"Su imc es {imc}")

#Ejercicio 9

celsius = float(input("Ingrese la temperatura en celsius: "))

fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en Fahrenheit es {fahrenheit} ")

#Ejercicio 10

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los numeros ingresados es {promedio}")