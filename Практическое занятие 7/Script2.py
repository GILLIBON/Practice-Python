import numpy.random as nmr

mass = nmr.randint(1, 10, (3, 3))
print('Массив 3х3 случайных чисел от 1 до 10: \n%s' %mass)

mass_transp = mass.transpose()
print('\nТранспонированный массива: \n%s' %mass_transp)