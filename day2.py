lines = []
summ = 0


def calc(line):
    l, w, h = map(int, line.strip().split('x'))
    sides = [l*w, l*h, w*h]
    return sum(sides) * 2 + min(sides)
with open('data/2') as f:
    lines = f.readlines()
for line in lines:
    summ += calc(line)
print summ
