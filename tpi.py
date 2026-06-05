import csv
#Validacion espacios en blanco al ingreso de los paises
def validacion_paises():
    while True:

        consulta_pais=input("Ingresar el pais elegido: ").strip()
        if consulta_pais == "":
            print("Error: nose pueden deja el campor vacio")
            continue    
        break
    return consulta_pais

#busqueda rapida de paises en csv
def buscar_pais(paises,nombre):
    for pais in paises:
        if pais["nombre"].lower()==nombre.lower():
            return pais
        return None


#se ustilizan funciones de validacion, busqueda y se modifica poblacion
def actualizar_Poblacion():

    while True:
        consulta_pais=validacion_paises()
        pais=buscar_pais(paises,consulta_pais)
        if pais is None:
            print("Pais no encontrado")
            continue
        break

    while True:
        try:
            nueva_Poblacion=int(input("Ingesa la poblacion a modificar: "))
            break
        except ValueError:
            print("Error: ingresa un numero entero")
        
    pais["poblacion"]=nueva_Poblacion
    print(f"La polbacion de {pais['nombre']} se actualizo a : {nueva_Poblacion}")
    
#se ustilizan funciones de validacion, busqueda y se modifica Superficie
def actualizar_Superficie():

    while True:
        consulta_pais=validacion_paises()
        pais=buscar_pais(paises,consulta_pais)
        if pais is None:
            print("Pais no encontrado")
            continue
        break

    while True:
        try:
            nueva_Superficie=float(input("Ingesa la superficie a modificar: "))
            break
        except ValueError:
            print("Error: ingresa un numero")
        
    pais["superficie"]=nueva_Superficie
    print(f"La superficie de {pais['nombre']} se actualizo a : {nueva_Superficie} Km2")


##se ustilizan funciones de validacion, busqueda, se implemento el agregar paises con su diccionarios
def agregar_pais():

    while True:
        nombre=validacion_paises()
        pais=buscar_pais(paises,nombre)
        if pais is not None:
            print("El pais ya se encuentra en la base")
            continue
        break

    while True:
        try:
            poblacion=int(input("ingresa la poblacion: "))
            break
        except ValueError:
            print("Error: no se pueden ingresar letras ni espacios vacios")

    while True:
        try:
            superficie=float(input("Ingresa la superficie: "))
            break
        except ValueError:
            print("Error: no se pueden ingresar letras ni espacios vacios")

    while True:
    
        continente=validacion_paises()
        if not continente.isalpha():
            print("Error: Ingresa solamente letras")
            continue
        break
#Se agrega el diccionario del nuevopais
    pais_a_agregar={
        "nombre":nombre,
        "poblacion":poblacion,
        "superficie":superficie,
        "continente":continente
    }

    paises.append(pais_a_agregar)
    print(f"se agrego {pais_a_agregar} a la base")

paises = []


#Lector de arvhivos csv
with open("base.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for pais in lector:
        paises.append(pais)


actualizar_Poblacion()
actualizar_Superficie()
agregar_pais()
