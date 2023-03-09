import random
n = int(input('Введите количество чисел в массиве: '))
arr = [random.randrange(10) for _ in range(n)]

num = int(input('Введите число: '))
print(arr)
count = 0

for i in range(len(arr)):
    if arr[i] == num and len(arr) > i + 1:
        if arr[i - 1] < arr[i] > arr[i + 1]:
            count += 1    
print(count)