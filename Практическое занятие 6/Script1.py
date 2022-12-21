def list_to_bytes(list):
    blist = []
    for i in list:
        blist.append(bytes(i, encoding='utf-8'))
    return (blist)

def bytes_to_list(blist):
    list = []
    for i in blist:
        list.append(bytes.decode(i, encoding='utf-8'))
    return (list)

list = ('Привет', 'я', 'пример', 'текста')
blist = (list_to_bytes(list))

print(list_to_bytes(list))
print(bytes_to_list(blist))
