""" Домашнее задание №2.4

Вводится радиус круга. Необходимо вычислить его площадь.
"""
def area_of_circle(radius):
  from math import pi

  if (radius != int(radius)
        and radius != float(radius)
      ):
    return('Радиус должен быть числом.')

  elif (radius < 0
        or radius == 0
      ):
    return('Радиус должен быть больше нуля.')

  else:
    return(radius**2 * pi)


print(area_of_circle(0.1))

