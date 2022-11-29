from collections import deque

PREMIKI = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def sosedi(x, y):
    out = []
    for dx, dy in PREMIKI:
        test_x, test_y = x + dx, y + dy
        if 0 <= test_x < 4 and 0 <= test_y < 9:
            out.append((test_x, test_y))
    return out

with open('input.txt', 'r') as f:
    obdelani = set()
    mreza = []
    max_dolzina = 0
    for x, line in enumerate(f):
        line = line.strip()
        mreza.append(line)
    for x, line in enumerate(mreza):
        for y, znak in enumerate(line):
            if (x, y) in obdelani or znak == '.':
                continue
            dolzina = 0
            queue = deque([(x,y)])
            obdelani.add((x,y))
            while queue:
                i, j = queue.popleft()
                dolzina += 1
                for u, v in sosedi(i, j):
                    if (u, v) not in obdelani and mreza[u][v] == '#':
                        queue.append((u, v))
                        obdelani.add((u, v))
            max_dolzina = max(dolzina, max_dolzina)
    print(max_dolzina)