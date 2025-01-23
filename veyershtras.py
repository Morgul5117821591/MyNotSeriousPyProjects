import numpy as np
import matplotlib.pyplot as plt

def weierstrass_function(x, a, b, n_terms):
    """
    x: Значения x, для которых вычисляется функция.
    a: Коэффициент, где 0 < a < 1.
    b: Положительное нечётное целое число, удовлетворяющее ab > 1 + 3 * pi / 2.
    n_terms: Количество слагаемых в ряде.
    """
    result = np.zeros_like(x, dtype=np.float64)
    for n in range(n_terms):
        result += a**n * np.cos(b**n * np.pi * x)
    return result

# Параметры функции
x = np.linspace(-2, 2, 1000)
a = 0.5
b = 5
n_terms = 50

# Вычисление функции
y = weierstrass_function(x, a, b, n_terms)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f"Weierstrass Function (a={a}, b={b}, terms={n_terms})")
plt.title("График функции Вейерштрасса")
plt.xlabel("x")
plt.ylabel("W(x)")
plt.grid(True)
plt.legend()
plt.show()
