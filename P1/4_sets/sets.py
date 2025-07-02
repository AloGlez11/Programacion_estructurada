'''


Sets.-
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden
  
  Set es una coleccion desordenada, inmutable y no indexada. No hay miembros duplicados
'''
import os
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios={3,12,3,True,"Hola"}
print(varios)


#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

os.system("cls")
opc="si"
emails=[]
while opc=="si":
    emails.append(input("Dame el email: "))
    #print(emails)
    opc=input("Deseas solicitar otro email (si/no)").lower()

#Imprimir los email sin duplicados
print(emails)
set1=set(emails)
print(set1)
emails=list(set1)
print=(emails)





