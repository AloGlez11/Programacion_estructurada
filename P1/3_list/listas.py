# Ejemplo 1 Crear una lista de numeros e imprimir el contenido
import os

numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numeros.sort()
print(numeros)

for i in numeros:
    print(i)

for i in range(0, len(numeros)):
    print(numeros[i])

#os.system("cls")

# Ejemplo 2 Crear una lista de palabras y posteriormente la coincidencia de una palabra

palabras = ["pan", "platillo", "jugo", "carne", "arroz"]

palabra_buscar = input("ingresa la palabra: ")

veces = palabras.count(palabra_buscar)
print(f"El numero de veces que se encontro la palabra es: {veces}")

# 1era forma
if palabra_buscar in palabras:
    print("Si encontro la palabra")
else:
    print("No se encontro la palabra")

# 2da forma
encontro = False
for i in range(0, len(palabras)):
    if palabras[i] == palabra_buscar:
        encontro = True
if encontro:
    print(f"Si encontro la palabra en posicion {i} ")
else:
    print(f"No encontro la palabra en posicion {i}")

# 3ra forma
encontro = False
for i in palabras:
    if i == palabra_buscar:
        encontro = True
if encontro:
    print("Si encontro la palabra")
else:
    print("No encontro la palabra")
input("Oprima tecla para continuar. . .")


# Ejemplo 3 Agregar elementos a una lista
#os.system("cls")
nuumeritos = []
opc = True
while opc:
    numerito = float(input("Dame un numero entero o decimal: "))
    nuumeritos.append(numerito)
    respuesta = input("Deseas agregar otro numero? ").lower()
    if respuesta == "si":
        opc = True
    else:
        opc = False

print(f"La lsta quedo asi: {nuumeritos}")
input("Oprima tecla para continuar. . .")
#os.system("cls")


# Ejemplo 4 crear una lista multidimensional que sea una agenda

agenda = [["Carlos", "6189807654"], ["Alberto", "9877647736"], ["Martin", "8768746532"]]

print(agenda)

for i in agenda:
    print(i)

cadena = ""
for r in range(0, 3):
    for c in range(0, 2):
        cadena += f"{agenda[r][c]}, "
    cadena += "\n"
print(cadena)
