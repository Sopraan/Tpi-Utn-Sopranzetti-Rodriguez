import csv

# Constantes
CONTINENTES = {
    "america",
    "asia",
    "europa",
    "oceania",
    "africa",
}


def buscar_pais(paises, nombre):
    """Busca un pais por nombre exacto (case-insensitive)."""
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
            return pais

    return None


def pedir_texto(texto):
    """Solicita texto al usuario, rechaza cadenas vacias."""
    while True:
        texto_usuario = input(texto).strip()
        if texto_usuario == "":
            print("Error: ingrese un valor")
            continue

        return texto_usuario


def pedir_entero(texto, min=None):
    """Solicita un entero al usuario con validación y mínimo opcional."""
    while True:
        try:
            numero = int(input(texto))
            if min is not None and numero < min:
                print(f"Error: ingrese un número mayor o igual a {min}")
                continue
            return numero

        except ValueError:
            print("Error: ingrese un número entero")


def pedir_entero_opcional(texto):
    """Solicita un entero opcional (Enter para omitir)."""
    while True:
        valor = input(texto).strip()
        if valor == "":
            return None
        try:
            return int(valor)
        except ValueError:
            print("Error: ingrese un número entero")


def pedir_flotante(texto, min=None):
    """Solicita un número flotante con validación y mínimo opcional."""
    while True:
        try:
            numero = float(input(texto))
            if min is not None and numero < min:
                print(f"Error: ingrese un número mayor o igual a {min}")
                continue
            return numero

        except ValueError:
            print("Error: ingrese un número")


def formatear_numero(numero, decimales=2):
    """Devuelve el número con separadores de miles."""
    if isinstance(numero, float):
        return f"{numero:,.{decimales}f}".replace(",", "_").replace(".", ",").replace("_", ".")

    return f"{numero:,}".replace(",", ".")


def pedir_pais(paises, texto):
    """Solicita un nombre y devuelve el pais si existe."""
    while True:
        consulta_pais = pedir_texto(texto)
        pais = buscar_pais(paises, consulta_pais)
        if pais is None:
            print("País no encontrado")
            continue

        return pais


def pedir_continente(texto):
    """Solicita un continente validando que exista en las constantes."""
    while True:
        continente = pedir_texto(texto).lower()
        if continente not in CONTINENTES:
            print("Error: continente inválido")
            continue

        return continente.title()


def buscar_pais_con_similares(paises, mensaje):
    """Retorna paises cuyo nombre contenga el texto ingresado (coincidencia parcial)."""
    texto = pedir_texto(mensaje).lower()

    encontrados = []

    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    return encontrados


def actualizar_poblacion(paises):
    """Actualiza la población de un pais existente."""
    pais = pedir_pais(paises, "Ingresar el pais elegido: ")

    nueva_poblacion = pedir_entero("Ingrese la población a modificar: ", min=0)

    pais["poblacion"] = nueva_poblacion
    print(f"La población de {pais['nombre']} se actualizó a: {nueva_poblacion}")


def actualizar_superficie(paises):
    """Actualiza la superficie de un pais existente."""
    pais = pedir_pais(paises, "Ingresar el pais elegido: ")

    nueva_superficie = pedir_flotante("Ingrese la superficie a modificar: ", min=0)

    pais["superficie"] = nueva_superficie
    print(f"La superficie de {pais['nombre']} se actualizó a: {nueva_superficie} Km2")


def agregar_pais(paises):
    """Agrega un nuevo pais con validación de campos vacios, duplicados y continente."""
    while True:
        nombre = pedir_texto("Ingresar el pais elegido: ")
        pais = buscar_pais(paises, nombre)
        if pais is not None:
            print("El pais ya se encuentra en la base")
            continue
        break

    poblacion = pedir_entero("Ingrese la población: ", min=0)
    superficie = pedir_entero("Ingrese la superficie: ", min=0)
    continente = pedir_continente("Ingresa el continente: ")

    pais_a_agregar = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }

    paises.append(pais_a_agregar)
    print(
        f"Se agregó {pais_a_agregar['nombre']} - Población: {pais_a_agregar['poblacion']} - Superficie: {pais_a_agregar['superficie']} - Continente: {pais_a_agregar['continente']}"
    )


def filtro_por_continente(paises):
    """Muestra los paises que pertenecen al continente ingresado."""
    print("Continentes:")
    for continente in sorted(CONTINENTES):
        print("  - " + continente.title())

    continente = pedir_continente("Ingresa el continente a filtrar: ")

    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(f"{pais['nombre']}")


def filtro_por_poblacion(paises):
    """Filtra paises dentro de un rango de población (mínimo y máximo opcionales)."""
    poblacion_minima = pedir_entero_opcional(
        "Ingresa el número de población mínima: (Enter para omitir) "
    )
    poblacion_maxima = pedir_entero_opcional(
        "Ingresa el número de población máxima: (Enter para omitir) "
    )

    if poblacion_minima is None:
        poblacion_minima = 0
    if poblacion_maxima is None:
        poblacion_maxima = float("inf")

    if poblacion_minima > poblacion_maxima:
        print("Error: la población mínima no puede superar a la población máxima")
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
    """Filtra paises dentro de un rango de superficie (mínimo y máximo opcionales)."""
    superficie_minima = pedir_entero_opcional(
        "Ingresa el número de superficie mínima: (Enter para omitir) "
    )
    superficie_maxima = pedir_entero_opcional(
        "Ingresa el número de superficie máxima: (Enter para omitir) "
    )

    if superficie_minima is None:
        superficie_minima = 0
    if superficie_maxima is None:
        superficie_maxima = float("inf")

    if superficie_minima > superficie_maxima:
        print("Error: la superficie mínima no puede superar a la superficie máxima")
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


def cargar_datos():
    """Carga los paises desde el archivo CSV y convierte los tipos numéricos."""
    paises = []

    try:
        with open("base.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for pais in lector:
                pais["poblacion"] = int(pais["poblacion"])
                pais["superficie"] = int(float(pais["superficie"]))

                paises.append(pais)

    except FileNotFoundError:
        print("Error: No se encontró el dataset inicial.")
    except (ValueError, KeyError):
        print("Error: formato incorrecto en el CSV")

    return paises


def guardar_datos(paises):
    """Guarda la lista de paises en el archivo CSV."""
    try:
        columnas = ["nombre", "poblacion", "superficie", "continente"]
        with open("base.csv", "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(paises)

    except Exception as e:
        print(f"Error al guardar los datos: {e}")


def ordenar_paises(paises, clave, descendente=False):
    """Ordena la lista de paises por una clave (nombre/población/superficie)."""
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)


def listar_datos(datos, maximo_por_pagina=10):
    """Muestra los datos paginados de a 10 registros con opción de salir."""
    mostrados = 0
    total = len(datos)
    paginas = (total + maximo_por_pagina - 1) // maximo_por_pagina

    while mostrados < total:
        lote = datos[mostrados : mostrados + maximo_por_pagina]
        for i, pais in enumerate(lote, start=mostrados + 1):
            poblacion = formatear_numero(pais["poblacion"])
            superficie = formatear_numero(pais["superficie"])

            print(
                f"{i}. {pais['nombre']} ({pais['continente']}) - Población: {poblacion} - Superficie: {superficie} Km2"
            )

        print()

        mostrados += len(lote)
        if paginas > 1:
            print(f"Mostrados {mostrados} de {total} paises.")

        if mostrados >= total:
            break

        entrada = (
            input(f"Presione [Enter] para cargar más  [q] Salir → ").strip().lower()
        )

        if entrada == "q":
            break


def mostrar_mayor_poblacion(paises):
    """Muestra el pais con la población más alta."""
    if not paises:
        print("No hay datos cargados.")
        return

    pais_mayor = max(paises, key=lambda p: p["poblacion"])
    poblacion = formatear_numero(pais_mayor["poblacion"])

    print(f"País con mayor población: {pais_mayor['nombre']} - Población: {poblacion}")


def mostrar_menor_poblacion(paises):
    """Muestra el pais con la población más baja."""
    if not paises:
        print("No hay datos cargados.")
        return

    pais_menor = min(paises, key=lambda p: p["poblacion"])
    poblacion = formatear_numero(pais_menor["poblacion"])

    print(f"País con menor población: {pais_menor['nombre']} - Población: {poblacion}")


def mostrar_promedio_poblacion(paises):
    """Calcula y muestra el promedio de población entre todos los paises."""
    if not paises:
        print("No hay datos cargados.")
        return

    total_paises = len(paises)

    poblacion_total = 0

    for pais in paises:
        poblacion_total += pais["poblacion"]

    promedio = poblacion_total / total_paises
    promedio = formatear_numero(round(promedio))

    print(f"Población promedio: {promedio} habitantes por pais")


def mostrar_promedio_superficie(paises):
    """Calcula y muestra el promedio de superficie entre todos los paises."""
    if not paises:
        print("No hay datos cargados.")
        return

    total_paises = len(paises)

    superficie_total = 0

    for pais in paises:
        superficie_total += pais["superficie"]

    promedio = superficie_total / total_paises
    promedio = formatear_numero(promedio, 2)

    print(f"Superficie promedio: {promedio} Km2")


def mostrar_cantidad_por_continente(paises):
    """Muestra cuántos paises hay en cada continente."""
    continente_paises = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in continente_paises:
            continente_paises[continente] = 0
        continente_paises[continente] += 1

    for continente, paises_continente in continente_paises.items():
        print(f"\nContinente: {continente}")
        print(f"Cantidad de paises: {paises_continente}")


def main():
    """Bucle principal del programa: menú de opciones y ejecución de funcionalidades."""
    paises = cargar_datos()

    while True:

        print(f"""
{"~" * 60}
{"Menú".center(60)}
{"~" * 60}

1. Agregar pais
2. Actualizar datos

3. Listado de paises
4. Buscar pais por nombre

5. Filtrar paises

6. Estadísticas

7. Salir
""")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_pais(paises)
            guardar_datos(paises)

        elif opcion == "2":
            print("\n Opciones de actualización")
            print("1. Actualizar población")
            print("2. Actualizar superficie")
            print("3. Volver")

            sub_menu = pedir_entero("Seleccione una opción: ")

            if sub_menu == 1:
                actualizar_poblacion(paises)
                guardar_datos(paises)

            elif sub_menu == 2:
                actualizar_superficie(paises)
                guardar_datos(paises)

            elif sub_menu == 3:
                continue

            else:
                print("Error: ingresa alguna de las opciones disponibles")

        elif opcion == "3":
            print("\nListado de paises")
            print("Ordenar por: ")
            print("1. Nombre ")
            print("2. Población ")
            print("3. Superficie")
            print("4. Volver")

            sub_menu = pedir_entero("Seleccione una opción: ")

            if sub_menu == 1:
                print("1. Ascendente  \n2. Descendente ")
                orden = pedir_entero("Seleccione una opción: ")
                if orden == 1:
                    paises_ordenados = ordenar_paises(paises, "nombre")
                elif orden == 2:
                    paises_ordenados = ordenar_paises(paises, "nombre", True)
                else:
                    print("Opción inválida")
                    continue

            elif sub_menu == 2:
                print("1. Ascendente  \n2. Descendente ")
                orden = pedir_entero("Seleccione una opción: ")
                if orden == 1:
                    paises_ordenados = ordenar_paises(paises, "poblacion")
                elif orden == 2:
                    paises_ordenados = ordenar_paises(paises, "poblacion", True)
                else:
                    print("Opción inválida")
                    continue

            elif sub_menu == 3:
                print("1. Ascendente  \n2. Descendente ")
                orden = pedir_entero("Seleccione una opción: ")
                if orden == 1:
                    paises_ordenados = ordenar_paises(paises, "superficie")
                elif orden == 2:
                    paises_ordenados = ordenar_paises(paises, "superficie", True)
                else:
                    print("Opción inválida")
                    continue

            elif sub_menu == 4:
                continue

            else:
                print("Error: ingresa alguna de las opciones disponibles")
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

            print("\n Filtros")
            print("1. Filtrar por continente")
            print("2. Filtrar por población")
            print("3. Filtrar por superficie")
            print("4. Volver")

            sub_menu = pedir_entero("Seleccione una opción: ")

            if sub_menu == 1:
                filtro_por_continente(paises)
            elif sub_menu == 2:
                filtro_por_poblacion(paises)
            elif sub_menu == 3:
                filtro_por_superficie(paises)
            elif sub_menu == 4:
                continue
            else:
                print("Error: ingresa alguna de las opciones disponibles")

        elif opcion == "6":

            print("\n Estadísticas ")
            print("1. País con mayor población")
            print("2. País con menor población")
            print("3. Promedio de población")
            print("4. Promedio de superficie")
            print("5. Cantidad de paises por continente")
            print("6. Volver")

            sub_menu = pedir_entero("Seleccione una opción: ")

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

            elif sub_menu == 6:
                continue

            else:
                print("Error: ingresa alguna de las opciones disponibles")
                continue

        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor selecciona una opción del menú")


if __name__ == "__main__":
    main()
