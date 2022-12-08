with open('day3.txt', 'r') as f:
    for line in f:
        ident, left, top, width, heigth = None, None, None, None, None
        sez = line.strip().split()
        ident = int(sez[0][1:])

        left_top = sez[2].split(',')
        left = int(left_top[0])
        top = int(left_top[1][:-1])

        width_height = sez[3].split('x')
        width = int(width_height[0])
        heigth = int(width_height[1])

        