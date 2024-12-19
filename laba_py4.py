def filter_words(input_string):
    # Разбиваем строку на слова
    words = input_string.split()
    # Фильтруем слова, начинающиеся на 'а' или заканчивающиеся на 'я'

    filtered_words = [word for word in words if word.lower().startswith('а') or word.endswith('я')] 
    return filtered_words

# Пример использования функции
input_string = input("Введите строку: ")
result = filter_words(input_string)
print(result)
