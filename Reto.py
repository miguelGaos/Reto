# Defino
from typing import Counter
contador = 0
Estado = True
datosContadorExterno = [1] * 11
numeros_repetidos = None
frecuencias = [0] * 10

while True:
    print("\n--- MENÚ ---")
    print("1.Solicitar un número del 0 al 9")
    print("2.No elegidos")
    print("3.Salir del programa...")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            try:
                num = int(input("Introduce un número del 0 al 9: "))
                if 0 <= num <= 9:
                    frecuencias[num] += 1
                    break
                else:
                    print("Número fuera de rango. Debe estar entre 0 y 9.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    elif opcion == "2":
        print("Números no elegidos: ", end="")
        for i in range(10):
            if frecuencias[i] == 0:
                print(i, end=" ")
        print()


    frecuencia = Counter(datosContadorExterno)
    numeros_repetidos = [numero for numero , cantidad in frecuencia.items() if cantidad > 1]
    print("La frecuencia es :", numeros_repetidos)
