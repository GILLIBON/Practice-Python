# !/usr/bin/python3

field = '........\n........\n........'
playerpos = 12
move = None

print('Добро пожаловать! Перед вами ваш персонаж (Х) и игровое поле.\nНе покидайте его, иначе Х погибнет и игра закончится! \n\n........\n...X....\n........')

while move != 'Стоп':
    move = str(input('\nДоступные направления движения: \n1)Вверх \n2)Вниз \n3)Влево \n4)Вправо \n\nВведите цифру или введите "Стоп" чтобы закончить: '))
    if move == '1':
        playerpos = playerpos - 9
    elif move == '2':
        playerpos = playerpos + 9
    elif move == '3':
        playerpos = playerpos - 1
    elif move == '4':
        playerpos = playerpos + 1
    elif move == 'Стоп':
        break
    else:
        print('Вы ввели неверное значение!')

    if (playerpos > 25 
          or playerpos < 0 
            or playerpos == 8 
              or playerpos == 17
        ):
        print('\n........\n...:(...\n........\n\nВЫ ВЫШЛИ ЗА ПРЕДЕЛЫ ИГРОВОГО ПОЛЯ!\nИгра окончена.')
        break
    else: 
        print(field[:playerpos] + 'X' + field[playerpos+1 :])
