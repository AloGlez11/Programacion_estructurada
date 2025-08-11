from conexion_BD import Conectar_BD

def registrar_venta(venta: dict):
    """
    Inserta una nueva venta en la base de datos.
    Recibe un diccionario con id_usuario, id_producto, cantidad.
    """
    try:
        conexion = Conectar_BD()
        cursor = conexion.cursor()
        consulta = "insert into ventas (id_usuario, id_producto, cantidad) values (%s, %s, %s)"
        valores = (
            venta["id_usuario"],
            venta["id_producto"],
            venta["cantidad"]
        )
        cursor.execute(consulta, valores)
        conexion.commit()
        print("\n\t \u2705 venta realizada con exito \u2705")
    except:
        print("\n\t \u26A0 Error al conectar con la base de datos...")


