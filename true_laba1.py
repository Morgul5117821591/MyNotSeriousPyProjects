from math import *

def s(x, y, z):
    return fabs(pow(x, (y/z))-cbrt((y/x)))+(y-x)*(cos(y)-pow(z, 2))/(1+pow((y-x), 2))
    
x = float(input('Введите значение х -> '))
y = float(input('Введите значение y -> '))
z = float(input('Введите значение z -> '))
print('Ваши значения: x = ', x)
print('Ваши значения: y = ', y)
print('Ваши значения: z = ', z)
print('S = ', s(x, y, z))
