#Ввод переменных
print("Введите n: ", end="")
n = int(input())
print("Введите m: ", end="")
m = int(input())

#Инициализация массивов
arr = []
path = []

#Заполнение массива
for i in range(n):
    arr.append(i+1)

#Создание кугового массива
arr*=m+1

#Инициализация дополнительных переменных
b = 0
n = m

#Создание интервалов
for i in range(m+1):
    path.append(arr[b:n])
    b +=m-1
    n +=m-1

print("Полученный путь: ", end="")

#Вывод пути кругового массива
for i in range(len(path)):
    if i!= 0 and path[i] == path[0]:
        break
    print(path[i][0], end="")

