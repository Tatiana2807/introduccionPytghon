import random 
#generar un numero aleatorio entre el 1 y el 100
numero_aleatorio = random.randint(1,100)
numero_usuario= 0
intentos= 0
while numero_usuario != numero_aleatorio:
    numero_usuario= int(input("Ingrese un número:")) 
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print("Muy bajo")
        elif numero_usuario > numero_aleatorio:
            print("Muy alto")
            print(f"Felicidades, adivinaste el número en {intentos} intentos")
            print("Fin del programa")
            
        