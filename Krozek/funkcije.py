# def sestej(a, b, c=0, d=0):
#     return a + b + c + d, 'a='+str(a), 'b='+str(b), 'c='+str(c), 'd='+str(d)

# def primer(*, n1=0, n2=3):
#     return n1 * n2

# def primer2(*args, **kwargs):
#     return(args, kwargs)

# x=5
# y=3
# def zmnozi(x, y):
#     print(x)
#     print(y)
#     return x*y

# li = [10, 20, 30, 40]
# def dodaj_element(sez, el):
#     sez.append(el)
#     print('sez =', sez)
# dodaj_element(li, 1)
# print(li)


# def popravi_funkcijo(f, x):
#     return f(x + 1)

import time
def stopaj(f):
    def stopana(x):
        start = time.time()
        for _ in range(10):
            f(x)
        end = time.time()
        return f(x), (end - start)/10
    return stopana

# def g(x):
#     for _ in range(1000000):
#         x += 1
#     return x

# spremenjena = stopaj(g)
# print(spremenjena(2))

# x = 10
# def povecaj_za_ena(x):
#     x = x + 1
#     return x
# # print(povecaj_za_ena(x))
# # print(x)
# print(popravi_funkcijo(povecaj_za_ena, 10))
# # print(zmnozi(10, 4))
# # print(sestej(a=5, c=4, b=6))
# # print(primer(n1=5, n2=4))
# # print(primer2(8,84,3,34,234,243,234,1, kwarg1=45, kwarg3=2, kwarg2=0))

@stopaj
def vsota_stevk(n):
    vsota = 0
    while n != 0:
        zadnja_stevka = n % 10
        vsota += zadnja_stevka
        n = n // 10
    return vsota

@stopaj
def pocasna_vsota_stevk(n):
    n = str(n)
    vsota = 0
    for c in n:
        vsota += int(c)
    return vsota

n = 879246987375894327985438568743658379587349857349759843775894375987438597438975893427598438954370687986389427594376894759798573894798-843758974285892
print(vsota_stevk(n))
print(pocasna_vsota_stevk(n))

def najvecji_skupni_delitelj(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

def dolzina_zaporedja(n):
    dolzina = 1
    while n != 1:
        dolzina += 1
        n = naslednji_clen(n)
    return dolzina

def najvecji(n):
    maks = n
    while n != 1:
        n = naslednji_clen(n)
        if n > maks:
            maks = n
    return maks

def splosci(sez):
    nov = []
    for podsez in sez:
        if type(podsez) != type([]):
            nov.append(podsez)
        else:
            nov.extend(splosci(podsez))
    return nov
gnezden = [[1, [[2], [3,4]], [[5, [6]], [7]]], [8], 9]
print(splosci(gnezden))
najvecji_cleni = [najvecji(n) for n in range(1, 100)]
# print(najvecji_cleni)

def ali_je_pravilno_gnezden(niz):
    nivo = 0
    for znak in niz:
        if znak == '[':
            nivo += 1
        elif znak == ']':
            nivo -= 1
        if nivo < 0:
            return False
    return nivo == 0

def pravilno_gnezden(niz):
    odprti = []
    oklepaji = '([<{'
    zaklepaji = ')]>}'
    for znak in niz:
        print(odprti, znak)
        if znak in oklepaji:
            odprti.append(znak)
        elif znak in zaklepaji:
            if len(odprti) == 0:
                return False
            if zaklepaji.index(znak) != oklepaji.index(odprti[-1]):
                return False
            odprti.pop()
    return len(odprti) == 0    

print(pravilno_gnezden('{<[<[<[()][]>[]]>([]){}]>'))
# print(ali_je_pravilno_gnezden(str(gnezden) + ']' + str(gnezden)))