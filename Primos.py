n = int(input('Digite um número inteiro: '))
tot = 0
for i in range (1,n+1):
    if n%i == 0:
        print('\33[7;32m',i, end=' ')
        tot += 1
    else:
        print('\33[7;31m',i, end=' ')


if tot == 2:
    print('\33[m\nprimo')
else:
    print('\33[m\nnão primo')



