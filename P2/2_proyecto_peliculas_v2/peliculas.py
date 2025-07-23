
peliculas = []

#DICT U OBJETO para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

#            "nombre":"",
#           "categoria":"",
#            "clasificacion":"",
#            "genero":"idioma",
#            }

pelicula={}

def borrarpantalla():
    import os
    os.system("cls")


def esperartecla():
    input("\t Oprima cualquier tecla para continuar ...")


def crearPeliculas():
    borrarpantalla()
    print("\n\t.::\U0001F4DD Alta de Peliculas \U0001F4DD::. ")
    pelicula.update({"nombre":input("Ingresa el nombre: ".upper().strip())}) 
    pelicula.update({"categoria":input("Ingresa la categoria: ".upper().strip())}) 
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ".upper().strip())}) 
    pelicula.update({"genero":input("Ingresa el genero: ".upper().strip())}) 
    pelicula.update({"idioma":input("Ingresa el idioma: ".upper().strip())}) 
    input("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")

def borrarPeliculas():
   borrarpantalla()
   print("\n\t .::\U0001F4DB Borrar o Quitar TODAS las Peliculas \U0001F4DB::. \n")
   resp=input("\U0001F4DBDeseas quitar o borrar todas las peliculas del sistema? (Si/No): ").lower()
   if resp=="si":
       pelicula.clear()
       input("\n\t\t ::: \u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")

def mostrarPeliculas():
    borrarpantalla()
    print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D::. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t{(i)} : {pelicula[i]}")
    else:
        print("\t \u26A0 No hay peliculas en el sistema \u26A0")

def agregarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t .:: \U0001F4DD Agregar Caracteristica a Peliculas \U0001F4DD::.\n")
    atributo=input("Ingresa la nueva caracteristica de la Pelicula: ").lower().strip()
    valor=input("\U0001F4DD Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    pelicula.update({atributo:valor})

def modificarCaracteristicasPeliculas():
    borrarpantalla()
    print("\n\t .::\U0001F501 Modificar Caracteristicas a Peliculas \U0001F501::.\n")
    if len(pelicula) > 0:
        print(f"\n\t Valores actuales: ")
        for i in pelicula:
            print(f"\t {i} : {pelicula[i]}")
            resp=input(f"\t Deseas cambiar el valor de {i}? (Si/No) ")
            if resp=="si":
                pelicula.update({f"{i}":input("\t \U0001F501 el nuevo valor: ").upper().strip()})
                print("\n\t\t .:: \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705::.")
                esperartecla()
                borrarpantalla()
    else:
        print("\t .:: \u26A0 No hay peliculas en Sistema \u26A0 ::.")
        esperartecla()

def borrarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t .:: \U0001F4DB Borrar caracteristica de pelicula \U0001F4DB ::.\n")
    if len(pelicula)>0:
        print(f"\n\t Valores actuales: ")
        for i in pelicula:
            print(f"\t {(i)} : {pelicula[i]}")
        resp=input(f"\t¿Deseas borrar una caracteristica? (Si/No) ")
        if resp=="si":
            atributo=input("Escribe la caracteristica que deseas borrar o quitar: ").lower().strip()
            try:
                pelicula.pop(atributo)
                print("\n\t\t .:: \u2705 ¡LA OPERACION SE REALIZO CON EXITO! \u2705::.")
            except KeyError:
                print(f"\n\t \u26A0 La característica '{atributo}' no existe, pruebe con alguna que se muestra anteriormente")
            esperartecla()
            borrarpantalla()
    else:
        print("\t.::\u27A0 No hay peliculas en Sistema \u26A0::.")
        esperartecla()


