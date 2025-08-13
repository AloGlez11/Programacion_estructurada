from conexion_BD import Conectar_BD
import funciones

def agregar_producto(producto: dict):
    try:
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        sql_checar = "select nombre_producto FROM inventario where nombre_producto = %s"
        cursor.execute(sql_checar, (producto["nombre_producto"],))
        duplicado = cursor.fetchone()
        if duplicado:
            return False
        consulta = "insert into inventario (id_usuario, nombre_producto, unidades, precio_costo, precio_venta, cantidad_minima)values (%s, %s, %s, %s, %s, %s)"
        valores = (
            producto["id_usuario"],
            producto["nombre_producto"],
            producto["unidades"],
            producto["precio_costo"],
            producto["precio_venta"],
            producto["cantidad_minima"]
            )
        cursor.execute(consulta, valores)
        conexion.commit()
        return True
    except:
        print("\n\t \u26A0 Error al conectarse con la base de datos...")

def mostrar_inventario():
    "Devuelve todos los productos almacenados en el inventario."
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="select * from inventario"
        cursor.execute(sql)
        resultado=cursor.fetchall()
        if resultado:
            print(f"\n{'ID producto':<12} {'ID usuario':<12} {'Nombre':<25} {'Unidades':<10} {'Precio costo':<12} {'Precio venta':<12}")
            print("-" * 80)
            for fila in resultado:
                print(f"{fila[0]:<12} {fila[1]:<12} {fila[2]:<25} {fila[3]:<10} {fila[4]:<12.2f} {fila[5]:<12.2f}")
                print("-" * 80)
            print("-" * 70)
        else:
            print("\n\t \u26A0 No hay productos con ese nombre en el inventario")
    except:
        print("\n\t \u26A0 Error al intentar conectar con la base de datos...")


def mostrar_un_producto(producto):
    #Permite buscar un producto de nuestro inventario por nombre, en caso de haber duplicados se imprime una tabla donde se muestran los productos.
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="select * from inventario where nombre_producto=%s"
        valores=(producto,)
        cursor.execute(sql,valores)
        resultado = cursor.fetchall()
        if resultado:
            print(f"\n{'ID producto':<12} {'ID usuario':<12} {'Nombre':<25} {'Unidades':<10} {'Precio venta':<12}")
            print("-" * 80)
            for fila in resultado:
                print(f"{fila[0]:<12} {fila[1]:<12} {fila[2]:<25} {fila[3]:<10} {fila[5]:<12.2f}")
                print("-" * 80)
        else:
            print("\n\t \u26A0 No hay productos con ese nombre en el inventario")
    except:
        print("\n\t \u26A0 Error al intentar conectar con la base de datos")
        
def modificar_producto(producto: dict, id_producto):
    try:
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        sql_checar = "SELECT nombre_producto FROM inventario WHERE nombre_producto = %s AND id_producto <> %s"
        cursor.execute(sql_checar, (producto["nombre_producto"], id_producto))
        duplicado = cursor.fetchone()
        if duplicado:
            return False
        sql = "UPDATE inventario SET id_usuario=%s, nombre_producto=%s, unidades=%s, precio_costo=%s, precio_venta=%s, cantidad_minima=%s WHERE id_producto=%s"
        valores = (
            producto["id_usuario"], 
            producto["nombre_producto"],
            producto["unidades"],
            producto["precio_costo"],
            producto["precio_venta"],
            producto["cantidad_minima"],
            id_producto
        )
        cursor.execute(sql, valores)
        conexion.commit()
        return True
    except:
        print("\n\t \u26A0 Error al conectarse con la base de datos...")    
        
def eliminar_producto(opc):
    #Despues de mostrar al usuario las opciones de su busqueda se pide confirmar si quiere eliminar el producto y que ingrese el ID del producto en caso de que un producto este duplicado.
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="delete from inventario where id_producto=%s"
        valores=(opc,)
        cursor.execute(sql,valores)
        conexion.commit()
        print("\n\t \U0001F4DB Producto eliminado con éxito \U0001F4DB")
    except:
        print("\n\t \u26A0 Error al intentar concectar con la base de datos")
        
def stock_bajo():
    #Funcion que imprime los productos con bajo stock, es decir los productos en los que la cantidad de articulos es menor a la cantidad minima que el usuario ingrese
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="select * from inventario where unidades < cantidad_minima"
        cursor.execute(sql)
        productos=cursor.fetchall()
        if productos:
            print("\n\t Producto encontrado:")
            print(f"\n{'ID':<5} {'Nombre':<20} {'Unidades':<15} {'Precio venta':<10}")
            print("-" * 70)
            for fila in productos:
                print("-" * 70)
                print(f"{fila[0]:<5} {fila[2]:<20} {fila[3]:<15} {fila[5]:<10}")
            print("-" * 70)
        else:
            print("\n\t No hay productos bajos en stock")
    except:
        print("Ocurrio un error al conectar con la base de datos")
    
    
def existe_producto(id):
    try:
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        sql = "SELECT COUNT(*) FROM inventario WHERE id_producto = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado[0] == 1:
            return True
        else:
            return False
    except:
        print("\n\t \u26A0 Error al conectar con la base de datos...")
        return False

def verif_stock(id_producto,cantidad):
    #Verifica que la cantidad de un producto sea mayor a 0
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="select unidades from inventario where id_producto=%s"
        cursor.execute(sql, (id_producto,))
        resultado=cursor.fetchone() 
        if resultado[0] >= cantidad:
            return True
        else:
            return False
    except:
        print("\n\t \u26A0 Error al conectar con la base de datos...") 
    
def descontar_stock(cantidad,id_producto):
    #Descuenta la cantidad vendida del inventario.
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="update inventario set unidades = unidades - %s where id_producto = %s"
        cursor.execute(sql, (cantidad, id_producto))
        conexion.commit()
    except:
        print("\n\t \u26A0 Error al conectar con la base de datos...")
    
def obtener_precio_venta(id_producto):
    try:
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        sql = "SELECT precio_venta FROM inventario WHERE id_producto = %s"
        cursor.execute(sql, (id_producto,))
        return cursor.fetchone()
    except:
        print("\n\t \u26A0 Error al conectar con la base de datos...")
        
def obtener_nombre(id_producto):
    try:
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        sql = "SELECT nombre_producto FROM inventario WHERE id_producto = %s"
        cursor.execute(sql, (id_producto,))
        return cursor.fetchone()
    except:
        print("\n\t \u26A0 Error al conectar con la base de datos...")
        return None