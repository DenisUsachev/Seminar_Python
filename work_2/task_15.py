"""
15. Иван Васильевич пришел на рынок и решил купить два арбуза: 
один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9"""

quantity = int(input('Введите количесвто арбузов: '))
weight = input('Введите вес каждого арбуза: ').split()
max_weight = int(weight[0])
min_weight = int(weight[0])

for i in range(1, quantity):
    if int(weight[i]) > max_weight:
        max_weight = int(weight[i])
    if int(weight[i]) < min_weight:
        min_weight = int(weight[i])

print(min_weight, max_weight)