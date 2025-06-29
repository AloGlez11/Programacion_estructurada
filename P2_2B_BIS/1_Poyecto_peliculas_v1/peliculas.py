peliculas = []

def borrar_pantalla():
    import os 
    os.system("cls")

def esperar_tecla():
    input("Presione cualquier tecla para continuar...")    

def agregar():
    borrar_pantalla()
    print("\n\t.::Alta de Películas::.") 
    peliculas.append(input("Ingresa el nombre: ").upper().strip())
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def consultar():
    borrar_pantalla()
    print("\n\t.:: Consultar ó Mostrar las Películas ::.")
    if len(peliculas) > 0:
        for i in range(0, len(peliculas)):
            print(f"{i+1}:{peliculas[i]}")
    else:
        print("\t..:: No hay películas en el sistema ::.")        

def vaciar_peliculas():
    borrar_pantalla()
    print("\n\t.:: Borrar o quitar todas las películas ::.")
    respuesta = input("¿Deseas quitar o borrar todas las películas del sistema? (si)/(no)").lower()
    if respuesta == "si":
        peliculas.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    
def buscar_peliculas():
    borrar_pantalla()
    print("\n\t.:: Buscar películas ::.")
    pelicula_buscada = input("Ingrese el nombre de la película a buscar: ").upper().strip()
    encontro = 0
    if not(pelicula_buscada in peliculas):
        print("\n\t\t ¡No se encuentra la película a buscar!")
    else:
        for i in range(0, len(peliculas)):
            if pelicula_buscada == peliculas[i]:
                print(f"La película {pelicula_buscada} sí la tenemos y está en la casilla: {i+1}")
                encontro += 1
        if encontro > 0:
            print(f"Tenemos {encontro} película(s) con este título")
            input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")            

def eliminar():
    borrar_pantalla()
    contador = 0
    pelicula_eliminar = input("Teclea la película de la lista deseas eliminar: ").upper().strip()
    if not (pelicula_eliminar) in peliculas:
        print("La película que se tecleó no la tenemos.")
    else:
        validar = "si"
        while pelicula_eliminar in peliculas and validar == "si":
            validar = input("¿Deseas quitar o borrar la película del sistema? (Si/No)").lower().strip()
            if validar == "si":
                posicion = peliculas.index(pelicula_eliminar)
                print(f"La película que se borró es {pelicula_eliminar} y se encuentra en la casilla {posicion}")
                peliculas.remove(pelicula_eliminar)
                contador += 1
                input("La operación se realizó con éxito")
        print(f"Se borró {contador} película(s) con este título")        

def actualizar_peliculas():
    borrar_pantalla()
    contador = 0
    seleccion = input("Teclee la película que desea modificar: ").upper().strip()
    
    if not(seleccion) in peliculas:
        print("No se encontró la película")
    else:
        for i in range(0, len(peliculas)):
            if seleccion == peliculas[i]:
                contador += 1

        if contador > 1:
            print(peliculas)
            casilla = int(input(f"Se encontraron {contador} películas con el mismo nombre, ingresa la posición de la película: "))
            cambio = input("Ingresa el reemplazo o cambio: ").upper().strip()
            casilla = casilla - 1
            peliculas[casilla] = cambio
            print("El cambio se ha realizado correctamente")
            print(peliculas)
        else:
            cambio = input("Ingresa el reemplazo o cambio: ").upper().strip()
            peliculas[i] = cambio
