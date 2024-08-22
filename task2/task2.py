with open(input('файл с координатами и радиусом окружности\n'), 'r') as file:
    o = list(map(int, file.readline().split()))
    r = int(file.readline())
a = []
with open(input('файл с координатами точек\n'), 'r') as file:
    for i in file:
        if '\n' in i:
            i = i[:-1]
        a.append(list(map(int, i.split())))
for i in a:
    result = ((o[0]-i[0])**2 + (o[1]-i[1])**2)**0.5
    if result == r:
        print(0)
    if result > r:
        print(2)
    if result < r:
        print(1)