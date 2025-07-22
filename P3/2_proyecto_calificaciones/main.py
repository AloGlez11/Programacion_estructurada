import calificaciones


def main():
    opcion = True

    while opcion:
        calificaciones.borrarpantalla()
        opcion = calificaciones.menu_principal() 
        match opcion:
            case "1":
                calificaciones.agregar_calificaciones()
                calificaciones.esperartecla()
            case "2":
                calificaciones.mostrar_calificaciones()
                calificaciones.esperartecla()
            case "3":
                calificaciones.calcular_promedio()
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