#Ejercicio 1 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3

solo_frutas = precios_frutas.keys()

print(solo_frutas)

#Ejercicio 4

contactos = {}

for i in range (1,6,1):
    
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero: ")
    contactos [nombre] = numero

nombre = input("Ingrese el nombre del que desea saber el numero: ")
print(f"El numero es {contactos[nombre]}")

#Ejercicio 5 

frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

print(f"Palabras unicas {palabras_unicas}")

print("Recuento")

for palabra in palabras_unicas:
    print(f"{palabra} : {palabras.count(palabra)}")

#Ejercicio 6

alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = int(input("Ingrese la primer nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercer nota: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)


for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
    
#Ejercicio 7

parcial1 = {"Ana", "Luis", "Sofía", "Pedro"}
parcial2 = {"Sofía", "Pedro", "María", "Lucía"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print(f"Aprobaron ambos parciales : {ambos}")
print(f"Aprobaron solo uno : {solo_uno}")
print(f"Aprobaron al menos un parcial : {al_menos_uno}")

#Ejercicio 8

productos = {'Fideos': 10, 'Arroz':20, 'Pure':25, 'Aceite': 13, 'Harina': 5}

opcion = 4

while opcion != 0:
        
    print("1.Consultas stock de un producto ingresado \n 2.Agregar unidades a stock existente \n 3.Agregar nuevo producto")
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
    
        producto = input("Ingrese el producto del que desea saber el stock: ")
        
        if producto in productos:
            print(f"La cantidad es {productos[producto]} unidades")
        else:
            print("El producto ingresado no existe.")
    
    elif opcion == 2:
        
        producto = input("Ingrese el producto que desea modificar el stock: ")
        
        if producto in productos:
            print("El producto se encontraba en la lista.")
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            
            productos[producto] = productos[producto] + cantidad
            
            print("Stock actualizado.")
            print(f"El stock ahora es de {productos[producto]} unidades.")
            
        else:
            print("El producto ingresado no existe.")
    
    elif opcion == 3: 
        
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad del nuevo producto: "))
        
        productos[producto] = cantidad

#Ejercicio 9

agenda = {
    ("Lunes","10:30"): "Reunion",
    ("Martes","18:00"): "Entrevista",
    ("Viernes","12:00"): "Almuerzo laboral",
    ("Sabado","21:30"): "Fiesta de la empresa"
}

dia = input("Ingrese el dia:")
hora = input("Ingrese la hora con formato hh:mm: ")

if (dia,hora) in agenda:
    print(f"El evento que usted tiene el dia {dia} a las {hora} es: {agenda[dia,hora]}")
else:
    print("No tiene ningun evento o ingreso mal un dato, intente nuevamente.")

#Ejercicio 10

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago de Chile",
    "Bolivia": "La Paz",
    "Brasil": "Brasilia",
    "Venezuela": "Caracas",
    "Colombia": "Bogotá",
}

invertido = {capital : pais for pais, capital in original.items()}

print(invertido)