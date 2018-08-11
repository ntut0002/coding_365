num = int(input())

for x in range(1, num+1):
    for y in range(num, x, -1):
        print(' ',end='')
    for y in range(0, 2*x-1, 1):
        print('*',end='')
    print()