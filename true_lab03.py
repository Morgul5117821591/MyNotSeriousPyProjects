from math import *
import numpy as np

def cicle_for(x1, xn, delta, a, b):
    y = None
    for x1 in np.arange(x1, xn, delta):
        y = b * log((a * x1**2), exp(1)) + b * pow(log(x1, exp(1)), 2)
    return y

def cicle_while(x1, xn, delta, a, b):
    y = None
    while(x1 < xn-0.3):
        y = b * log((a * x1**2), exp(1)) + b * pow(log(x1, exp(1)), 2)
        x1 += delta
    return y

def main():
    x1 = 1.0
    xn = 4.0
    delta = 0.3
    a = 4.3
    b = 5.4
    print('For: ', cicle_for(x1, xn, delta, a, b))
    print('While: ', cicle_while(x1, xn, delta, a, b))
    

if __name__ == '__main__':
    main()  # Вызов главной функции
