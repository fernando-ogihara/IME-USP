n1 = int(input('Por favor, entre com o número de segundos que deseja converter: '))
d = n1//86400
s1 = n1%86400
h = s1//3600
s2 = s1%3600
m = s2//60
s3 = s2%60
print('{} dias, {} horas, {} minutos e {} segundos.'.format(d, h, m, s3))
