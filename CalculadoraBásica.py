def calculadora ():
    print("Calculadora Básica")
    print("Seleccione una operacion:")
    print("1. suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingrese el número de la operación deseada: ")

    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingrese el primer número: " ))
        num2 = float(input("Ingrese el segundo número: " ))

        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")  
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}") 
                elif opcion == '3':
                    print(F"Resultado: {num1} * {num2} = {num1 * num2}")
                    elif opcion == '4':
                        print (f"Resultado: {num1} / {num2} = {num1 / num2}")
                        else:
                            print("Error: No se puede dividir por cero.")
                            else:
                            print("Opción no válida. Intente de nuevo.")
                            

