decrescente = True #ja colocamos a variavel bolena como TRUE
anterior = int(input('Digite o primeiro número: '))
proximo=1 #se for 0 o programa nem inicia

while (proximo != 0) and decrescente: #começam as condições
    proximo = int(input('Digite o próximo número: '))
    if proximo > anterior: #se essa condição for verdade, a var boleana vira FALSA
        decrescente = False #variavel vira FALSA
    anterior = proximo
if decrescente:
    print ('A sequencia está em ordem decrescente')
else:
    print('A sequencia não está em ordem decrescente')
