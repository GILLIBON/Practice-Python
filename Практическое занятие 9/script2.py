""" Написать функцию, принимающую строку-пароль. 

Функция должна проверить подходит ли этот пароль условиям и вернуть 
True - если подходит; False - если не подходит. 

Условия:   
- Должен быть не менее 6 символов;
- Должен содержать хотя бы одну цифру;
- Не должен состоять только из цифр;
- Не должен содержать слово “password” в любом регистре.
"""

def pass_check(passwd):
    """ Функция проверки пароля

        Если пароль меньше 6 символов;
          Или не содержит цифр;
            Или не содержит букв;
              Или содержит слово “password” в любом регистре:
        
        Возвращает False

        Иначе:
        Возвращает True
    """
    passwd = str(passwd)
    result = False
    if (len(passwd) >= 6
          and any(sym.isdigit() for sym in passwd)
            and any(sym.isalpha() for sym in passwd)
              and 'password' not in passwd.lower()
        ):
        result = True
    return(result)


