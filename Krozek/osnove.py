# print(53 / 4)
# print(53 // 4)
# print(53 % 4)

# x = 10 + 2
# print(x + 5)

# x = int(input('povej mi stevilko: '))
# print('rezultat je: ', x + 10)

# crkovni nizi


y = str(128390)
z = 'rekel je: "doma sem". '
w = 'rekel je: \nNova vrstica'
# print('prvi niz' + 'drugi niz')
niz = 'neko dolgo besedilo je ... kk l'
# print(niz.islower())

boolean = True
drugi = False

# print(bool(12398))

# if x > 10:
#     print('vnesel si stevilo vecje od 10')
# elif x <= 7:
#     print('vnesel si stevilko manjso ali enako 7')
# else:
#     print('vnesena stevilka je med 8 in 10')

# y = int(input('vnsei se eno stevilko: '))
# print(not y < x)

print(13 & 9)
print(13 | 9)
print(13 ^ 9)
print(~13)
print(13 >> 2)

stevilo = 14
ugib = None
stevilo_ugibov = 0
while stevilo != ugib:
    ugib = int(input('ugani mojo stevilko: '))
    stevilo_ugibov += 1 # stevilo_ugibov = stevilo_ugibov + 1
print('uganil si mojo stevilko po', stevilo_ugibov, 'ugibov')

# indeks = 0
# while indeks < 10:
#     print(indeks)
#     indeks += 1

i = 0
while True:
    i += 1
    if i == 4:
        continue
    if i == 9:
        break
    # print(i)

for j in range(10): #range(10) ... [0, 1, 2, 3, ..., 8, 9]
    print(2*j)

# najdi prastevila do 1000
for stevilo in range(2, 1001):
    # preveri vsa manjsa, ce ga delijo
    for manjse in range(2, stevilo):
        if stevilo % manjse == 0:
            break
    else: # no break
        print(stevilo, 'je prastevilo')

i = 1
while i < 5:
    i += 1
    if i == 3:
        break
    else:
        print('koncali smo zanko')    



# seštevanje ... +
# odštevanje ... -
# množenje ... *
# potenciranje ... **
# deljenje ... /
# celoštevilsko deljenje ... //
# ostanek ... %