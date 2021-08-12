
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
