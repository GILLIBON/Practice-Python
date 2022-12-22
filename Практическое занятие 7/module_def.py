def fibon(n):
    """Функция вывода числа Фибоначчи
    
    Принимает:
        n - порядковый номер числа Фибоначчи
    Возвращает:
        fib - число Фибоначчи
    """
    if n == 0 or n == 1:
        fib = n
    else:
        fib = fibon(n - 1) + fibon(n - 2)
    return(fib)

def summ(*param):
    """Функция суммирования

    Принимает: 
        *param - несколько параметров одного типа
    Возвращает: 
        sumparam - сумму этих параметров
    """
    sumparam = 0

    for n in param:
        sumparam = sumparam + n
    return(sumparam)