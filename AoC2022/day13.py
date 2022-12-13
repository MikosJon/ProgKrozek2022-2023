from functools import cmp_to_key

def compare_int_to_int(x, y):
    if x < y:
        return True
    if y < x:
        return False
    return None

def compare_list_to_int(x, y):
    return compare(x, [y], 0, 0)

def compare_int_to_list(x, y):
    return compare([x], y, 0, 0)

def compare(list1, list2, i, j):
    if i == len(list1):
        if j == len(list2):
            return None
        return True
    if j == len(list2):
        if i == len(list1):
            return None
        return False
    
    left = list1[i]
    right = list2[j]
    result = None
    if type(left) == type(1):
        if type(right) == type(1):
            result = compare_int_to_int(left, right)
        else:
            result = compare_int_to_list(left, right)
    elif type(right) == type(1):
        result = compare_list_to_int(left, right)
    else:
        result = compare(left, right, 0, 0)
    
    if result is not None:
        return result
    return compare(list1, list2, i+1, j+1)

def list_compare(item1, item2):
    result = compare(item1, item2, 0, 0)
    dic = {False: 1, None: 0, True: -1}
    return dic[result]

with open('day13.txt', 'r') as f:
    vsota = 0
    indeks = 1
    li = [[[2]], [[6]]]
    while True:
    # for _ in range(1):
        line = f.readline().strip()
        if len(line) == 0:
            break
        first = eval(line)
        second = eval(f.readline())
        _ = f.readline()
        li.append(first)
        li.append(second)
        if compare(first, second, 0, 0):
            vsota += indeks
        indeks += 1
    li.sort(key=cmp_to_key(list_compare))
    print('Part1:', vsota)
    print('Part2:', (li.index([[2]]) + 1) * (li.index([[6]]) + 1))