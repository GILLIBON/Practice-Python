import random

N = 5
a = []
b = []

for i in range(N):
    a.append(random.randint(1, 5))
    b.append(random.randint(1, 5))
print ('Список 1:',a,'\nСписок 2:',b)

print('Входят в оба списка:',list(set(a) & set(b)))
print('Входят в первый, не входят во второй:',list(set(a) - set(b)))
print('Входят в первый, не входят во второй:',list(set(b) - set(a)))
print('Входят в первый или второй список, но не в оба:',list(set(a) ^ set(b)))