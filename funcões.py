# def soma (x,y):
#     return (x + y)
#
# print(soma(10,10))

# repetir = 'S'
# tot = 0
# i = 0
#
# while repetir == 'S':
#     x = int(input('Digite um valor para X: '))
#     y = int(input('Digite um valor para Y: '))
#     n = soma(x,y)
#
#     for i in range(1,n+1):
#         if n % i == 0:
#             tot += 1
#     if tot == 2:
#         print('PRIMO')
#     else:
#         print('NÃO É PRIMO')
#
#     repetir = input('Deseja somar outros valores, S ou N? ').upper()
#
#
# # print(soma(2*4*1,soma(10,10,10),soma(1,1,1)))

# def troca(x, y):
#     aux = x
#     x = y
#     y = aux
#
# x = 10
# y = 20
# troca (x,y)
# print("x =", x,"e y =",y)

# x = input('x:')
# y = input('y:')
# z = input('z:')
#
# s = x+y+z
#
# print(x,y,z,a,s)
#
# def totalCaracteres (x, y, z):
#         return len(x,y,z)
#
# print(totalCaracteres(fe,fe,fe))

# import math
#
# def suspense(x):
#     return math.sqrt(x)
#
# print(suspense(25))

def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x

print(leitura())

# def multiplica (a,b):
#     return a * b
#
# print(multiplica(4,5))