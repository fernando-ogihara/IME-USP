import math
a=float(input('digite um valor para A '))
b=float(input('digite um valor para B '))
c=float(input('digite um valor para C '))

delta = (b**2)-(4*a*c)

if delta == 0:
    raiz1 = (-b+math.sqrt(delta))/(2*a)
    print('a raiz desta equação é {}'.format(raiz1))
else:
    if delta<0:
        print('Esta equação não possui raízes reais')
    else:
        raiz1 = (-b+(math.sqrt(delta))/(2*a))
        raiz2 = (-b-(math.sqrt(delta))/(2*a))
        if delta>0 and raiz1<raiz2:
            print('as raízes da equação são {} e {}'.format(raiz1,raiz2))
        else:
            print('as raízes da equação são {} e {}'.format(raiz2, raiz1))
