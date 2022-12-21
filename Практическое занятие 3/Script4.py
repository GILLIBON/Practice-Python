# !/usr/bin/python3
import cmath

a = complex(input('Квадратное уравнение имеет следующий вид - ax^2+bx+c=0.\nВведите комплексное число a: '))
b = complex(input('Введите комплексное число b: '))
c = complex(input('Введите комплексное число c: '))

D = b**2 - 4*a*c

x1 = (-b + cmath.sqrt(D)) / (2*a)
x2 = (-b - cmath.sqrt(D)) / (2*a)
print('Число х1 =', x1,', число х2 =', x2)
