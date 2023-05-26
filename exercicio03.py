def calcular(numero):
    soma = 0
    multiplicacao = 1
    for digito in numero:
        digitoInt = int(digito)
        soma = soma + digitoInt
        multiplicacao = multiplicacao * digitoInt
    return soma, multiplicacao
numero_str = input("Digite um número positivo: ")
soma, multiplicacao = calcular(numero_str)
print("Soma dos dígitos:", soma)
print("Multiplicação dos dígitos:", multiplicacao)