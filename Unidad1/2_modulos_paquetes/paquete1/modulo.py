'''Un modulo es simplemente un archivo con extension .py que contiene codigo de python (funciones, clases, variables, etc.).

#Un paquete es una carpeta que contiene varios modulos (archivos .py) y un archivo especial llamado _init_.py que le indica a python que esa carpeta debe tratarse como un paquete.
'''

import os

# 1.- Funcion que no recibe parametros y no regresa valor
def SolicitarDatos1():
    nombre=input("nombre:")
    tel=input("Telefono:")
    print(f"Soy la funcion 1. El nombre es: {nombre} y su telefono es: {tel}")

#3.- Funcion que recibe parametros y no regresa valor
def SolicitarDatos3(nombre,tel):
    nombre=nombre
    tel=tel
    print(f"Soy la funcion 2. El nombre es: {nombre} y su telefono es: {tel}")

#2.- Funcion que no recibe parametros y regresa valor
def SolicitarDatos2():
    nombre=input("nombre: ")
    tel=input("Telefono:")
    return nombre,tel

# 4.- Funcion que recibe parametros y regresa valor
def SolicitarDatos4(nombre,tel):
    nombre=nombre
    tel=tel
    return nombre,tel

def borrarpantalla():
    os.system("cls")

def espereTecla():
    input("...Espere tecla para continuar...")

def saludar(nombre):
    nom=nombre
    return f"\tHola, bienvenido {nom}!\n"