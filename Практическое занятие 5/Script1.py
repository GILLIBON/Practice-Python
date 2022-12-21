def pwdcheck(pwd):
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
