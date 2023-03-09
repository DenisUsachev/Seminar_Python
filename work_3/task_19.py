"""
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на 
K элементов вправо, K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3

Output: [4, 5, 1, 2, 3]

Примечание: Пользователь может вводить значения списка или список задан изначально.
"""


import random

num = int(input('Введите количество чисел в массиве: '))
k = int(input('Введите индекс числа: '))
lst = [random.randint(0, 10) for i in range(num)]

if k > len(lst):
    k = k - len(lst)
    b = *lst[-k:],*lst[:-k]
else: 
    b = *lst[k:],*lst[:k]

print(lst)
print(list(b))



import random

N = 10

lst = [random.randrange(10) for _ in range(N)]
print(f'{lst = }')

k = int(input('k = '))
for _ in range(k):
lst.insert(0, lst.pop())

print(f'{lst = }')