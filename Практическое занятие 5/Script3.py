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

print(fibon(3))

