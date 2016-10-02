import re
import argparse
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
MIN_STRENGTH = 1
MAX_STRENGTH = 10


def get_password_strength(password):
    password_strength = 0
    # получим вес длинны пароля
    password_strength += MAX_WEIGHT_LEN * (len(password) / MAX_LENGTH_PASS)
    # проверим наличие строчных симоволов
    if bool(re.search('[a-z]', password)):
        password_strength += WEIGHT_LOWERCASE
    # проверим наличие прописных символов
    if bool(re.search('[A-Z]', password)):
        password_strength += WEIGHT_CAPITAL
    # проверим наличие цифр
    if bool(re.search('\d', password)):
        password_strength += WEIGHT_NUM
    # проверим наличие специальных символов
    if bool(re.search('[\W_]', password)):
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
                    '%d-%m', '%d.%m', '%d/%m', '%d%m']
    for date_format in date_formats:
        try:
            if datetime.strptime(password, date_format):
                pass_as_date += True
        except ValueError:
            pass
    if pass_as_date:
        password_strength += WEIGHT_AS_DATE

    if password_strength < MIN_STRENGTH:
        password_strength = MIN_STRENGTH
    elif password_strength > MAX_STRENGTH:
        password_strength = MAX_STRENGTH
    return password_strength


def check_len_password(password):
    if 0 < len(password) <= MAX_LENGTH_PASS:
        return True
    else:
        return False


def create_parser():
    parser = argparse.ArgumentParser(description='Script to assess \
                                     password strength.')
    parser.add_argument('-p', '--password', metavar='PASSWORD',
                        help='Password to assess strength.')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.password:
        password = namespace.password
    else:
        password = input('Enter password (max length %s): ' % MAX_LENGTH_PASS)
    if check_len_password(password):
        print('password strength: %s' % get_password_strength(password))
    else:
        print('Password length must be between %s and %s characters!'
              % (1, MAX_LENGTH_PASS))
