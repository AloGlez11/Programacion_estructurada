import funciones
from inventarios import inventario
from ventas import venta
from usuarios import usuario
import getpass
from datetime import datetime

def main():
    opcion=True
    while opcion:
        funciones.borrarpantalla()
        print("\n\t \U0001F389 Bienvenidos al sistema de gestión de Papeleria Tikis \U0001F389`")
        opcion=funciones.menu_usurios()

        if opcion=="1":
            funciones.borrarpantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")
            credenciales={}    
            credenciales["correo"]=input("\t Ingresa tu Correo Electronico: ").lower().strip()
            credenciales["contrasena"]=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            registro=usuario.iniciar_sesion(credenciales["correo"],credenciales["contrasena"])
            if registro:
                menu_inicio(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t \u274C Email y/o contraseña incorrectas, vuelva a intentarlo \u274C")
            funciones.esperartecla()
        elif opcion=="2":
            funciones.borrarpantalla()
            print("\n \t ..:: \U0001F4DD Registro en el sistema \U0001F4DD ::.. ")
            registros={}           
            registros["nombre"]=input("\t Ingresa el nombre: ").upper().strip()
            registros["apellidos"]=input("\t Ingresa los apellidos: ").upper().strip()
            registros["email"]=input("\t Ingresa el correo electronico: ").strip()
            opc=True
            while opc:
                telefono=input("\t Ingresa el numero de telefono: ")
                if telefono.isdigit():
                    registros["telefono"]=telefono
                    opc=False
                else:
                    print("\n\t \u26A0 Debe ingresar solo numeros")
            registros["contrasena"]=getpass.getpass("\t Ingresa la contraseña: ").strip()
            resultado=usuario.registrar_usuario(registros)
            if resultado:
                print(f"\n\t \u2705 {registros['nombre']} {registros['apellidos']}, se registró correctamente con el email: {registros['email']} \u2705")
            elif resultado is False:
                print("\n\t \u26A0 El correo ingresado ya está registrado \u26A0")
            funciones.esperartecla()
        elif opcion=="3":
            print("\n\t \U0001F6AA Termino la Ejecución del Sistema \U0001F6AA")
            opcion=False
            funciones.esperartecla()  
        else:
            print("\n\t \u274C Opcion no valida \u274C")
            funciones.esperartecla()
            
def menu_inicio(usuario_id,nombre,apellidos):
    opcion=True
    while opcion:
        funciones.borrarpantalla()
        print(f"\n\t \u2705 Bienvenido {nombre} {apellidos}, has iniciado sesion con exito \u2705 \n\t ¿Qué deseas realizar?")
        opcion=funciones.menu_inicio()
        if opcion=="1" or opcion=="PAPELERIA":
            menu_papeleria(usuario_id,nombre,apellidos)
        if opcion=="2" or opcion=="VENTAS":
            menu_ventas(usuario_id,nombre,apellidos)
        if opcion=="3" or opcion=="REGRESAR AL MENU DE INICIO":
            opcion=False
        else:
            print("\n\t \u274C Opcion no valida")
    

def menu_papeleria(usuario_id,nombre,apellidos):
    opcion=True
    while opcion:
        funciones.borrarpantalla()
        print(f"\n\t \u2705 Hola {nombre} {apellidos}, estas en el menu del inventario \u2705 \n\t ¿Qué deseas realizar?")
        opcion=funciones.menu_papeleria()
        match opcion:
            case "1":
                funciones.borrarpantalla()
                print("\n\t \U0001F4DD Agregar un producto al Inventario \U0001F4DD")
                producto = {}
                producto["id_usuario"] = usuario_id
                producto["nombre_producto"] = input("\nIngrese el nombre del producto: ").upper().strip()
                op = True
                while op:
                    unidades = input("Ingrese la cantidad de unidades del producto: ").strip()
                    if unidades.isdigit() and int(unidades) > 0:
                        producto["unidades"] = int(unidades)
                        op = False
                    else:
                        print("\n\t \u26A0 Debe ingresar un número entero positivo \u26A0")
                opc = True
                while opc:
                    precio_costo = input("Ingresa el precio de costo del producto: ").strip()
                    try:
                        precio_costo_val = float(precio_costo)
                        if precio_costo_val > 0:
                            producto["precio_costo"] = precio_costo_val
                            opc = False
                        else:
                            print("\n\t \u26A0 El precio debe ser mayor que 0 \u26A0")
                    except:
                        print("\n\t \u26A0 Debe ingresar un valor decimal válido \u26A0")
                op1 = True
                while op1:
                    precio_venta = input("Ingrese el precio unitario del producto: ").strip()
                    try:
                        precio_venta_val = float(precio_venta)
                        if precio_venta_val > 0:
                            producto["precio_venta"] = precio_venta_val
                            op1 = False
                        else:
                            print("\n\t \u26A0 El precio debe ser mayor que 0 \u26A0")
                    except:
                        print("\n\t \u26A0 Debe ingresar un valor decimal válido \u26A0")
                opc1 = True
                while opc1:
                    cantidad_minima = input("Ingrese la cantidad mínima del producto: ").strip()
                    if cantidad_minima.isdigit() and int(cantidad_minima) > 0:
                        producto["cantidad_minima"] = int(cantidad_minima)
                        opc1 = False
                    else:
                        print("\n\t \u26A0 Debe ingresar un número entero positivo \u26A0")
                if inventario.agregar_producto(producto):
                    print("\n\t \u2705 Producto agregado con éxito \u2705")   
                else:
                    print("\n\t \u26A0 Ya se encuentra registrado un producto con ese nombre, por favor use otro \u26A0")
                    continue 
                funciones.esperartecla()
            case "2":
                funciones.borrarpantalla()
                print("\n\t \U0001F4C2 Mostrar todos los productos del Inventario \U0001F4C2")
                inventario.mostrar_inventario()
                resp = input("\n\t ¿Desea exportar el inventario a PDF? (si/no): ").upper().strip()
                opt = True
                while opt:
                    if resp != "SI" and resp != "NO":
                        print("\n\t ⚠ Ingresa una respuesta válida (si/no) ⚠")
                        resp = input("\n\t ¿Desea exportar el inventario a PDF? (si/no): ").upper().strip()
                    else:
                        opt = False 
                if resp == "SI":
                    funciones.exportar_inventario_excel()
                funciones.esperartecla()
            case "3":
                funciones.borrarpantalla()
                print("\n\t \U0001F501 Modificar producto dentro del inventario \U0001F501")
                inventario.mostrar_inventario()
                id=input("Ingrese el id del producto que desea modificar: ").upper().strip()
                resul=inventario.existe_producto(id)
                if resul:
                    producto = {}
                    producto["id_usuario"] = usuario_id
                    producto["nombre_producto"] = input("\n Ingrese el nuevo nombre del producto: ").upper().strip()
                    op = True
                    while op:
                        unidades = input("Ingrese la nueva cantidad de unidades: ").strip()
                        if unidades.isdigit() and int(unidades) > 0:
                            producto["unidades"] = int(unidades)
                            op = False
                        else:
                            print("\n\t \u26A0 Debe ingresar un número entero positivo \u26A0")
                    opc = True
                    while opc:
                        precio_costo = input("Ingrese el nuevo precio de costo: ").strip()
                        try:
                            precio_costo_val = float(precio_costo)
                            if precio_costo_val > 0:
                                producto["precio_costo"] = precio_costo_val
                                opc = False
                            else:
                                print("\n\t \u26A0 El precio debe ser mayor que 0")
                        except:
                            print("\n\t \u26A0 Debe ingresar un valor decimal válido")
                    op1 = True
                    while op1:
                        precio_venta = input("Ingrese el nuevo precio de venta: ").strip()
                        try:
                            precio_venta_val = float(precio_venta)
                            if precio_venta_val > 0:
                                producto["precio_venta"] = precio_venta_val
                                op1 = False
                            else:
                                print("\n\t \u26A0 El precio debe ser mayor que 0")
                        except:
                            print("\n\t \u26A0 Debe ingresar un valor decimal válido")
                    opc1 = True
                    while opc1:
                        cantidad_minima = input("Ingrese la nueva cantidad mínima: ").strip()
                        if cantidad_minima.isdigit() and int(cantidad_minima) > 0:
                            producto["cantidad_minima"] = int(cantidad_minima)
                            opc1 = False
                        else:
                            print("\n\t \u26A0 Debe ingresar un número entero positivo")
                    if inventario.modificar_producto(producto, id):
                        print("\n\t \u2705 Producto modificado con éxito \u2705")
                    else:
                        print("\n\t \u26A0 Ya se encuentra registrado un producto con ese nombre, por favor use otro    \u26A0")
                        funciones.esperartecla()
                        continue
                else:
                    print("\n\t No existe un producto con ese ID")
                funciones.esperartecla()
            case "4":
                funciones.borrarpantalla()
                print("\n\t \U0001F50D Buscar un articulo por nombre \U0001F50D")
                producto=input("Ingrese el nombre del producto que desea buscar: ")
                inventario.mostrar_un_producto(producto)
                funciones.esperartecla()
            case "5":
                funciones.borrarpantalla()
                print("\n\t \U0001F4DB Eliminar articulo \U0001F4DB")
                inventario.mostrar_inventario()
                id = input("Ingrese el ID del producto que desea eliminar: ").upper().strip()
                resul=inventario.existe_producto(id)
                if resul:
                    inventario.eliminar_producto(id)
                else:
                    print("\n\t \u274C Producto no encontrado en el inventario \u274C")
                funciones.esperartecla()
            case "6":
                funciones.borrarpantalla()
                print("\n\t \U0001F4CB Mostrar productos bajos en stock \U0001F4CB")
                inventario.stock_bajo()            
                funciones.esperartecla()
            case "7":
                funciones.borrarpantalla()
                opcion=False
            case _:
                print("\n\t Opción inválida.")
                funciones.esperartecla()
                
def menu_ventas(usuario_id,nombre,apellidos):
    opcion=True
    while opcion:
        funciones.borrarpantalla()
        print(f"\n\t \u2705 Hola {nombre} {apellidos}. Estas en el menu de ventas \u2705 \n\t ¿Qué deseas realizar?")
        opcion=funciones.menu_ventas()
        match opcion:
            case "1":
                id_usuario=usuario_id
                funciones.borrarpantalla()
                productos_vendidos=[]
                total = 0
                opc=True
                while opc:
                    funciones.borrarpantalla()
                    print("\n\t \U0001F6D2 Registrar venta")
                    inventario.mostrar_inventario()
                    id = input("Ingrese el ID del producto que desea vender: ").upper().strip()
                    resul=inventario.existe_producto(id)
                    if resul:
                        op = True
                        while op:
                            cantidad=input("Ingrese la cantidad a vender: ").strip()
                            if cantidad.isdigit() and int(cantidad)>0:
                                cantidad = int(cantidad)
                                op = False
                            else:
                                print("\n\t \u26A0 Debe ingresar un número entero mayor a 0 \u26A0")
                        if inventario.verif_stock(id,cantidad):
                            venta.registrar_venta(id_usuario,id,cantidad)
                            inventario.descontar_stock(cantidad,id)
                            precio=inventario.obtener_precio_venta(id)[0]
                            subtotal = cantidad * precio
                            total+=subtotal
                            nombre_producto = inventario.obtener_nombre(id)[0]
                            productos_vendidos.append((nombre_producto, cantidad, subtotal))
                            resp=input("\n\t ¿Desea Realizar otra venta?(si/no)").upper().strip()
                            opt=True
                            while opt:
                                if resp !="SI" and resp !="NO":
                                    print("\n\t Ingresa una respuesta valida: ")
                                    resp = input("\n\t ¿Desea Realizar otra venta?(si/no)").upper().strip()
                                else:
                                    opt=False
                            if resp=='NO':
                                opc=False
                            print("\n\t Ticket de venta.")
                            for nombre, cant, sub in productos_vendidos:
                                print(f"- {cant :<5}  {nombre:<15} → ${sub :<10}")
                            print(f"El total de la venta es: {total}")
                        else:
                            print("No hay stock suficiente para vender esa cantidad de productos")
                            funciones.esperartecla()
                    else:
                        print("\n\t \u26A0 No existe un producto con ese id")
                        funciones.esperartecla()
                funciones.esperartecla()
            case "2":
                funciones.borrarpantalla()
                venta.mostrar_ventas_usuario(usuario_id)
                funciones.esperartecla()
            case "3":
                funciones.borrarpantalla()
                print("\n\t \U0001F4DD Modificar venta")
                venta.mostrar_ventas_usuario(usuario_id)
                id_venta = input("\nIngrese el ID de la venta a modificar: ").strip()
                nueva_cantidad = input("Ingrese la nueva cantidad: ").strip()
                if nueva_cantidad.isdigit() and int(nueva_cantidad) > 0:
                    if venta.cambiar(id_venta, nueva_cantidad):
                        print("\n\t \u2705 Venta modificada con éxito \u2705")
                    else:
                        print("\n\t \u26A0 No se encontró ninguna venta con ese ID. Verifica e inténtalo de nuevo")
                else:
                    print("\n\t \u26A0 Cantidad inválida")
                funciones.esperartecla()
            case "4":
                funciones.borrarpantalla()
                print("\n\t \U0001F4DB Eliminar venta")
                venta.mostrar_ventas_usuario(usuario_id)  # Mostrar ventas del usuario
                id_venta = input("\n\t Ingrese el ID de la venta a eliminar: ").strip()
                if venta.eliminar(id_venta):
                    print("\n\t \U0001F4DB Venta eliminada con éxito \U0001F4DB")
                else:
                    print("\n\t \u26A0 No se encontró ninguna venta con ese ID. Verifica e inténtalo de nuevo")
                funciones.esperartecla()
            case "5":
                funciones.borrarpantalla()
                opcion=False
            
                                        
    
    

if __name__ == "__main__":
    main()
