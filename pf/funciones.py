
from reportlab.pdfgen import canvas

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\n\t \U0001F552 Presiona ENTER para continuar...")
    
def menu_usurios():
   print("\n \t.:: Menu de usuarios::.. \n\t\t1.-Login  \n\t\t2.-Registro  \n\t\t3.-Salir ")
   opcion=input("\t Elige una opción: ").upper().strip() 
   return opcion

def menu_papeleria():
   print("\n \t .::  Menu Inventario::. \n\t1.- \U0001F4DD Agregar producto \n\t2.- \U0001F4C2 Mostrar inventario \n\t3.- \U0001F501 Modificar producto \n\t4.- \U0001F50D Buscar producto \n\t5.- \U0001F4DB Eliminar producto \n\t6.- \U0001F4CB Productos bajos en stock \n\t7.- \U0001F6D2 Realizar una venta \n\t8.- \U0001F6AA Salir """)
   opcion = input("\t\t Elige una opción (utiliza numero): ").upper().strip()
   return opcion  


def exportar_pdf(producto, cantidad, total, fecha):
    c = canvas.Canvas("reporte.pdf")
    c.drawString(100, 750, "Reporte de Ventas - Papelería Tikis")
    c.drawString(100, 730, f"Producto: {producto}")
    c.drawString(100, 710, f"Cantidad: {cantidad}")
    c.drawString(100, 690, f"Total: ${total:.2f}")
    c.drawString(100, 670, f"Fecha: {fecha}")
    c.save()
    print("\n\t \U0001F389 PDF exportado con éxito \U0001F389`")