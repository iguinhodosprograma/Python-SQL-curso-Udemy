def Divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor #Não usar diferentes tipos de variáveis em uma função (string, int, etc) pode dar alguns erros no código
    else:
        return "You fool!"
        
result = Divide(15, 2) * 5
print(result)