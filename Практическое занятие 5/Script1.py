def pwdcheck(pwd):
    """Проверка пароля

    Принимает:
        pwd - пароль в виде строки
    Возвращает:
        True - если пароль корректный
        False - в ином случае

    Пароль корректен, если длина > 6, содержит в себе минимум 1 цифру, 
    1 букву и не содержит слово "password" в любом регистре.
    """
    if (len(pwd) >= 6 
      and any(sym.isdigit() for sym in pwd) 
        and any(sym.isalpha() for sym in pwd) 
          and "password" not in pwd.lower()
        ):
        return True
    else:
        return False

passw = str(input('Введите пароль: '))

print(pwdcheck(passw))
