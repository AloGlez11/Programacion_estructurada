import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
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
    print( "\n\t\t .:: \U0001F4DD Sistema de Gestión de Agenda de Contactos \U0001F4DD:::...\n\t\t\t \u0031\uFE0F\u20E3  Agregar Contacto \n\t\t\t \u0032\uFE0F\u20E3  Mostrar todos los contactos \n\t\t\t \u0033\uFE0F\u20E3  Buscar contacto por nombre \n\t\t\t \u0034\uFE0F\u20E3  Modificar \n\t\t\t \u0035\uFE0F\u20E3  Eliminar agenda \n\t\t\t \u0036\uFE0F\u20E3  SALIR ")
    opcion = input("\n\t\t\t \U0001F449 Elige una opción (1-6): ").upper()
    return opcion

def agregar_contacto(agenda):
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t\t \U0001F4BE .::Agregar Contacto::. \U0001F4BE")
        agenda["nombre"] = input("Ingresa el nombre: ").upper().strip()
        cursor=conexion.cursor()
        sql="SELECT * FROM agenda WHERE nombre = %s"
        values=(agenda['nombre'],)
        cursor.execute(sql,values)
        registro=cursor.fetchone()
        if registro:
            print("\n\t\t El contacto ya existe...")
        else:
        #Agregar atributo "Nombre al diccionario con los valores telefono y email en una lista"
            agenda["telefono"] = input("Ingresa el telefono: ").upper().strip()
            agenda["correo"] = input("Ingresa el correo electronico: ").lower().strip()
            try:  
                cursor=conexion.cursor()
                sql="insert into agenda (nombre,telefono,correo) values (%s,%s,%s)"
                values=(agenda['nombre'], agenda['telefono'], agenda['correo'])
                cursor.execute(sql, values)
                conexion.commit()
                print("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
            except Error as e:
                print("\n\t\t \u26A0 Error al intentar conectar a la base de datos \u26A0")


def mostrar_contacto():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t\t \U0001F50D .::Mostrar contactos::. \U0001F50D")
        cursor=conexion.cursor()
        sql="SELECT * FROM agenda"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':>5}{'Nombre':>20}{'telefono':>20}{'Correo electronico':>20}")
            for contacto in registros:
                print(f"{contacto[0]:>5}{contacto[1]:>20}{contacto[2]:>20}{contacto[3]:>20}")
        else:
            print("\n\t.::No hay registros en el sistema")   

            
def buscar_contactos():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t\t \U0001F50D .::Buscar contacto::. \U0001F50D")
        try:
            cursor=conexion.cursor()
            nombre=input("Dame el nombre del contacto a buscar: ").upper().strip()
            sql="SELECT * FROM agenda WHERE nombre=%s"
            val=(nombre,)
            cursor.execute(sql,val)
            registros=cursor.fetchone()
            if registros:
                print(f"\n{'ID':>5}{'Nombre':>20}{'Teléfono':>20}{'Correo electrónico':>30}")
                print(f"{registros[0]:>5}{registros[1]:>20}{registros[2]:>20}{registros[3]:>30}")
            else:
                print("El contacto a buscar no se encuentra en el sistema")            
        except:
            print("\n\t\t \u26A0 Error al intentar conectar a la base de datos \u26A0")
            
            
def modificar_contactos(agenda):
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Modificar  contacto \U0001F50D ::.\n ")
        nombre=input("Dame el nombre del contacto a modificar: ").upper().strip()
        try:
            cursor=conexion.cursor()
            sql="SELECT * FROM agenda WHERE nombre=%s"
            val=(nombre,)
            cursor.execute(sql,val)
            registros=cursor.fetchone()
            if registros:
                print(f"\n{'ID':>5}{'Nombre':>20}{'Teléfono':>20}{'Correo electrónico':>30}")
                print(f"{registros[0]:>5}{registros[1]:>20}{registros[2]:>20}{registros[3]:>30}")
                resp=input(f"\n\t Deseas modificar el contacto de nombre: {nombre}? (si/no)").lower().strip()
                if resp=="si":
                    agenda["nombre"] = input("\nIngresa el nombre: ").upper().strip()
                    agenda["telefono"] = input("Ingresa el telefono: ").upper().strip()
                    agenda["correo"] = input("Ingresa el correo electronico: ").lower().strip()
                    sql="update agenda set nombre=%s,telefono=%s,correo=%s where nombre=%s"
                    val=(agenda["nombre"],agenda["telefono"],agenda["correo"],nombre)
                    cursor.execute(sql,val)
                    conexion.commit()
                    print(f"\n\t\t \u2705 El contacto {nombre} ha sido modificado correctamente \u2705")
            else:
                print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
        except:
            print("\n\t\t \u26A0 Error al intentar conectar a la base de datos\u26A0")


def eliminar_contacto():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Eliminar  contacto \U0001F50D ::.\n ")
        conta_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ").upper().strip()
        try:
            cursor=conexion.cursor()
            sql="SELECT * FROM agenda WHERE nombre=%s"
            val=(conta_eliminar,)
            cursor.execute(sql,val)
            registros=cursor.fetchone()
            if registros:
                print(f"\n{'ID':>5}{'Nombre':>20}{'Teléfono':>20}{'Correo electrónico':>30}")
                print(f"{registros[0]:>5}{registros[1]:>20}{registros[2]:>20}{registros[3]:>30}")
                resp=input(f"\n\t Deseas eliminar el contacto de nombre: {conta_eliminar}? (si/no)").lower().strip()
                if resp=="si":
                    sql="delete from agenda where nombre=%s"
                    val=(conta_eliminar,)
                    cursor.execute(sql,val)
                    conexion.commit()
                    print(f"\n\t\t \u2705 El contacto {conta_eliminar} ha sido modificado correctamente \u2705")
        except:
            print("\n\t\t \u26A0 Error al intentar conectar a la base de datos \u26A0")












                






