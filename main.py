lista=[
    {
        "id":0,
        "name":"tornillos",
        "precio": 10,
        "stock": 100
    }
]

while True:
    comando=int(input("Ingrese comando\n0:listar articulos\n1:consultar stock\n2:añadir articulo\n3:modificar stock\n\n"))
    if(comando==0):
        print("hay " + str(len(lista)) + " articulos: ")
        for n in range(len(lista)):
            print (str(lista[n]['id'])+ "-" +str(lista[n]['name']))
    elif(comando==1):
        input_id=int(input("Ingresar ID del articulo a consultar: "))
        if input_id>=0 and input_id<len(lista):
            print("El stock disponible de "+str(lista[input_id]['name'])+" es: "+str(lista[input_id]['stock']))
        else:
            print("ERROR: ID no valido")
    else:
        break
    print("\n\n")



