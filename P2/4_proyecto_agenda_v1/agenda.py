def borrarpantalla():
    import os
    os.system("cls")


def esperartecla():
    input("\n\t\t \U0001F552 Oprima cualquier tecla para continuar \U0001F552")

def menu_principal():
    print( "\n\t\t .:: \U0001F4DD Sistema de Gestión de Agenda de Contactos \U0001F4DD:::...\n\t\t\t \u0031\uFE0F\u20E3  Agregar Contacto \n\t\t\t \u0032\uFE0F\u20E3  Mostrar todos los contactos \n\t\t\t \u0033\uFE0F\u20E3  Buscar contacto por nombre \n\t\t\t \u0034\uFE0F\u20E3  Modificar \n\t\t\t \u0035\uFE0F\u20E3  Eliminar agenda \n\t\t\t \u0036\uFE0F\u20E3  SALIR ")
    opcion = input("\n\t\t\t \U0001F449 Elige una opción (1-6): ").upper()
    return opcion

def agregar_contacto(agenda):
    borrarpantalla()
    print("\n\t\t \U0001F4BE .::Agregar Contacto::. \U0001F4BE")
    nombre=input("Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t\t El contacto ya existe...")
    else:
        tel=input("Telefono: ").strip()
        email=input("Email: ").lower().strip()
        #Agregar atributo "Nombre al diccionario con los valores telefono y email en una lista"
        agenda[nombre]=[tel,email]
        print("\n\t\t \u2705 .::Accion realizada con exito!::.\u2705")

def mostrar_contacto(agenda):
    borrarpantalla()
    print("\n\t\t \U0001F50D .::Mostrar contatactos::. \U0001F50D")
    if not agenda:
        print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
    else:
        for nombre,datos in agenda.items():
            print(f"\n\t{'nombre:'+nombre}\n\t{'telefono:'+datos[0]}\n\t{'E-mail:'+datos[1]}")
            
def buscar_contactos(agenda):
    borrarpantalla()
    print("\n\t\t \U0001F50D .::Buscar contacto::. \U0001F50D")
    if not agenda:
        print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
    else:
        nom=input("Ingresa el nombre del contacto que desea buscar: ").upper().strip()
        encontro=0
        for nombre,datos in agenda.items():
            if nom==nombre:
                print(f"Se ha encontrado un contacto con el nombre {nombre} \n\t{'telefono:'+datos[0]}\n\t{'E-mail:'+datos[1]}")
                encontro+=1
        if encontro==0:
            print(f" \u274C No se ha encontrado un contacto con el nombre {nom}")

def modificar_contactos(agenda):
    borrarpantalla()
    print("\n\t\t \U0001F501 .::Modificar Contactos::. \U0001F501")
    if not agenda:
        print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
    else:
        nom=input("Ingresa el nombre del contacto que desea modificar: ").upper().strip()
        encontro=0
        for nombre,datos in agenda.items():
            if nombre==nom:
                print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:'+datos[0]}\n\t{'E-mail:'+datos[1]}")
                tel=input("Ingrese el nuevo numero de telefono: ")
                mail=input("Ingrese el nuevo e-mail: ")
                datos[0]=tel
                datos[1]=mail
                encontro+=1
        if encontro==0:
            print(f"\n\t \u274C No se encontro un contacto con el nombre {nom} para modificar \u274C")

def eliminar_contacto(agenda):
    borrarpantalla()
    encontro = 0
    conta_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ").upper().strip()
    confirmar = ""
    for nombre, datos in agenda.items():
        if nombre == conta_eliminar:
            print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:' + datos[0]}\n\t{'E-mail:' + datos[1]}")
            while confirmar != "si" and confirmar != "no":
                confirmar = input("¿Estás seguro que deseas eliminar este contacto? (Si/No): ").lower().strip()
                if confirmar != "si" and confirmar != "no":
                    print("\n\t\t \u274C Respuesta inválida. Por favor escribe 'Si' o 'No' \u274C")
            if confirmar == "si":
                agenda.pop(nombre)
                print(f"\n\t \u2705 El contacto '{nombre}' ha sido eliminado exitosamente. \u2705")
                encontro += 1
    if encontro == 0:
        print(f"\n\t \u274C No se encontró un contacto con el nombre {conta_eliminar} \u274C")









def eliminar_contacto(agenda):
    borrarpantalla()
    encontro = 0
    conta_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ").upper().strip()
    confirmar=""
    eliminar=""  
    for nombre, datos in agenda.items():
        if nombre == conta_eliminar:
            print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:' + datos[0]}\n\t{'E-mail:' + datos[1]}")
            while confirmar != "si" and confirmar != "no":
                confirmar = input("¿Estás seguro que deseas eliminar este contacto? (Si/No): ").lower().strip()
                if confirmar != "si" and confirmar != "no":
                    print("\n\t\t \u274C Respuesta inválida. Por favor escribe 'Si' o 'No' \u274C")
            if confirmar == "si":
                eliminar=nombre
                encontro+=1
    if eliminar!="":
        agenda.pop(eliminar)
        print(f"\n\t \u2705 El contacto '{eliminar}' ha sido eliminado exitosamente. \u2705")
    if encontro == 0:
        print(f"\n\t \u274C No se encontró un contacto con el nombre {conta_eliminar} \u274C")


def vaciar_agenda(agenda):
    borrarpantalla()
    print("\n\t.:: Borrar o quitar todos los contactos ::.")
    respuesta = input("¿Deseas quitar o borrar todas los contactos del sistema? (si)/(no)").lower()
    if respuesta == "si":
        agenda.clear()
        input("\n\t\t::: \u2705 ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::: \u2705")


                






