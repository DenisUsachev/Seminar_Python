"""Задача №35. Решение в группах Напишите функцию, которая принимает одно число и проверяет,
является ли оно простым Напоминание: Простое число - это число,
которое имеет 2 делителя: 1 и n(само число) Input: 5 Output: yes"""

n = int(input('Введите число: '))
res = True

for i in range(2, (n ** 0.5) + 1): #корень числа ** 0.5
    if n % i == 0:
        res = False
print(res)