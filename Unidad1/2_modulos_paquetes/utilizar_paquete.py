from paquete1 import modulo

print(modulo.saludar("Sebastian Gonzalez de Leon"))


modulo.borrarpantalla()
nom,tel=modulo.SolicitarDatos2()
print(f"\n\t.::Agenda Telefonica::.\n\t\tNombre: {nom}\n\t\tTelefono:{tel}")
modulo.espereTecla()
