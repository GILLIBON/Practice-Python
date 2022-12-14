msg = 'Привет, я обычное сообщение!'
key  = 12341

if key is not int:
    print('Ключ может принимать только числа. Установлено число 1.\n')
    key = 1

if key > 999999:
    print('Ключ не может принимать более чем шестизначное значение. Установлено число 1.')
    key = 1

def xor(msg, key):
    """Функция XOR-шифрования

    Принимает:
        msg - сообщение в незашифрованном виде
        key - общий ключ

    Возвращает:
        xorstr - сообщение, зашифрованное общим ключом 
    """
    xorstr = ''
    for i in msg:
        xorstr += chr(ord(i) ^ key)
    return xorstr    
 
xorstr = xor(msg, key)
print('Сообщение до шифрования: ', msg)
print('Зашифрованное сообщение: ', xorstr)
print('Расшифрованное сообщение: ', xor(xorstr,key))
