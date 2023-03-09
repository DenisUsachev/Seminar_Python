"""В некоторой школе решили набрать три новых
 математических класса и оборудовать кабинеты
для них новыми партами.
За каждой партой может сидеть два учащихся.
Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32"""

first_grade = int(input('Введите кол-во учеников в 1-ом классе: '))
second_grade = int(input('Введите кол-во учеников во втором классе: '))
third_grade = int(input('Введите кол-во учеников в третьем классе: '))
one_desk = 2

# первый способ
import math #  через библиотеку
result = math.ceil(first_grade / one_desk) + math.ceil(second_grade / one_desk) + math.ceil(third_grade / one_desk)
print(result)

# второй способ решения
# int + bool(True, False) или (0, 1)
result1 = first_grade // one_desk + (first_grade % one_desk > 0) 
result2 = second_grade // one_desk + (second_grade % one_desk > 0)
result3 = third_grade // one_desk + (third_grade % one_desk > 0)

result = result1 + result2 + result3

print(result)

# третий способ

result = (first_grade  + 1) // one_desk + (second_grade + 1) // one_desk + (third_grade + 1) // one_desk
print(result)
