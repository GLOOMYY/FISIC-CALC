#calculadora fisica

limite = int(input("Cuantas veces desea usar la calculadora "))
i = 0

def distancia():
    v = int(input("Ingrese la velocidad "))
    t = int(input("Ingrese el tiempo "))
    d = v * t
    print("El resultado es: ", d )

def velocidad():
    d = int(input("Ingrese la distancia "))
    t = int(input("Ingrese el tiempo "))
    v = d / t
    print("El resultado es: ", v)

def tiempo():
    d = int(input("Ingrese la distancia "))
    v = int(input("Ingrese la velocidad "))
    t = d / v
    print("El resultado es: ", t)

def km_a_m():
    km = int(input("Ingrese los kilometros "))
    m = km * 1000
    print("El resultado es: ", m ," metros")

def hrs_a_s():
    h = int(input("Ingrese las horas "))
    s = h * 3600
    print("El resultado es: ", s, " segundos")

for i in range(limite):
    i= i+1
    print("Opciones")
    print("1. Distancia teniendo velocidad y tiempo")
    print("2. Velocidad teniendo distancia y tiempo")
    print("3. Tiempo teniendo velocidad y distancia")
    print("4. Kilometros a metros")
    print("5. Horas a segundos")
    print("0. Salir")
    opcion = int(input("Selecciona la operacion a realizar "))
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
    elif (opcion == 0):
        print("")
    else:
        print("Opcion incorrecta")

print("Se cerrara el programa")