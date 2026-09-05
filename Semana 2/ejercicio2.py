def pedir_numero():
    numero = int(input("Ingrese un número: "))
    return numero

def separar_numeros(numero):
    numero_cadena = str(numero)

    u = numero_cadena[2]
    d = numero_cadena[1]
    c = numero_cadena[0]

    return u,d,c

def realizar_operaciones(n1,n2):
    u1,d1,c1 = separar_numeros(n1)
    u2,d2,c2 = separar_numeros(n2)

    n1_invertido = int(u1 + d1 + c1)
    n2_invertido = int(u2 + d2 + c2)

    sumar_todo = n1 + n2 + n1_invertido + n2_invertido

    primero_original_y_segundo_invetido = int(str(n1) + str(n2_invertido))

    print(f"u1={u1}, d1={d1}, c1={c1}, u2={u2}, d2={d2}, c3={c2}")
    print(f"{n1_invertido}, {n2_invertido}")
    print(f"La suma de todos los números originales y invertidos: {sumar_todo}")
    print(f"El número formado por el primero original y el segundo invertido: {primero_original_y_segundo_invetido}")


n1 = pedir_numero()
n2 = pedir_numero()

realizar_operaciones(n1,n2)
