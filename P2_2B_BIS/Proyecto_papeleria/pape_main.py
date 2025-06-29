import papeleria

opcion = True

while opcion:
    print(
        "\n\t\t\t..::: \U0001f4dd PAPELERIA TIKIS\U0001f4dd :::.. \n\n\t\t..::: \U0001f4dd GESTION DE TAREAS\U0001f4dd :::..\n\t\t 1.- Agregar al inventario\U0001f4be \n\t\t 2.- Eliminar elemento\U0001f4db \n\t\t 3.- Mostrar inventario\U0001f6aa \n\t\t 4.- Buscar elemento\U0001f50d \n\t\t 5.- Vaciar\u274c \n\t\t 6.- Registrar ventas\U0001f4b0 \n\t\t 7.- Salir\U0001f6aa \n\n"
    )
    opcion = input("\t\t\t Elige una opción: ").upper()
    papeleria.borrarpantalla()
    match opcion:

        case "1":
            papeleria.borrarpantalla()
            papeleria.agregarinventario()
            papeleria.esperartecla()

        case "2":
            papeleria.borrarpantalla()
            papeleria.borrarelementoss()
            papeleria.esperartecla()

        case "3":
            papeleria.borrarpantalla()
            papeleria.consultarinventario()
            papeleria.esperartecla()

        case "4":
            papeleria.borrarpantalla()
            papeleria.buscarelemento()
            papeleria.esperartecla()

        case "5":
            papeleria.borrarpantalla()
            papeleria.vaciarinventario()
            papeleria.esperartecla()

        case "6":
            papeleria.borrarpantalla()
            papeleria.ventas()
            papeleria.esperartecla()

        case "7":
            opcion = False
            papeleria.borrarpantalla()
            print("\n\tVuelva pronto! ")

        case _:
            papeleria.borrarpantalla()
            input("\n\t\u26a0Opción invalida vuelva a intentarlo ... por favor")
