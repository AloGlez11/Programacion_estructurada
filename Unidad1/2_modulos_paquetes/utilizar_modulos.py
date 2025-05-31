#1er utilizar los modulos
import modulo

modulo.borrarpantalla()
print(modulo.saludar("Alondra Gonzalez Cabral"))

#2da forma de utilizar modulos

from modulo import saludar,borrarpantalla

borrarpantalla()
print(saludar("Sebastian Gonzalez de Leon"))

nombre=input("ingresa el nombre del contacto: ")
telefono=input("Ingrese su numero de telefono: ")
nom,tel=modulo.SolicitarDatos4(nombre,telefono)
print(f"\tNombre Completo: {nom}\n\tTelefono:{tel}")
