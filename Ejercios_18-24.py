import math
def numero_entero (x):
    conteo = 1
    suma=0
    while conteo<=100:
        suma+= x + conteo 
        ##print(suma)
        conteo+= 1
    print(suma)
    return suma

def euros_dolares(e):
    dolares = 1.1301 * e
    print (f"{e} euros son aproximadamente {dolares} dolares")
    return dolares

def area_rectangulo(b,h):
    area_reg = b * h
    print(f"El área del regtángulo es igual a {area_reg}m^2")

def mayor_menor(a,y):
    if a<y:
        print(f"{y} es el número mayor y {a} es el número menor")
    elif y<a:
        print(f"{a} es el número mayor y {y} es el número menor")
    else:
        print("Los numeros son iguales")

def impares(n):
    rango = 0 - n
    while rango < n:
        if rango%2 != 0:
            print(rango)
        rango+= 1

def euclides(x,y):
    mcd = math.gcd(x,y)
    print(f"El máximo común divisor de {x} y {y} es {mcd}")
    return mcd

def cuadratica(a,b,c):
    discri = b**2 - (4*a*c)
    print(discri)
    if discri>0:
        soluciones1= (-b + math.sqrt(discri)) / (2*a)
        soluciones2= (-b - math.sqrt(discri)) / (2*a)
        print(f"Las soluciones del sistema son: X1= {soluciones1} y X2= {soluciones2}")
    elif discri==0:
        sol = (-b)/(2*a)
        print(f"La solución del sistema es: {sol}")
    else:
        print("No tiene soluciones reales")
##Menu 
pregun = (int(input("Dime que ejercicio quieres realizar, para esto dame un número del 1-7\n")))

if(pregun==1):
    numero_entero(int(input("Introduce un número entero, para hacer la suma con los siguiente cien numeros \n")))
elif(pregun==2):
   euros_dolares(float(input("Intoduce la cantidad de euros que quieres convertir a dolres \n")))
elif(pregun == 3):
    area_rectangulo(float(input("Dime la b del rectangulo en m\n")), float(input("La h del mismo en m\n")))
elif(pregun == 4):
    mayor_menor(float(input("Introduce un número \n")), float(input("Ahora otro para saber cual es el mayor y menor\n")))
elif(pregun == 5):
    impares(int(input("Introduce un número entero \n")))
elif(pregun == 6):
    euclides(int(input("Introduce un número entero \n")),int(input("cual es el otro número para hallar el mcd \n")))
elif(pregun == 7):
    print("Dame los valores de los coeficientes de la ecuación cuadratica")
    cuadratica(int(input("Introduce a \n")),int(input("ahora b \n")),int(input("y c \n")))
else:
    print("Selecciono una opción invalida")
