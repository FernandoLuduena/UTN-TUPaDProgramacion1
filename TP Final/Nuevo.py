import csv, os
from Funciones import agregar_pais,actualizar_pais, buscar_pais,filtrar_pais,ordenar_paises,mostrar_estadisticas

ARCHIVO = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(CAMPOS)

opcion = None
while opcion != 0:
    print("\n1.Agregar un pais.")
    print("2.Actualizar los datos de poblacion y superficie de un pais.")
    print("3.Buscar paises.")
    print("4.Filtrar paises.")
    print("5.Ordenar paises.")
    print("6.Mostrar estadisticas.")
    print("0.Salir.")
    try:
        opcion = int(input("Ingrese una opcion (0 para salir): "))
    except ValueError:
        print("Opcion incorrecta, ingrese un numero.")
        continue
    if opcion == 1:
        agregar_pais()
    elif opcion == 2:
        actualizar_pais()
    elif opcion == 3:
        buscar_pais()
    elif opcion == 4:
        filtrar_pais()
    elif opcion == 5:
        ordenar_paises()
    elif opcion == 6:
        mostrar_estadisticas()
    elif opcion == 0:
        print("Saliendo...")
    else:
        print("Opcion incorrecta, ingrese una opcion nuevamente.")
