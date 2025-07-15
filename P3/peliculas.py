import mysql.connector
from mysql.connector import Error

#DICT U OBJETO para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

#            "nombre":"",
#           "categoria":"",
#            "clasificacion":"",
#            "genero":"idioma",
#            }
            
pelicula={}

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None
    

def borrarpantalla():
    import os
    os.system("cls")
        


def esperartecla():
    input("\t Oprima cualquier tecla para continuar ...")


def crearPeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.::\U0001F4DD Alta de Peliculas \U0001F4DD::. ")
        pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
        pelicula.update({"categoria": input("Ingresa la categoria: ").upper().strip()})
        pelicula.update({"clasificacion": input("Ingresa la clasificacion: ").upper().strip()})
        pelicula.update({"genero": input("Ingresa el genero: ").upper().strip()})
        pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})

        #AGREGAR REGISTRO A LA BASE DE DATOS
        try:
            cursor=conexion.cursor()
            sql="INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s,%s,%s,%s,%s)"
            values = (pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        
            cursor.execute(sql, values)
            conexion.commit()
            print("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
        except Error as e:
            print("Error al intentar conectar a la base de datos")
                
        

def eliminarPeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t .::\U0001F4DB Borrar o Quitar TODAS las Peliculas \U0001F4DB::. \n")
        resp=input("\U0001F4DBDeseas quitar o borrar todas las peliculas del sistema? (Si/No): ").lower()
        if resp=="si":
            conexion=conectar()
            cursor=conexion.cursor()
            sql="DELETE FROM peliculas"
            cursor.execute(sql)
            conexion.commit()
            input("\n\t\t ::: \u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")

def mostrarPeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        sql="SELECT * FROM peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\t .::Mostrar peliculas::.")
            print(f"{'ID':>10}{'Nombre':>15}{'Categoria':>15}{'Clasificacion':>15}{'Genero':>15}{'Idioma':>15}")
            for pelicula in registros:
                print("-"*90)
                print(f"{pelicula[0]:>10}{pelicula[1]:>15}{pelicula[2]:>15}{pelicula[3]:>15}{pelicula[4]:>15}{pelicula[5]:>15}")
        else:
            print("\n\t.::No hay registros en el sistema")   

def modificarPeliculas():
  borrarpantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: \U0001F50D Buscar  Pelicula \U0001F50D ::.\n ")
    nombre=input("Dame el nombre de la pelicula a modificar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="SELECT * FROM peliculas WHERE nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<25}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)  
        resp=input(f"Deseas modifcar la pelicula de nombre {nombre}? (si/no)").lower().strip()
        if resp=="si":
          pelicula['nombre']=input("\U0001F4DD nombre: ").upper().strip()
          pelicula["categoria"]=input("\U0001F4DD categoría: ").upper().strip()
          pelicula["clasificacion"]=input("\U0001F4DD clasificación: ").upper().strip()
          pelicula["genero"]=input("\U0001F4DD genero: ").upper().strip()
          pelicula["idioma"]=input("\U0001F4DD idioma: ").upper().strip()
          sql="update peliculas  set nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s where nombre=%s"
          val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"],nombre)
          cursor.execute(sql,val)
          conexionBD.commit()
          print(f"La pelicula {nombre} ha sido modificada correctamente del proyecto")

    else:
       print("\t .:: \u26A0 Esta pelicula/s no se encuentra \u26A0 ::.")
        
def borrarPeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Eliminar una Pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        nombre=input("Dame el nombre de la pelicula a eliminar: ").upper().strip()
        sql="SELECT * FROM peliculas WHERE nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':>10}{'Nombre':>15}{'Categoria':>15}{'Clasificacion':>15}{'Genero':>15}{'Idioma':>15}")
            for pelicula in registros:
                print("-"*90)
                print(f"{pelicula[0]:>10}{pelicula[1]:>15}{pelicula[2]:>15}{pelicula[3]:>15}{pelicula[4]:>15}{pelicula[5]:>15}")
            resp=input(f"Deseas borrar la pelicula de {nombre}? (Si/No)").lower().strip()    
            if resp=="si":
                sql="delete from peliculas where nombre=%s"      
                val=(nombre,)
                cursor.execute(sql,val)
                conexion.commit()
                print("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")
        else:
            print("\n\t\t La pelicula a borrar no se encuentra en el sistema")
                
                
                
def buscarPeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Buscar una pelicula o Mostrar la Pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
        sql="SELECT * FROM peliculas WHERE nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\t .::Mostrar peliculas::.")
            print(f"{'ID':>10}{'Nombre':>15}{'Categoria':>15}{'Clasificacion':>15}{'Genero':>15}{'Idioma':>15}")
            for pelicula in registros:
                print("-"*90)
                print(f"{pelicula[0]:>10}{pelicula[1]:>15}{pelicula[2]:>15}{pelicula[3]:>15}{pelicula[4]:>15}{pelicula[5]:>15}")
        else:
            print("\n\t.::La pelicula a buscar no se encuentra en el sistema")   
