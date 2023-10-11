## hacer un to-do list que tenga las siguientes opciones
#crear tarea
# listar tarea
# eliminar tarea
#salir del programa

def menu():
    input("Presione enter para continuar")
    print("""
            TO-DO LIST CHECK
\n------------MENU DE OPCIONES-----------\n
          1)Crear tarea
          2)Listar tarea
          3)Actualizar tarea
          4)Borrar tarea
          5)Salir del programa
""")
    

def crear_tarea(all_todo):
    try:
        #fecha, hora y tarea
        fecha = input("Ingresa la fecha en formato DD/MM/YY: ")
        hora = input("Ingrese la hora en formato HH:MIN: ")
        tarea = input("Ingresa la tarea a realizar: ")

        #crear diccionario que almacene 
        tarea_completa = {"Fecha":fecha,"Hora":hora,"Tarea":tarea}
        #agregar tarea
        all_todo.append(tarea_completa)
        print("La tarea se agrego exitosamente")

    except:
        print("Error al ingresar la tarea")

def mostrar_tarea(all_todo):
    #validamos si hay tareas disponibles
    if not all_todo:
        print("No hay tareas ingresadas")
    else:
        print("\nLista de tareas")
        # indice: valor que aparece al inicio 0
        for indice, tarea_completa in enumerate(all_todo):
            #imprimimos en pantalla la tarea
            #0. -fecha: 11/12/01 Hora: 23:22 Tarea Hacer la comida
            print(indice,". -","Fecha:",tarea_completa["Fecha"],"Hora:",tarea_completa["Hora"],"Tarea:",tarea_completa["Tarea"])

def actualizar_tareas(all_todo):
    mostrar_tarea(all_todo)
    if not all_todo:
        return
    else:
        try:
            indice = int(input("Ingrese el valor del indice para actualizar la tarea: "))
            if(indice < 0 or indice >len(all_todo)):
                print("El indice no es valido")
            else:
                #fecha, hora y tarea
                fecha = input("Ingresa la fecha en formato DD/MM/YY: ")
                hora = input("Ingrese la hora en formato HH:MIN: ")
                tarea = input("Ingresa la tarea a realizar: ")

                #para actualizar
                all_todo[indice]["Fecha"] = fecha
                all_todo[indice]["Hora"] = hora
                all_todo[indice]["Tarea"] = tarea
                print("\nEl producto fue actualizado con exito")
        except:
            print("No se pudo actualizar con exito la tarea")

def eliminar_tarea(all_todo):
    mostrar_tarea(all_todo)
    if not all_todo:
        return
    else:
        try:
            indice = int(input("INgresa el valor del indice de la tarea a eliminar : "))
            if(indice < 0 or indice >len(all_todo)):
                print("El indice no es valido")
            else:
                print("Eliminando producto....")
                all_todo.pop(indice)
                print("El producto fue eliminado con exito")
                mostrar_tarea(all_todo)
                         

        except:
            print("Error intentando eliminar el producto")




def main():
    all_todo = []#almacenar las tareas, una lista
    while True:
        menu()
        opcion = int(input("Ingrese una opcion para continuar: "))
        match opcion:
            case 1:
                crear_tarea(all_todo)
            case 2:
                mostrar_tarea(all_todo)
            case 3:
                actualizar_tareas(all_todo)
            case 4:
                eliminar_tarea(all_todo)
            case 5:
                break


main()