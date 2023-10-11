#Crear juego de preguntas
# que tenga dos opciones 1.jugar 2.salir
#si selecciona 1 el usuario podra responder las preguntas
#que el sistema le muestre de forma aleatoria guardando cuantas
#respuestas esta contestando bien
#2. salir
#cuando termine el programa debe decirle cuantas respuestas acertop
# las preguntas son creadas por el dev
"""
{
    "question" :"pregunta1",
    "opciones": ["opcion1","opcion2","opcion3"]
    "respuesta" : "opcion2"
}

]
"""

def menu():
    input("Presiona enter para continuar")
    print("""
        \n--------Test Game Riwi---------\n
          1). Jugar
          2). Salir
          3). Modo admin
""")


def jugar(preguntas):

    #inicializamos el contador
    acomulador = 0
    #mostramos la pregunta
    for pregunta in preguntas:
        print(pregunta["Pregunta"])
        #mostramos las opciones
        for indice, valor in enumerate(pregunta["Opciones"]):
            print("Opcion ",indice, ". - ",valor)
        respuesta = int(input("Ingresa el numero de la respuesta correcta: "))
        if respuesta == pregunta["Respuesta"]:
            print("Respuesta correcta\n")
            acomulador = acomulador+1
        else:
            print("Respuesta incorrecta\n")
    
    print("En total tienes ",acomulador," respuestas correctas")
    porcentaje_ganadas = (acomulador*100)/len(preguntas)
    if(porcentaje_ganadas > 50):
        print(f"\n¡Felicidades! Has superado el 50% de respuestas correctas ({porcentaje_ganadas}% obtenido).")
    else:
        print(f"Lamentamos que hayas perdido en esta oportunidad, necesitas al menos el 51% de respuestas correctas y obtuviste {porcentaje_ganadas}")  
    
def menu_admin(preguntas):
    print("""
``````````WELCOME TO THE ADMIN MODE``````
          1)Create a question
          2) Update a question
          3) Delete a question
          4). EXIT ADMIN MODE
""")


def modo_admin(preguntas):
    opcion = int(input("Ingresa la opcion deseada: "))

    while True:
        menu_admin(preguntas)
        opcion = int(input("Ingresa la opcion deseada: "))
        match opcion:
            case 1:
                print("````````CREATE A QUESTION``````")
                try:
                    #crear pregunta: pregunta, opciones, respuestas
                    #creamos el diccionario
                    new_question = {}
                    new_question["Pregunta"] = input("Ingresa la nueva pregunta: \n")
                    new_question["Opciones"] = []

                    pregunta = input("Ingresa la pregunta\n")
                    opcion = input()

                except:
    
    




def main():
    preguntas = [
            {
                "Pregunta": "Cuantos continentes hay",
                "Opciones": ["5","6","7","8"],
                "Respuesta": 1
            },
            {
                "Pregunta": "Cuantos departamentos tiene Colombia",
                "Opciones": ["30","31","32","33"],
                "Respuesta": 2
            },
            {
                "Pregunta": "Donde se ubica Michigan",
                "Opciones": ["Inglaterra","Grecia","Colombia","EE.UU"],
                "Respuesta": 3
            },
            {
                "Pregunta": "Cuantas regiones tiene Colombia",
                "Opciones": ["3","4","5","6"],
                "Respuesta": 3
            },
            {
                "Pregunta": "Cual es el presidente de EE.UU",
                "Opciones": ["Joe Biden","Donald Trum","Michael Pense"],
                "Respuesta": 0
            }
    ]
    while True:
        
        
        menu()
        opcion = int(input("Ingresa una opcion: "))

        match opcion:
            case 1:
                print("lets go to play")
                jugar(preguntas)
                
            case 2:
                break
            case 3:
                menu_admin(preguntas)
                modo_admin(preguntas)
    
main()
