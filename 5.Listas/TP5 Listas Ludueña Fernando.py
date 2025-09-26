#Ejercicio 1 

notas_estudiantes = []
suma_promedio = 0

for i in range(0,10,1):
    nota = int(input("Ingrese la nota del estudiante : "))
    notas_estudiantes.append(nota)

for i in range(0,10,1):
    print(f"Nota en posicion[{i}]: {notas_estudiantes[i]}")

    suma_promedio += notas_estudiantes[i]

print(f"El promedio de las notas ingresadas es {suma_promedio/10}")

print(f"La maxima nota ingresada: {max(notas_estudiantes)}")
print(f"La minima nota ingresada: {min(notas_estudiantes)}")

#Ejercicio 2

productos = []

for i in range(1,5,1):
    producto = input("Ingrese el producto que desea cargar: ")
    productos.append(producto)

productos.sort()

print(productos)

eliminar = input("Ingrese el nombre del producto que desea eliminar: ")

productos.remove(eliminar)

print(productos)

#Ejercicio 3

import random
lista_numaleatorios = []
pares = []
impares = []

for i in range(1,15):
    num = random.randint(1,100)
    lista_numaleatorios.append(num)

for i in range(0,15):
    num = lista_numaleatorios[i]
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

for elemento in lista_numaleatorios:
    print(elemento)

for elemento in pares:
    print(f"Par: {elemento} ")

for elemento in impares:
    print(f"Impar: {elemento}")

#Ejercicio 4

datos =[1,3,5,3,7,1,9,5,3]

datos_norepetidos = list(set(datos))

print(f"Lista sin elementos repetidos: {datos_norepetidos}")

#Ejercicio 5

nombres_estudiantes = ["Fernando","German","Maria","Cecilia","Candela","Agustin","Gonzalo","Sandra"]

print(f"Estudiantes en el curso : {nombres_estudiantes}")
opcion = int(input("1)Agregar estudiante 2)Eliminar estudiante. Ingrese una opcion: "))

if opcion == 1:
    nombre = input("Ingrese el nombre que desea agregar: ")
    nombres_estudiantes.append(nombre)
    print(f"Estudiantes en el curso actuales : {nombres_estudiantes}")
elif opcion == 2:
    nombre = input("Ingrese el nombre que desea eliminar: ")
    nombres_estudiantes.remove(nombre)
    print(f"Estudiantes en el curso actuales : {nombres_estudiantes}")
else:
    print("Ingresó una opcion incorrecta! Vuelva a intentarlo.")

#Ejercicio 6

numeros = [43,12,1,3,98,54,67]
lista_nueva = [numeros[-1]] + numeros[:-1]

print(lista_nueva)

#Ejercicio 7

matriz_temperaturas = [
    [19,28],
    [19,29],
    [18,30],
    [20,31],
    [16,27],
    [18,27],
    [18,24]
]

for i in range(len(matriz_temperaturas)):
    print(matriz_temperaturas[i])

maximas = [fila[0] for fila in matriz_temperaturas]
minimas = [fila[1] for fila in matriz_temperaturas]

promedio_min = sum(minimas)/len(minimas)
promedio_max = sum(maximas)/len(maximas)

print(f"Promedio de minimas: {promedio_min:/.2f}")
print(f"Promedio de maximas  : {promedio_max:/.2f}")

amplitudes = [maxi - mini for mini,maxi in matriz_temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor = amplitudes.index(mayor_amplitud) + 1

print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C en el día {dia_mayor}")

#Ejercicio 8

notas = [
    [7, 8, 6],   
    [5, 6, 7],   
    [9, 8, 10],  
    [6, 7, 6],   
    [8, 9, 7]    
]

print("Promedio de cada estudiante:")
for i, fila in enumerate(notas, start=1):
    promedio_est = sum(fila) / len(fila)
    print(f"Estudiante {i}: {promedio_est:.2f}")
    
print("\nPromedio de cada materia:")
num_estudiantes = len(notas)
num_materias = len(notas[0])

for j in range(num_materias):
    suma_materia = sum(notas[i][j] for i in range(num_estudiantes))
    promedio_materia = suma_materia / num_estudiantes
    print(f"Materia {j+1}: {promedio_materia:.2f}")

#Ejercicio 9

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

for i in range(3):
    for j in range(3):
        print(tablero[i][j], end=" ")
    print()

print()

jugadores = ["X", "O"]

for turno in range(4):
    jugador = jugadores[turno % 2]
    print("Turno del jugador", jugador)

    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, perdés el turno 😅")

    # Mostrar tablero después de la jugada
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()
    print()


#Ejercicio 10

ventas = [
    [5, 3, 4, 6, 7, 2, 4],
    [2, 1, 3, 4, 5, 3, 2],
    [6, 7, 8, 5, 6, 7, 9],
    [3, 4, 2, 3, 4, 5, 3] 
]


print("Total vendido por cada producto:")
for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    print("Producto", i+1, ":", total_producto)

print()


mayor_ventas = -1
dia_mayor = -1

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    print("Total del día", j+1, ":", total_dia)

    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j+1

print("\nEl día con mayores ventas fue el día", dia_mayor, "con", mayor_ventas, "ventas")

print()

mas_vendido = -1
producto_mayor = -1

for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    if total_producto > mas_vendido:
        mas_vendido = total_producto
        producto_mayor = i+1

print("El producto más vendido fue el Producto", producto_mayor, "con", mas_vendido, "ventas en la semana")