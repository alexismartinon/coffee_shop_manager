from menu import mostrar_menu
from pedido import pedir_cafe
from historial import ver_historial_pedidos

def main():
    while True:         #este bucle se va a repetir
        mostrar_menu()              #va a mostrar el menu
        opcion = input("Selecciona una opción: ")

        if opcion == "1":            #siempre ponerlo como string
            pedir_cafe()
        elif opcion == "2":
            ver_historial_pedidos()
        elif opcion == "3":
         print("muchas garcias por tomar nuestros cafes")
         break
        else:
           print("opcion invalida, por favor indique una de las opciones sugeridas")
        
if __name__ == "__main__":
   main()