#Ejercicio 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

usuario = int(input("Ingrese el numero para el rango de factoriales: "))

for i in range(2, usuario, 1):
    print(f"El factorial de {i} es: {factorial(i)}")

#Ejercicio 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


posicion = int(input("Ingrese la posición hasta donde desea ver la serie de Fibonacci: "))

print("Serie de Fibonacci hasta la posición", posicion, ":")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
    
#Ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1 
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print(f"{base} elevado a la {exponente} es: {resultado}")

#Ejercicio 4

def decimal_a_binario(n):
    if n < 2:
        return str(n)  
    else:
        return decimal_a_binario(n // 2) + str(n % 2) 
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Debe ingresar un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
    
#Ejercicio 5
def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"La palabra '{texto}' ES un palíndromo.")
else:
    print(f"La palabra '{texto}' NO es un palíndromo.")
    
#Ejercicio 6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

#Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

#Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

n = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(n, d)} veces en {n}.")
