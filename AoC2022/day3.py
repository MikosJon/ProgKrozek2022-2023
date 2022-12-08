with open('day3.txt', 'r') as f:
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vsota = 0
    for line in f:
        line = line.strip()
        dolzina = len(line)
        prva_polovica = line[:dolzina//2]
        druga_polovica = line[dolzina//2:]
        vsota += 1 + alphabet.index(set(prva_polovica).intersection(druga_polovica).pop())
    print(vsota)

print(sum(1 + 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(set(line[:(len(line)-1)//2]).intersection(line[len(line)//2:]).pop()) for line in open('day3.txt', 'r')))