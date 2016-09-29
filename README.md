# 6_password_strength

#Сложность пароля

Скрипт оценивает криптостойкость переданного в него пароля по шкале от 1 до 10 исходя из следующиx параметров:
* длина пароля
* используются как прописные так и строчные символы
* используются цифры
* используются специальные символы, такие как @, #, $
* проверка на вхождение в черный список
* проверка на соответствие формата пароля календарным датам

**Параметры скрипта:**
* **-p ПАРОЛЬ (--password ПАРОЛЬ):** необязательный параметр, оцениваемый пароль.

**Пример использования:**
```
python password_strength.py -p "sd213+O"
```
При вводе пароля в виде параметра ключа **-p** рекомендуется строку пароля заключать в кавычки.
```
python password_strength.py
>>> Enter password (max length 32):
```
В этом случае скрипт, не обнаружив переданного при запуске параметра ключа **-p**, будет ожидать ввода пароля.
