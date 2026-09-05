def pedir_datos():
    numero_personas = int(input("Ingrese número de personas a cargo: "))
    salario_mensual = float(input("Ingrese el salario mensual: "))

    return numero_personas, salario_mensual

def calcular_linea(numero_personas, salario_mensual):

    linea = 'O'

    if numero_personas == 1:
        if salario_mensual <= 500:
            linea = 'P'
    elif 2 <= numero_personas <=4:
        if salario_mensual <= 750:
            linea = 'P'
    else:
        if salario_mensual <= 1000:
            linea = 'P'    

    print(f"Tipo de línea al que puede acceder: {linea}")


numero_personas, salario_mensual = pedir_datos()
calcular_linea(numero_personas, salario_mensual)
