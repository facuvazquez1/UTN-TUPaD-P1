##################################################
# 1) Crea una función recursiva que calcule el factorial de un número.
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial
# de todos los números enteros entre 1 y el número que indique el usuario
##################################################

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Ejecución ejercicio 1
def ejercicio1():
    num = int(input("Ejercicio 1 - Ingrese un número: "))
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")

##################################################
# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci
# en la posición indicada. Posteriormente, muestra la serie completa hasta la
# posición que el usuario especifique.
##################################################

def fibonacci(m):
    if m <= 0:
        return 0
    if m == 1:
        return 1
    return fibonacci(m - 1) + fibonacci(m - 2)

# Ejecución ejercicio 2
def ejercicio2():
    pos = int(input("Ejercicio 2 - Ingrese la posición de Fibonacci: "))
    serie = [fibonacci(i) for i in range(pos + 1)]
    print("Serie de Fibonacci hasta posición", pos, ":", serie)

##################################################
# 3) Crea una función recursiva que calcule la potencia de un número base
# elevado a un exponente, utilizando la fórmula n^m = n * n^(m-1).
# Prueba esta función en un algoritmo general.
##################################################

def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

# Ejecución ejercicio 3
def ejercicio3():
    b = int(input("Ejercicio 3 - Ingrese la base: "))
    e = int(input("Ejercicio 3 - Ingrese el exponente: "))
    print(f"{b}^{e} = {potencia(b, e)}")

##################################################
# 4) Crear una función recursiva en Python que reciba un número entero positivo
# en base decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0)
# y unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir
# este procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
##################################################

def decimal_a_binario(n):
    if n == 0:
        return "0"
    def _conv(n):
        if n == 0:
            return ""
        return _conv(n // 2) + str(n % 2)
    return _conv(n)

# Ejecución ejercicio 4
def ejercicio4():
    num = int(input("Ejercicio 4 - Ingrese un número decimal positivo: "))
    print(f"Representación binaria: {decimal_a_binario(num)}")

##################################################
# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba
# una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo
# o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
##################################################

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejecución ejercicio 5
def ejercicio5():
    p = input("Ejercicio 5 - Ingrese una palabra (sin espacios ni tildes): ")
    resultado = es_palindromo(p)
    print(f"¿'{p}' es palíndromo? {resultado}")

##################################################
# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4)
# suma_digitos(9)      → 9
# suma_digitos(305)    → 8   (3 + 0 + 5)
##################################################

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# Ejecución ejercicio 6
def ejercicio6():
    numero = int(input("Ejercicio 6 - Ingrese un número entero positivo: "))
    print(f"Suma de dígitos: {suma_digitos(numero)}")

##################################################
# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo
# coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta
# llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques
# en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1)   → 1         (1)
# contar_bloques(2)   → 3         (2 + 1)
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
##################################################

def contar_bloques(n):
    if n <= 1:
        return n
    return n + contar_bloques(n - 1)

# Ejecución ejercicio 7
def ejercicio7():
    base = int(input("Ejercicio 7 - Ingrese la cantidad de bloques en el nivel más bajo: "))
    print(f"Total de bloques: {contar_bloques(base)}")

##################################################
# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba
# un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas
# veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0
##################################################

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    cuenta = 1 if numero % 10 == digito else 0
    return cuenta + contar_digito(numero // 10, digito)

# Ejecución ejercicio 8
def ejercicio8():
    num = int(input("Ejercicio 8 - Ingrese un número entero positivo: "))
    d = int(input("Ejercicio 8 - Ingrese un dígito (0-9): "))
    print(f"El dígito {d} aparece {contar_digito(num, d)} veces en {num}")

##################################################
# Ejecución de todos los ejercicios
##################################################

