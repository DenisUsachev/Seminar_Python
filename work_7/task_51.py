"""Задача №51. Общее обсуждение
Напишите функцию same_by(characteristic, objects), которая 
проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов 
отличается - то False. Для пустого набора объектов, функция 
должна возвращать True. Аргумент characteristic - это 
функция, которая принимает объект и вычисляет его 
характеристику.

Ввод:                       Вывод:
values = [0, 2, 10, 6]      same
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')"""

def same_by(funk, values):
    for i in range(1, len(values)):
        if funk(values[i]) != funk(values[i - 1]):
            return False
    return True

values = [0, 2, 10, 6]

if int(same_by(lambda x: x % 2, values)):
    print('same')
else:
    print('different')
    
"""Другое решение"""
# Возвращает True or False (1 or 0)
def same_by(funk, lst):
    return len(set(map(funk, lst))) == 1 # длинна словаря хотем получить объект,
#который будет равен True or False, если она будут два значение, тогда условие не выполниться!!!