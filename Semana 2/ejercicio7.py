def pedir_numero(minimo,maximo):

    numero = 0
    while numero < minimo or numero > maximo:
        try:
            numero = int(input("Ingrese un número: "))                
        except ValueError:
                print("Error: Debe ingresar un número entero.")

    return numero


def calcular(n):
    for i in range(n):
        numero =pedir_numero(1,1000)

        if numero % 2 == 0:
            print("Es par")
        else:
            print("Es impar")


n = pedir_numero(1, 5)
calcular(n)
