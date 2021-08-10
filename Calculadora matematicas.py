#calculadora
import cmath
import math


def suma():
    numero1 = float(input("Ingrese un numero "))
    numero2 = float(input("Ingrese un numero "))
    resultado = numero1 + numero2
    print("El resultado es: ", resultado)

def resta():
    numero1 = float(input("Ingrese un numero "))
    numero2 = float(input("Ingrese un numero "))
    resultado = numero1 - numero2
    print("El resultado es: ", resultado)

def multiplicacion():
    numero1 = float(input("Ingrese un numero "))
    numero2 = float(input("Ingrese un numero "))
    resultado = numero1 * numero2
    print("El resultado es: ", resultado)

def division():
    numero1 = float(input("Ingrese un numero "))
    numero2 = float(input("Ingrese un numero ")) 
    resultado = numero1 / numero2
    print("El resultado es: ", resultado)

def potenciacion():
    numero1 = float(input("Ingrese el numero que desea potenciar "))
    numero2 = float(input("Ingrese el numero al que lo desea elevar "))
    resultado = pow(numero1,numero2)
    print("El resultado es: ", resultado)

def raiz_cuadrada():
    numero1 = float(input("Ingrese al numero que le desea sacar la raiz cuadrada "))
    if (numero1 > 0) :
        resultado = math.sqrt(numero1)
        print("el resultado es: ", resultado)
    else:
        resultado = cmath.sqrt(numero1)
        print("el resultado es: ", resultado)
    
def logaritmación():
    numero1 = float(input("Ingrese numero"))
    numero2 = float(input("Ingrese base"))    
    resultado = math.log(numero1, numero2)
    print("el resultado es: ", resultado)

print("""
 ___  ___       ___       ___________  __    __  
|   \/   |     /   \     |           ||  |  |  | 
|  \  /  |    /  ^  \    `---|  |----`|  |__|  | 
|  |\/|  |   /  /_\  \       |  |     |   __   | 
|  |  |  |  /  _____  \      |  |     |  |  |  | 
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
        suma()
    elif (opcion == 2):
        resta()
    elif (opcion == 3):
        multiplicacion()
    elif (opcion == 4):
        division()
    elif (opcion == 5):
        potenciacion()
    elif (opcion == 6):
        raiz_cuadrada()
    elif (opcion == 7):
        logaritmación()
    elif (opcion == 0):
        print("")
        break
    else:
        print("Opcion incorrecta")

print("Se cerrara el programa")