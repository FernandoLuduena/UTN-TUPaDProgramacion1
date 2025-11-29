import csv, os

# ============================================================
#  CONFIGURACIÓN INICIAL DEL ARCHIVO CSV
# ============================================================
# Nombre del archivo donde se guardarán todos los países.
ARCHIVO = "paises.csv"

# Campos (columnas) que tendrá el archivo CSV.
# Se usarán en varias funciones, especialmente al leer y escribir.
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

# Si el archivo no existe, lo creamos vacío con solo el encabezado.
# Esto evita errores al querer abrirlo por primera vez.
if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(CAMPOS)


# ============================================================
#  MOSTRAR TODOS LOS PAÍSES
# ============================================================
def mostrar_paises(paises=None):
    """
    Muestra todos los países almacenados en el CSV.
    Si se recibe una lista de países (parámetro 'paises'), se muestra esa lista.
    Caso contrario, se vuelven a leer del archivo.
    """
    print("\n=== Lista de países ===")

    # Si no se pasaron países, leemos el archivo CSV.
    if paises is None:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            paises = list(lector)

    if not paises:
        print("No hay países registrados.")
        return

    # Mostramos país por país de forma ordenada.
    for fila in paises:
        print(f"{fila['nombre']} - {fila['continente']} | "f"{fila['poblacion']} hab | {fila['superficie']} km²")


# ============================================================
#  AGREGAR PAÍS
# ============================================================
def agregar_pais():
    """
    Agrega un nuevo país al archivo CSV.
    Se valida que todos los campos se completen y que tengan formato válido.
    """

    print("-----AGREGAR UN PAIS-----")

    # Se piden los datos uno por uno.
    nombre = input("Nombre del pais: ").strip()
    poblacion = input("Cantidad de habitantes: ").strip()
    superficie = input("Superficie del pais: ").strip()
    continente = input("Continente: ").strip()

    # Validación: nada puede estar vacío.
    if not nombre or not poblacion or not superficie or not continente:
        print("Error: Todos los campos son obligatorios.")
        return

    # Validación numérica: población y superficie deben ser enteros positivos.
    if not poblacion.isdigit() or not superficie.isdigit():
        print("Error: Población y superficie deben ser números enteros.")
        return

    # Abrimos el archivo y agregamos una nueva línea con los datos ingresados.
    with open(ARCHIVO, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([nombre, poblacion, superficie, continente])

    print(f"País {nombre} agregado exitosamente.")


# ============================================================
#  ACTUALIZAR DATOS DE UN PAÍS
# ============================================================
def actualizar_pais():
    """
    Permite modificar la población y superficie de un país existente.
    La búsqueda se realiza por nombre (ignorando mayúsculas/minúsculas).
    """

    print("-----Actualizar País-----")

    nombre_buscar = input("Ingrese el país que desea actualizar: ").strip()

    # No se puede buscar un nombre vacío.
    if not nombre_buscar:
        print("Error: El nombre del país es obligatorio.")
        return

    # Leemos todos los países del archivo.
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)

    encontrado = False

    # Recorremos país por país buscando coincidencia.
    for pais in paises:
        # "lower()" se usa para comparar sin importar mayúsculas.
        if pais["nombre"].lower() == nombre_buscar.lower():

            encontrado = True
            print(f"País encontrado: {pais['nombre']}")

            nueva_poblacion = input("Ingrese la nueva población: ").strip()
            nueva_superficie = input("Ingrese la nueva superficie: ").strip()

            if not nueva_poblacion.isdigit() or not nueva_superficie.isdigit():
                print("Error: Población y superficie deben ser números enteros.")
                return

            # Se actualizan los valores en el diccionario.
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("Datos actualizados correctamente.")
            break

    if not encontrado:
        print("No se encontró el país especificado.")
        return

    # Escribimos la lista completa nuevamente en el archivo.
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(paises)


# ============================================================
#  BUSCAR UN PAÍS POR NOMBRE
# ============================================================
def buscar_pais():
    """
    Permite buscar países según una parte del nombre ingresado por el usuario.
    No es necesario escribir el nombre completo.
    """
    print("-----Buscar País-----")

    termino = input("Ingrese una parte o todo el nombre del país: ").strip().lower()

    if not termino:
        print("Error: debe ingresar un texto para buscar.")
        return

    encontrados = []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        # Buscamos coincidencias parciales dentro del nombre.
        for fila in lector:
            if termino in fila["nombre"].lower():
                encontrados.append(fila)

    if encontrados:
        print(f"Se encontraron {len(encontrados)} resultado(s):\n")
        for pais in encontrados:
            print(f"{pais['nombre']} - {pais['continente']} | "f"{pais['poblacion']} hab | {pais['superficie']} km²")
    else:
        print("No se encontraron países que coincidan con la búsqueda.")


# ============================================================
#  FILTRAR PAÍSES SEGÚN CRITERIOS
# ============================================================
def filtrar_pais():
    """
    Permite filtrar países por:
    1. Continente
    2. Rango de población
    3. Rango de superficie
    """

    print("-----Filtrar País-----")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")

    opcion = input("Elija una opción: ").strip()

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)

    filtrados = []

    # ------------------------------------------
    # Filtrar por CONTINENTE
    # ------------------------------------------
    if opcion == "1":
        cont = input("Ingrese el nombre del continente: ").strip().lower()

        # LIST COMPREHENSION:
        # Se recorre cada país "p" y se lo incluye solamente
        # si su continente coincide exactamente.
        filtrados = [p for p in paises if p["continente"].lower() == cont]

    # ------------------------------------------
    # Filtrar por POBLACIÓN
    # ------------------------------------------
    elif opcion == "2":
        min_pob = input("Población mínima: ").strip()
        max_pob = input("Población máxima: ").strip()

        if not (min_pob.isdigit() and max_pob.isdigit()):
            print("Error: los valores deben ser números.")
            return

        min_pob, max_pob = int(min_pob), int(max_pob)

        # Se filtran países que tengan un valor de población válido
        filtrados = [
            p for p in paises
            if p["poblacion"].strip() != ""
            and min_pob <= int(p["poblacion"].strip()) <= max_pob
        ]

    # ------------------------------------------
    # Filtrar por SUPERFICIE
    # ------------------------------------------
    elif opcion == "3":
        min_sup = input("Superficie mínima (KM): ").strip()
        max_sup = input("Superficie máxima (KM): ").strip()

        if not (min_sup.isdigit() and max_sup.isdigit()):
            print("Error: los valores deben ser números.")
            return

        min_sup, max_sup = int(min_sup), int(max_sup)

        filtrados = [
            p for p in paises
            if p["superficie"].strip() != ""
            and min_sup <= int(p["superficie"].strip()) <= max_sup
        ]

    else:
        print("Opción inválida.")
        return

    # ------------------------------------------
    # Mostrar los resultados obtenidos
    # ------------------------------------------
    if filtrados:
        print(f"Se encontraron {len(filtrados)} resultado(s):\n")
        for pais in filtrados:
            print(f"{pais['nombre']} - {pais['continente']} | "f"{pais['poblacion']} hab | {pais['superficie']} km²")
    else:
        print("No se encontraron países con esos criterios.")


# ============================================================
#  ORDENAR PAÍSES
# ============================================================
def ordenar_paises():
    """
    Ordena los países según:
    1. Nombre
    2. Población
    3. Superficie
    
    Además, permite elegir si se ordena ascendente o descendente.
    """

    print("-----Ordenar Países-----")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    criterio = input("Elija una opción: ").strip()
    orden = input("¿Orden Ascendente (A) o Descendente (D)? ").strip().upper()

    # Si el usuario elige "D", la variable será True.
    descendente = orden == "D"

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)

    if not paises:
        print("No hay países registrados.")
        return

    # Eliminamos cualquier fila vacía o incompleta.
    paises = [
        p for p in paises
        if p["nombre"].strip() != "" 
        and p["poblacion"].strip() != "" 
        and p["superficie"].strip() != ""
        and p["continente"].strip() != ""
    ]

    # ----------------------------------------------
    # ORDENAR POR NOMBRE
    # ----------------------------------------------
    if criterio == "1":

        # IMPORTANTE: LAMBDA EXPLICADA
        # lambda p: p["nombre"].lower()
        #
        # Esto significa:
        #   "Para cada país p, ordenar usando su nombre en minúsculas".
        #
        # ¿Por qué .lower()?
        #   Porque 'Argentina' y 'argentina' deben considerarse iguales
        #   para evitar errores en el orden.
        paises.sort(
            key=lambda p: p["nombre"].lower(),
            reverse=descendente
        )

    # ----------------------------------------------
    # ORDENAR POR POBLACIÓN
    # ----------------------------------------------
    elif criterio == "2":

        # Esta lambda convierte la población de TEXTO → ENTERO
        # para que Python pueda comparar correctamente.
        #
        # Si no se convierte, Python ordenaría alfabéticamente:
        #   "1000" < "50"  (lo cual sería incorrecto)
        paises.sort(
            key=lambda p: int(p["poblacion"].strip()),
            reverse=descendente
        )

    # ----------------------------------------------
    # ORDENAR POR SUPERFICIE
    # ----------------------------------------------
    elif criterio == "3":

        # Igual que en población, convertimos superficie
        # a entero antes de ordenar.
        paises.sort(
            key=lambda p: int(p["superficie"].strip()),
            reverse=descendente
        )

    else:
        print("Opción inválida.")
        return

    print("\nPaíses ordenados:\n")

    for p in paises:
        print(f"{p['nombre']} - {p['continente']} | "f"{p['poblacion']} hab | {p['superficie']} km²")


# ============================================================
#  MOSTRAR ESTADÍSTICAS GENERALES
# ============================================================
def mostrar_estadisticas():
    
    #  Muestra información general:
    # - País con mayor población
    #- País con menor población
    #- Promedio de población
    #- Promedio de superficie
    #- Cantidad de países por continente
    

    print("-----Estadísticas de Países-----")

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        paises = list(lector)

    if not paises:
        print("No hay datos cargados.")
        return

    # Solo consideramos países que tengan valores válidos
    paises = [
        p for p in paises
        if p["poblacion"].strip() != "" 
        and p["superficie"].strip() != ""
        and p["nombre"].strip() != ""
        and p["continente"].strip() != ""
    ]

    if not paises:
        print("No hay datos válidos para calcular estadísticas.")
        return

    # Convertimos población y superficie de TEXTO → ENTERO
    for p in paises:
        p["poblacion"] = int(p["poblacion"].strip())
        p["superficie"] = int(p["superficie"].strip())

    # LAMBDA EXPLICADA:
    # max(lista, key=lambda x: x["poblacion"])
    #
    # Eso significa:
    #   "Buscar en la lista el país que tenga el valor
    #    más grande en la clave 'poblacion'"
    mayor = max(paises, key=lambda x: x["poblacion"])

    # Lo mismo para el mínimo.
    menor = min(paises, key=lambda x: x["poblacion"])

    # Promedios simples
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    # Conteo: cuántos países hay por cada continente
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