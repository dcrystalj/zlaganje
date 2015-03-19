input()
input()

zlaganje = [map(int, input().split()) for i in range(300)]

for i in zlaganje:
    z = Zlaganje(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])

