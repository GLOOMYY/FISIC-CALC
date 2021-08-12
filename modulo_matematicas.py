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
    numero1 = float(input("Ingrese numero "))
    numero2 = float(input("Ingrese base "))    
    resultado = math.log(numero1, numero2)
    print("el resultado es: ", resultado)
    