
#Ejercicio 1 

with open("productos.txt", "w") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    archivo.write("Arroz,1200,15\n")
    archivo.write("Fideos,950,20\n")
    archivo.write("Aceite,2500,10\n")   

print("Archivo 'productos.txt' creado correctamente.\n")
#Ejercicio 2

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre,precio,cantidad = linea.split(",")
        print (f"Producto: {nombre} - Precio: {precio} - Cantidad: {cantidad}")

#Ejercicio 3

nombre_nuevo = input("Ingrese el nombre del nuevo producto: ")
precio_nuevo = input("Ingrese el precio del nuevo producto: ")
cantidad_nuevo = input("Ingrese la cantidad del nuevo producto: ")

with open ("productos.txt","a") as archivo:
    archivo.write(f"{nombre_nuevo},{precio_nuevo},{cantidad_nuevo}\n")

print("Nuevo producto agregado correctamente.")

#Ejercicio 4

productos = []

with open ("productos.txt","r") as archivo:
    next(archivo)
    for linea in archivo:
        linea = linea.strip()
        nombre,precio,cantidad = linea.split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print("\n=== lista de productos cargada en formato diccionario ===")

for p in productos:
    print(p)
    
#Ejercicio 5

nombre_buscar = input("\nIngrese el nombre del producto a buscar: ")
encontrado = False

for p in productos:
    if p["nombre"].capitalize() == nombre_buscar:
        print(f"Producto encontrado: ")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(f"\n El producto '{nombre_buscar}' no existe en la lista.")
    
#Ejercicio 6

with open("productos.txt", "w") as archivo:
    
    archivo.write("nombre,precio,cantidad\n")
    
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\n Archivo 'productos.txt' actualizado correctamente.")