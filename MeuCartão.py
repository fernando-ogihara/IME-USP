meucartão = int(input('Digite o número do seu cartão: '))

cartãolido = 1 #tem que ser != 0 por causa do while, e digitando 0 ele para a busca nos numeros digitados
encontreiMeuCartão = False #false pq ainda não encontrei o meu cartão

while cartãolido != 0 and not encontreiMeuCartão:
    cartãolido = int(input('Digite o número do próximo cartão: '))
    if cartãolido == meucartão:
        encontreiMeuCartão = True #achei meu cartão
if encontreiMeuCartão:
    print ('Achei meu cartão!')
else:
    print('Não sei onde está o meu cartão!!')