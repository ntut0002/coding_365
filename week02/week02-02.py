one1 = int(input())
one2 = int(input())
two1 = int(input())
two2 = int(input())
three1 = int(input())
three2 = int(input())
four1 = int(input())
four2 = int(input())
five1 = int(input())
five2 = int(input())
six1 = int(input())
six2 = int(input())
seven1 = int(input())
seven2 = int(input())
eight1 = int(input())
eight2 = int(input())
nine1 = int(input())
nine2 = int(input())
ten1 = int(input())
ten2 = int(input())
eleven = int(input())

#計算第一局
if one1 + one2 < 10 :
    one = one1 + one2
elif one1 + one2 == 10 :
    if one1 == 10 :
        if two1 != 0:
            one1 = one1 + two1 + two2
        if two2 = 0 :
            one1 = one1 + two1 + two2
    else:
        one2 = one2 + two1
        one = one1 + one2

#計算第二局
if two1 + two2 < 10 :
    two = two1 + two2
elif two1 + two2 == 10 :
    if two1 == 10 :
        two1 = two1 + three1 + three2
    else:
        two2 = two2 + three1
    two = two1 + two2

#計算第三局
if three1 + three2 < 10 :
    three = three1 + three2
elif three1 + three2 == 10 :
    if three1 == 10 :
        three1 = three1 + four1 + four2
    else:
        three2 = three2 + four1
    three = three1 + three2

#計算第四局
if four1 + four2 < 10 :
    four = four1 + four2
elif four1 + four2 == 10:
    if four1 == 10 :
        four1 = four1 + five1 + five2
    else :
        four2 = four2 + five1
    four = four1 + four2

#計算第五局
if five1 + five2 < 10 :
    five = five1 + five2
elif five1 + five2 == 10 :
    if five1 == 10 :
        five1 = five1 + six1 + six2
    else :
        five2 = five2 + six1
    five = five1 + five2

#計算第六局
if six1 + six2 < 10 :
    six = six1 + six2
elif six1 + six2 == 10:
    if six1 == 10 :
        six1 = six1 + seven1 + seven2
    else :
        six2 = six2 + seven1
    six = six1 + six2

#計算第七局
if seven1 + seven2 < 10 :
    seven = seven1 + seven2
elif seven1 + seven2 == 10:
    if seven1 == 10 :
        seven1 = seven1 + eight1 + eight2
    else:
        seven2 = seven2 + eight1
    seven = seven1 + seven2

#計算第八局
if eight1 + eight2 < 10 :
    eight = eight1 + eight2
elif eight1 + eight2 == 10:
    if eight1 == 10 :
        eight1 = eight1 + nine1 + nine2
    else :
        eight2 = eight2 + nine1
    eight = eight1 + eight2

#計算第九局
if nine1 + nine2 < 10 :
    nine = nine1 + nine2
elif nine1 + nine2 == 10 :
    if nine1 == 10 :
        nine1 = nine1 + ten1 + ten2
    else :
        nine2 = nine2 + ten1
    nine = nine1 + nine2

#計算第十局
if ten1 + ten2 < 10 :
    ten = ten1 + ten2
elif ten1 ==10 :
    ten1 = ten1 + ten2 +eleven
elif ten1 + ten2 == 10:
    ten2 = ten2 + eleven
ten = ten1 + ten2 +eleven


sum = one + two + three + four + five + six + seven + eight + ten
print(sum)