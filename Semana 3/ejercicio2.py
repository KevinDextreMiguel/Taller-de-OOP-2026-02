def ingresar_numero():
    numero = 0

    while numero < 2 or numero > 9:
        try:
            numero = int(input("Ingrese número entre 2 y 9: "))
        except Exception as e:
            print(f"Error al ingresar el número: {e}")

    return numero


def graficar():
    validar = 'S'
    contador = 0

    while validar == 'S' or validar == 's':
        filas = ingresar_numero()
        for i in range(filas): #filas
            for espacio in range(filas-i): #espacios
                print(end="  ") #espacio para que salgue hacia la derecha
            for j in range(i+1): #columnas
                print(end=" *")
            print() #se hace un salto de lìnea para imprimir la siguiete fila

        contador += 1

        validar = input("desea otros dibujos (S/N): ")

    print(f"Se han generado {contador} triángulos")


graficar()
