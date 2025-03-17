# calcular el área de un cuadrado

def calcular_area_cuadrado(lado):
    return lado * lado

#Solicitar al usuario la longitud del lado del cuadrado
lado = float(input("Ingresa la longitud del lado del cuadrado:"))

#Clcular el área del cuadrado
area = calcular_area_cuadrado(lado)

#Mostar el resultado
print("El área del  cuadrado es {área} unidades cuadradas")
