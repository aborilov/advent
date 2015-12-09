lines = []
summ = 0
ribbon = 0


def calc(l, w, h):
    sides = [l*w, l*h, w*h]
    return sum(sides) * 2 + min(sides)


def calc_ribon(l, w, h):
    sides = [l, w, h]
    sides.sort()
    sides.pop()
    return sum(sides)*2 + l*w*h

with open('data/2') as f:
    lines = f.readlines()
for line in lines:
    l, w, h = map(int, line.strip().split('x'))
    summ += calc(l, w, h)
    ribbon += calc_ribon(l, w, h)
print summ
print ribbon
