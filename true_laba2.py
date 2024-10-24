from math import *

def main():
    x = float(input('Введите значение х -> '))
    y = float(input('Введите значение y -> '))
    key = float(input('Тип ф-ции(1 -> sinh(y), 2 -> x^(e^x)), 3 -> sqrt(ln(x)): '))
    fx = None
    s = None
    match key:
        case 1:
            fx = sinh(y)
        case 2:
            fx = pow(x, (pow(exp(1), x)))
        case 3:
            fx = sqrt(log(x, (exp(1))))
        case _:
            print('Неверный выбор, пробуйте снова)')
            return

    if (fabs(x*y) > 10):
        s = log((fabs(fx) + fabs(y)), (exp(1)))
    elif (fabs(x*y) < 10):
        s = exp(fx+y)
    elif (fabs(x*y) == 10):
        s = cbrt((fx - y))
    else:
        s = 'No music'
    print('Результат: ', s)

if __name__ == '__main__':
    main()  # Вызов главной функции
    input('Перейдите в терминал и нажмите Enter для завершения')  # Ожидание нажатия от пользователя
