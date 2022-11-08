# 3) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
lst = list(map(int, input("Enter a numbers separated by a space:\n").split()))
print(f"Original list: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"A list of non-repeating elements: {new_lst}")
