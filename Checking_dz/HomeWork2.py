# Задача 10
import random # импортировали из внешней библиотеки функцию рандом
coins = [random.randint(0, 1) for _ in range(int(input('Введите кол-во монет: ')))]
 # в переменную 'coins' создаем массив 'Для переменной которая не будет использована в диапазоне' и вводим диапазон в терминале

print(coins) # выводим массив заполненный 0 и 1 из введенного через терминал количества монет
print(min( 
    coins.count(0), # метод count проходит по объекту
    coins.count(1)
)) # функиця 'min' проверяет наименшее значение (0 или 1) и выводит ответ



# Задача 12 правильный вариант!!!!!!
summ = int(input('Введите сумму чисел: '))
multiply = int(input('Введите произведение чисел: '))

for i in range(summ):
    for j in range(multiply):
        if i + j == summ and i * j  == multiply:
            print(i, j)
            break; # сработает, когда мы найдём нужное значение и делает полное прерываение
    else:
        continue # если мы не нашли нужное значение то, он сбрасывает на следующию итерацию for i(+1)
    break # когда нашли нужные значения прерывает итерации(для экономии памяти)
else:
    print('Решения с данными значения не найдено')

#Другой вариант
for x in range(1, 1000):
    if s - x == p // x and p % x == 0:
        print(x, p // x)
        break
else:
    print('решения нет')