# # # slovarji
# # dic = {0: 1, 1: 10, 2: 30, 10: 1, 'a': True}
# # sez = [1, 10, 30]

# # clovek = {'visina': 181, 'teza': 77, 'starost': 22}
# # clovek_sez = [181, 77, 22]

# # print(clovek['visina'])
# # print(clovek_sez[0])

# # print(clovek)
# # clovek['izobrazba'] = 'magisterij'
# # print(clovek)

# # clovek_dodatno = {'poklic': None, 'starost': 20}
# # clovek.update(clovek_dodatno)

# # for k, v in clovek.items():
# #     print(k, v)

# # x = clovek.get('hrana', None)

# # for i in range(10):
# #     if 'kljuc' in clovek:
# #         clovek['kljuc'].append(i)
# #     else:
# #         clovek['kljuc'] = [i]

# #     clovek.get('kljuc', []).append(i)

# # clovek.pop('kljuc', 0)

# # sez = [['a', 1], ['b', 10], ['ahah', 20], ['n', 0]]
# # print(dict(sez))

# from re import X


# slovar = {(1,2): True, (2,1): False}
# slovar2 = {10: 1}
# print((1,2,3) + (10, 20))

# mnozica = {1,1,1,1,1,1,1,1, 2,10}
# mnozica.add(3)
# mnozica.remove(10)
# mnozica.discard(12390)
# nova = mnozica.intersection_update({2,7})
# print(mnozica)
# print(nova)

# mnoz = frozenset([1,2,3,4,10,None])
# print(mnoz)

# x = list('abacaba')
# y = x
# x = x + list('neki')
# print(x)
# print(y)
import math
n = 625
sez = [n/2]
koraki = 100
eps = 1e-4
for i in range(1, koraki):
    prejsni = sez[i-1]
    naslednji = (prejsni + n/prejsni)/2
    if abs(naslednji - prejsni) < eps:
        break
    sez.append(naslednji)
print('priblizek za koren', n, 'je', sez[-1])
print(math.sqrt(n) - sez[-1])
print(len(sez))

