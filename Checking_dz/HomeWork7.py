"""task.34 Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам"""
    

def count_letter(text):
    return len(list(filter(lambda letter: letter in 'аоуыэеёиюя', text.lower())))

count = list(map(count_letter, text))
if len(set(count)) == 1:
    print('Пам-парам-пам')
else:
    print('Парам-пам') 
    
"""task_36. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, 
у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36"""

"""Другой способ"""

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    table = map(lambda i: map(lambda j: operation(i, j), range(1,num_columns +1)), range(1, num_rows + 1))
    for row in table:
        print(*row, sep='\t')

print_operation_table(lambda x, y: x * y)
        
"""Способ преподавателя"""
def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for row in range(1, num_rows + 1): # Создаёт строку от 1 до 6
        print(*map(operation, [row] * num_columns, range(1, num_columns + 1)), sep ='\t')
        # печатать два итеррируемых объекта(оператион - в чём хранится, строка * длинну столбцов) - x ,  range(1, num_columns + 1) - y , знак табуляции - '\t'
print_operation_table(lambda x, y: x * y)