import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente con el email: {email}")
            else:
                print(f"\n\t Por favor intentelo de nuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            registro=usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas, vuelva a intentarlo")
                funciones.esperarTecla() 
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"\n\t Se creo la nota: {titulo} exitosamente")
            else:
                print("\n\t No fue posible crear la nota en este momentos, vuelve a intentar...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print("\n\t Mostrar las Notas")
                print(f"{'ID':>5}{'Titulo':>35}{'Descripcion':>35}  {'Fecha'}")
                for fila in lista_notas:
                    print("-"*90)
                    print(f"{fila[0]:>5}{fila[2]:>35}{fila[3]:>35}  {fila[4]}")
            else:
                print(f"\n\t No existen notas de acuerdo al usuario")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            lista=nota.mostrar(usuario_id)
            if len(lista)>0:
                print("\n\t Mostrar las Notas")
                print(f"{'ID':>5}{'Titulo':>35}{'Descripcion':>35}    {'Fecha'}")
                for fila in lista:
                    print("-"*90)
                    print(f"{fila[0]:>5}{fila[2]:>35}{fila[3]:>35}     {fila[4]}")
                print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una Nota ::. \n")
                id = input("\t \t ID de la nota a actualizar: ")
                verificacion=nota.verificar(id)
                if verificacion:
                    resp=input("\n\t Estas seguro que deseas modificar la nota? (si/no): ").lower().strip()
                    if resp=="si":
                        titulo = input("\t Nuevo título: ")
                        descripcion = input("\t Nueva descripción: ")
                        respuesta=nota.cambiar(id,titulo,descripcion)
                        if respuesta:
                            print(f"\n\t\t Se modifico la nota de titulo: {titulo}")   
                        else:
                            print("\n\t No fue posible actualizar la nota en este momentos, vuelve a intentar...")
                elif verificacion==None:
                    print(f"\n\t No existe una nota con el id : {id}")
                else:
                    print("\n\t No fue posible actualizar la nota en este momentos, vuelve a intentar...")
            else:
                print(f"\n\t No existen notas de acuerdo al usuario")
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            lista=nota.mostrar(usuario_id)
            if len(lista)>0:
                print("\n\t Mostrar las Notas")
                print(f"{'ID':>5}{'Titulo':>35}{'Descripcion':>35}    {'Fecha'}")
                for fila in lista:
                    print("-"*90)
                    print(f"{fila[0]:>5}{fila[2]:>35}{fila[3]:>35}     {fila[4]}")
                print(f"\n \t .:: {nombre} {apellidos}, vamos a eliminar una Nota ::. \n")
                id = input("\t \t ID de la nota a eliminar: ")
                    #Agregar codigo
                verificacion=nota.verificar(id)
                if verificacion:
                    resp=input("\n\t Estas seguro que deseas eliminar la nota? (si/no): ").lower().strip()
                    if resp=="si":
                        respuesta=nota.borrar(id)
                        if respuesta:
                            print(f"\n\t\t Se elimino la nota con id: {id}")
                        else:
                            print("\n\t No fue posible actualizar la nota en este momentos, vuelve a intentar...")
                elif verificacion==None:
                    print(f"\n\t No existe una nota con el id : {id}")
                else:
                    print("\n\t No fue posible actualizar la nota en este momentos, vuelve a intentar...")
            else:
                print(f"\n\t No existen notas de acuerdo al usuario")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


