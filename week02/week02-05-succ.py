Positional_notation = int(input())
num = int(input())

if 2<= Positional_notation <=9 and 0<= num <=10000000 :
    a = []
    while num > Positional_notation :
        Remainder = num % Positional_notation
        a.append(Remainder)
        num = num // Positional_notation

    a.append(num)
    a.reverse()
    a = list(map(str,a))
    print(''.join(a))

else:
    print(-1)



#B (2<=B<=9)與十進位數N(0<=N<=10,000,000)