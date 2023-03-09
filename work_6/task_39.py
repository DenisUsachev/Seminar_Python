
import random
n1 = int(input('Введите количество чисел в первом массиве: '))
n2 = int(input('Введите количество чисел в втором массиве: '))

arr1 = [random.randrange(10) for _ in range(n1)]
arr2 = [random.randrange(10) for _ in range(n2)]
ar = arr1
print(arr1, arr2)
 
# 2 способ
print([i for i in arr1 if not i in arr2])
