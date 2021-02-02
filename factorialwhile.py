def fator():

    import math
    user = int(input('Digite um número inteiro para saber o seu factorial: '))
    while user > 0:
        fac = math.factorial(user)
        print ('O factorial de {} é'.format(user),fac)
        user = int(input('Digite um número inteiro para saber o seu factorial: '))

fator()