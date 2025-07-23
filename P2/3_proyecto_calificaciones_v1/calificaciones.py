def borrarpantalla():
    import os
    os.system("cls")


def esperartecla():
    input("\n\t\t \U0001F552 Oprima cualquier tecla para continuar \U0001F552")

def menu_principal():
     print( "\n\t\t .:: \U0001F4DD Sistema de Gestión de Calificaciones \U0001F4DD:::...\n\t\t \U0001F4DD 1.- Agregar \n\t\t \U0001F50D 2.- Mostrar \n\t\t \U0001F9EE 3.- Calcular promedio \n\t\t \U0001F6AA 4.-SALIR ")
     opcion = input("\n\t\t \U0001F449 Elige una opción (1-4): ").upper()
     return opcion

def agregar_calificaciones(lista):
    borrarpantalla()
    print("\n\t\t \U0001F4DD Agregar Calificaciones \U0001F4DD")
    nombre=input("\U0001F464 Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"Calificacion {i}:  "))
                if cal>=0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\n\t\t \u274C Ingresa un numero valido \u274C")
            except ValueError:
                print("n\t\t \u274C Ingresa un valor numerico \u274C")
    lista.append([nombre]+calificaciones)   
    print("\n\t\t \u2705 Accion realizada con exito \u2705")

def mostrar_calificaciones(lista):
    borrarpantalla()
    print("\n\t\t \U0001F9FE Mostrar calificaciones \U0001F9FE")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calf 1':<10}{'Calf 2':<10}{'Calf 3':<10}")
        print(f"{'-'*40}")
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*40}")
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("\n\t\t \u274C No hay calificaciones registradas en el sistema \u274C")


def calcular_promedio(lista):
    borrarpantalla()
    print("\n\t\t \U0001F9EE Calcular Promedio \U0001F9EE")
    if len(lista)>0:
        print(f"{'Estuadiante':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"{nombre:<15}{promedio:.2}")
            promedio_grupal+=promedio
        print(f"{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
    else:
        print("\n\t\t \u274C No hay calificaciones guardadas en el sistema \u274C")

        