##################################################
# 1) Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#    Añadir las siguientes frutas con sus respectivos precios:
#    • Naranja = 1200
#    • Manzana = 1500
#    • Pera = 2300
##################################################
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
def ejercicio1():
    global precios_frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    print("Ejercicio 1 - Diccionario con frutas añadidas:", precios_frutas)

##################################################
# 2) Siguiendo con el diccionario precios_frutas resultante del punto anterior,
#    actualizar los precios de las siguientes frutas:
#    • Banana = 1330
#    • Manzana = 1700
#    • Melón = 2800
##################################################
def ejercicio2():
    global precios_frutas
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    print("Ejercicio 2 - Diccionario con precios actualizados:", precios_frutas)

##################################################
# 3) Siguiendo con el diccionario precios_frutas resultante del punto anterior,
#    crear una lista que contenga únicamente las frutas sin los precios.
##################################################
def ejercicio3():
    frutas = list(precios_frutas.keys())
    print("Ejercicio 3 - Lista de frutas:", frutas)

##################################################
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
#    • Permitir cargar 5 contactos (nombre: número).
#    • Luego, pedir un nombre y mostrar el número asociado, si existe.
##################################################
def ejercicio4():
    agenda_tel = {}
    for i in range(5):
        nombre = input(f"Ejercicio 4 - Ingrese nombre del contacto {i+1}: ")
        numero = input(f"Ejercicio 4 - Ingrese teléfono de {nombre}: ")
        agenda_tel[nombre] = numero
    consulta = input("Ejercicio 4 - Ingrese nombre a consultar: ")
    print("Número encontrado:" if consulta in agenda_tel else "Contacto no existe.", agenda_tel.get(consulta))

##################################################
# 5) Solicitar al usuario una frase e imprimir:
#    • Las palabras únicas (usando un set).
#    • Un diccionario con la cantidad de veces que aparece cada palabra.
##################################################
def ejercicio5():
    frase = input("Ejercicio 5 - Ingrese una frase: ")
    palabras = frase.split()
    unicas = set(palabras)
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    print("Ejercicio 5 - Palabras únicas:", unicas)
    print("Ejercicio 5 - Frecuencia de palabras:", contador)

##################################################
# 6) Permitir ingresar los nombres de 3 alumnos y para cada uno una tupla de 3 notas.
#    Luego, mostrar el promedio de cada alumno.
##################################################
def ejercicio6():
    notas_alumnos = {}
    for i in range(3):
        nombre = input(f"Ejercicio 6 - Ingrese nombre del alumno {i+1}: ")
        notas = tuple(map(float, input(f"Ejercicio 6 - Ingrese 3 notas separadas por espacio para {nombre}: ").split()))
        notas_alumnos[nombre] = notas
    for alumno, notas in notas_alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"Alumno {alumno}: promedio = {promedio}")

##################################################
# 7) Dado dos sets de números, representando legajos de estudiantes que aprobaron
#    Parcial 1 y Parcial 2:
#    • Mostrar los que aprobaron ambos parciales.
#    • Mostrar los que aprobaron solo uno de los dos.
#    • Mostrar la lista total de estudiantes que aprobaron al menos un parcial.
##################################################
def ejercicio7():
    p1 = set(map(int, input("Ejercicio 7 - Ingrese legajos que aprobaron Parcial 1 (separados por espacio): ").split()))
    p2 = set(map(int, input("Ejercicio 7 - Ingrese legajos que aprobaron Parcial 2 (separados por espacio): ").split()))
    ambos = p1 & p2
    solo_uno = p1 ^ p2
    al_menos_uno = p1 | p2
    print("Ejercicio 7 - Ambos parciales:", ambos)
    print("Ejercicio 7 - Solo uno:", solo_uno)
    print("Ejercicio 7 - Al menos uno:", al_menos_uno)

##################################################
# 8) Armar un diccionario de stock de productos.
#    Permitir al usuario:
#    • Consultar el stock de un producto.
#    • Agregar unidades al stock si el producto ya existe.
#    • Agregar un nuevo producto si no existe.
##################################################
def ejercicio8():
    stock = {}
    operaciones = int(input("Ejercicio 8 - ¿Cuántas operaciones desea realizar? "))
    for i in range(operaciones):
        accion = input("Ingrese acción ('consultar', 'agregar_unidades', 'nuevo_producto'): ")
        if accion == 'consultar':
            prod = input("Producto a consultar: ")
            print(f"Stock de {prod}:", stock.get(prod, 'No existe'))
        elif accion == 'agregar_unidades':
            prod = input("Producto al que desea agregar unidades: ")
            unidades = int(input("Cantidad de unidades a agregar: "))
            if prod in stock:
                stock[prod] += unidades
                print(f"Nuevo stock de {prod}: {stock[prod]}")
            else:
                print("El producto no existe.")
        elif accion == 'nuevo_producto':
            prod = input("Ingrese nombre del nuevo producto: ")
            unidades = int(input("Ingrese stock inicial: "))
            if prod not in stock:
                stock[prod] = unidades
                print(f"Producto {prod} agregado con stock {unidades}.")
            else:
                print("El producto ya existe.")
        else:
            print("Acción no reconocida.")
    print("Ejercicio 8 - Stock final:", stock)

##################################################
# 9) Crear una agenda donde las claves sean tuplas (día, hora) y los valores eventos.
#    Permitir consultar qué actividad hay en cierto día y hora.
##################################################
def ejercicio9():
    agenda = {}
    eventos = int(input("Ejercicio 9 - ¿Cuántos eventos desea cargar? "))
    for i in range(eventos):
        dia = input("Ingrese día del evento: ")
        hora = input("Ingrese hora del evento (HH:MM): ")
        desc = input("Ingrese descripción del evento: ")
        agenda[(dia, hora)] = desc
    dia_c = input("Ejercicio 9 - Ingrese día a consultar: ")
    hora_c = input("Ingrese hora a consultar (HH:MM): ")
    print("Actividad en esa fecha y hora:", agenda.get((dia_c, hora_c), 'No hay evento'))

##################################################
# 10) Dado un diccionario que mapea países con sus capitales,
#     construir un nuevo diccionario donde:
#     • Las capitales sean las claves.
#     • Los países sean los valores.
##################################################
def ejercicio10():
    pais_capital = {}
    n = int(input("Ejercicio 10 - ¿Cuántos países desea ingresar? "))
    for i in range(n):
        pais = input("Ingrese nombre del país: ")
        capital = input("Ingrese capital: ")
        pais_capital[pais] = capital
    capital_pais = {cap: pais for pais, cap in pais_capital.items()}
    print("Ejercicio 10 - Diccionario invertido (capital: país):", capital_pais)

