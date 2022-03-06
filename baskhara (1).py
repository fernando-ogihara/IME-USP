import math
a = float(input('Digite um valor para A: '))
b = float(input('Digite um valor para B: '))
c = float(input('Digite um valor para C: '))

d = b**2 - (4*a*c)

if d == 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    print('A única raiz é {}.'.format(r1))
else:
    if d <0:
        print('Essa equação não possui raízes reais')
    else:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        print('A primeira raiz é {}.'.format(r1))
        print('A segunda raiz é {}.'.format(r2))