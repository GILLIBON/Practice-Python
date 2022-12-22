file = open('Input.txt', 'r')
"""Переменная для работы с файлами"""
finput = file.read()
"""Переменная для чтения содержимого переменной file"""
file.close()

c = int(finput[:finput.find(',')])
"""Переменная количества С в формуле С2Н5(ОН). 
Содержит целое число, полученные из переменной finput от начала строки до первой встреченной запятой
"""
finput = finput[finput.find(',') + 1:]
"""Обрезаем содержимое переменной до первого знака запятой включительно"""
h = int(finput[:finput.find(',')])
"""Переменная количества H в формуле С2Н5(ОН). 
Содержит целое число, полученные из переменной finput от начала строки до первой встреченной запятой 
"""
o = int(finput[:finput.find(','):-1])
"""Переменная количества О в формуле С2Н5(ОН). 
Содержит целое число, полученные из переменной finput от конца строки до первой встреченной запятой 
"""

listout = []
listout.append(c // 2)
listout.append((h-1) // 5)
listout.append(o // 1)

out = str(min(listout))
file = open('Output.txt', 'w')
print = (file.write('Максимальное кол-во молекул спирта: %s' %out))
file.close()
