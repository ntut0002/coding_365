x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
z1 = int(input())
z2 = int(input())



if x2 >= y2 :
    if z2 <= x2 :
        L = x2 - x1
    if z2 > x2 :
        L = z2 - x1
    if x2 < z1 :
        L = x2 - x1 + z2 - z1

if x2 < y2 :
    if z2 <= y2 :
        L = y2 - x1
    if z2 > y2 :
        L = z2 - x1
    if z1 > y2 :
        L = y2 - x1 + z2 - z1

if x2 < y1 :
    if z2 <= y2 :
        L = y2 - y1 + x2 - x1
    if z2 > y2 :
        L = z2 - y1 + x2 - x1
    if z1 > y2 :
        L = z2- z1 + y2 - y1 + x2 - x1

print(L)
