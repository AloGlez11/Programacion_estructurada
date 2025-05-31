'''
Crear un programa que calcule e imprima la tabla de multiplicar del 2

  Requisitos:
Funcion que regrese valor y utilize parametros
'''
#version1
numero=int(input("Dame el numero de la tabla de ultiplicar a calcular: "))
multi=numero*1
print(f"{numero} x 1 = {multi}")
multi=numero*2
print(f"{numero} x 2 = {multi}")
multi=numero*3
print(f"{numero} x 3 = {multi}")
multi=numero*4
print(f"{numero} x 4 = {multi}")
multi=numero*5
print(f"{numero} x 5 = {multi}")
multi=numero*6
print(f"{numero} x 7 = {multi}")
multi=numero*8
print(f"{numero} x 8 = {multi}")
multi=numero*9
print(f"{numero} x 9 = {multi}")
multi=numero*10
print(f"{numero} x 10 = {multi}")

#version2
numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
print(f"Tabla de multiplicar del {numero}")
for i in range (1,11,1):
    multi=numero*i
    print(f"{numero} x {i} = {multi}")

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
print(f"Tabla de multiplicar del {numero}")
i=1
while i<=10:
    multi=numero*i
    print(f"{numero} x {i} = {multi}")
    i+=1

#version3
def tablas_multiplicar(num):
    num = numero
    respuesta = ""
    for i in range(1, 11):
        multi = num * i
        respuesta += f"{num} x {i}: {multi}\n "
    return respuesta


numero = int(input("Dame el numero de la tabla a calcular: "))
print(f"Tablas de multiplicar del {numero}")

resultado = tablas_multiplicar(numero)
print(f"{resultado}")

