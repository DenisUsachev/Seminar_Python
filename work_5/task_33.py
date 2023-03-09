import random

array = [random.randint(1,5) for _ in range(int(input('Чисел в массиве: ')))]
print(array)
max_arr,min_arr = min(array),max(array)
for i in array:
    if i == max_arr:
        array[i] = min_arr
    if i == min_arr:
        array[i] = max_arr
print(*array)
