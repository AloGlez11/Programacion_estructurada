import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"Error en conexión:")
        return None

def borrarpantalla():
    import os
    os.system("cls")


def esperartecla():
    input("\n\t\t \U0001F552 Oprima cualquier tecla para continuar \U0001F552")

def menu_principal():
     print( "\n\t\t .:: \U0001F4DD Sistema de Gestión de Calificaciones \U0001F4DD:::...\n\t\t \U0001F4DD 1.- Agregar \n\t\t \U0001F50D 2.- Mostrar \n\t\t \U0001F9EE 3.- Calcular promedio \n\t\t \U0001F6AA 4.-SALIR ")
     opcion = input("\n\t\t \U0001F449 Elige una opción (1-4): ").upper()
     return opcion

def agregar_calificaciones():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t\t \U0001F4DD Agregar Calificaciones \U0001F4DD")
        nombre = input("\U0001F464 Nombre del Alumno: ").upper().strip()
        calificaciones = []
        for i in range(1,4):
            continua = True
            while continua:
                try:
                    cal = round(float(input(f"Calificación {i}: ")), 2)
                    if cal >= 0 and cal < 11:
                        calificaciones.append(cal)
                        continua = False
                    else:
                        print("\n\t\t \u274C Ingresa un numero valido \u274C")
                except ValueError:
                    print("n\t\t \u274C Ingresa un valor numerico \u274C")
        try:  
            cursor = conexion.cursor()
            sql = "insert into calificaciones (nombre,calificacion1,calificacion2,calificacion3) values (%s,%s,%s,%s)"
            values = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
            cursor.execute(sql, values)
            conexion.commit()
            print("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
        except Error as e:
            print("\n\t\t \u26A0 Error al intentar conectar a la base de datos \u26A0")
    print("\n\t\t \u2705 Accion realizada con exito \u2705")

def mostrar_calificaciones():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t\t ::. \U0001F50D Mostrar calificaciones \U0001F50D ::.")
        try:
            cursor=conexion.cursor()
            sql="SELECT * FROM calificaciones"
            cursor.execute(sql)
            registros=cursor.fetchall()
            if registros:
                print(f"{'ID':>5} {'Nombre':<20} {'Calificación 1':>15} {'Calificación 2':>15} {'Calificación 3':>15}")
                print("-" * 95)
                for alumno in registros:
                    if alumno[5]!=None:
                        print(f"{alumno[0]:>5} {alumno[1]:<20} {alumno[2]:>15} {alumno[3]:>15} {alumno[4]:>15}")
                    else:
                        print(f"{alumno[0]:>5} {alumno[1]:<20} {alumno[2]:>15} {alumno[3]:>15} {alumno[4]:>15}")
            else:
                print("\n\t.:: \u26A0 No hay registros en el sistema \u26A0")   
        except:
            print("\n\t\t \u26A0 Error al intentar conectar a la base de datos \u26A0")    


def calcular_promedio():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t\t \U0001F9EE Calcular Promedio \U0001F9EE")
        print("\n\t\t ::. \U0001F50D Mostrar calificaciones \U0001F50D ::.")
        try:
            cursor=conexion.cursor()
            sql="SELECT * FROM calificaciones"
            cursor.execute(sql)
            registros=cursor.fetchall()
            if registros:
                print(f"{'ID':<5} {'Nombre':<25} {'Promedio':<10}")
                for alumno in registros:
                    promedio = round((alumno[2] + alumno[3] + alumno[4]) / 3, 2)
                    sql = "UPDATE calificaciones SET promedio = %s WHERE id = %s"
                    values = (promedio, alumno[0])
                    cursor.execute(sql, values)
                    conexion.commit()
                    print(f"{alumno[0]:<5} {alumno[1]:<25} {promedio:<10}")
            else:
                print("\n\t.:: \u26A0 No hay registros en el sistema \u26A0")   
        except:
            print("\u26A0 Error al intentar conectar a la base de datos \u26A0") 

        