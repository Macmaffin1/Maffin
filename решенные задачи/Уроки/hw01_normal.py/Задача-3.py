__author__ = 'Мельник Виктория'
import math
print('ax**2+b*x+c=0')
a = int(input('Введите a '))
b = int(input('Введите b '))
c = int(input('Введите c '))
d = (b ** 2) - (4 * a * c)
if d > 0:
    x_1 = ((- b) - (d ** 0.5)) / (2 * a)
    x_2 = ((- b) + (d ** 0.5)) / (2 * a)
    print('X_1 =', x_1)
    print('X_2 =', x_2)
elif d == 0:
    x_1 = (- b) / (2 * a)
    print('Уравнение имеет один корень X = ', x_1)
elif d < 0:
    print('Уравнение не имеет корней')
