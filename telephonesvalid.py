import re

phone = input("Введите номер телефона: ")

# Проверка формата номера телефона
test = re.fullmatch(r'((8|\+7)[\- ]?)?\(?\d{3}\)?[\- ]?\d{3}[\- ]?\d{2}[\- ]?\d{2}', phone)
if not test:
    print('Неправильный номер телефона')
    exit(1)

print(phone, type(phone))

phone_book = [phone]
phone_book += ['8(495)430-23-97', '+7-495-430-23-97', '430-23-97',
               '8-495-430', '+79185238495', '+79896213707']
print('phone_book =', phone_book, type(phone_book))

# Очистка телефонных номеров от лишних символов
phone_book_new = [re.sub(r'[\-\(\) ]', '', s) for s in phone_book]

for i in range(len(phone_book_new)):
    if len(phone_book_new[i]) == 7:
        phone_book_new[i] = '+7495' + phone_book_new[i]
    elif len(phone_book_new[i]) == 10:
        phone_book_new[i] = '+7' + phone_book_new[i]
    elif phone_book_new[i][0] == '8':
        phone_book_new[i] = '+7' + phone_book_new[i][1:]

print('phone_book_new =', phone_book_new, type(phone_book_new))

# Проверка на совпадение номеров
s1 = phone_book_new[0]
for s in phone_book_new[1:]:
    if s1 == s:
        print('YES')
    else:
        print('NO')