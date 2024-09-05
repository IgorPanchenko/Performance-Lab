import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("file1")
parser.add_argument("b")

args = parser.parse_args()

def local(n):
    with open(n, 'r') as file:
        o = list(map(int, file.readline().split()))
        r = int(file.readline())
    return o, r


def results(b):
    a = []
    with open(b, 'r') as file:
        for i in file:
            if '\n' in i:
                i = i[:-1]
            a.append(list(map(int, i.split())))
    return a


if __name__ == "__main__":
    points = local(args.file1)
    center = points[0]
    radius = points[1]
    a = results(args.b)
    for i in a:
        result = ((center[0]-i[0])**2 + (center[1]-i[1])**2)**0.5
        if result == radius:
            print(0)
        if result > radius:
            print(2)
        if result < radius:
            print(1)
