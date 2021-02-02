n1 = int(input('digite um numero '))

soma = 0

while (n1 != 0):
    resto = n1%10 #resto da divisão por 10
    n1 = (n1 - resto)//10 #numero solicitado menos o resto e divisão inteira por 10
    #n1 assume a partir desse ponto outro valor, diferente do imputado pelo usuário
#    print(resto)
    soma = soma+resto
#
#    print(soma), teste para saber se o loop funciona, saidas 3,5 e 6
print(soma)

