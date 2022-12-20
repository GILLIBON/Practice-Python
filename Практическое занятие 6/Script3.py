msg = 'Привет, я обычное сообщение!'
key  = 12341
if key > 999999:
    print('Ключ не может принимать более чем шестизначное значение. Установлено число 1.')
    key = 1

def xor(msg,key):
    xorstr = ''
    for i in msg:
        xorstr += chr(ord(i) ^ key)
    return xorstr    
 
xorstr = xor(msg,key)
print('Сообщение до шифрования: ',msg)
print('Зашифрованное сообщение: ',xorstr)
print('Расшифрованное сообщение: ',xor(xorstr,key))
