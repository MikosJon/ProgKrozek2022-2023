seznam_stevilk = []
with open('day20.txt') as f:
    for line in f:
        stevilka = int(line.strip())
        seznam_stevilk.append(stevilka)

N = len(seznam_stevilk)
ll = {}
for i, stevilka in enumerate(seznam_stevilk):
    ll[stevilka] = [seznam_stevilk[(i-1)%N], seznam_stevilk[(i+1)%N]]

def premakni_desno(start, n):
    end = start
    for _ in range(n):
       end = ll[end][1]
    return end 

def premakni_levo(start, n):
    end = start
    for _ in range(n):
        end = ll[end][0]
    return end

# a = 0
# out = [a]
# for _ in range(N):
#     a = ll[a][1]
#     out.append(a)
# print(out)
# print(out, f'{start=} {end=} {ll[start]} {ll[end]}')

for idx, stevilka in enumerate(seznam_stevilk):
    if stevilka > 0:
        prev, next = ll[stevilka]
        final = ll[next][1]
        for _ in range(stevilka):
            ll[prev][1] = next
            ll[next][0] = prev

            ll[next][1] = stevilka
            ll[stevilka][0] = next

            ll[stevilka][1] = final
            ll[final][0] = stevilka

            # a = 0
            # out = [a]
            # for _ in range(N):
            #     a = ll[a][1]
            #     out.append(a)
            # print(out)

            prev,next,final = next, final, ll[final][1]

    elif stevilka < 0:
        prev, next = ll[stevilka]
        initial = ll[prev][0]
        for _ in range(abs(stevilka)):
            ll[prev][1] = next
            ll[next][0] = prev

            ll[initial][1] = stevilka
            ll[stevilka][0] = initial

            ll[stevilka][1] = prev
            ll[prev][0] = stevilka

            # a = 0
            # out = [a]
            # for _ in range(N):
            #     a = ll[a][1]
            #     out.append(a)
            # print(out)

            initial,prev,next = ll[initial][0], initial, prev

    print(idx)

# a = 0
# out = [a]
# for _ in range(N):
#     a = ll[a][1]
#     out.append(a)
# print(out)
# print(out, f'{start=} {end=} {ll[start]} {ll[end]}')

# print(ll)

vsota = 0
pos = 0
for _ in range(3):
    pos = premakni_desno(pos, 1000)
    vsota += pos
    print(pos)
print(vsota)