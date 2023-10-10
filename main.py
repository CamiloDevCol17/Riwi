#Practicando diccionarios
#Sistema de inventario para una tienda de ropa
#nombre, stock, cantidad
def Menu():
    input("Presione ENTER para continuar")
    print("\n-------------MENU DE OPCIONES----------\n")
    print("1. Listar productos")
    print("2.Agregar producto")
    print("3. Actualizar producto")
    print("4.Eliminar producto")
    print("5.Salir")

def agregar_producto(inventario):
    try:
        nombre_producto = input("INgrese el nombre del producto: ")
        cantidad_producto = input("INgrese la cantidad del producto: ")
        precio_producto = input("INgrese el precio del producto: ")

        #Creamo el diccionario
        Producto = {"Nombre":nombre_producto,"Cantidad":int(cantidad_producto), "Precio":float(precio_producto)}
        inventario.append(Producto)#agregar producto
        print("Se agrego el producto con exito")
    except:
        print("Error al ingresar el producto")

    

def listar_producto(inventario):
    #valido si hay productos e eñ inventario
    if not inventario:
        print("No hay productos en el inventario\n")
    else:
        print("\nLista de productos")

        for indice, producto in enumerate (inventario):
            print(indice, ". -", "Nombre:", producto["Nombre"], "Cantidad:", producto["Cantidad"], "Precio:", producto["Precio"])


def actualizar_producto(inventario):
    listar_producto(inventario)
    if not inventario:
        return 
    else:
        try:
            
            indice = int(input("Ingresa el indice del producto a actualizar: "))
            if (indice<0 or indice >len(inventario)):
                print("El indice no es valido o no existe en la lista")
            else:
                nombre_producto = input("INgrese el nuevo nombre del producto: ")
                cantidad_producto = input("INgrese la nueva cantidad del producto: ")
                precio_producto = input("INgrese el nuevo precio del producto: ")

                inventario[indice]["Nombre"]= nombre_producto
                inventario[indice]["Cantidad"]= int(cantidad_producto)
                inventario[indice]["Precio"]= float(precio_producto)
                print("\nEl producto fue actualizado con exito\n")
                listar_producto(inventario)
        except:
            print("Algo salio mal, intentalo mas tarde")
        
def eliminar_producto(inventario):
    listar_producto(inventario)
    if not inventario:
        return
    else:
        try:
            
            indice = int(input("Ingrese el indice a llamar: "))

            if(indice <0 or indice >len(inventario)):
                print("El indice no corresponde con el inventario")
                
            else:
                print("Eliminado producto....")
                inventario.pop(indice)
                print("El producto fue eliminado con exito")
                listar_producto(inventario)
        except:
            print("Algo salio mal, intentalo de nuevo o mas tarde")



def main():
    inventario = []
    while True:
        Menu()

        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                listar_producto(inventario)
            case 2:
                agregar_producto(inventario)
            case 3:
                actualizar_producto(inventario)
            case 4:
                eliminar_producto(inventario)
            case 5:
                break
main()
        