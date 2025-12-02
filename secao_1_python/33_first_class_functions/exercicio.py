def dobro(*valores):
    return valores * 2


def somar(*valores):
    return sum(valores)


def calcular(operador, *valores):
    return operador(*valores)


print(calcular(somar, 10, 8, 9))


