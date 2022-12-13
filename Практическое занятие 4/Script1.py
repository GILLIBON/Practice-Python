list1 = []
listsize = int(input('Введите количество чисел в списке: '))
print('Введите элементы списка:')

for a in range(listsize):
    list1.append(int(input()))
print('Список, полученный при вводе: %s' %list1)

for a in range(len(list1)):
    a = 0
    while a != len(list1)-1:
        if list1[a] > list1[a+1]:
            list1[a], list1[a+1] = list1[a+1], list1[a]
        a = a+1

print ('Список после сортировки: %s' %list1)