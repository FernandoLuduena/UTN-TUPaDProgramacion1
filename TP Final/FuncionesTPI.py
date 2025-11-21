import csv, os 

ARCHIVO = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(CAMPOS)


def mostrar_paises(paises=None):
    print("\n=== Lista de países ===")
    if paises is None:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            paises = list(lector)
    if not paises:
        print("No hay países registrados.")
        return
    for fila in paises:
        print(f"{fila['nombre']} - {fila['continente']} | {fila['poblacion']} hab | {fila['superficie']} km²")

def agregar_pais():
    
    print("-----AGREGAR UN PAIS-----")
    nombre = input("Nombre del pais: ").strip()
    poblacion = input("Cantidad de habitantes: ").strip()
    superficie = input("Superficie del pais: ").strip()
    continente = input("Continente: ").strip()
    
    if not nombre or not poblacion or not superficie or not continente:
        print("Error: Todos los campos son obligatorios.")
        return
    
    if not poblacion.isdigit() or not superficie.isdigit():
        print("Error: Poblacion y superficie deben ser numeros enteros.")
        return
    
    with open(ARCHIVO, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([nombre, poblacion, superficie, continente])
        
    print(f"Pais {nombre} agregado exitosamente.")

def actualizar_pais():
    print("-----Actualizar País-----")
    nombre_buscar = input("Ingrese el país que desea actualizar: ").strip()
    if not nombre_buscar:
        print("Error: El nombre del país es obligatorio.")
        return
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)
    encontrado = False
    for pais in paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            encontrado = True
            print(f"País encontrado: {pais['nombre']}")
            nueva_poblacion = input("Ingrese la nueva población: ").strip()
            nueva_superficie = input("Ingrese la nueva superficie: ").strip()
            if not nueva_poblacion.isdigit() or not nueva_superficie.isdigit():
                print("Error: Población y superficie deben ser números enteros.")
                return
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            print("Datos actualizados correctamente.")
            break
    if not encontrado:
        print("No se encontró el país especificado.")
        return
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(paises)

def buscar_pais():
    print("-----Buscar Pais-----")
    termino = input("Ingrese una parte o todo el nombre del pais: ").strip().lower()
    if not termino:
        print("Error: debe ingresar un texto para buscar.")
        return
    encontrados = []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if termino in fila["nombre"].lower():
                encontrados.append(fila)
    if encontrados:
        print(f"Se encontraron {len(encontrados)} resultado(s):\n")
        for pais in encontrados:
            print(f"{pais['nombre']} - {pais['continente']} | {pais['poblacion']} hab | {pais['superficie']} km²")
    else:
        print("No se encontraron paises que coincidan con la busqueda.")

def filtrar_pais():
    print("-----Filtrar Pais-----")
    print("1.Por continente")
    print("2.Por rango de poblacion.")
    print("3.Por rango de superficie.")
    opcion = input("Elija una opcion: ").strip()
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)
    filtrados = []
    if opcion == "1":
        cont = input("Ingrese el nombre del continente: ").strip().lower()
        filtrados = [p for p in paises if p["continente"].lower() == cont]
    elif opcion == "2":
        min_pob = input("Poblacion minima: ").strip()
        max_pob = input("Poblacion maxima: ").strip()
        if not (min_pob.isdigit() and max_pob.isdigit()):
            print("Error: los valores deben ser numeros.")
            return
        min_pob, max_pob = int(min_pob), int(max_pob)
        filtrados = [p for p in paises if min_pob <= int(p["poblacion"]) <= max_pob]
    elif opcion == "3":
        min_sup = input("Superficie minima(KM): ").strip()
        max_sup = input("Superficie maxima(KM): ").strip()
        if not (min_sup.isdigit() and max_sup.isdigit()):
            print("Error: los valores deben ser numeros.")
            return
        min_sup, max_sup = int(min_sup), int(max_sup)
        filtrados = [p for p in paises if min_sup <= int(p["superficie"]) <= max_sup]
    else:
        print("Opcion invalida.")
        return
    if filtrados:
        print(f"Se encontraron {len(filtrados)} resultado(s):\n")
        for pais in filtrados:
            print(f"{pais['nombre']} - {pais['continente']} | {pais['poblacion']} hab | {pais['superficie']} km²")
    else:
        print("No se encontraron paises con esos criterios.")

def ordenar_paises():
    print("-----Ordenar Paises-----")
    print("1.Por nombre.")
    print("2.Por poblacion.")
    print("3.Por superficie.")
    criterio = input("Elija una opcion: ").strip()
    orden = input("¿Orden Ascendente(A) o Descendente(D)? ").strip().upper()
    descendente = orden == "D"
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)
    if not paises:
        print("No hay paises registrados.")
        return
    if criterio == "1":
        paises.sort(key=lambda p: p["nombre"].lower(), reverse=descendente)
    elif criterio == "2":
        paises.sort(key=lambda p: int(p["poblacion"]), reverse=descendente)
    elif criterio == "3":
        paises.sort(key=lambda p: int(p["superficie"]), reverse=descendente)
    else:
        print("Opción inválida.")
        return
    print("\nPaíses ordenados:\n")
    mostrar_paises(paises)

def mostrar_estadisticas():
    print("-----Estadisticas de Paises-----")
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)
    if not paises:
        print("No hay datos cargados.")
        return
    for p in paises:
        p["poblacion"] = int(p["poblacion"])
        p["superficie"] = int(p["superficie"])
    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)
    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1
    print(f"\n País con mayor población: {mayor['nombre']} ({mayor['poblacion']} hab)")
    print(f" País con menor población: {menor['nombre']} ({menor['poblacion']} hab)")
    print(f"\n Promedio de población: {prom_pob:.2f}")
    print(f" Promedio de superficie: {prom_sup:.2f} km²")
    print("\n Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  - {cont}: {cant}")