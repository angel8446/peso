def calcular_peso(masa):
    gravedad_tierra = 9.8
    gravedad_luna = 1.6
    gravedad_marte = 3.7

    peso_tierra = masa * gravedad_tierra
    peso_luna = masa * gravedad_luna
    peso_marte = masa * gravedad_marte

    return peso_tierra, peso_luna, peso_marte


try:
    masa = float(input("Ingresa la masa en kilogramos: "))

    peso_tierra, peso_luna, peso_marte = calcular_peso(masa)

    print("Peso en la Tierra: {} newtons".format(peso_tierra))
    print("Peso en la Luna: {} newtons".format(peso_luna))
    print("Peso en Marte: {} newtons".format(peso_marte))
except ValueError:
    print("Error: Ingresa un valor numérico válido para la masa.")
