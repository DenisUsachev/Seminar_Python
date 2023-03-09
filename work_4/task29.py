import random
count = int(input('Введите количество чисел массива:'))
#array = [random.randrange(10) for _ in range(count)]
array = [8, 3, 8, 3, 0, 9]
b = array[0]
print(array)

for i in array:
    if i == 0:
        break
    else:
        b = i
print(max(b)) 
