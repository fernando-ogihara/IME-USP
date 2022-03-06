numero = n1 = int(input('Digite um número: '))

anterior = n1%10
n1 = n1//10
pos = 0
ad = False

while n1 > 0 and not ad:
    atual = n1%10

    if atual == anterior:
        ad = True
    else:
        pos += 1
        anterior = atual
        n1 = n1//10

if ad:
    print('sim')
else:
    print('não')
