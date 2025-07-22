lista=[]

if len(lista)==0:
    resp=True
    while resp:
        lista.append(input("Dame una palabra o frase: ").upper())
        resp=input("¿Deseas solicitar una palabra o frase? (si/no): ").lower().strip()
    print(lista)
        