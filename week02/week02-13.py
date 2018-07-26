#輸入
one = input()
two = input()

#分解第一個數
oneX = int(one[:one.find('/')])
#print(oneX)
oneY = int(one[one.find('/')+1:])
#print(oneY)

#分解第二個數
twoX = int(two[:one.find('/')])
#print(twoX)
twoY = int(two[one.find('/')+1:])
#print(twoY)

if oneY ==0 or twoY ==0:
    if oneY ==0 :
        print('ERROR')
    if twoY ==0 :
        print('ERROR')
else :
    ## 運算one + two 
    X = ((oneX) * (twoY) + (twoX) * (oneY))
    Y = (oneY) * (twoY)
    # X/Y 
    X = oneX * twoY + twoX * oneY
    Y = oneY * twoY
    # X/Y
    if abs(X) > abs(Y):
        if X*Y > 0:
            Quotient = X//Y 
            Remainder = X % Y
            print('%d%s%d%s%d%s'%(Quotient, '(', Remainder, '/', Y, ')' ))
        else:
            Quotient = X//Y 
            Remainder = X % Y
            print('%d%s%d%s%d%s'%(Quotient, '(', Remainder, '/', Y, ')' ))
    else:
        if X*Y > 0 :
            print('%d%s%d'%(X, '/', Y))
        else:
            print('%d%s%d'%( X, '/', Y))

    ## 運算 one x two
    X = oneX * twoX
    Y = oneY * twoY
    # X/Y
    if abs(X) > abs(Y):
        if X*Y > 0:
            Quotient = X//Y 
            Remainder = X % Y
            print('%d%s%d%s%d%s'%(Quotient, '(', Remainder, '/', Y, ')' ))
        else:
            Quotient = X//Y 
            Remainder = X % Y
            print('%d%s%d%s%d%s' % (Quotient, '(', Remainder, '/', Y, ')' ))
    else:
        if X*Y > 0 :
            print('%d%s%d'%(X, '/', Y))
        else:
            print('%d%s%d'%( X, '/', Y))




##2/6
# -2/-2  