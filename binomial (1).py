def binomial (n,k):
    import math
    # n = int(input('Digite um valor para N: '))
    # k = int(input('Digite um valor para K: '))
    nk = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    print ('O valor binomial dos valores N = {} e K = {} é de {}'.format(n,k,nk))

binomial(20,10)

