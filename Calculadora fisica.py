#calculadora fisica
import os
import modulo_fisica


print("""
 _______  __       _______  __    ______      ___
|   ____||  |     /       ||  |  /      |    /   \     
|  |__   |  |    |   (----`|  | |  ,----'   /  ^  \    
|   __|  |  |     \   \    |  | |  |       /  /_\  \   
|  |     |  | .----)   |   |  | |  `----. /  _____  \  
|__|     |__| |_______/    |__|  \______|/__/     \__\ 
                    """)

limite = int(input("Cuantas veces desea usar la calculadora "))
i = 0


for i in range(limite):
    i= i+1
    print("Opciones")
    print("1. Distancia teniendo velocidad y tiempo")
    print("2. Velocidad teniendo distancia y tiempo")
    print("3. Tiempo teniendo velocidad y distancia")
    print("4. Kilometros a metros")
    print("5. Horas a segundos")
    print("6. Tipos de error")
    print("0. Salir")
    opcion = int(input("Seleccione la operacion a realizar "))
    os.system ("cls") 
    if (opcion == 1):
        modulo_fisica.distancia()
    elif (opcion == 2):
        modulo_fisica.velocidad()
    elif (opcion == 3):
        modulo_fisica.tiempo()
    elif (opcion == 4):
        modulo_fisica.km_a_m()
    elif (opcion == 5):
        modulo_fisica.hrs_a_s()
    elif (opcion == 6):
        print("Tipos de error")
        print("1. Error absoluto")
        print("2. Error relativo")
        print("3. Porcetaje de error")
        print("0. Volver")
        opcion_error = int(input("Seleccione la operacion a realizar "))
        os.system ("cls") 
        if (opcion_error == 1):
            modulo_fisica.error_absoluto()
        elif (opcion_error == 2):
            modulo_fisica.error_relativo()
        elif (opcion_error == 3):
            modulo_fisica.porcentaje_error()
        elif (opcion_error == 0):
            print("")
        else:
            print("Opcion equivocada")
    elif (opcion == 0):
        print("")
        break
    else:
        print("Opcion incorrecta")

print("Se cerrara el programa")