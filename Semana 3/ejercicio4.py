import random

def ingresar_numero():
    numero = 0

    while numero < 1 or numero > 40:
        try:
            numero = int(input("Ingrese número entre 1 y 40: "))
        except Exception as e:
            print(f"Error al ingresar el número: {e}")

    return numero


def generar_numeros(n, lista):
    for i in range(n):
        numero = random.randint(1,9)
        lista.append(numero)

def mostrar_valores(lista):
    for valor in lista:
        print(valor, end=" ")
    print()


def repeticiones(lista):
    lista_unicos = []
    for valor in lista:
        if valor not in lista_unicos:
            lista_unicos.append(valor)
            cantidad = lista.count(valor)
            print(f"cantidad de {valor} en la lista: {cantidad}")

def sumar_1_primos(lista):
    lista_primos = [2,3,5,7]
    for i, valor in enumerate(lista):
        if valor in lista_primos:
            lista[i] = valor + 1 # lista[i] = lista[i] + 1


lista = []
n = ingresar_numero()
generar_numeros(n, lista)
mostrar_valores(lista)
repeticiones(lista)
sumar_1_primos(lista)
mostrar_valores(lista)
