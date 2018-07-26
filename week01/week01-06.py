import math 

#input 
a = int(input ())
b = int(input ())
c = int(input ())

T = (b*b-4*a*c)
#math.sqrt(b*b-4*a*c)

if T >= 0 :
    x1 = int(((-b+(math.sqrt(T))) / (2*a))*10) /10
    x2 = int(((-b-(math.sqrt(T))) / (2*a))*10) / 10
    print ("%.1f" % x1)
    print ("%.1f" % x2)

else:
    x1 = int((-b / (2 * a))*10) / 10
    x1i =int((( math.sqrt ( abs (b**2-4 *a *c) )) / (2 * a))*10) / 10
    print ("%.1f + %.1f i" % (x1 , x1i))
    print ("%.1f - %.1f i" % (x1 , x1i))