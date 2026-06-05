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
        if pais["nombre"].lower() == nombre.lower():
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


paises = []


# Lector de arvhivos csv
with open("base.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for pais in lector:
        paises.append(pais)


actualizar_poblacion()
actualizar_superficie()
agregar_pais()
