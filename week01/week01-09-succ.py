#input
A , B , C = map( int , (input ( )).split( ))
if A + B <= C or  B + C <= A or C + A <= B or A <= 0 or B <= 0 or C <= 0 :
    print ('Not Triangle')
else:
    if A **2 + B **2 == C **2   or   B **2 + C **2 == A **2   or   C **2 + A **2 == B **2 :
        print('Right Triangle')
    else:
        if A **2 + B **2 < C **2   or   B **2 + C **2 < A **2   or   C **2 + A **2 < B **2 :
            print('Obtuse Triangle')
        else:
            if A ** 2 + B ** 2 > C ** 2 or B ** 2 + C ** 2 > A ** 2 or C ** 2 + A ** 2 > B ** 2 :
                print('Acute Triangle')
#Right_Triangle 其中有兩個邊的平方和等於第三邊的平方
#Obtuse_Triangle 其中有兩個邊的平方和小於第三邊的平方
#Acute_Triangle 任兩邊的平方和大於第三邊的平方。
#Not_Triangle