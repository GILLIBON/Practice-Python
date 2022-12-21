inventory = {'Двуручный стальной меч': 4, 'Грубый баклер': 3, 
             'Кольцо удачи': 0.2, 'Шлем из кожи вепря': 1.5, 
             'Зелье здоровья': 0.3, 'Картофель': 0.2
             }
bpvol = 10
action = None

while action != ('Стоп'):
  print ('{0} предметов в рюкзаке\nВес: {1}/{2}\n' .format(len(inventory), sum(inventory.values()), bpvol))
  for key, value in inventory.items():
    print('{0}, {1} кг' .format(key, value))

  action = input('\nВы хотите добавить или выбросить предмет? Введите + или -, либо "Стоп", чтобы выйти: ')

  if action == '+':
    item = (str(input('Введите название предмета: ')))
    weight = (float(input('Введите вес предмета: ')))
  
    if weight < 0 or weight == 0:
      print('\nВес предмета не может быть меньше или равен 0!\n')
    elif weight + sum(inventory.values()) > bpvol:
      print ('\nПредмет не влезает в рюкзак! Необходимо выбросить лишнее.\n')
    else:
      inventory[item] = weight
      print ('\nНовый предмет %s добавлен!\n' %item)

  elif action == '-':
    item = (str(input('Введите название предмета: ')))
    isitem = inventory.get(item, None)
    if isitem is None:
      print('\nУ вас нет такого предмета в инвентаре!\n')
    else:
      inventory.pop(item)
      print('\nПредмет %s выброшен!\n' %item)
