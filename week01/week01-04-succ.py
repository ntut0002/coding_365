###input
A , B , C = map (int,(input()).split())

###math
#1. 不能成為三角形：任兩邊和不大於第三邊，或任一邊長不大於 0。
if  A + B < C or  B + C < A or C + A < B or A < 0 or B < 0 or C < 0 :
    print ('1')

#2. 正三角形：三個邊相等。
else:
    if A == B == C :
         print ('2')

    else:
        #3. 等腰三角形：任兩邊相等，平方和大於第三邊的平方
        if A == B and A **2 + B **2 > C **2 or B == C and B **2 + C **2 > A **2 or C == A and C **2 + A **2 > B **2 :
            print ('3')        

        else:
            #4. 一般三角形：非正三角形與等腰三角形。
            print('4')