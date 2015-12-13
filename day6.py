lines = []
grid = {}
count = 0
with open('data/6') as f:
    lines = f.readlines()
def setup(line):
    global count
    if len(line.split()) == 5:
        _, action, start, _, end = line.split()
    else:
        action, start, _, end = line.split()
    start = map(int, start.split(','))
    end = map(int, end.split(','))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if action == 'on':
                if not grid.setdefault(x, {}).get(y, 0):
                    grid[x][y] = True
                    count += 1
            elif action == 'off':
                if grid.setdefault(x, {}).get(y, 0):
                    grid[x][y] = False
                    count -= 1
            else:
                grid.setdefault(x, {})[y] = not grid.setdefault(x, {}).get(y, 0)
                if grid[x][y]:
                    count += 1
                else:
                    count -= 1
for line in lines:
    setup(line)
print count

# part 2

grid2 = {}
def setup2(line):
    if len(line.split()) == 5:
        _, action, start, _, end = line.split()
    else:
        action, start, _, end = line.split()
    start = map(int, start.split(','))
    end = map(int, end.split(','))
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if action == 'on':
                grid2.setdefault(x, {})[y] = grid2.setdefault(x, {}).get(y, 0) + 1
            elif action == 'off':
                grid2.setdefault(x, {})[y] = grid2.setdefault(x, {}).get(y, 0) - 1
                if grid2[x][y] < 0:
                    grid2[x][y] = 0
            else:
                grid2.setdefault(x, {})[y] = grid2.setdefault(x, {}).get(y, 0) + 2
for line in lines:
    setup2(line)
count = 0
for x in grid2.values():
    for y in x.values():
        count += y
print count


