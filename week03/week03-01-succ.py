A = []
B = []
process = []


stop = 0


while stop == 0:
    inputNum = input()
    option = int(inputNum[0:1])
    

    if option > 0:
        if option == 1: #清空集合A
            A.clear()
            
            strA = ''.join(A) #目前狀態轉換文字
            strB = ''.join(B)

            C = []
            D = []
            C.append(strA)
            D.append(strB)

            E = []
            E.append(C)
            E.append(D)
            process.append(E)


            
        elif option == 2: #清空集合B
            B.clear()
            
            strA = ''.join(A) #目前狀態轉換文字
            strB = ''.join(B)

            C = []
            D = []
            C.append(strA)
            D.append(strB)

            E = []
            E.append(C)
            E.append(D)
            process.append(E)



        elif option == 3: #增加項目至A
            
            A.append(inputNum[2:3])
            A.append(',')
            #A_processSpace.append(strA)#儲存

            strA = ''.join(A) #目前狀態轉換文字
            strB = ''.join(B)

            C = []
            D = []
            C.append(strA)
            D.append(strB)

            E = []
            E.append(C)
            E.append(D)
            process.append(E)



        elif option == 4: #增加項目至B

            B.append(inputNum[2:3])
            B.append(',')
            #strB = ''.join(B)
            #B_processSpace.append(strB)

            strA = ''.join(A) #目前狀態轉換文字
            strB = ''.join(B)

            C = []
            D = []
            C.append(strA)
            D.append(strB)

            E = []
            E.append(C)
            E.append(D)
            process.append(E)

            
            
        elif option == 5: #刪除項目 A
            A.remove(inputNum[2:3])
            A.remove(',')
            
            strA = ''.join(A) #目前狀態轉換文字
            strB = ''.join(B)

            C = []
            D = []
            C.append(strA)
            D.append(strB)

            E = []
            E.append(C)
            E.append(D)
            process.append(E)

            
            
        elif option == 6: #刪除項目 B
            B.remove(inputNum[2:3])
            B.remove(',')
            
            strA = ''.join(A) #目前狀態轉換文字
            strB = ''.join(B)

            C = []
            D = []
            C.append(strA)
            D.append(strB)

            E = []
            E.append(C)
            E.append(D)
            process.append(E)

        elif option == 7: #聯集
            mirrorA = A.copy()
            for i in B:
                if i not in A:
                    mirrorA.append(i)
                    mirrorA.append(',')
            #print('mirrorA:',mirrorA)################################################################
            strUni = ''.join(mirrorA)          
            #if len(strUni) != 0:
                #strUni = strUni + ','

            C = []
            C.append(strUni)
            #E = []
            #E.append(C)
            process.append(C)


            
        elif option == 8: #交集
            Intersection = []
            originalA = []
            originalB = []
            for i in A:
                if i != ',':
                    originalA.append(i)
            for i in B:
                if i!=',':
                    originalB.append(i)
            

            for i in originalB:
                if i in originalA:
                    Intersection.append(i)
            #print('Intersection:',Intersection)#################################
            strIntersection = ','.join(Intersection)
            if len(strIntersection) != 0:
                strIntersection = strIntersection + ','
            
            #print('strIntersection:',strIntersection)###########

            

            C = []
            C.append(strIntersection)
            #E = []
            #E.append(C)
            process.append(C)




        elif option == 9: #是否A為B的子集合 Ture or False
            for i in B:
                if i in A:
                    A.remove(i)
            if A == []:#是子集合
                
                C = []
                C.append('1')
                #E = []
                #E.append(C)
                process.append(C)
 
            else: #不是子集合
                
                C = []
                C.append('0')
                #E = []
                #E.append(C)
                process.append(C)


    elif option == 0:
        stop = 1 #啟動暫停機制

    else:
        print('error! Please retype')


#print(process)###############################
#print()########################

for i in process:
    if len(i) == 2:
        print('%s%s%s' %('A:[', ''.join(i[0]), ']'), end='')
        print('%s%s%s' %('B:[', ''.join(i[1]), ']'))
    if len(i) == 1:
        #print('i[0]:',i[0])###############################
        if i[0] == '0' or i[0] == '1':
            print(''.join(i[0:1]))
        else:
            print('%s%s%s' %('[', ''.join(i[0]), ']'))





############################
#3 4
#3 7
#4 8
#4 9
#5 4
#6 8
#3 8
#7
#8
#9
#0




#測資1

#3 1
#3 2
#3 3
#3 4
#3 5
#4 1
#4 6
#4 8
#4 9
#7
#8
#9
#0

#測資2 

#3 1
#3 2
#3 3
#4 1
#4 2
#4 3
#4 4
#7
#8
#9
#0