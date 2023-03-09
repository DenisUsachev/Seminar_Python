import random
a = [random.randint(-10, 10) for i in range(int(input()))]  #random.randint-обязательно, (в скобках указывается диапозон)
b = [random.randrange(10) for i in range(int(input()))] # выводит число от 0 до введенного