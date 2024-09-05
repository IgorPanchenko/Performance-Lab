from itertools import cycle
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("n")
parser.add_argument("m")
 
args = parser.parse_args()


def task_1(n, m) -> str:
    """
    Программа принимает два аргумента в качестве командной строки. Выводит путь, по которому, двигаясь интервалом длины
    m по заданному массиву n, концом будет являться первый элемент.
    """
    try:
        n = int(n)
        m = int(m)
        if n <= 0 or m <= 0:
            return 'Числа должны быть положительными'
        if n < m:
            return 'Число n должно быть больше или равно числу m'
    except:
        return 'Убедитесь, что вы вводите числа'

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

if __name__ == "__main__":
    print(task_1(args.n, args.m))

