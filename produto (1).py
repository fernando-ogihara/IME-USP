tamanho = int(input('Digite a quantidade de números a serem multiplicados: '))
produto = 1
i = 0

while i < tamanho:
    num = int(input('Digite o valor: '))
    produto = produto*num
    i = i + 1
print(produto)