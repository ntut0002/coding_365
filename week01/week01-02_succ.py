#input
a_str = input()
b_str = input()
c_str = input()

#transform-str_to_int
a = int(a_str)
b = int(b_str)
c = int(c_str)



#math
import math
x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)

#小數點第一位
x1_00 = round(x1,1)
x2_00 = round(x2,1)

x1_00_word = str(x1_00)
x2_00_word = str(x2_00)

print(x1_00)
print(x2_00)
