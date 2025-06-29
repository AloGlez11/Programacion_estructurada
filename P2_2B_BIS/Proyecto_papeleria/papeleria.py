inventario = []


def borrarpantalla():
    import os

    os.system("cls")


def esperartecla():
    borrarpantalla()
    print("Oprima cualquier tecla para continuar ...")
    input()


def agregarinventario():
    borrarpantalla()
    print("\n\t.:: \U0001f4be Almacenar en inventario\U0001f4be ::. ")
    nombre = input("Ingresa el nombre: ").upper().strip()
    while True:
        try:
            stock = int(input("Ingresa la cantidad en stock: "))
            if stock < 0:
                print("El stock no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingresa un número válido para el stock.")
    while True:
        try:
            precio = float(input("Ingresa el precio del elemento: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingresa un número válido para el precio.")
    inventario.append({'nombre': nombre, 'stock': stock, 'precio': precio})
    input("\n\t\t ::: \u2705 LA OPERACION SE REALIZO CON EXITO!\u2705 :::")


def borrarelementoss():
    borrarpantalla()
    print("\n\t\t ::: \U0001f4db BORRAR ELEMENTO \U0001f4db :::")
    elemento_borrar = input("\U0001f4db Ingrese el nombre del elemento que desea borrar: ").upper().strip()
    borrados = 0
    for i in range(len(inventario)-1, -1, -1):
        if inventario[i]['nombre'] == elemento_borrar:
            print(f"El elemento que se borró es: {elemento_borrar} \U0001f4db y estaba en la casilla: {i+1}")
            inventario.pop(i)
            borrados += 1
    if borrados == 0:
        print("No se encontró el elemento en el inventario.")
    input("\n\t\t ::: Operación finalizada :::")


def consultarinventario():
    borrarpantalla()
    print("\n\t.:: \U0001F4DD Consultar Inventario \U0001F4DD ::.")
    if len(inventario) > 0:
        print(f"{'No.':<5}{'Nombre':<20}{'Stock':<10}")
        print("-"*35)
        for i, item in enumerate(inventario):
            print(f"{i+1:<5}{item['nombre']:<20}{item['stock']:<10}")
    else:
        print("\t ..:: No hay elementos en el sistema ::..")
    input("Presiona ENTER para continuar...")


def buscarelemento():
    borrarpantalla()
    print("\n\t .:: 🔍 Buscar en inventario 🔍 ::.")
    if len(inventario) == 0:
        print("\n\t\t 🗃️ No hay inventario existente. Agregue elementos primero.")
        return
    inventario_buscar = input("Ingrese el nombre del elemento a buscar 🔍: ").upper().strip()
    encontro = 0
    for i, item in enumerate(inventario):
        if inventario_buscar == item['nombre']:
            print(f"✅ El elemento '{inventario_buscar}' sí existe y está en la casilla: {i+1} con stock: {item['stock']}")
            encontro += 1
    if encontro == 0:
        print(f"\n\t\t ❌ El elemento '{inventario_buscar}' NO se encuentra en el inventario.")
    else:
        print(f"\nTenemos {encontro} elemento(s) de este tipo.")
    input("\n\t\t ::: ✅ LA OPERACIÓN SE REALIZÓ CON ÉXITO ✅ :::")


def vaciarinventario():
    borrarpantalla()
    print("\n\t .:: ⚠️ Vaciar Inventario ⚠️ ::.")
    if len(inventario) == 0:
        print("\n\t\t 🗃️ El inventario ya está vacío.")
        return
    confirmacion = input("¿Está seguro que desea eliminar TODOS los elementos? (SI/NO): ").upper().strip()
    if confirmacion == "SI":
        inventario.clear()
        print("\n\t✅ Inventario vaciado correctamente.")
    else:
        print("\n\t❌ Operación cancelada. El inventario no se modificó.")
    input("\n\tPresione ENTER para continuar...")


def ventas():
    borrarpantalla()
    carrito = []
    total = 0
    while True:
        print("\n\t.:: 🛒 Realizar Venta 🛒 ::.")
        if len(inventario) == 0:
            print("No hay elementos en el inventario para vender.")
            break
        print(f"{'No.':<5}{'Nombre':<20}{'Stock':<10}{'Precio':<10}")
        print("-"*50)
        for i, item in enumerate(inventario):
            print(f"{i+1:<5}{item['nombre']:<20}{item['stock']:<10}{item['precio']:<10.2f}")
        eleccion = input("\nIngrese el nombre del elemento a comprar: ").upper().strip()
        encontrado = False
        for item in inventario:
            if item['nombre'] == eleccion:
                encontrado = True
                while True:
                    try:
                        cantidad = int(input(f"Ingrese la cantidad de '{eleccion}' a comprar: "))
                        if cantidad <= 0:
                            print("La cantidad debe ser mayor a cero.")
                        elif cantidad > item['stock']:
                            print("No hay suficiente stock disponible.")
                        else:
                            break
                    except ValueError:
                        print("Ingrese un número válido para la cantidad.")
                subtotal = cantidad * item['precio']
                carrito.append({'nombre': eleccion, 'cantidad': cantidad, 'precio': item['precio'], 'subtotal': subtotal})
                total += subtotal
                item['stock'] -= cantidad
                print(f"\nAgregado al carrito: {cantidad} x {eleccion} (${item['precio']:.2f} c/u) = ${subtotal:.2f}")
                break
        if not encontrado:
            print("Elemento no encontrado en el inventario.")
        otra = input("\n¿Desea realizar otra venta? (SI/NO): ").upper().strip()
        if otra != "SI":
            break

    if carrito:
        borrarpantalla()
        print("\n\t.:: 🧾 Ticket de Venta 🧾 ::.\n")
        print(f"{'Producto':<20}{'Cantidad':<10}{'Precio':<10}{'Subtotal':<10}")
        print("-"*50)
        for prod in carrito:
            print(f"{prod['nombre']:<20}{prod['cantidad']:<10}{prod['precio']:<10.2f}{prod['subtotal']:<10.2f}")
        print("-"*50)
        print(f"{'TOTAL':<40}${total:.2f}")
        print("\nOPERACION REALIZADA CON EXITO")
    else:
        print("\nNo se realizó ninguna venta.")
    input("\nPresione ENTER")