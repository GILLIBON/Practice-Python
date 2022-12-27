def deco_log(func):
    """Декоратор Логирования
Создает файл "Log.txt" и делает запись при выполнении функции.
    """
    def wrapper(val1, val2):
        file = open('Log.txt', 'w')
        file.write('Функция успешно выполнена')
        file.close
        func(val1, val2)
    return wrapper

def deco_time(func):
    """Декоратор Времени выполнения
Выводит время, которое прошло между началом и окончанием выполнения функции.
    """
    def wrapper(val1, val2):
        import time 
        start = time.time()
        func(val1, val2)
        end = time.time() - start
        print(end)
    return wrapper

def deco_pause(func):
    """Декоратор Паузы
Выводит сообщение, после которого отсчитывает 1 секунду, затем выполняет функцию.
    """
    def wrapper(val1, val2):
        import time 
        print ('Функция выполнится спустя 1 секунду')
        time.sleep(1)
        func(val1, val2)
    return wrapper

@deco_log
def summ_str(str1, str2):
    """ Функция Сумма
Выводит сумму str1 и str2.
    """
    summ = ''
    summ = str1 + str2
    print(summ)

summ_str('1', '4')



