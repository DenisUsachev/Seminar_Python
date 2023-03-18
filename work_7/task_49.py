"""Планеты вращаются вокруг звезд по эллиптическим орбитам. 
Назовем самой далекой планетой ту, орбита которой имеет 
самую большую площадь. Напишите функцию 
find_farthest_orbit(list_of_orbits), которая среди списка орбит 
планет найдет ту, по которой вращается самая далекая 
планета. Круговые орбиты не учитывайте: вы знаете, что у 
вашей звезды таких планет нет, зато искусственные спутники 
были были запущены на круговые орбиты. Результатом 
функции должен быть кортеж, содержащий длины полуосей 
эллипса орбиты самой далекой планеты. Каждая орбита 
представляет из себя кортеж из пары чисел - полуосей ее 
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
где a и b - длины полуосей эллипса. При решении задачи 
используйте списочные выражения. Подсказка: проще всего 
будет найти эллипс в два шага: сначала вычислить самую 
большую площадь эллипса, а затем найти и сам эллипс, 
имеющий такую площадь. Гарантируется, что самая далекая 
планета ровно одна
Вывод:
2.5 10
"""
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(x):
    c = 0
    for i,(a, b) in enumerate(x): # i - index , (два значение) - обязательно в скобках!!!!!
        if a != b and c < a * b: 
            c = a * b
            m = i
    return x[m]      

print(*find_farthest_orbit(orbits))

'''Решение в одну строчку'''

def find_farthest_orbit(list_of_orbits):
    return max(list_of_orbits, key = lambda i: (i[0] != i[1]) * i[0] * i[1])
    
    # Возвращаем максимальный(кортеж, его значение = для i: если (i[0] != i[1]) - вернёт значение True, то есть '1' и умножаем на произведение.
    # Иначе значение False, то есть '0')

print(*find_farthest_orbit(orbits))