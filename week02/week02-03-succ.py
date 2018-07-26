type1or2 = int(input())
a = int(input())

if type1or2 == 1 :
    for j in range(1, (a//2+1)+1 ):
        for i in range(1,j+1):
            print(i,end='')
        print()
    for j in range((a//2), 0, -1):
        for i in range(1,j+1):
            print(i,end='')
        print()

######type2

L = []
if type1or2 == 2 :
    for j in range(1, (a//2+1)+1):
        for i in range(j, 0, -1):
            L.append(i)
        L2 = list(map(str,L))
        L3 = ''.join(L2)
        print('%s%s'%(((a//2+1)-j)*'.',L3))
        
        L = []


    for j in range((a//2), 0, -1):
        for i in range(j, 0, -1):
            L.append(i)
        L2 = list(map(str,L))
        L3 = ''.join(L2)
        print('%s%s'%(((a//2+1)-j)*'.',L3))
        
        L = []