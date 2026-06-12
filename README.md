# Trabajo Práctico Integrador - Programación 1

**Gestión de datos de paises**

Sistema en Python para gestionar información de países con operaciones de filtrado, ordenamiento y estadísticas. Trabajo Práctico Integrador de Programación 1 — UTN.


## Instalación y uso

```bash
git clone https://github.com/Sopraan/Tpi-Utn-Sopranzetti-Rodriguez.git
cd Tpi-Utn-Sopranzetti-Rodriguez
python3 tpi.py
```

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Agregar un país (valida duplicados, campos vacíos y continente) |
| 2 | Actualizar población o superficie de un país |
| 3 | Listar países ordenados por nombre, población o superficie (asc/desc) |
| 4 | Buscar país por nombre (coincidencia parcial) |
| 5 | Filtrar por continente, rango de población o rango de superficie |
| 6 | Estadísticas: mayor/menor población, promedios, cantidad por continente |
| 7 | Salir |

## Estructura del dataset

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
```

Los datos se cargan desde `base.csv` y se guardan automáticamente al agregar o actualizar.

## Ejemplos

**Agregar un país:**
```
Selecciona una opcion: 1
Ingresar el pais elegido: Uruguay
Ingrese la poblacion: 3500000
Ingrese la superficie: 176215
Ingresa el continente: america
Se agrego Uruguay - Poblacion: 3.500.000 - Superficie: 176.215 - Continente: america
```

**Ordenar países:**
```
Selecciona una opcion: 3

Ordenar por:
1. Nombre
2. Poblacion
3. Superficie
4. Volver
Seleccione una opcion: 2
Ordena por: 
1. Ascendente  
2. Descendente
```

**Filtrar por continente:**
```
Selecciona una opcion: 5
Filtros
1. Filtrar por continente
2. Filtrar por poblacion
3. Filtrar por superficie
4. Volver
Seleccione una opcion: 1
Continentes: Africa, America, Asia, Europa, Oceania
Ingresa el continente a filtrar: africa
```

## Integrantes

- Tomas Sopranzetti
- Nicolás Rodriguez

## Enlaces

- PDF: *[pendiente]*
- Video: *[pendiente]*
