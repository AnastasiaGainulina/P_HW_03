# Дана последовательность чисел. Получить список уникальных элементов заданной 
# последовательности, список повторяемых и убрать дубликаты из заданной 
# последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

print('исходная последовательность:', sequence := [1, 2, 3, 5, 1, 5, 3, 10])
print('уникальные: ', [n for n in set (sequence) if sequence.count(n)==1])
print('повторные: ', [n for n in set(sequence) if sequence.count(n)>1])
print('без дубликатов: ', list(set(sequence)))