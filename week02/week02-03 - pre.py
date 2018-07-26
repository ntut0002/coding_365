#input
triangle_type = int(input())
column = int(input())

#math
if triangle_type ==1 :
    for x in range(1,column+1):
        for y in range(0,x):
            print('*',end='')
        print()
        for y in range()
            print('*',end='')
elif triangle_type == 2 :





def ps(n):
	for i in range(n):
	ps(i)
		print('*',end= '')
	
for i in range(n)
		print()





def ps(n):
	for i in range(n):
		print('*',end= '')
	
for i in range(n)
		print()


#自己做三角形
x = int(input())
for i in range(1,x+1):
    print('*'*i)

#老師作的三角形
def loop(n):
    for i in range(n):
        print('*',end='')
for m in range(4)
    loop(m)
    print()

#模仿老師作的
a = int(input())
for i in range(1,a+1):
    print('*'*i)

#--------試寫等腰三角形---------
#v1-------
a = int(input())
for i in range(a+1,1):
    print('*'*i)
#a = int(input())
for i in range(a,0,-1):
    print('*'*i)

#v2--type1-------------
a = int(input())

for i in range(1,a+1):
    print('*'*i)

for i in range(a-1,0,-1):
    print('*'*i)

#-------type2---------
a = int(input())

for i in range(1,a+1):
    print('%s%s' % ('.'*(a-i), '*'*i))


for i in range(a-1,0,-1):
    print('%s%s'% ('.'*(a-i), '*'*i))

#---v3--------------------------------------
#----type1-----
a = int(input())
#上半部
for i in range(1,(a//2+1)+1):
    print('*'*i)
#下半部
for i in range((a//2+1)-1,0,-1):
    print('*'*i)

#----type2-----
a = int(input())
#上半部
for i in range(1,(a//2+1)+1):
    print('%s%s' % ('.'*((a//2+1)-i), '*'*i))
#下半部
for i in range((a//2+1)-1,0,-1):
    print('%s%s'% ('.'*((a//2+1)-i), '*'*i))
#------------------------





#----type1-----
a = int(input())
#上半部
for i in range(1,(a//2+1)+1):
    print('*'*i)
#下半部
for i in range((a//2+1)-1,0,-1):
    print('*'*i)

#----type2-----
a = int(input())
#上半部
for i in range(1,(a//2+1)+1):
    print('%s%s' % ('.'*((a//2+1)-i), '*'*i))
#下半部
for i in range((a//2+1)-1,0,-1):
    print('%s%s'% ('.'*((a//2+1)-i), '*'*i))
#------------------------


#--V4---------------------
a = int(input())

#(a//2+1)
for j in range(1, (a//2+1)+1 ):
    for i in range(1,j+1):
        print(i,end='')
    print()
for j in range((a//2+1), 0, -1):
    for i in range(1,j+1):
        print(i,end='')
    print()

######type2
L = []
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
#----------------------------------------