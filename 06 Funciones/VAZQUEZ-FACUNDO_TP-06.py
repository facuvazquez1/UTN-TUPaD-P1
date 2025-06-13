# Práctico 2: Funciones en Python
# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA

import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: "Hola Mundo!".
def imprimir_hola_mundo():
    # Imprime el saludo genérico
    print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
def saludar_usuario(nombre):
    # Devuelve un saludo con el nombre proporcionado
    return f"Hola {nombre}!"

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima la información personal.
def informacion_personal(nombre, apellido, edad, residencia):
    # Imprime la información formateada
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Funciones para área y perímetro de un círculo.
def calcular_area_circulo(radio):
    # Calcula el área usando PI * r^2
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    # Calcula el perímetro usando 2 * PI * r
    return 2 * math.pi * radio

# 5. Crear una función llamada segundos_a_horas(segundos) que convierta segundos a horas.
def segundos_a_horas(segundos):
    # Convierte segundos a horas (float)
    return segundos / 3600

# 6. Crear una función llamada tabla_multiplicar(numero) que imprima la tabla de multiplicar del 1 al 10.
def tabla_multiplicar(numero):
    # Itera del 1 al 10 y muestra el producto
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Crear una función llamada operaciones_basicas(a, b) que devuelva suma, resta, multiplicación y división.
def operaciones_basicas(a, b):
    # Retorna una tupla con los cuatro resultados
    suma = a + b
    resta = a - b
    producto = a * b
    division = None
    if b != 0:
        division = a / b
    return suma, resta, producto, division

# 8. Crear una función llamada calcular_imc(peso, altura) que calcule el IMC.
def calcular_imc(peso, altura):
    # Calcula el índice de masa corporal y lo devuelve
    return peso / (altura ** 2)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que transforme Celsius a Fahrenheit.
def celsius_a_fahrenheit(celsius):
    # Convierte grados Celsius a Fahrenheit
    return (celsius * 9/5) + 32

# 10. Crear una función llamada calcular_promedio(a, b, c) que devuelva el promedio de tres números.
def calcular_promedio(a, b, c):
    # Calcula y devuelve el promedio aritmético
    return (a + b + c) / 3

if __name__ == "__main__":
    # Ejecución de cada ejercicio

    # 1.
    imprimir_hola_mundo()

    # 2.
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    # 3.
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # 4.
    radio = float(input("Radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    # 5.
    segundos = int(input("Ingrese cantidad de segundos: "))
    print(f"Horas: {segundos_a_horas(segundos):.2f}")

    # 6.
    num = int(input("Número para tabla de multiplicar: "))
    tabla_multiplicar(num)

    # 7.
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))
    suma, resta, producto, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {producto}")
    if division is not None:
        print(f"División: {division}")
    else:
        print("División: No se puede dividir por cero")

    # 8.
    peso = float(input("Ingrese peso en kg: "))
    altura = float(input("Ingrese altura en metros: "))
    print(f"IMC: {calcular_imc(peso, altura):.2f}")

    # 9.
    celsius = float(input("Temperatura en Celsius: "))
    print(f"Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")

    # 10.
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    n3 = float(input("Número 3: "))
    print(f"Promedio: {calcular_promedio(n1, n2, n3):.2f}")
