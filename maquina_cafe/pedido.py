ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n eligue el cafe que quieras: ")
    print("1. expresso")
    print("2. capuccino")
    print("3. latte")
    print("4. americano")

    opcion = input("opcion: ")

    cafes = {
        "1": "expresso",
        "2": "cappuccino",
        "3": "latte",
        "4": "americano" 
    }

    if opcion in cafes:  #si la OPCION esta dentros de los CAFES entonces vamos a poder seguir haciendo el codigo
        cafe_elegido = cafes[opcion]
        print("has pedido un: " + cafe_elegido + ". ¡preparando tu cafe!")

        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else: 
        print("opcion no valida intenta de nuevo")

pedir_cafe()