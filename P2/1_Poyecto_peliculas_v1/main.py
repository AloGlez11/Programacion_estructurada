# Crear un proyeto que permita gestionar (administrar) peliculas, colocar un menu de opciones
# para agregar, eliminar, modificar y consultar peliculas
# Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas


import peliculas
opcion=True
while opcion:
    peliculas.borrar_pantalla()
    print("\n\t\t\t..::CINEPOLIS CLON::..\n\t\t..:::Sistema de Gestión De Películas :::....\n\t\t 1.-Agregar\n\t\t 2.-Eliminar\n\t\t 3.-Actualizar\n\t\t 4.-Consultar\n\t\t 5.-Buscar\n\t\t 6.-Vaciar\n\t\t 7.-SALIR")
    pregunta=input("\tSeleccione una opcion: ")

    match pregunta:
        case "1":
            peliculas.agregar()
            peliculas.esperar_tecla()
        case "2":
            peliculas.eliminar()
            peliculas.esperar_tecla()
        case "3":
            peliculas.actualizar_peliculas()
            peliculas.esperar_tecla()
        case "4":
            peliculas.consultar()
            peliculas.esperar_tecla()
        case "5":
            peliculas.buscar_peliculas()
            peliculas.esperar_tecla()

        case "6":
            peliculas.vaciar_peliculas()
            peliculas.esperar_tecla()

        case "7":
            opcion=False
            peliculas.borrar_pantalla()
            print("\n\t Terminaste la ejecusion del sw")
        case _:
            input("\n\t Opcion invalida vuelva a intentar...")
      
