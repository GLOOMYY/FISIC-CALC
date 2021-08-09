#calculadora fisica
import os

limite = int(input("Cuantas veces desea usar la calculadora "))
i = 0

def distancia():
    print("Distancia")
    v = float(input("Ingrese la velocidad "))
    t = float(input("Ingrese el tiempo "))
    d = v * t
    print("El resultado es: ", d )

def velocidad():
    print("Velocidad")
    d = float(input("Ingrese la distancia "))
    t = float(input("Ingrese el tiempo "))
    v = d / t
    print("El resultado es: ", v)

def tiempo():
    print("Tiempo")
    d = float(input("Ingrese la distancia "))
    v = float(input("Ingrese la velocidad "))
    t = d / v
    print("El resultado es: ", t)

def km_a_m():
    print("Kilometros a metros")
    km = float(input("Ingrese los kilometros "))
    m = km * 1000
    print("El resultado es: ", m ," metros")

def hrs_a_s():
    print("Horas a segundos")
    h = float(input("Ingrese las horas "))
    s = h * 3600
    print("El resultado es: ", s, " segundos")

def error_absoluto():
    print("Error absoluto")
    valor_teorico = float(input("Ingrese el valor teorico "))
    valor_experimental = float((input("Ingrese el valor experimental ")))
    resultado = abs(valor_teorico - valor_experimental)
    print("El error absoluto es: ", resultado)

def error_relativo():
    print("Error relativo")
    error_absolut = float(input("Ingrese el error absoluto "))
    valor_teorico = float(input("Ingrese el valor teorico "))
    resultado = error_absolut/valor_teorico
    print("El error relativo es: ", resultado)

def porcentaje_error():
    print("Porcentaje de error")
    error_relati = float(input("Ingreese el error relativo "))
    resultado = error_relati*(100/100)
    print("El porcentaje de error es de: ", resultado, "%")


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
        distancia()
    elif (opcion == 2):
        velocidad()
    elif (opcion == 3):
        tiempo()
    elif (opcion == 4):
        km_a_m()
    elif (opcion == 5):
        hrs_a_s()
    elif (opcion == 6):
        print("Tipos de error")
        print("1. Error absoluto")
        print("2. Error relativo")
        print("3. Porcetaje de error")
        print("0. Volver")
        opcion_error = int(input("Seleccione la operacion a realizar "))
        os.system ("cls") 
        if (opcion_error == 1):
            error_absoluto()
        elif (opcion_error == 2):
            error_relativo()
        elif (opcion_error == 3):
            porcentaje_error()
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