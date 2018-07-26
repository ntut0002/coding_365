#input 購入幾本書 
x = int(input ())
y = int(input ())
z = int(input ())

if x <= 10 :
    Σx = x * 380 * 1
else :
    if 10 < x <= 20 :
        Σx = x * 380 * 0.9
    else :
        if 20 < x <= 30 :
            Σx = x * 380 * 0.85
        else :
            Σx = x * 380 * 0.8

if y <= 10 :
    Σy = y * 1200 * 1
else :
    if 10 < y <= 20 :
        Σy = y * 1200 * 0.95
    else :
        if 20 < y <= 30 :
            Σy = y * 1200 * 0.85
        else :
            Σy = y * 1200 * 0.8

if z <= 10 :
    Σz = z * 180 * 1
else :
    if 10 < z <= 20 :
        Σz = z * 180 * 0.85
    else :
        if 20 < z <= 30 :
            Σz = z * 180 * 0.8
        else :
            Σz = z * 180 * 0.7

Σcost  =  Σx + Σy +  Σz

print (int(Σcost))
#轉整數
#9 / 8.5  / 8 
#9.5 /  8.5 /  8 
#8.5 /  8 /  7 