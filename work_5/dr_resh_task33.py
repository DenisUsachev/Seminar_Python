import random

array = [random.randint(1,5) for _ in range(int(input('Чисел в массиве: ')))]
print(array)

max_arr,min_arr = sorted(array)[:: - 1] # сортируем список из двух элементов

print(list(enumerate(array))) # Первый элемент, это индекс, второй элемент из нашего итерируемого элемента

for i,value in enumerate(array): # функция enumerate возвращает кортеж из двух элементов
    if value == max_arr: # i - это индекс того значения, который у нас в переменной value
        array[i] = min_arr
    if value == min_arr:
        array[i] = max_arr
print(*array)