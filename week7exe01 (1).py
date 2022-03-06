# def retangulo():
#
#     largura = int(input('digite a largura: '))
#
#     while largura > 0 :
#         altura = int(input('digite a altura: '))
#         print(altura*'{}\n'.format(largura*'#'),end='')
#         largura = int(input('digite a largura: '))
#
# retangulo()

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
linha = 1

while linha <= altura:
    print('#',end='')
    coluna=2
    while coluna < largura:
        print('#',end='')
        coluna += 1
    print('#')
    linha = linha + 1