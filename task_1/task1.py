from itertools import cycle

def task_1(numbers: str) -> str:
    """
    Программа, которая выводит путь, по которому, двигаясь интервалом длины
    m по заданному массиву n, концом будет являться первый элемент.
    """
    try:
        numbers = numbers.split(' ')
        n = int(numbers[0])
        m = int(numbers[1])
        if n <= 0 or m <= 0:
            return 'Числа должны быть положительными'
        if n < m:
            return 'Число n должно быть больше или равно числу m'
    except:
        return 'Ошибка ввода'

    n = int(n)
    m = int(m)
    array = [i for i in range(1, n + 1)]
    path = []
    pool = cycle(array)
    index = 1

    for item in pool:
        if index == m and item == array[0]:
            return ''.join(str(i) for i in path)
        elif index == m:
            index = 2
            path.append(item)
        elif index == 1:
            index += 1
            path.append(item)
        else:
            index += 1

print(task_1(numbers=(input('введите числа через пробел: \n'))))

