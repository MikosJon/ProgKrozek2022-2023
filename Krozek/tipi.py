# stevilo = int('10001010010101011', 2)

# sestnajtiski = 0x12fa3
# osmiski = 0o1547
# dvojiski = 0b100101

# scientific = 1.78e8

# inf = float('inf')
# # print(inf - inf)
# # # print(1.0/0)


# # print(bool(0.1 + 0.2 - 0.3))

# x = 'gimvic'
# # print(x[1:])
# # print(x[:3])
# # print(x[1:6:2])
# # print(x[2:20])

# x = [1, 2, 3]
# print(x.append(4))
# x.insert(60, 100)
# print(x)

# # ali je beseda palindrom (enaka ce beremo nazaj)
# beseda = 'perica    reze      raci rep'
# beseda = beseda.replace(' ', '')
# # i = 0
# # j = len(beseda) - 1
# # while i <= j:
# #     while beseda[i] == ' ':
# #         i += 1
# #     while beseda[j] == ' ':
# #         j -= 1
    
# for i in range(-1, (-len(beseda))//2 - 1, -1):
#     if beseda[i] != beseda[-i-1]:
#         print(beseda, 'ni palindrom')
#         break
#     # i += 1
#     # j -= 1
# else: # no break
#     print(beseda, 'je palindrom')

# import random
# # vsote zaporednih v seznamu
# sez = [random.randint(1,10) for i in range(10)]
# # sez = []
# # for i in range(10):
# #     sez.append(random.randint(1,10))
# nov_sez = []
# prejsni = None
# for stevilo in sez:
#     if prejsni is None:
#         prejsni = stevilo
#     else:
#         nov_sez.append(prejsni + stevilo)
#         prejsni = stevilo

# nov_sez2 = []
# for i in range(len(sez)-1):
#     nov_sez2.append(sez[i] + sez[i+1])

# for i, stevilo in enumerate(sez[:-1]):
#     nov_sez2.append(stevilo + sez[i+1])
# print(sez)
# print(nov_sez)
# print(nov_sez2)

# sez == reversed(sez)
# sez.reverse()

# sorted(sez)
# sez.sort()

# M = int(1e7)
# prastevila = [None] * (M + 2)
# sez = []
# for stevilo in range(2, M+1):
#     if prastevila[stevilo] is None:
#         sez.append(stevilo)
#         if stevilo < M**0.5 + 1:
#             for veckratnik in range(stevilo**2, M+1, stevilo):
#                 prastevila[veckratnik] = stevilo

# N = 12784
# faktorji = []
# temp = N
# while True:
#     if prastevila[N] is not None:
#         faktorji.append(prastevila[N])
#         N //= prastevila[N]
#     else:
#         faktorji.append(N)
#         break
# N = temp
# print(faktorji)
# zmnozek = 1
# for faktor in faktorji:
#     zmnozek *= faktor 
# print(N, zmnozek)
# print('prastevil do', M, 'je', len(sez))
# print(','.join(map(str, sez)))


# y = []
# print(y.remove(2))
# print(y.pop())

sez = set()

def stevila(stevke, max_dolzina):
    if max_dolzina == 1:
        sez.add('8')
        return ['0', '8']
    if max_dolzina == 0:
        return ['']
    zrcaljena = []
    for s in stevke:
        for x in stevila(stevke, max_dolzina-2):
            if s == '6':
                sez.add('6' + x + '9')
                zrcaljena.append('6' + x + '9')
            else:
                if s != '0':
                    sez.add(s + x + s)
                zrcaljena.append(s + x + s)
    return zrcaljena    

stevila(['0', '6', '8'], 4)
stevila(['0', '6', '8'], 5)
print(sez)
