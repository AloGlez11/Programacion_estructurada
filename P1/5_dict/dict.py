'''

dict.
 Es un tipo de datos que se utiliza para almacenar datos de diferentes tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir, es algo parecido como los Objetos
 
 Tambien se conoce como un arreglo asosiativo u objeto JSON

 El diccionario es una coleccion ordenada y modificable. No hay miembros duplicados
 '''

import os
os.system("cls")

#Lista
#paises=["Mexico","Brasil","Canada","España"]

#diccionario u objeto
pais_mexico={
    "nombre":"Mexico",
    "capital":"CDMX",
    "Poblacion":12000000,
    "Idioma":"Español",
    "Status":True
    }

pais_brasil={
    "nombre":"Brasil",
    "capital":"Brasilia",
    "Poblacion":100000000,
    "Idioma":"portuges",
    "Status":True
    }

paises_canada={
    "nombre":"Canada",
    "capital":"Ottawa",
    "poblacion":9000000,
    "idioma":["ingles","Frances"],
    "status":False
    }

alumno1={
    "nombre":"Diego",
    "apellido_paterno":"Guevara",
    "apellido_materno":"de Leon",
    "aspecialidad":"TI",
    "matricula":"31783115",
    "area":"software mulriplataforma",
    "modalidad":"bilingue",
    "semestre":"2"
}

print(alumno1)

for i in alumno1:
    print(f"{i}={alumno1[i]}")

#Agregar un campo o atributo
alumno1["telefono"]="618732783"

for i in alumno1:
    print(f"{i}={alumno1[i]}")