
from FuncionesTPI import agregar_pais, actualizar_pais, buscar_pais, filtrar_pais, ordenar_paises, mostrar_estadisticas

opcion = ""

while opcion != "0":
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar un país")
    print("2. Actualizar país")
    print("3. Buscar países")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("0. Salir")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1":
            agregar_pais()
        case "2":
            actualizar_pais()
        case "3":
            buscar_pais()
        case "4":
            filtrar_pais()
        case "5":
            ordenar_paises()
        case "6":
            mostrar_estadisticas() 
        case "0":
            print("Saliendo...") 
        case _:
            print("Opción inválida.")