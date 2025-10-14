#Ejercicio 1

def holaMundo():
    print("Hola mundo")

holaMundo()

#Ejercicio 2 

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario("Fernando")

#Ejercicio 3 

def info_personal(nombre, apellido, edad, residencia ):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

info_personal("Juan", "Lopez", 22, "Cordoba")

#Ejercicio 4 

from math import pi

def calcular_area_circulo(radio):
    area = pi * pow(radio,2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

radio = int(input("Ingrese el radio del circulo para saber su area y perimetro: "))

print(f"El area es {calcular_area_circulo(radio)} y su perimetro es {calcular_perimetro_circulo(radio)}")

#Ejercicio 5 

def segundos_a_horas(segundos):
    
    conversion = segundos / 3600
    return conversion

segundos = int(input("Ingrese la cantidad de segundos que desea convertir en horas: "))

print(f"La cantidad de segundos en hs es: {segundos_a_horas(segundos)} hs")

#Ejercicio 6

def tabla_multiplicar(numero):
    
    for i in range(1,11,1):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese el numero del que desea saber la tabla de multiplicar: "))

tabla_multiplicar(numero)

#Ejercicio 7

def operaciones_basicas(a,b):
    
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if a > b:
        division = a / b
    else:
        division = 0
    
    return (suma, resta, multiplicacion, division)

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

print(operaciones_basicas(a,b))

#Ejercicio 8

def calcular_imc(peso, altura):
    
    imc = peso / pow(altura,2)
    return imc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en mts: "))

print(f"Su imc es {round(calcular_imc(peso,altura), 2)}")

#Ejercicio 9

def celsius_a_fahrenheit(celsius):
    
    fahrenheit = (9/5 * celsius + 32)
    
    return fahrenheit


celsius = float(input("Ingrese los grados celsius que desea transformar a fahrenheit: "))

print(f"Los grados celsius ingresados en Fahrenheit son: {celsius_a_fahrenheit(celsius)} F")


#Ejercicio 10 

def calcular_promedio(a,b,c):
    
    promedio = (a + b + c) / 3

nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

print(f"El promedio de los numeros ingresados es {calcular_promedio(nota1,nota2,nota3)}")

