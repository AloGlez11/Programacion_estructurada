#Proyecto 3
#Crear un proyecto que permita gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante

#NOTAS:
#1-.Utilizar funciones y maandar llamar desde otro archivo (modulos)
#2-.Utilizar una lista bidimensional para almacenar el nombre del estudiante y sus tres calificaciones.

import calificaciones

def main():
    datos=[]

    import calificaciones

def main():
    datos = []
    opcion = True

    while opcion:
        calificaciones.borrarpantalla()
        opcion = calificaciones.menu_principal() 
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperartecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperartecla()
            case "3":
                calificaciones.calcular_promedio(datos)
                calificaciones.esperartecla()
            case "4":
                calificaciones.borrarpantalla()
                print("\n\tTerminaste la ejecución del SW")
                opcion = False 
            case _:
                calificaciones.borrarpantalla()
                input("\n\tOpción inválida, vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()