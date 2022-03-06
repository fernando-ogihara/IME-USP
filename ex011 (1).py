import math
xa = float(input('Digite a coordenada xa '))
xb = float(input('Digite a coordenada xb '))
ya = float(input('Digite a coordenada ya '))
yb = float(input('Digite a coordenada yb '))

dist = math.sqrt(((xb-xa)**2) + ((yb-ya)**2))

print('longe' if dist>=10 else 'perto')