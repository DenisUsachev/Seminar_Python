"""
Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
Их интересует, сколько дней длилась самая длинная оттепель.
Оттепелью они называют период,в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

Input: 6 -> -20 30 -40 50 10 -10
Output: 2"""

days = int(input('Введите общее количество рассматриваемых дней: '))
temp1 = -50
temp2 = 50
temp = 0
temp_max = 0

if 1 <= days <= 100:
    for day in range(1, days + 1):
        print('Температура в', day ,'-ый день')
        temperature = int(input('Введите температуру: '))
        if temp1 <= temperature <= temp2:
            if temperature > 0:
                temp += 1
                if temp_max < temp:
                    temp_max = temp
            else: temp = 0
        else: print('Температура за границей диапазона')
else: print('Рассматриваемые дни за границей диапазона')
print(temp_max)