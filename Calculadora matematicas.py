#calculadora
import modulo_matematicas



print("""
 ___  ___       ___       ___________  __    __  
|   \/   |     /   \     |           ||  |  |  | 
|  \  /  |    /  ^  \    `---|  |----`|  |__|  | 
|  |\/|  |   /  /_\  \       |  |     |   __   | 
|__|  |__|  /  _____  \      |__|     |__|  |__| 
                    """)

limite = int(input("Cuantas veces desea usar la calculadora"))
i = 0


for i in range(limite):
    i= i+1
    print("Opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raiz cuadrada")
    print("7. Logaritmación")
    print("0. Salir")
    opcion = int(input("Selecciona la operacion a realizar "))
    if (opcion == 1):
        modulo_matematicas.suma()
    elif (opcion == 2):
        modulo_matematicas.resta()
    elif (opcion == 3):
        modulo_matematicas.multiplicacion()
    elif (opcion == 4):
        modulo_matematicas.division()
    elif (opcion == 5):
        modulo_matematicas.potenciacion()
    elif (opcion == 6):
        modulo_matematicas.raiz_cuadrada()
    elif (opcion == 7):
        modulo_matematicas.logaritmación()
    elif (opcion == 0):
        print("")
        break
    else:
        print("Opcion incorrecta")

print("Se cerrara el programa")