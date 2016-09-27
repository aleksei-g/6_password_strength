import re
from datetime import datetime


MAX_LENGTH_PASS = 32
MAX_WEIGHT_LEN = 4
WEIGHT_NUM = 2
WEIGHT_SUMBOL = 2
WEIGHT_CAPITAL = 1
WEIGHT_LOWERCASE = 1
WEIGHT_AS_DATE = -2
WEIGHT_BLACKLIST = -2
BLACKLIST = {'qwerty', 'password', 'password1', '123', 'google'}


def get_password_strength(password):
    password_strength = 0
    # получим вес длинны пароля
    password_strength += MAX_WEIGHT_LEN * (len(password) / MAX_LENGTH_PASS)
    # проверим наличие строчных симоволов
    if bool(re.match('^.*[a-z]+.*$', password)):
        password_strength += WEIGHT_LOWERCASE
    # проверим наличие прописных символов
    if bool(re.match('^.*[A-Z]+.*$', password)):
        password_strength += WEIGHT_CAPITAL
    # проверим наличие цифр
    if bool(re.match('^.*\d+.*$', password)):
        password_strength += WEIGHT_NUM
    # проверим наличие специальных символов
    if bool(re.match('^.*[\W_]+.*$', password)):
        password_strength += WEIGHT_SUMBOL
    # проверим на вхождение пароля в черный список
    if password in BLACKLIST:
        password_strength += WEIGHT_BLACKLIST
    # проверим пароль на соответствие формата даты
    pass_as_date = False
    date_formats = ['%Y-%m-%d', '%Y.%m.%d', '%Y/%m/%d', '%Y%m%d',
                    '%Y-%m', '%Y.%m', '%Y/%m', '%Y%m',
                    '%m-%d', '%m.%d', '%m/%d', '%m%d',
                    '%d-%m-%Y', '%d.%m.%Y', '%d/%m/%Y', '%d%m%Y',
                    '%m-%Y', '%m.%Y', '%m/%Y', '%m%Y',
                    '%d-%m', '%d.%m', '%d/%m''%d%m']
    for date_format in date_formats:
        try:
            if datetime.strptime(password, date_format):
                pass_as_date += True
        except:
            pass
    if pass_as_date:
        password_strength += WEIGHT_AS_DATE

    if password_strength < 1:
        password_strength = 1
    elif password_strength > 10:
        password_strength = 10
    return 'password strength: %s' % password_strength


if __name__ == '__main__':
    while True:
        password = input('Enter password (max length %s): ' % MAX_LENGTH_PASS)
        if 0 < len(password) <= MAX_LENGTH_PASS:
            break
        else:
            print('Password length must be between %s and %s characters!'
                  % (1, MAX_LENGTH_PASS))
    print(get_password_strength(password))
