with open('day2.txt', 'r') as f:
    num_2 = 0
    num_3 = 0
    for line in f:
        counter = dict()
        for char in line.strip():
            counter[char] = counter.get(char, 0) + 1
        if 2 in counter.values():
            num_2 += 1
        if 3 in counter.values():
            num_3 += 1
    print('Part1:', num_2 * num_3)

def blizu(niz1, niz2):
    razlik = 0
    for c1, c2 in zip(niz1, niz2):
        if c1 != c2:
            razlik += 1
            if razlik == 2:
                return False
    return True

def skupni(niz1, niz2):
    out = []
    for c1, c2 in zip(niz1, niz2):
        if c1 != c2:
            continue
        out.append(c1)
    return ''.join(out)

with open('day2.txt', 'r') as f:
    vrstice = f.readlines()
    konec = False
    for i in range(len(vrstice)):
        for j in range(i + 1, len(vrstice)):
            if blizu(vrstice[i], vrstice[j]):
                print('Part2:', skupni(vrstice[i], vrstice[j]))
                konec = True
                break
        if konec:
            break