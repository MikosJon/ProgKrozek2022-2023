# with open('besede.txt', 'r', encoding='utf-8') as f:
#     with open('dolzine_5.txt', 'w', encoding='utf-8') as g:
#         for line in f:
#             line = line.strip()
#             if len(line) == 5 and line.isalpha():
#                 g.write(line + '\n')

import random
secret = ''
sez = []
with open('dolzine_5.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        sez.append(line)
    # 1. nacin
    # indeks = random.randint(0, len(sez)-1)
    # secret = sez[indeks]
    # 2.nacin
    secret = random.choice(sez)

def preberi_besedo():
    while True:
        beseda = input('Vnesi besedo: ').lower()
        if len(beseda) != 5:
            print('Beseda ni pravilne dolzine.')
            continue
        if beseda not in sez:
            print('To ni veljavna beseda.')
            continue
        return beseda

def primerjaj(beseda):
    out = [None] * 5
    for i, crka in enumerate(beseda):
        if crka not in secret:
            out[i] = ('S', crka)
            continue
        if crka == secret[i]:
            out[i] = ('Z', crka)
            continue
        out[i] = ('R', crka)
    return out

GREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'
def generiraj_namig(primerjava):
    namig = ''
    for barva, crka in primerjava:
        if barva == 'S':
            namig += crka
        elif barva == 'Z':
            namig += GREEN + crka + ENDC
        else:
            namig += YELLOW + crka + ENDC
    return namig

namigi = []
for i in range(6):
    beseda = preberi_besedo()
    primerjava = primerjaj(beseda)
    namig = generiraj_namig(primerjava)
    namigi.append(namig)
    for n in namigi:
        print(n)
    print('--------------')
    if primerjava == ['Z'] * 5:
        print('Uganil si besedo', secret)
        break
    elif i == 5:
        print('U suck big pp. Beseda je', secret)