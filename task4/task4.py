import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("file")
 
args = parser.parse_args()

a = []
with open(args.file, 'r') as file:
    for i in file:
        if '\n' in i:
            i = i[:-1]
        a.append(int(i))

m = sorted(a)[len(a) // 2]
print(sum(abs(v - m) for v in a))