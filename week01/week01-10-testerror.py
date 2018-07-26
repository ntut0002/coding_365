##課堂筆記
#one 
#two
#three

#set 
#list []
###課堂筆記

#week 1-5
#1-8
correct = True
a_ClassNum = int( input() )
a_take = int( input() )
a_when1 = int( input() )
if a_take == 2 :
    a_when2 = int( input() )

b_ClassNum = int( input() )
b_take = int( input() )
b_when1 = int( input() )
if b_take == 2 :
    b_when2 = int( input() )

c_ClassNum = int( input() )
c_take = int( input() )
c_when1 = int( input() )
if c_take == 2 :
    c_when2 = int( input() )

a1 = a_when1
if a_take == 2 :
    a2 = a_when2
b1 = b_when1
if b_take == 2 :
    b2 = b_when2
c1 = c_when1
if c_take == 2 :
    c2 = c_when2
 
##error 
#10 or 19 or 20 or 29 or 30 or 39 or 40 or 49 or 50 or 59     or 60 or 61 or 62 or 63 or 64 or 65 or 66 or 67 or 68 or 69 or 70 or 71 or 72 or 73 or 74 or 75 or 76 or 77 or 78 or 79 or 80 or 81 or 82 or 83 or 84 or 85 or 86 or 87 or 88 or 89 or 90 or 91 or 92 or 93 or 94 or 95 or 96 or 97 or 98 or 99 or 100
#課程編號錯誤
if  len (str(a_ClassNum)) != 4 or len (str(b_ClassNum)) != 4 or len (str(c_ClassNum)) != 4 :
    print('-1')
    #print('ClassNum')
    correct = False
#課程所需時間錯誤
elif a_take < 1 or a_take > 2 or b_take < 1 or b_take > 2 or c_take < 1 or c_take > 2 :
    print('-1')
    #print('take')
    correct = False
#課程時間錯誤
elif a_when1 == 10 or a_when1 == 19 or a_when1 == 20 or a_when1 == 29 or a_when1 == 30 or a_when1 == 39 or a_when1 == 40 or a_when1 == 49 or a_when1 == 50 or a_when1 == 59 or  a_when1 > 58 : 
    print('-1')
    #print('when')
    correct = False
elif a_take == 2 :
    if a_when2 == 10 or a_when2 == 19 or a_when2 == 20 or a_when2 == 29 or a_when2 == 30 or a_when2 == 39 or a_when2 == 40 or a_when2 == 49 or a_when2 == 50 or a_when2 == 59 or a_when2 > 58 : 
        print('-1')
        #print('when')
        correct = False

elif  b_when1 == 10 or  b_when1 == 19 or  b_when1 == 20 or  b_when1 == 29 or  b_when1 == 30 or  b_when1 == 39 or  b_when1 == 40 or  b_when1 == 49 or  b_when1 == 50 or  b_when1 == 59 or b_when1 > 58 : 
    print('-1')
    #print('when')
    correct = False
elif b_take == 2 :
    if b_when2 == 10 or b_when2 == 19 or b_when2 == 20 or b_when2 == 29 or b_when2 == 30 or b_when2 == 39 or b_when2 == 40 or b_when2 == 49 or b_when2 == 50 or b_when2 == 59 or b_when2 > 58 : 
        print('-1')
        #print('when')
        correct = False

elif c_when1 == 10 or c_when1 == 19 or c_when1 == 20 or c_when1 == 29 or c_when1 == 30 or c_when1 == 39 or c_when1 == 40 or c_when1 == 49 or c_when1 == 50 or c_when1 == 59 or c_when1 > 58 : 
    print('-1')
    #print('when')
    correct = False
elif c_take == 2 :
    if c_when2 == 10 or c_when2 == 19 or c_when2 == 20 or c_when2 == 29 or c_when2 == 30 or c_when2 == 39 or c_when2 == 40 or c_when2 == 49 or c_when2 == 50 or c_when2 == 59 or c_when2 > 58 : 
        print('-1')
        correct = False
        #print('when')

###error

# a1 == b1 == c1  or  a1 == b2 == c1  or  a1 == b2 == c2  or  a2 == b2 == c2  or  a2 == b1 == c2  or  a2 == b1 == c1

elif a1 == b1 == c1 :
    print( a_ClassNum , b_ClassNum , c_ClassNum , a1 )
    print('%d,%d,%d,%d' % (a_ClassNum, b_ClassNum, c_ClassNum , a1 ))
    correct = False
if b_take == 2 :
    if a1 == b2 == c1 :
        print( a_ClassNum , b_ClassNum , c_ClassNum , a1 )
        print('%d,%d,%d,%d' % (a_ClassNum, b_ClassNum, c_ClassNum , a1 ))
        correct = False
if b_take == 2 and c_take ==2 :
    if a1 == b2 == c2 :
        #print( a_ClassNum , b_ClassNum , c_ClassNum , a1 )
        print('%d,%d,%d,%d' % (a_ClassNum, b_ClassNum, c_ClassNum , a1 ))
        correct = False
if a_take ==2 and b_take == 2 and c_take ==2 :
    if a2 == b2 == c2 :
        #print( a_ClassNum , b_ClassNum , c_ClassNum , a2 )
        print('%d,%d,%d,%d' % (a_ClassNum, b_ClassNum, c_ClassNum , a2 ))
        correct = False
if a_take ==2 and c_take ==2 :
    if a2 == b1 == c2 :
        #print( a_ClassNum  , b_ClassNum , c_ClassNum , a2 )
        print('%d,%d,%d,%d' % (a_ClassNum, b_ClassNum, c_ClassNum , a2 ))
        correct = False
if a_take ==2  :
    if a2 == b1 == c1 :
        #print( a_ClassNum , b_ClassNum , c_ClassNum , a2 )
        print('%d,%d,%d,%d' % (a_ClassNum, b_ClassNum, c_ClassNum , a2 ))
        correct = False

# a1 == b1 or a1 == b2 or a2 == b2 or a2 ==b1

if a1 == b1 :
    print( a_ClassNum , b_ClassNum ,a1 )
    #print('%d,%d,%d' % (a_ClassNum, b_ClassNum, a1 ))
if b_take == 2 :
    if a1 == b2 :
        #print( a_ClassNum , b_ClassNum ,a1 )
        print('%d,%d,%d' % (a_ClassNum, b_ClassNum, a1 ))
        correct = False
if a_take ==2 :
    if a2 ==b1 :
        #print( a_ClassNum , b_ClassNum , a2 )
        print('%d,%d,%d' % (a_ClassNum, b_ClassNum, a2 ))
        correct = False
if a_take ==2 and b_take == 2 :
    if a2 == b2 :
        #print( a_ClassNum , b_ClassNum , a2 )
        print('%d,%d,%d' % (a_ClassNum, b_ClassNum, a2 ))
        correct = False

#  b1 == c1 or b1 == c2 or b2 ==c1 or b2 == c2
if b1 == c1 :
    #print( b_ClassNum , c_ClassNum ,b1 )
    print('%d,%d,%d' % (b_ClassNum, c_ClassNum, b1 ))
    correct = False
if c_take ==2 :
    if b1 == c2 :
        #print( b_ClassNum , c_ClassNum ,b1 )
        print('%d,%d,%d' % (b_ClassNum, c_ClassNum, b1 ))
        correct = False
if b_take == 2 :
    if b2 ==c1 :
        #print( b_ClassNum , c_ClassNum , b2 )
        print('%d,%d,%d' % (b_ClassNum, c_ClassNum, b2 ))
        correct = False
if b_take == 2 and c_take == 2 :
    if b2 == c2 :
        #print( b_ClassNum , c_ClassNum , b2 )
        print('%d,%d,%d' % (b_ClassNum, c_ClassNum, b2 ))
        correct = False

# c1 == a1 or c1 == a2 or c2 == a2 or c2 == a1


if c1 == a1 :
    #print( a_ClassNum , c_ClassNum , c1 )
    print('%d,%d,%d' % (a_ClassNum, c_ClassNum, c1 ))
    correct = False
if a_take ==2 :
    if c1 == a2 :
        #print( a_ClassNum , c_ClassNum , c1 )
        print('%d,%d,%d' % (a_ClassNum, c_ClassNum, c1 ))
        correct = False
if c_take ==2 :
    if c2 == a1:
        #print( a_ClassNum , c_ClassNum , c2 )
        print('%d,%d,%d' % (a_ClassNum, c_ClassNum, c2 ))
        correct = False
if a_take ==2 and c_take ==2 :
    if c2 == a2 :
        #print( a_ClassNum , c_ClassNum , c2 )
        print('%d,%d,%d' % (a_ClassNum, c_ClassNum, c2 ))
        correct = False


if correct == True :
    print ('correct')