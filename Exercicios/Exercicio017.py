from math import hypot, trunc
cateto1 = float(input('Digite o valor do cateto oposto: '))
cateto2 = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa do triangulo é de {}'.format(trunc(hypot(cateto1, cateto2))))
