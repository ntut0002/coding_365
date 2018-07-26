listAns = []
stop = 0

while stop == 0 :
    try:
        a = int(input())
        if a == -1 :
            stop = 1
            for i in listAns:
                print (i)

        elif a < 1 or a > 100:
            listAns.append("Error")
            
        else :
            oldsum = 0
            newsum = 1

            for i in range( 1, a ) :
                b = oldsum + newsum
                oldsum = newsum
                newsum = b
            listAns.append(newsum)
            stop = 0
    except ValueError:
        listAns.append("Error")

#1 2 3 4 5 6 7 8 
#1 1 2 3 5 8 13 21