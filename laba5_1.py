def decrease_even_positions():
    # Вводим список с клавиатуры
    input_list = input("Введите числа через пробел: ")
    numbers = list(map(float, input_list.split()))  # Используем float для работы с числами
    if len(numbers) < 2:
        print("Список должен содержать как минимум два элемента.")
        return

    # Получаем значение элемента второго с конца
    decrease_value = numbers[-2]

    # Уменьшаем элементы на четных позициях
    for i in range(0, len(numbers), 2):  # Четные позиции: 0, 2, 4, ...
        numbers[i] -= decrease_value

    # Выводим преобразованный список
    print("Преобразованный список:", numbers)
# Вызов функции
decrease_even_positions()
