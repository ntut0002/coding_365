n = int(input())

for i in range(1, (n//2+1)+1):
    print('%s%s%s'%(int(((n - (i*2-1))/2)) *'.', (i*2-1)*'*', int(((n - (i*2-1))/2)) *'.'))

for i in range(n//2,0,-1):
    print('%s%s%s'%(int(((n - (i*2-1))/2)) *'.', (i*2-1)*'*', int(((n - (i*2-1))/2)) *'.'))