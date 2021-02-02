print('=-'*30)
print('Digite valores a serem somados e para terminar digite 0.')
print('=-'*30)

soma = 0

valor = 1
while valor!=0:
    valor = int(input('Digite um valor a ser somado: '))    
    soma = soma+valor
print('A soma dos valores digitados é',soma)
