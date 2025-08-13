from conexion_BD import Conectar_BD
from inventarios import inventario

def registrar_venta(id_usuario,id_producto,cantidad):
    """
    Inserta una nueva venta en la base de datos.
    Recibe un diccionario con id_usuario, id_producto, cantidad.
    """
    try:
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        sql = "insert into ventas (id_usuario, id_producto, cantidad) values (%s, %s, %s)"
        valores = (id_usuario,id_producto,cantidad)
        cursor.execute(sql, valores)
        conexion.commit()
        print("\n\t \u2705 venta realizada con exito \u2705")
    except:
        print("\n\t \u26A0 Error al conectar con la base de datos...")

def mostrar(usuario_id):
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="select * from ventas where id_usuario=%s"
        val=(usuario_id,)
        cursor.execute(sql, val)
        return cursor.fetchall()
    except:
        return []

def cambiar(id_venta, nueva_cantidad):
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="update ventas set cantidad=%s where id_venta=%s"
        cursor.execute(sql, (nueva_cantidad, id_venta))
        conexion.commit()
        return cursor.rowcount > 0
    except:
        return False

def mostrar_ventas_usuario(usuario_id):
    ventas = mostrar(usuario_id)
    if not ventas:
        print("\n\t \u26A0 No hay ventas registradas para este usuario.")
        return
    print(f"\n{'ID Venta':<10} {'ID Usuario':<12} {'ID Producto':<12} {'Nombre Producto':<20} {'Cantidad':<10} {'Total':<10} {'Fecha':<15}")
    print("-" * 90)
    for venta in ventas:
        id_venta = venta[0]
        id_usuario = venta[1]
        id_producto = venta[2]
        cantidad = int(venta[3])
        fecha = venta[4]
        nombre_producto = inventario.obtener_nombre(id_producto)[0]
        precio_venta = float(inventario.obtener_precio_venta(id_producto)[0])
        total = cantidad * precio_venta
        print(f"{id_venta:<10} {id_usuario:<12} {id_producto:<12} {nombre_producto:<20} {cantidad:<10} ${total:<10.2f} {fecha:<15}")

def eliminar(id_venta):
    try:
        conexion=Conectar_BD()
        cursor=conexion.cursor()
        sql="delete from ventas where id_venta=%s"
        cursor.execute(sql, (id_venta,))
        conexion.commit()
        return cursor.rowcount > 0
    except:
        return False