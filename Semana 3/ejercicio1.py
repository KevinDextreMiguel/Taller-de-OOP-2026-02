def ingresar_codigo():

    codigo = 0

    while len(str(codigo)) != 10:
        try:
            codigo = int(input("Ingrese código generado: "))
        except Exception as e:
            print(f"Error al ingresar el código: {e}")

    return codigo


def descomponer():
    codigo_generado = str(ingresar_codigo())
    # [inicio,final,paso]  -> TTTTHHMMSS  TTTT HH MM SS
    TTTT = codigo_generado[:4] 
    HH = int(codigo_generado[4:6])
    MM = int(codigo_generado[6:8])
    SS = int(codigo_generado[8:])

    print(f"Código del trabajador: {TTTT}")
    print(f"Hora de entrada: {HH}")
    print(f"Minuto de entrada: {MM}")
    print(f"Segundos de entrada: {SS}")



descomponer()
