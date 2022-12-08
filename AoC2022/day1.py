with open('day1.txt', 'r') as f:
    skrati = []
    trenutni = 0
    for line in f:
        line = line.strip()
        if line == '':
            skrati.append(trenutni)
            trenutni = 0
        else:
            trenutni += int(line)
    skrati.sort()
    print('Part1:', skrati[-1])
    print('Part2:', sum(skrati[-3:]))