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

print(summ(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
