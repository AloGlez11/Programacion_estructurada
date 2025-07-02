
'''
un modulo es simplemente un archivos con extension .py que contiene codigo python (funciones, clases, variables, etc)
 que puede ser reutilizado en otros archivos.
 
 un paquete es una carpeta que contiene uno o mas modulos (archivos .py) y un archivo __init__.py que indica a python que
 la carpeta es un paquete.
'''

def borrar_pantalla():
    import os
    os.system("cls")

def esperar_tecla():
    input("Presiona una tecla para continuar...")

def saludar(nombre):
    return (f"Hola, bienvenido {nombre}")
    
    
#funcion que no recibe parametros y no regresa valor
def solicitar_datos1():
    nombre = input("¿Cual es tu nombre? ")
    telefono = input("¿Cual es tu telefono? ")
    print(f"Hola {nombre}, tu telefono es {telefono}")

#funcion que no recibe parametros y regresa valor
def solicitar_datos2():
    nombre = input("¿Cual es tu nombre? ")
    telefono = input("¿Cual es tu telefono? ")
    return nombre, telefono

#funcion que recibe parametros y no regresa valor
def solicitar_datos3(nombre, telefono):
    nombre=nombre
    telefono=telefono
    print(f"Hola {nombre}, tu telefono es {telefono}")

#funcion que recibe parametros y regresa valor
def solicitar_datos4(nombre, telefono):
    nom=nombre
    tel=telefono
    return nom, tel