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

def pedir_entero_opcional(texto):
    while True:
        valor=input(texto).strip()
        if valor == "":
            return None
        try:
            return int(valor)
        except ValueError:
            print("Error: ingrese un numero entero")


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
    print(f"Se agrego {pais_a_agregar['nombre']} - Poblacion: {pais_a_agregar['poblacion']} - Superficie: {pais_a_agregar['superficie']} - Continente: {pais_a_agregar['continente']}")


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
    poblacion_minima = pedir_entero_opcional(
        "Ingresa el número de poblacion mínima: (Enter para omitir)"
    )
    poblacion_maxima = pedir_entero_opcional(
        "Ingresa el número de poblacion maxima: (Enter para omitir)"
    )

    if poblacion_minima is None:
        poblacion_minima = 0
    if poblacion_maxima is None:
        poblacion_maxima = float("inf")

    encontrado = False

    for pais in paises:
        poblacion = pais["poblacion"]
        if poblacion_minima <= poblacion <= poblacion_maxima:
            print(f"{pais['nombre']} - poblacion: {poblacion}")
            encontrado = True

    if not encontrado:
        print("No se encontraron paises dentro del rango de población.")
        return


def filtro_por_superficie(paises):
    superficie_minima = pedir_entero_opcional("Ingresa el número de superficie mínima: ")
    superficie_maxima = pedir_entero_opcional("Ingresa el número de superficie maxima: ")

    if superficie_minima is None:
        superficie_minima=0
    if superficie_maxima is None:
        superficie_maxima=float("inf")


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
    except ValueError:
        print("Error: formato incorrecto en el CSV")    

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
def mostrar_mayor_poblacion(paises):

    pais_mayor=paises[0]
   
    for pais in paises:
        if pais["poblacion"]>pais_mayor["poblacion"]:
            pais_mayor=pais

    print(
        f"pais con mayor poblacion: {pais_mayor['nombre']} - Poblacion: {pais_mayor['poblacion']}"        
    )

def mostrar_menor_poblacion(paises):

    pais_menor=paises[0]
   
    for pais in paises:
        if pais["poblacion"]<pais_menor["poblacion"]:
            pais_menor=pais

    print(
        f"pais con menor poblacion: {pais_menor['nombre']} - Poblacion: {pais_menor['poblacion']}"        
    )

def mostrar_promedio_poblacion(paises):

    total_paises = len(paises)

    poblacion_total = 0

    for pais in paises:
        poblacion_total += pais["poblacion"]

    promedio = poblacion_total / total_paises

    print(
        f"Poblacion promedio: {promedio:.0f} habitantes por pais"
    )
   
def mostrar_promedio_superficie(paises):
    
    total_paises = len(paises)

    superficie_total = 0

    for pais in paises:
        superficie_total += pais["superficie"]

    promedio = superficie_total / total_paises

    print(
        f"Superficie promedio: {promedio:.2f} Km2"
    )

def mostrar_cantidad_por_continente(paises):

    continente_paises = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in continente_paises:
            continente_paises[continente] = []
        continente_paises[continente].append(pais)

    for continente, paises_continente in continente_paises.items():
        print(f"\nContinente: {continente}")
        print(f"Cantidad de paises: {len(paises_continente)}")


def main():
    paises = cargar_datos()

    while True:
        
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
            print("\n Opciones de actualizacion")
            print("1. Actualizar poblacion")
            print("2. Actualizar superficie")
       
            sub_menu = pedir_entero("Seleccione una opcion: ")

            if sub_menu == 1:
                actualizar_poblacion(paises)
            
            elif sub_menu == 2:
                actualizar_superficie(paises)

            else:
                print("Error: ingresa alguna delas opciones disponibles")
               
            guardar_datos(paises)

        elif opcion == "3":
            print("\n Ordenar por: ")
            print("1. Nombre ")
            print("2. Poblacion ")
            print("3. Superficie")
       
            sub_menu = pedir_entero("Seleccione una opcion: ")

            if sub_menu == 1:
                paises_ordenados=ordenar_paises(paises,"nombre")
            
            elif sub_menu == 2:
                paises_ordenados=ordenar_paises(paises,"poblacion")

            elif sub_menu == 3:
                orden=pedir_entero("Ordena por: 1. ascendente  2. descendente: ")

                if orden == 1:
                  paises_ordenados=ordenar_paises(paises,"superficie") 

                elif orden == 2:
                  paises_ordenados=ordenar_paises(paises,"superficie",True) 

                else:
                    print("Opcion Invalida")  
                    continue
            else:
                print("Error: ingresa alguna delas opciones disponibles")
                continue

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

            print("\n filtros")
            print("1. Filtrat por continente")
            print("2. Filtrat por poblacion")
            print("3. Filtrat por superficie")

            sub_menu = pedir_entero("Seleccione una opcion: ")

            if sub_menu == 1:
                filtro_por_continente(paises)
            elif sub_menu == 2:
                filtro_por_poblacion(paises)
            elif sub_menu == 3:
                filtro_por_superficie(paises)
            else:
                print("Error: ingresa alguna delas opciones disponibles")

        elif opcion == "6":

            print("\n Estadisticas ")
            print("1. Pais con mayor poblacion")
            print("2. Pais con menor poblacion")
            print("3. Promedio de poblacion")
            print("4. Promedio de superficie")
            print("5. Cantidad de paises por continente")            

            sub_menu = pedir_entero("Seleccione una opcion: ")

            if sub_menu == 1:
                mostrar_mayor_poblacion(paises)
            
            elif sub_menu == 2: 
                mostrar_menor_poblacion(paises)

            elif sub_menu == 3:
                mostrar_promedio_poblacion(paises)

            elif sub_menu == 4:
                mostrar_promedio_superficie(paises)
            
            elif sub_menu == 5:
                mostrar_cantidad_por_continente(paises)
                
            else:
                print("Error: ingresa alguna delas opciones disponibles")
                continue

        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, por favor selecciona una opcion del menu")


if __name__ == "__main__":
    main()