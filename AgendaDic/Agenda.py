def opciones():
    print("Bienvenido al sistema de agenda")
    print("0)Salir\n"
    "1)agregar evento\n"
    "2)consultar eventos de una fecha\n"
    "3)Mostrar agenda completa\n"
    "4)Eliminar evento\n"
    "5)Liberar fecha\n"
    "6)Vacias agenda")
    opcion = print(input("Que opcion va a escoger?"))
    if opcion < 6 or opcion < 0:
        print("Disculpe, esa no es una opcion valida")
    else:
        print("ok")
