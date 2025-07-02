# Crear un proyeto que permita gestionar (administrar) peliculas, colocar un menu de opciones
# para agregar, eliminar, modificar y consultar peliculas
# Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar dict para almacenar los siguientes atributos de peliculas (nombre, categoria, clasificacion, genero, idioma)


import peliculas

opcion = True
while opcion:
    print(
        "\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- U0001F4DDCrear  \n\t\t 2.- \U0001F4DB Borrar \n\t\t 3.- \U0001F50D Mostrar \n\t\t 4.- \U0001F4DD Agregar caracteristicas \n\t\t 5.- \U0001F501 Modificar caracteristicas \n\t\t 6.- \U0001F4DB Borrar caracteristicas \n\t\t 7.- \U0001F6AA SALIR "
    )
    opcion = input("\t\t\t Elige una opción: ").upper()

    peliculas.borrarpantalla()
    match opcion:
        case "1":
            print(".::\U0001F4DBAgregar Peliculas ::.")
            peliculas.crearPeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperartecla()
        case "3":
            peliculas.mostrarPeliculas()
            input("Oprima cualquier tecla para continuar ...")
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperartecla()
        case "5":
            peliculas.modificarCaracteristicasPeliculas()
            peliculas.esperartecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperartecla()
        case "7":
            opcion = False
            peliculas.borrarpantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            peliculas.borrarpantalla()
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")
