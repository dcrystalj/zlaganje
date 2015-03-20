from Zlaganje import *

with open('Zlaganje.in.txt', 'r+') as f:
    content = f.readlines()

content = content[2:]


zlaganje = [[j for j in map(int, content[i].split())] for i in range(300)]

for i in zlaganje:
    print(i[0])
    z = Zlaganje(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
    z.solve()


