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
                menu_papeleria(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t \u274C Email y/o contraseña incorrectas, vuelva a intentarlo \u274C")
            funciones.esperartecla()
        elif opcion=="2":
            funciones.borrarpantalla()
            print("\n \t ..:: \U0001F4DD Registro en el sistema \U0001F4DD ::.. ")
            registros={}           
            registros["nombre"]=input("\t Ingresa el nombre: ").upper().strip()
            registros["apellidos"]=input("\t Ingresa los apellidos: ").upper().strip()
            registros["email"]=input("\t Ingresa el correo electronico: ").lower().strip()
            registros["telefono"]=input("\t Ingresa el numero de telefono: ")
            registros["contrasena"]=getpass.getpass("\t Ingresa la contraseña: ").strip()
            resultado=usuario.registrar_usuario(registros)
            if resultado:
                print(f"\n\t \u2705 {registros['nombre']} {registros['apellidos']}, se registró correctamente con el email: {registros['email']} \u2705")
            elif resultado is False:
                print("\n\t \u26A0 El correo ingresado ya está registrado \u26A0")
            else:
                print("\n\t \u26A0 Error al conectar con la base de datos \u26A0")
            funciones.esperartecla()
        elif opcion=="3":
            print("\n\t \U0001F6AA Termino la Ejecución del Sistema \U0001F6AA")
            opcion=False
            funciones.esperartecla()  
        else:
            print("\n\t \u274C Opcion no valida \u274C")
            funciones.esperartecla()

def menu_papeleria(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarpantalla()
        print(f"\n\t \u2705 Bienvenido {nombre} {apellidos}, has iniciado sesion con exito \u2705 \n\t ¿Qué deseas realizar?")
        opcion=funciones.menu_papeleria()
        match opcion:
            case "1":
                funciones.borrarpantalla()
                print("\n\t \U0001F4DD Agregar un producto al Inventario \U0001F4DD")
                producto = {}
                producto["id_usuario"] = usuario_id
                producto["nombre_producto"] = input("\n Ingrese el nombre del producto: ").upper().strip()
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
                if not inventario.agregar_producto(producto):
                    print("\n\t \u26A0 Ya se encuentra registrado un producto con ese nombre, por favor use otro \u26A0")
                    continue 
                funciones.esperartecla()
            case "2":
                funciones.borrarpantalla()
                print("\n\t \U0001F4C2 Mostrar todos los productos del Inventario \U0001F4C2")
                inventario.mostrar_inventario()
                funciones.esperartecla()
            case "3":
                funciones.borrarpantalla()
                print("\n\t \U0001F501 Modificar producto dentro del inventario \U0001F501")
                nombre_busqueda = input("Ingrese el nombre del producto que desea modificar: ").upper().strip()
                inventario.mostrar_un_producto(nombre_busqueda)
                id_producto = inventario.obtener_id_producto(nombre_busqueda)
                if not id_producto:
                    print("\n \u274C No se encontró el producto en el inventario \u274C")
                    funciones.esperartecla()
                    break
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
                if not inventario.modificar_producto(producto, id_producto):
                    print("\n\t \u26A0 Ya se encuentra registrado un producto con ese nombre, por favor use otro \u26A0")
                    funciones.esperartecla()
                    continue
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
                producto = input("Ingrese el nombre del producto que desea eliminar: ").upper().strip()
                id_producto = inventario.obtener_id_producto(producto)
                if id_producto:
                    inventario.eliminar_producto(id_producto)
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
                print("\n\t \U0001F6D2 Registrar venta")
                nombre_producto = input("Ingrese el nombre del producto: ").upper().strip()
                id_producto = inventario.obtener_id_producto(nombre_producto)
                if id_producto:
                    opc = True
                    while opc:
                        cantidad_str = input("Ingrese la cantidad a vender: ").strip()
                        if cantidad_str.isdigit() and int(cantidad_str) > 0:
                            cantidad = int(cantidad_str)
                            opc = False
                        else:
                            print("\n\t \u26A0 Debe ingresar un número entero positivo.")
                    op = True
                    while op:
                        if inventario.verificar_stock(id_producto, cantidad):
                            op = False
                        else:
                            print("\n\t \u26A0 No hay suficiente stock disponible.")
                            cantidad_str = input("Ingrese una cantidad válida según el stock disponible: ").strip()
                            if cantidad_str.isdigit() and int(cantidad_str) > 0:
                                cantidad = int(cantidad_str)
                            else:
                                print("\n\t \u26A0 Debe ingresar un número entero positivo.")
                    precio_unitario = inventario.obtener_precio_venta(id_producto)[0]
                    total = cantidad * precio_unitario
                    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    vender = {
                        "id_usuario": usuario_id,
                        "id_producto": id_producto,
                        "cantidad": cantidad
                            }
                    venta.registrar_venta(vender)
                    inventario.descontar_stock(id_producto, cantidad)
                    opcion_pdf = input("\n¿Desea exportar esta venta a PDF? (SI/NO): ").strip().upper()
                    if opcion_pdf == "SI":
                        funciones.exportar_pdf(nombre_producto, cantidad, total, fecha_actual)
                    print(f"\n \U0001F389 Se vendió {cantidad} pieza(s) de '{nombre_producto}' con un total de ${total:.2f} el día {fecha_actual} \U0001F389")
                else:
                    print("\n\t \u274C Producto no encontrado en el inventario. \u274C")
                funciones.esperartecla()
            case "8":
                funciones.borrarpantalla()
                print("\n\t \U0001F6AA Has terminado la ejecucion del Software \U0001F6AA")
                funciones.esperartecla()
                break
            case _:
                print("\n\t Opción inválida.")
                funciones.esperartecla()

if __name__ == "__main__":
    main()
