def menu():
    print("""
=========================================
==============MENU DE OPCIONES===========
========================================
0)Listar municipios.
1)Lectura de datos
2)Municipio que mas toneladas/dia genera
3)Promedio de toneladas de basura/dia
4)Promedio de toneladas de basura/mes
5)Mayor problema ambiental
6)Menor problema ambiental
7)Promedio de olores ofensivos
8)Promedio de creacion asentamientos ilegales
9)Mayor problema ambiental general
10)Terminar
""")
    
def Lectura_datos(all_municipios):
    
    try:
        cantidad_municipios = int(input("Ingresa la cantidad de municipios: "))
        for i in range(1,cantidad_municipios+1):
            print("\nMUNICIPIO ",i)
            nombre_municipio = input("Ingresa el nombre del municipio: ")
            cantidad_toneladas = int(input("Ingresa la cantidad de toneladas de residuos x dia: "))
            
            #solicitamos los porcentajes
            print("PORCENTAJE DE CONTAMINACION")
            olores_ofensivos = float(input("Ingresa el porcentaje de contaminacion de los Olores Ofensivos:  "))
            asentamientos_ilegales = float(input("Ingresa el porcentaje de contaminacion de la creacion de asentamientos ilegales: "))
            corrientes_hidricas = 100-asentamientos_ilegales-olores_ofensivos
            #LA SUMA DEBE DAR 100
            
            #creamos el diccionario con los datos proporcionados
            problemas_ambientales = {
                "Nombre": nombre_municipio,
                "Toneladas":cantidad_toneladas,
                "Porcentajes": {
                    "Olores_ofensivos":olores_ofensivos,
                    "Asentamientos_ilegales":asentamientos_ilegales,
                    "Corrientes_hidricas":corrientes_hidricas
                }
            }
            #agregar el diccionario problemas_ambientales a la lista all municipios
            all_municipios.append(problemas_ambientales)

            print("\nDATOS INGRESADOS\n","Nombre: ",problemas_ambientales["Nombre"],"\n","Cantidad de toneladas: ",problemas_ambientales["Toneladas"], "\nPorcentajes: \n")
            
            #el diccionario["clave"].items() lo que hace es que con clave, valor recorre todo el diccionario
            for problema, porcentaje in problemas_ambientales["Porcentajes"].items():
                print(f"{problema}: {porcentaje}")

            print("Datos del municipio ingresados con exito....")
    except Exception as e:
        print(f"ERROR AL INGRESO DE DATOS: {e}")


def Municipio_mas_toneladas(all_municipios):
    if not all_municipios:
        print("No hay municipios registrados")
    
    #se va almacenando la cantidad mayor de tonelada
    max_toneladas = 0
    #se almacena el municipio con mayor tonelada
    municipio_max_toneladas = ""

    for municipio in all_municipios:
        toneladas = municipio["Toneladas"]
        if toneladas > max_toneladas:
            max_toneladas = toneladas
            municipio_max_toneladas = municipio["Nombre"]

    if municipio_max_toneladas:
        print(f"""
    El municipio con mas toneladas es {municipio_max_toneladas}
    El total de toneladas por {municipio_max_toneladas} fue {max_toneladas}
""")

def mostrar_municipios(all_municipios):
    contador = 1
    print("\nMunicipios Ingresados :\n")
    for i in all_municipios:
        print("Municipio ",contador,": ",i["Nombre"])
        contador = contador+1

def Promedio_basura_dia(all_municipios):

    try:
        od  = 0
        #recorre todos los municipios
        for i in all_municipios:
            #accede al valor de toneladas y los va sumando
            od = od + i["Toneladas"]
            
        cantidad_municipios = len(all_municipios)
        promedio_ton_mun = od/cantidad_municipios

        print(f"""
        El promedio de toneladas de basura por dia es {promedio_ton_mun}
        """)
    except Exception as e:
        print(f"ERROR AL SACAR PROMEDIO error:{e}")

def Promedio_basura_mes(all_municipios):
    try:
        x = 0
        for i in all_municipios:
            x = x + i["Toneladas"]*30
        promedio_ton_mes = x/len(all_municipios)
        print(f"""
            El promedio de toneladas de basura por mes es {promedio_ton_mes}
            """)

    except Exception as e:
        print(f"ERROR AL SACAR EL PROMEDIO: {e}")


def mayor_problema_ambiental(all_municipios):
        try:
                suma_problematicas_olores = 0
                suma_problematicas_asentamientos = 0
                suma_problematicas_corrientes = 0
                #correrr todo los municipios
               
                for i in all_municipios:
                    suma_problematicas_olores = suma_problematicas_olores+i["Porcentajes"]["Olores_ofensivos"]
                    suma_problematicas_asentamientos = suma_problematicas_asentamientos+i["Porcentajes"]["Asentamientos_ilegales"]
                    suma_problematicas_corrientes = suma_problematicas_corrientes+i["Porcentajes"]["Corrientes_hidricas"]
                
                if suma_problematicas_corrientes>suma_problematicas_asentamientos and suma_problematicas_corrientes>suma_problematicas_olores:
                    print(f"El mayor problema ambiental es Corrientes hidricas con {suma_problematicas_corrientes}%")
                if suma_problematicas_olores>suma_problematicas_asentamientos and suma_problematicas_olores>suma_problematicas_corrientes:
                    print(f"El mayor problema ambiental es Corrientes hidricas con {suma_problematicas_olores}%")
                if suma_problematicas_asentamientos>suma_problematicas_olores and suma_problematicas_asentamientos>suma_problematicas_corrientes:
                    print(f"El mayor problema ambiental es Corrientes hidricas con {suma_problematicas_asentamientos}%")       
        except Exception as e:
            print("ERROR ENCONTRANDO EL MAYOR PROBLEMA: ERROR:",e)
        

def menor_problema_ambiental(all_municipios):
    try:

        suma_problematicas_olores = 0
        suma_problematicas_asentamientos = 0
        suma_problematicas_corrientes = 0
        #correrr todo los municipios
           
        for i in all_municipios:
            suma_problematicas_olores = suma_problematicas_olores+i["Porcentajes"]["Olores_ofensivos"]
            suma_problematicas_asentamientos = suma_problematicas_asentamientos+i["Porcentajes"]["Asentamientos_ilegales"]
            suma_problematicas_corrientes = suma_problematicas_corrientes+i["Porcentajes"]["Corrientes_hidricas"]
            
        if suma_problematicas_asentamientos<suma_problematicas_corrientes and suma_problematicas_asentamientos<suma_problematicas_olores:
            print(f"El menor problema ambiental es Asentamientos ilegales con {suma_problematicas_asentamientos}%")
        if suma_problematicas_olores<suma_problematicas_asentamientos and suma_problematicas_olores<suma_problematicas_corrientes:
            print(f"El menor problema ambiental es Olores ofensivos con {suma_problematicas_olores}%")
        if suma_problematicas_corrientes<suma_problematicas_asentamientos and suma_problematicas_corrientes<suma_problematicas_olores:
            print(f"El menor problema ambiental es Corrientes hidricas con {suma_problematicas_corrientes}%")     
        

    except Exception as e:
        print("ERROR ENCONTRANDO EL MUNICIPIO CON MENOR PROBLEMA AMBIENTAL :ERROR",e)

def promedio_olores_ofensivos(all_municipios):
    #suma olores/ cantidad olores
    suma_olores_ofensivos = 0
    contador = 0
    promedio = 0
    for i in all_municipios:
        suma_olores_ofensivos = suma_olores_ofensivos + i["Porcentajes"]["Olores_ofensivos"]
        contador = contador+1
    promedio = suma_olores_ofensivos/contador


    print(f"El promedio de olores ofensivos es {promedio}")

def promedio_asentamientos_ilegales(all_municios):
    suma_porcentajes  = 0
    contador = 0
    promedio = 0
    for i in all_municios:
        suma_porcentajes = suma_porcentajes + i["Porcentajes"]["Asentamientos_ilegales"]
        contador = contador +1
    promedio = suma_porcentajes/contador
    print(f"El promedio de los Asentamientos ilegales es {promedio}")


def main():

    all_municipios = []

    while True:
        menu()
        opcion = int(input("Ingresa una opcion: "))
        if opcion == 0:
            mostrar_municipios(all_municipios)
        if opcion == 1:
            Lectura_datos(all_municipios)
        if opcion == 2:
            Municipio_mas_toneladas(all_municipios)
        if opcion == 3:
            Promedio_basura_dia(all_municipios)
        if opcion == 4:
            Promedio_basura_mes(all_municipios)
        if opcion == 5:
            mayor_problema_ambiental(all_municipios)
        if opcion == 5:
            menor_problema_ambiental(all_municipios)
        if opcion == 6:
            menor_problema_ambiental(all_municipios)
        if opcion == 7:
            promedio_olores_ofensivos(all_municipios)
        if opcion == 8:
            promedio_asentamientos_ilegales(all_municipios)
        elif(opcion == 10):
            break



main()