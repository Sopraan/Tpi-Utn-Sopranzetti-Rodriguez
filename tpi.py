import csv


# Validacion espacios en blanco al ingreso de los paises
def validacion_paises():
    while True:
        consulta_pais = input("Ingresar el pais elegido: ").strip()
        if consulta_pais == "":
            print("Error: no se puede dejar el campo vacio")
            continue
        break

    return consulta_pais


# busqueda rapida de paises en csv
def buscar_pais(paises, nombre):
    for pais in paises:
        if nombre.lower() in pais ["nombre"].lower():
            return pais

        return None


# se utilizan funciones de validacion, busqueda y se modifica poblacion
def actualizar_poblacion():
    while True:
        consulta_pais = validacion_paises()
        pais = buscar_pais(paises, consulta_pais)
        if pais is None:
            print("Pais no encontrado")
            continue
        break

    while True:
        try:
            nueva_poblacion = int(input("Ingrese la poblacion a modificar: "))
            break
        except ValueError:
            print("Error: ingrese un numero entero")

    pais["poblacion"] = nueva_poblacion
    print(f"La poblacion de {pais['nombre']} se actualizo a: {nueva_poblacion}")


# se ustilizan funciones de validacion, busqueda y se modifica superficie
def actualizar_superficie():

    while True:
        consulta_pais = validacion_paises()
        pais = buscar_pais(paises, consulta_pais)
        if pais is None:
            print("Pais no encontrado")
            continue
        break

    while True:
        try:
            nueva_Superficie = float(input("Ingrese la superficie a modificar: "))
            break
        except ValueError:
            print("Error: ingrese un numero")

    pais["superficie"] = nueva_Superficie
    print(f"La superficie de {pais['nombre']} se actualizo a: {nueva_Superficie} Km2")


## se utilizan funciones de validacion, busqueda, se implemento el agregar paises con su diccionarios
def agregar_pais():

    while True:
        nombre = validacion_paises()
        pais = buscar_pais(paises, nombre)
        if pais is not None:
            print("El pais ya se encuentra en la base")
            continue
        break

    while True:
        try:
            poblacion = int(input("Ingrese la poblacion: "))
            break
        except ValueError:
            print("Error: no se pueden ingresar letras ni espacios vacios")

    while True:
        try:
            superficie = float(input("Ingrese la superficie: "))
            break
        except ValueError:
            print("Error: no se pueden ingresar letras ni espacios vacios")

    while True:

        continente = validacion_paises()
        if not continente.isalpha():
            print("Error: Ingrese solamente letras")
            continue
        break
    # Se agrega el diccionario del nuevo pais
    pais_a_agregar = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }

    paises.append(pais_a_agregar)
    print(f"Se agrego {pais_a_agregar} a la base")


def filtro_por_continente():
    print("Continentes: \n 1. America\n 2. Europa\n 3. Asia\n 4. Africa\n 5. Oceania")
    while True:
        continente = input("Ingresa el continente a filtrar: ").strip()
        if continente == "":
            print("Error: no se piueden ingresar campos vacios")
            continue
        if not continente.isalpha():
            print("Error: No se pueden ingresar numeros, escribi el continente")
            continue
        # se limita el filtro a los contientes reales, para evitar errores
        if continente not in ["america", "asia", "europa", "oceania", "africa"]:
            print("Error: Continente invalido")
            continue
        break
    # se inprimen los paises que corresponden al continente elegido
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(f"{pais['nombre']}\n")


def filtro_por_poblacion():

    while True:
        try:
            poblacion_minima = int(input("Ingresa el numero de poblacion minima: "))
            break
        except ValueError:
            print("Error: ingresa solamente numeros")
    while True:
        try:
            poblacion_maxima = int(input("Ingresa el numero de poblacion maxima: "))
            break
        except ValueError:
            print("Error: ingresa solamente numeros")

    if poblacion_minima > poblacion_maxima:
        print("Error: la poblacion minima no puede superar a la poblacion maxima ")
        return

    encontrado = False

    for pais in paises:
        poblacion = int(pais["poblacion"])
        if poblacion_minima <= poblacion <= poblacion_maxima:
            print(f"{pais['nombre']} - Poblacion: {poblacion}")
            encontrado = True

    if not encontrado:
        print(
            "No se encontraron paises dentro del rango de poblacion, proba con una poblacion mayor"
        )
        return
    
def filtro_por_superficie():

    while True:
        try:
            superficie_minima = int(input("Ingresa el numero de superficie minima: "))
            break
        except ValueError:
            print("Error: ingresa solamente numeros")
    while True:
        try:
            superficie_maxima = int(input("Ingresa el numero de superficie maxima: "))
            break
        except ValueError:
            print("Error: ingresa solamente numeros")

    if superficie_minima > superficie_maxima:
        print("Error: la superficie minima no puede superar a la superficie maxima ")
        return

    encontrado = False

    for pais in paises:
        superficie = int(pais["superficie"])
        if superficie_minima <= superficie <= superficie_maxima:
            print(f"{pais['nombre']} - Superficie: {superficie} Km2")
            encontrado = True

    if not encontrado:
        print(
            "No se encontraron paises dentro del rango de superficie, proba con una superficie mayor"
        )
        return



paises = []


# Lector de arvhivos csv
with open("base.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for pais in lector:
        paises.append(pais)


actualizar_poblacion()
actualizar_superficie()
agregar_pais()
filtro_por_continente()
filtro_por_poblacion()
filtro_por_superficie()


# Estadísticas
def estadisticas():
    total_paises = len(paises)
    print(f"Total de paises cargados: {total_paises}")

    poblacion_total = sum(int(pais["poblacion"]) for pais in paises)
    poblacion_promedio = poblacion_total / total_paises if total_paises > 0 else 0
    print(f"Poblacion promedio: {poblacion_promedio:.0f} habitantes por pais")

    superficie_total = sum(float(pais["superficie"]) for pais in paises)
    superficie_promedio = superficie_total / total_paises if total_paises > 0 else 0
    print(f"Superficie promedio: {superficie_promedio:.2f} Km2")

    continente_paises = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in continente_paises:
            continente_paises[continente] = []
        continente_paises[continente].append(pais)

    for continente, paises_continente in continente_paises.items():
        print(f"\nContinente: {continente}")
        print(f"Cantidad de paises: {len(paises_continente)}")
        poblacion_continente = sum(int(pais["poblacion"]) for pais in paises_continente)
        print(f"Poblacion total: {poblacion_continente}")
        superficie_continente = sum(float(pais["superficie"]) for pais in paises_continente)
        print(f"Superficie total: {superficie_continente} Km2")

    # Cuando esten listas las funciones para ordenar paises, mostrar:
    # Paises con mayor y menor poblacion
estadisticas()
