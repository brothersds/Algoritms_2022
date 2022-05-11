"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно
в этих позициях первого массива стоят четные числа.
"""
# постановка задачи
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
ls = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ls)

# решение задачи
en_ls = enumerate(ls)
result_list = []
for index, item in en_ls:
    if item % 2 == 0:
        result_list.append(index)
print(f'Четные индексы:\n{result_list}')
