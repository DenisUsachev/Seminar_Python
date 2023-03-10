"""16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
   В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""
import random
array = [random.randrange(10) for _ in range(int(input('Введите количество чисел в массиве: ')))]
quantity_num = int(input('Введите число которое будет считать: '))
count = 0
for arr in array:
    if arr == quantity_num:
        count += 1
print(array)
print(count)

"""18.Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

import random

lst = [random.randrange(10) for _ in range(int(input('Введите количество чисел в массиве: ')))]
print(lst)
x = int(input('Введите число: '))

# Способ 1 (рассписанный)
dct = {abs(x - item): item for item in lst}  # Создает ключ в котором указана разница между нашим числом и числом в массиве
"""abs(x - item) - это ключ(произведение введенного - число в массиве), : - двоеточие это разделитель, item - значение."""
print(dct)
print(dct[min(dct)]) # Обращаемся по ключю, а в качестве ключа будем брать [min]мин разницу

# Способ 2 (сразу указывается в принте используя функцию lambda - безимянная функция)

print(min(lst, key=lambda i: abs(i - x)))

# Способ 3 (с объявлением функции)

def dct(i): # Вызываем функции присваиваем ей имя
    return abs(i - x) # Возвращаем значение модуля (i - x) - где "i" это число массива, а "x" - это наше введенное число
print(min(lst, key=dct)) #min -минимальное, (из нашего массива, и ключа вызванной функции)