def verificar_par_impar_2():
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Llamada
resultado = verificar_par_impar_2()
print(f"El número es {resultado}.")