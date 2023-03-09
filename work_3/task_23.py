"""Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)"""

array = [0, -1, 5, 2, 3]
conversely_arr = array[4::-1]
num = 0
count = 0

for inequalities in conversely_arr:
    if inequalities % 2 == 0 or inequalities % 4 == 0:
        if count != 0:
            num = 0
        else:
            num = conversely_arr[inequalities]
            print(num)
    else:
        if num > conversely_arr[inequalities]:
            count += 1

        print(count)