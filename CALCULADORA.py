#calculadora

limite = int(input("Cuantas veces desea usar la calculadora"))
i = 0

def suma():
    numero1 = int(input("Ingrese un numero "))
    numero2 = int(input("Ingrese un numero "))
    resultado = int(numero1) + int(numero2)
    print("El resultado es: ", resultado)

def resta():
    numero1 = int(input("Ingrese un numero "))
    numero2 = int(input("Ingrese un numero "))
    resultado = int(numero1) - int(numero2)
    print("El resultado es: ", resultado)

def multiplicacion():
    numero1 = int(input("Ingrese un numero "))
    numero2 = int(input("Ingrese un numero "))
    resultado = int(numero1) * int(numero2)
    print("El resultado es: ", resultado)

def division():
    numero1 = int(input("Ingrese un numero "))
    numero2 = int(input("Ingrese un numero ")) 
    resultado = int(numero1) / int(numero2)
    print("El resultado es: ", resultado)

for i in range(limite):
    i= i+1
    print("Opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
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
    elif (opcion == 0):
        print("")
    else:
        print("Opcion incorrecta")

print("Se cerrara el programa")