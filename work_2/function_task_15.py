num = int(input('Введите общее количество арбузов: '))
a = [int(input()) for i in range(num)]
print(f'для тёщи арбуз {min(a)} кг, для себя {max(a)} кг')