# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

a = int(input("Integer: "))
multipliers = []
b = 2
c = a
while b * b <= a:
        if a % b == 0:
            multipliers.append(b)
            a//=b
        else:
            b += 1
multipliers.append(a)
print('{} = {}' .format(c, multipliers))
