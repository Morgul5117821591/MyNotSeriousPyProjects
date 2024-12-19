def find_duplicates():
    # Вводим список с клавиатуры
    input_list = input("Введите целые числа через пробел: ")
    numbers = list(map(int, input_list.split()))

    # Словарь для хранения индексов элементов
    index_dict = {}

    # Находим дубликаты
    for index, number in enumerate(numbers):
        if number in index_dict:
            index_dict[number].append(index)
        else:
            index_dict[number] = [index]

    # Выводим дубликаты и их индексы
    duplicates_found = False
    for number, indices in index_dict.items():
        if len(indices) > 1:
            print(f"Элемент {number} встречается на индексах: {indices}")
            duplicates_found = True 
    if not duplicates_found:
        print("Дубликатов не найдено.")

# Вызов функции
find_duplicates()
