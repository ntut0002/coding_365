x = float(input())

if int(x) > 1 and x - int(x) == 0  and 2 <= int(x) <= 1000:#判斷正整數
    k = int(x)

elif int(x) == 0 or x == 1:
    k = 1000

elif int(x) < 0 and x - int(x) == 0: # x = 負數
    k = int(x) * -11 

elif int(x) > 0 and x - int(x) != 0: # 為正小數
    k = int(x) #小數點前面的數

elif int(x) < 0 and  x - int(x) != 0: # x 為負小數
    x = str(x)
    postion = x.find('.')
    k = x[postion+1 :]
    k = int(k)

else:
    print('error')

#找質數
stop = 0
for i in range(k,2,-1):
    for j in range(2,i):
        if i%j == 0 :
            stop = 1
            break
        else:
            stop = 0
            #break
    if stop == 0 :
        print(i)
        break