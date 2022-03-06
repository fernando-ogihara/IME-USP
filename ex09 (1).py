n1 = int(input('Digite um número '))
x = n1%3
y = n1%5

if x==0 and y == 0 :
    print('FizzBuzz')
else:
    print(n1)
