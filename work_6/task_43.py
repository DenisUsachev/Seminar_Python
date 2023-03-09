import random
n = int(input('Введите количество чисел в массиве: '))
arr = [random.randrange(10) for _ in range(n)]

count = 0

for i in range(len(arr)):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            count += 1
print(arr)
print(count)

# 2 способ через сотртировку
count = 0
for k in range(len(arr)):
    count += arr[k + 1:].count(arr[k]) 
print(count)

# 3-ий способ через рекурсию

def func(lst: list)-> int:
    el, *lst = lst #в эл помещается 1 элемент(el = lst[0], lst = [1:])
    if lst:
        return func(lst) + lst.count(el)
    return 0