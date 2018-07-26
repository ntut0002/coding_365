#保齡球


#a = input()
#a = input()
#a = input()
#a = input()
#a = input()
#a = input()
#a = input()

#if c = 10 or d = 10 : 
    #e = input()

#else:
n1 = int( input() )
n2 = int( input() )
t1 = int( input() )
t2 = int( input() )


if n1 == 10 and t1 == 10 :
    e1 = int( input() )
    Σ = n1 + t1 + e1
elif n1 == 10 and t1 < 10 :
    Σ = n1 + t1 + t2
elif n1 < 10 and t1 < 10 :
        Σ = n1 + n2 + t1 + t2
elif n1 < 10 and t1 == 10 :
            e1 = int( input() )
            Σ = n1 + n2 + t1 + e1

print ( Σ )
