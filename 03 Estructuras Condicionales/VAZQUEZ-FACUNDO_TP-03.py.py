""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad” """

# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#    print("Usted es mayor de edad.") 

""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado” """

# nota = float(input("Ingrese su nota: "))

# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

"""  3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. """

# numero_par = float(input("Ingrese un numero par: "))


# if numero_par % 2 == 0:
#     print("Ha ingresado un número par.")
# else:
#     print("Por favor, ingrese un número par.")

""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años. """

# edad = int(input("Ingrese su edad:"))

# if edad < 12:
#     print("Niño/a")
# elif edad >= 12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto joven")
# elif edad >= 30:
#     print("Adulto")

""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string """

# password = input("Ingrese una contraseña de 8 a 14 caracteres: ")
# password_long = len(password)

# if password_long >= 8 and password_long <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

""" 6) escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma """

# from statistics import mode, median, mean
# import statistics as st
# import random

# numeros_aleatorios = [random.randint(1,100) for i in range(50)]

# moda = st.mode(numeros_aleatorios)
# mediana = st.median(numeros_aleatorios)
# media = st.mean(numeros_aleatorios)

# if media > mediana and mediana > moda:
#     print("Sesgo positivo")
# elif media < mediana and mediana < moda:
#     print("Sesgo negativo")
# elif media == mediana:
#     print("Sin sesgo")
# else:
#     print("Sesgo indeterminado")

""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla. """

# def terminaConVocal (texto):

#     texto = texto.lower()
#     vocales = "aeiou"

#     if texto and texto[-1] in vocales:
#         return True
#     else:
#         return False
    
# texto = input("Ingrese una frase o palabra: ")

# if terminaConVocal(texto):
#     print(f"{texto}¡")
# else: 
#     print(f"{texto}")

""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas """

# name = input("Ingrese su nombre: ")
# option = int(input("Ingrese el numero de la opcion deseada 1. Mayuscula 2. Minuscula 3. Primer letra mayuscula: "))

# option_1 = name.upper()
# option_2 = name.lower()
# option_3 = name.title()

# if option == 1:
#     print(f"{option_1}")
# elif option == 2:
#     print(f"{option_2}")
# elif option == 3:
#     print(f"{option_3}")
# else:
#     print("Por favor, ingrese una opcion valida.")

""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

# mag_terremoto = float(input("Ingrese la magnitud del terremoto para poder clasificarlo: "))

# if mag_terremoto < 3:
#     print("Muy leve (imperceptible).")
# elif mag_terremoto >= 3 and mag_terremoto < 4:
#     print("Leve (ligeramente perceptible).")
# elif mag_terremoto >= 4 and mag_terremoto < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños).")
# elif mag_terremoto >= 5 and mag_terremoto < 6:
#     print("Fuerte (puede causar daños en estructurasdébiles).")
# elif mag_terremoto >= 6 and mag_terremoto < 7:
#     print("Muy Fuerte (puede causar daños significativos).")
# elif mag_terremoto >= 7:
#     print("Extremo (puede causar graves daños a gran escala).")
# else:
#     print("Por favor, ingrese un numero valido, recuerde que la escala de terremotos se mide del 1 al 7.")

""" 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:

+------------------------------------------+-----------------------+-----------------------+
|              Periodo del año             | Estación en el        | Estación en el        |
|                                          | hemisferio norte      | hemisferio sur        |
+------------------------------------------+-----------------------+-----------------------+
| Desde el 21 de diciembre hasta el 20 de  | Invierno              | Verano                |
| marzo (incluidos)                        |                       |                       |
+------------------------------------------+-----------------------+-----------------------+
| Desde el 21 de marzo hasta el 20 de junio| Primavera             | Otoño                 |
| (incluidos)                              |                       |                       |
+------------------------------------------+-----------------------+-----------------------+
| Desde el 21 de junio hasta el 20 de      | Verano                | Invierno              |
| septiembre (incluidos)                   |                       |                       |
+------------------------------------------+-----------------------+-----------------------+
| Desde el 21 de septiembre hasta el 20 de | Otoño                 | Primavera             |
| diciembre (incluidos)                    |                       |                       |
+------------------------------------------+-----------------------+-----------------------+

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano. """

# hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper() 
# mes = input("¿Qué mes del año es? (Enero a Diciembre): ").capitalize()
# dia = int(input("¿Qué día es? (1-31): "))

# if hemisferio == "N": 
#     if mes == "Diciembre" and dia >= 21 or mes == "Enero" or mes == "Febrero" or mes == "Marzo" and dia <= 20:
#         print("Estas en Invierno.")
#     elif mes == "Marzo" and dia >= 21 or mes == "Abril" or mes == "Mayo" or mes == "Junio" and dia <=20:
#         print("Estas en Primavera.")
#     elif mes == "Junio" and dia >= 21 or mes == "Julio" or mes == "Agosto" or mes == "Septiembre" and dia <=20:
#         print("Estas en Verano.")
#     elif mes == "Septiembre" and dia >= 21 or mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre" and dia <=20:
#         print("Estas en Otoño.")

# elif hemisferio == "S":
#     if mes == "Diciembre" and dia >= 21 or mes == "Enero" or mes == "Febrero" or mes == "Marzo" and dia <= 20:
#         print("Estas en Verano.")
#     elif mes == "Marzo" and dia >= 21 or mes == "Abril" or mes == "Mayo" or mes == "Junio" and dia <=20:
#         print("Estas en Otoño.")
#     elif mes == "Junio" and dia >= 21 or mes == "Julio" or mes == "Agosto" or mes == "Septiembre" and dia <=20:
#         print("Estas en Invierno.")
#     elif mes == "Septiembre" and dia >= 21 or mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre" and dia <=20:
#         print("Estas en Primavera.")
# else:
#     print("Porfavor ingrese datos validos¡")
    