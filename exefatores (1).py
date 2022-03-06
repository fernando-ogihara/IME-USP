n = int(input('Digite um número inteiro: '))

fator = 2
multi = 0
tot = 0

for i in range(1,n+1):
    if n%i == 0:
        tot += 1
if tot == 2:
    print('Número {} é PRIMO.'.format(n))
else:
    print('Número {} é NÃO É PRIMO.'.format(n))

while n > 1: #quando chegar no 1 o laço para
    while n%fator == 0: #para sabermos a quantidade precisamos saber se o resto é igual a 0
        multi = multi + 1 #somamos a multiplicidade a 1
        n = n/fator #
    if multi > 0: #devemos printar apenas os numeros que possuel multiplicidade
        print('Fator = ', fator,'Multiplicidade = ',multi)
    fator += 1 #soma-se 1 para saber se é divisivel por um novo fator
    multi = 0 #a multiplicidade tem que retornar a 0


