Вычислить число c заданной точностью d
Пример:
при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from math import pi
from decimal import Decimal

d =  (input("Введите число для заданной точности числа Пи:\n"))

num = Decimal(pi)
num =num.quantize(Decimal(d))
print(f'число Пи с заданной точностью {d} равно {num}')
