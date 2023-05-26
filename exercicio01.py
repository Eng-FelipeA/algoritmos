def contar_animais(cabecas, patas):
    coelhos = (patas - 2*cabecas)/2
    patos = cabecas - coelhos
    return patos, coelhos
cabecas = int(input("Digite a quantidade de cabeças: "))
patas = cabecas * 3 + 1
print(contar_animais(cabecas,patas))
