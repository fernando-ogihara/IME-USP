linha = 1
coluna = 1

while linha <= 10:
    while coluna <=10:
        print('{} x {} ='.format(linha,coluna), linha*coluna, end='\t') #entre aspas podemos colocar só espaço ou utilizar
        #\t para ficar mais clean
        coluna +=1
    linha += 1
    print ()
    coluna = 1