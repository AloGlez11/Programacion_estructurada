
import agenda

def main():
    agenda_contactos = {}
    opcion = True

    while opcion:
        agenda.borrarpantalla()
        opcion = agenda.menu_principal() 
        match opcion:
            case "1":
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperartecla()
            case "2":
                agenda.mostrar_contacto()
                agenda.esperartecla()
            case "3":
                agenda.buscar_contactos()
                agenda.esperartecla()
            case "4":
                agenda.modificar_contactos(agenda_contactos)
                agenda.esperartecla()
            case "5":
                agenda.eliminar_contacto()
                agenda.esperartecla()
            case "6":
                agenda.borrarpantalla()
                print("\n\tTerminaste la ejecución del SW")
                opcion = False 
            case _:
                agenda.borrarpantalla()
                input("\n\tOpción inválida, vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()

