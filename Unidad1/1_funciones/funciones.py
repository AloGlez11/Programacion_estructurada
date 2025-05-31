'''
Una funcion es un conjunto de intrucciones agrupadas bajo un nombre en particular como un porgrama mas pequeño que cumple una funcion especifica. La funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar

sintaxis:

    def nombredeMifuncion(parametros):
        bloque o conjunto de instrucciones

    nombredeMifuncion(paramatros)

    Las funciones pueden ser de 4 tipos

         Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor
        '''

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
    nombre=input("nombre")
    tel=input("Telefono:")
    return nombre,tel

# 4.- Funcion que recibe parametros y regresa valor
def SolicitarDatos4(nombre,tel):
    nombre=nombre
    tel=tel
    return nombre,tel

#Llamar mis funciones
SolicitarDatos1()

nom3=input("nombre")
tel3=input("Telefono:")
SolicitarDatos3(nom3,tel3)

nom2,tel2=SolicitarDatos2()
print(f"Nombre: {nom2} \n Telefono {tel2}")

nom4=input("nombre")
tel4=input("Telefono:")
nombre4,telefono4=SolicitarDatos3(nom4,tel4)
print(f"Nombre {nombre4} \n Telefono {telefono4}")