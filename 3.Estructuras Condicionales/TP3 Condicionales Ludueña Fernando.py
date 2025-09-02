#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad.")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero para saber si es par o impar: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es un niño/a.")
elif edad >= 12 and edad < 18:
    print("Es un adolescente.")
elif edad >= 18 and edad < 30:
    print("Es un un/a adulto/a joven.")
elif edad >= 30:
    print("Es un/a adulto/a.")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string

contrasena = input("Ingrese su contraseña: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100 ) for i in range(50)]

if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Hay sesgo positivo.")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) <  mode(numeros_aleatorios):
    print("Hay sesgo negativo.")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) and mean(numeros_aleatorios) == mode(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("No hay sesgo.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla

palabra = input("Ingrese una palabra: ")

if palabra(-1) == ['a','e','i','o','u']:
    print(f"{palabra}!")
else:
    print(palabra)

#8

nombre = input("Ingrese su nombre: ")
opcion = input("Opciones: 1)Mayusculas 2)Minusculas 3)Primera Mayuscula: ")

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else: 
    print("Ingrese una opcion correcta.")


#9 Magnitud de terremoto.

magnitud = input(float("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte.")
elif magnitud >= 6 and magnitud < 7: 
    print("Muy fuerte.")
elif magnitud >= 7:
    print("Extremo.")

#10

hemisferio = input("Ingrese en que hemisferio se encuentra N/S: ")
dia = int(input("Ingrese en que dia del mes se encuentra (1-31): "))
mes = int(input("Ingrese el mes en el que se encuentra (1-12) : "))

if hemisferio.lower() == "n":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print ("Se encuentra en Invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print ("Se encuentra en Verano")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en Otoño")
elif hemisferio.lower() == "s":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en Primavera")
else:
    print("Hemisferio no válido")