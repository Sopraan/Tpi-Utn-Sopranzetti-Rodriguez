import csv

paises=[]

with open("base.csv","r",encoding="utf-8") as archivo:
    lector=csv.DictReader(archivo)
    for pais in lector:
        paises.append(pais)
   

