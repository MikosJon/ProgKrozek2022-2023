with open('day1.txt', 'r') as f:
    frequency = 0
    spremembe = []
    for line in f:
        sprememba = int(line.strip())
        spremembe.append(sprememba)
        frequency += sprememba
    print('Part1:', frequency)

    frequencies = {0}
    i = 0
    trenutna = 0
    while True:
        trenutna += spremembe[i]
        if trenutna in frequencies:
            print('Part2:', trenutna)
            break
        frequencies.add(trenutna)
        i += 1
        i %= len(spremembe)
