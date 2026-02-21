ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial_pedidos():
    try:
        print("\n Historial de pedidos:")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
               for i, pedido in enumerate(pedidos, start=1):
                   print(str(i) + ". " + pedido.strip()) #el strip quita los espacios en blanco y los saltos de linea
            else:
                print("No hay pedidos realizados aún.")
    except FileNotFoundError:
        print("No hay pedidos realizados aún.")
        return