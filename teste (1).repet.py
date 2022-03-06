# x = 1
# cont = 0
# while x < 3:
#     y = 0
#     while y <= 4:
#         # Iteração
#         y = y + 1
#     x = x + 1

# def desenha(linha):
#     while linha > 0:
#         coluna = 1
#         while coluna <= linha:
#             print('*', end = "")
#             coluna = coluna + 1
#         print()
#         linha = linha - 1
#
# desenha(5)

# def tabuada():
#     tab = 1
#     while tab <= 10:
#         i = 1
#         print(tab * i, end="\t")
#         i = i + 1
#         print()
#         tab = tab + 1
#
# tabuada()

# x = 2
# cont = 0
# while x >= 0:
#     y = 0
#     while y >= 4:
#         print(x*cont)
#         y = y + 1
#     x = x - 1

# x = 2
# cont = 0
# while x >= 0:
#     y = 0
#     while y <= 4:
#         print(x*cont)
#         y = y - 1
#     x = x - 1

altura = 5
linha = 1
while linha <= altura:
    print("*", end = "")
    coluna = 2
    while coluna < altura:
        if linha == 1 or linha == altura:
            print("*", end = '')
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    linha = linha + 1