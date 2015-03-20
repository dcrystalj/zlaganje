from Zlaganje import * 
from time import time

with open('zlaganje.in.txt', 'r+') as f:
    content = f.readlines()

content = content[2:]


zlaganje = [[j for j in map(int, content[i].split())] for i in range(int(input()),300)]

for i in zlaganje:
    print(i[0])
    t1 = time()
    z = Zlaganje(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
    try:
        z.solve()
    except:
        print(time()-t1)


