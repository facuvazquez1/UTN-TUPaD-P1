import random
"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

"""
# for i in range(101):
#     print(i)

##############################################################################################

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. Si ingreso cero tiene que contar 1 digito tambien.
"""
# num = int(input("Ingrese un número entero: "))
# contador = 0

# if num == 0:
#     contador = 1
# else:
#     while num != 0:
#         num //= 10
#         contador += 1
# print("La cantidad de dígitos es:", contador)

##############################################################################################

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.

"""
# Pedimos dos números al usuario

# inicio = int(input("Ingrese el primer número: "))
# fin = int(input("Ingrese el segundo número: "))

# if inicio > fin:
#     aux = inicio
#     inicio = fin
#     fin = aux

# suma = 0

# for i in range(inicio + 1, fin):
#     suma += i

# print("La suma de los números entre", inicio, "y", fin, "es:", suma)

##############################################################################################

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
# suma = 0  
# numero = None  

# while numero != 0:
#     numero = int(input("Ingrese un número entero (0 para salir): "))
#     if numero != 0:
#         suma += numero

# print("La suma total es:", suma)

###############################################################################################

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
# numero_aleatorio = random.randint(0, 9)
# intentos = 0
# numero_usuario = None

# while numero_usuario != numero_aleatorio:
#     numero_usuario = int(input("Adivina el número entre 0 y 9: "))
#     intentos += 1
#     if numero_usuario < numero_aleatorio:
#         print("Demasiado bajo. Intenta de nuevo.")
#     elif numero_usuario > numero_aleatorio:
#         print("Demasiado alto. Intenta de nuevo.")
#     else:
#         print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")

################################################################################################

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
# for i in range(100, -1, -1):
#     if i % 2 == 0:
#         print(i)

################################################################################################

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
# numero = int(input("Ingrese un número entero positivo: "))
# suma = 0

# for i in range(1, numero + 1):
#     suma += i   

# print("La suma de los números entre 0 y", numero, "es:", suma)

################################################################################################

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).

"""
# contador_pares = 0
# contador_impares = 0
# contador_positivos = 0
# contador_negativos = 0
# contador_ceros = 0
# contador_total = 0

# for i in range(100):
#     numero = int(input("Ingrese un número entero: "))
#     contador_total += 1
#     if numero == 0:
#         contador_ceros += 1
#     elif numero > 0:
#         contador_positivos += 1
#         if numero % 2 == 0:
#             contador_pares += 1
#         else:
#             contador_impares += 1
#     else:
#         contador_negativos += 1
#         if numero % 2 == 0:
#             contador_pares += 1
#         else:
#             contador_impares += 1

# print("Cantidad de números pares:", contador_pares)
# print("Cantidad de números impares:", contador_impares)
# print("Cantidad de números positivos:", contador_positivos)
# print("Cantidad de números negativos:", contador_negativos)
# print("Cantidad de números ceros:", contador_ceros)
# print("Cantidad total de números ingresados:", contador_total)

################################################################################################

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).

"""

# def calcular_media():
#
#     numeros = []
#     print("Por favor, ingresa 100 números enteros:")
#     for i in range(100):
#         while True:
#             try:
#                 numero_str = input(f"Ingresa el número {i + 1}: ")
#                 numero = int(numero_str)
#                 numeros.append(numero)
#                 break
#             except ValueError:
#                 print("¡Entrada inválida! Por favor, ingresa un número entero.")

#     if numeros:
#         media = sum(numeros) / len(numeros)
#         print(f"\nLa media de los 100 números ingresados es: {media}")
#     else:
#         print("No se ingresaron números.")

# if __name__ == "__main__":
#     calcular_media()

################################################################################################

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

"""

# def invertir_numero_sin_break(numero):
#     numero_str = str(numero)
#     numero_invertido_str = numero_str[::-1]
#     numero_invertido = int(numero_invertido_str)
#     return numero_invertido

# if __name__ == "__main__":
#     entrada_valida = False
#     num_ingresado = 0
#     while not entrada_valida:
#         try:
#             num_ingresado_str = input("Ingresa un número entero: ")
#             num_ingresado = int(num_ingresado_str)
#             entrada_valida = True
#         except ValueError:
#             print("¡Entrada inválida! Por favor, ingresa un número entero.")

#     numero_invertido = invertir_numero_sin_break(num_ingresado)
#     print(f"El número invertido es: {numero_invertido}")


