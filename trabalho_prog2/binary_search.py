
def buscaBin(x, l):
    """
    Busca binária alterada para lidar com números repetidos e em ordem decresente.
    Recebe um número 0.5 unidades menor que o desejado (no nosso caso, 60, que será 59.5)
    Ele irá retornar o endereço de algum número maior que isso (que pode ser o primeiro depois do desejado ou não)
    Após receber esse endereço, ele irá começar a procurar sequencialmente
    pelo número inteiro mais próximo de x (arredondando pra cima), assim obtendo quais notas estão acima ou igual a X
    """
    63
    left, right = 0, len(l) - 1
    while left <= right:
        
        middle = (left + right) // 2
        if l[middle] == x:
            return middle
        elif l[middle] < x:
            right = middle - 1
        else:
            left = middle + 1

    while l[middle] < (x + 0.5):
        middle -= 1
    return middle + 1