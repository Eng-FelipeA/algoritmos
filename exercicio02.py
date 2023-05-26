def ehprimo(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
                break
        else:
            return True
    elif number == 0:
        return False
    elif number == 1:
        return False
    else:
        return False
def listprimo(number):
    nprimos = []
    num = 2
    while len(nprimos) < number:
        if ehprimo(num):
            nprimos.append(num)
        num += 1
    return nprimos

def somalista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

y = int(input("Informe os dois últimos números do seu RA: "))
print(f"Y {ehprimo(y)} é primo.\nY*2+5 = {y*2+5}.\nValor da soma de todos os números: {somalista(listprimo(y*2+5))}")
print(listprimo(y*2+5))