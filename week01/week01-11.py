#線段

#條件判斷
#迴圈

#x2 - x1 
#----------------
#   -------

#if y2> x2 
#len + y2 - x2
#------------------
#        ------------------


#if y1 > x2 
#len + y2 - y1 
#   --------------
#                     -----------------


##重點 最右邊得點
#leftPoint =

#--------------------------------------------------------------------------------------
a1 = int( input() )
a2 = int( input() )
b1 = int( input() )
b2 = int( input() )
c1 = int( input() )
c2 = int( input() )


#完全重疊
if  x2 > y1 and x2 > y2 and x1 < y1 :

    print (L)

elif x2 > y1 and x2 < y2 :
     L = abs( x1 - y2 )
    print(L)

elif x2 < y2 and x2 < y1

    L = abs( x1 - x2 ) + abs( y1 - y2 )
    print(L)
    


if  x2 > y1 and x2 > y2 and x1 < y1 and x1 < c1 
__________________________
#重疊
x1 <= y1 and x2 >= y2
    L = abs ( x1 - x2 )
    if 
#部分重疊
x1 <= y1 and x2 < y2
    L = abs ( x1-y2 )

#分離
x1 <= y1 and x2 < y1
    L = abs ( x1 - x2 ) + abs ( y1 - y2 )



