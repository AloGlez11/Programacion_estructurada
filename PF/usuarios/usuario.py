from conexion_BD import Conectar_BD
import hashlib
from mysql.connector import Error

def registrar_usuario(registros: dict):
    try:
        registros["contrasena"]= hashlib.sha256(registros["contrasena"].encode()).hexdigest()
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        sql_checar = "select correo_electronico from usuarios where correo_electronico = %s"
        cursor.execute(sql_checar, (registros["email"],))
        duplicado = cursor.fetchone() 
        if duplicado:
            return False
        consulta = """insert into usuarios (nombre, apellido, correo_electronico, contrasena, numero_celular) values (%s, %s, %s, %s, %s)"""
        valores = (
            registros["nombre"], 
            registros["apellidos"], 
            registros["email"],
            registros["contrasena"], 
            registros["telefono"]
        )
        cursor.execute(consulta, valores)
        conexion.commit()
        print("\n\t \u2705 Usuario registrado correctamente \u2705")
        return True
    except:
        print("\n\t \u26A0 Error al intentar conectar con la base de datos...")
        return None
        

def iniciar_sesion(correo,contrasena):
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        sql="select * from usuarios where correo_electronico=%s and contrasena=%s"
        val=(correo,contrasena)
        cursor.execute(sql,val)
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        print("\n\t \u26A0 Error al intentar conectar con la base de datos...")
