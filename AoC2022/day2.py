with open('day2.txt', 'r') as f:
    tocke1 = {
        'A X' : 4,
        'A Y' : 8,
        'A Z' : 3,
        'B X' : 1,
        'B Y' : 5,
        'B Z' : 9,
        'C X' : 7,
        'C Y' : 2,
        'C Z' : 6
    }
    tocke2 = {
        'A X' : 3,
        'A Y' : 4,
        'A Z' : 8,
        'B X' : 1,
        'B Y' : 5,
        'B Z' : 9,
        'C X' : 2,
        'C Y' : 6,
        'C Z' : 7
    }
    vsota1, vsota2 = 0, 0
    for line in f:
        line = line.strip()
        vsota1 += tocke1[line]
        vsota2 += tocke2[line]
    print('Part1', vsota1)
    print('Part2', vsota2)
