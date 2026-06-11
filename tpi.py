import csv

# Constantes
CONTINENTES = {
    "america",
    "asia",
    "europa",
    "oceania",
    "africa",
}


# busqueda de pais con coincidencia exacta
def buscar_pais(paises, nombre):
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            return pais

    return None


# Validacion espacios en blanco al ingreso de los paises
def pedir_texto(texto):
    while True:
        texto_usuario = input(texto).strip()
        if texto_usuario == "":
            print("Error: ingrese un valor")
            continue

        return texto_usuario


def pedir_entero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Error: ingrese un número entero")


def pedir_flotante(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error: ingrese un número")


def pedir_pais(paises, texto):
    while True:
        consulta_pais = pedir_texto(texto)
        pais = buscar_pais(paises, consulta_pais)
        if pais is None:
            print("Pais no encontrado")
            continue

        return pais


def pedir_continente(texto):
    while True:
        continente = pedir_texto(texto).lower()
        if continente not in CONTINENTES:
            print("Error: Continente invalido")
            continue

        return continente


def buscar_pais_con_similares(paises, mensaje):
    texto = pedir_texto(mensaje)

    encontrados = []

    for pais in paises:
        if texto.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    return encontrados


# se utilizan funciones de validacion, busqueda y se modifica poblacion
def actualizar_poblacion(paises):
    pais = pedir_pais(paises, "Ingresar el pais elegido: ")

    nueva_poblacion = pedir_entero("Ingrese la poblacion a modificar: ")

    pais["poblacion"] = nueva_poblacion
    print(f"La poblacion de {pais['nombre']} se actualizo a: {nueva_poblacion}")


# se utilizan funciones de validación, búsqueda y se modifica superficie
def actualizar_superficie(paises):

    pais = pedir_pais(paises, "Ingresar el pais elegido: ")

    nueva_superficie = pedir_flotante("Ingrese la superficie a modificar: ")

    pais["superficie"] = nueva_superficie
    print(f"La superficie de {pais['nombre']} se actualizo a: {nueva_superficie} Km2")


# se utilizan funciones de validacion, busqueda, se implemento el agregar paises con su diccionarios
def agregar_pais(paises):

    while True:
        nombre = pedir_texto("Ingresar el pais elegido: ")
        pais = buscar_pais(paises, nombre)
        if pais is not None:
            print("El pais ya se encuentra en la base")
            continue
        break

    poblacion = pedir_entero("Ingrese la poblacion: ")
    superficie = pedir_flotante("Ingrese la superficie: ")
    continente = pedir_continente("Ingresa el continente: ")

    # Se agrega el diccionario del nuevo pais
    pais_a_agregar = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }

    paises.append(pais_a_agregar)
    print(f"Se agrego {pais_a_agregar} a la base")


def filtro_por_continente(paises):
    print("Continentes: ")
    for continente in sorted(CONTINENTES):
        print(" - " + continente.title())

    continente = pedir_continente("Ingresa el continente a filtrar: ")

    # se imprimen los paises que corresponden al continente elegido
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(f"{pais['nombre']}\n")


def filtro_por_poblacion(paises):
    poblacion_minima = pedir_entero("Ingresa el número de poblacion mínima: ")
    poblacion_maxima = pedir_entero("Ingresa el número de poblacion maxima: ")

    if poblacion_minima > poblacion_maxima:
        print("Error: la poblacion mínima no puede superar a la poblacion maxima ")
        return

    encontrado = False

    for pais in paises:
        poblacion = pais["poblacion"]
        if poblacion_minima <= poblacion <= poblacion_maxima:
            print(f"{pais['nombre']} - Población: {poblacion}")
            encontrado = True

    if not encontrado:
        print("No se encontraron paises dentro del rango de población.")
        return


def filtro_por_superficie(paises):
    superficie_minima = pedir_entero("Ingresa el número de superficie mínima: ")
    superficie_maxima = pedir_entero("Ingresa el número de superficie maxima: ")

    if superficie_minima > superficie_maxima:
        print("Error: la superficie mínima no puede superar a la superficie maxima ")
        return

    encontrado = False

    for pais in paises:
        superficie = pais["superficie"]
        if superficie_minima <= superficie <= superficie_maxima:
            print(f"{pais['nombre']} - Superficie: {superficie} Km2")
            encontrado = True

    if not encontrado:
        print("No se encontraron paises dentro del rango de superficie.")
        return


# Lector de archivos csv
def cargar_datos():
    paises = []

    try:
        with open("base.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for pais in lector:
                pais["poblacion"] = int(pais["poblacion"])
                pais["superficie"] = float(pais["superficie"])

                paises.append(pais)

    except FileNotFoundError:
        print("Error: No se encontro el dataset inicial.")

    return paises


def guardar_datos(paises):
    try:
        columnas = ["nombre", "continente", "poblacion", "superficie"]
        with open("base.csv", "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(paises)

    except Exception as e:
        print(f"Error al guardar los datos: {e}")


# Ordenamiento
def ordenar_paises(paises, clave, descendente=False):
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)


def listar_datos(datos, maximo_por_pagina=10):
    mostrados = 0
    total = len(datos)

    while mostrados < total:
        lote = datos[mostrados : mostrados + maximo_por_pagina]
        for i, pais in enumerate(lote, start=mostrados + 1):
            print(
                f"{i}. {pais['nombre']} ({pais['continente']}) - Población: {pais['poblacion']} - Superficie: {pais['superficie']} Km2"
            )

        print()

        mostrados += len(lote)
        if mostrados >= total:
            print("No hay mas paises para mostrar.\n")
            break

        print(f"Mostrados {mostrados} de {total} paises.")
        entrada = (
            input(f"Presione [Enter] para cargar más  [q] Salir → ").strip().lower()
        )

        if entrada == "q":
            break


# Estadísticas
def estadisticas(paises):
    total_paises = len(paises)
    print(f"Total de paises cargados: {total_paises}")

    poblacion_total = sum(int(pais["poblacion"]) for pais in paises)
    poblacion_promedio = poblacion_total / total_paises if total_paises > 0 else 0
    print(f"Población promedio: {poblacion_promedio:.0f} habitantes por pais")

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
        print(f"Población total: {poblacion_continente}")
        superficie_continente = sum(
            float(pais["superficie"]) for pais in paises_continente
        )
        print(f"Superficie total: {superficie_continente} Km2")

    # Falta mostrar:
    # Paises con mayor y menor poblacion


def main():
    paises = cargar_datos()

    while True:
        print("Menu")
        print(f"""
{"~" * 60}
{"Menú".center(60)}
{"~" * 60}

1. Agregar país
2. Actualizar datos

3. Listado de paises
4. Buscar país por nombre

5. Filtrar paises

6. Estadísticas

7. Salir  
""")
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            agregar_pais(paises)
            guardar_datos(paises)

        elif opcion == "2":
            # TODO: Agregar un submenú
            # 1. Actualizar población
            actualizar_poblacion(paises)

            # 2. Actualizar superficie
            actualizar_superficie(paises)

            guardar_datos(paises)
        elif opcion == "3":
            # TODO: Agregar un submenú
            # 1. Ordenar por nombre
            paises_ordenados = ordenar_paises(paises, "nombre")
            # 2. Ordenar por población
            # 3. Ordenar por superficie
            listar_datos(paises_ordenados)

        elif opcion == "4":
            paises_encontrados = buscar_pais_con_similares(
                paises, "Ingresar el pais a buscar: "
            )
            if paises_encontrados:
                listar_datos(paises_encontrados)
            else:
                print("No se encontraron paises con ese nombre.")

        elif opcion == "5":
            # TODO: Agregar submenu
            # 1. Filtrar por continente
            filtro_por_continente(paises)
            # 2. Filtrar por población
            filtro_por_poblacion(paises)
            # 3. Filtrar por superficie
            filtro_por_superficie(paises)

            # Permitir que el valor mínimo o el valor máximo sea opcional
            # Si no se ingresa valor máximo, buscar mayor al mínimo
            # Si no se ingresa mínimo, buscar desde 0 hasta el máximo
        elif opcion == "6":
            # TODO: Agregar submenu
            # 1. País con mayor población
            # 2. País con menor población
            # 3. Promedio de población
            # 4. Promedio de superficie
            # 5. Cantidad de países por continente
            estadisticas(paises)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, por favor selecciona una opcion del menu")


if __name__ == "__main__":
    main()
