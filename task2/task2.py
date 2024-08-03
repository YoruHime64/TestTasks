import math

#Чтение данных окружности из файла
with open('input1.txt', 'r') as file:
    cx, cy, r = map(float, file.read().split())

flag = 0

#Чтение данных точек из файла
with open('input2.txt', 'r') as file:
    str = file.readline()
    while str and flag<100:
        px, py = map(float, str.split())
        flag +=1

        #Расстояние от центра окружности до точки
        distance = math.sqrt((px - cx)**2 + (py - cy)**2)

        #Проверка положения точки относительно окружности
        if distance < r:
            print("1")
        elif distance == r:
            print("0")
        else:
            print("2")
        str = file.readline()