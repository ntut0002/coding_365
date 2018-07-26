#input
num01_input = input()
num02_input = input()

#transform_strToint
num01 = int(num01_input)
num02 = int(num02_input)

#math
import math 

sum =  (num01 + num02)
Difference =  (math.fabs(num01 - num02))
Product =  (num01 * num02 )
Quotient =  (num01 / num02)

sum_x_xx =  (math.floor (sum* 100) ) / 100
Difference_x_xx =  (math.floor (Difference* 100) ) / 100
Product_x_xx = (math.floor (Product* 100) ) / 100
Quotient_x_xx = ( math.floor (Quotient* 100) ) / 100

sum_x_xx2 = "%.2f" % sum_x_xx
Difference_x_xx2 = "%.2f" % Difference_x_xx
Product_x_xx2 = "%.2f" % Product_x_xx
Quotient_x_xx2 = "%.2f" % Quotient_x_xx



#transform_intTostr
sum_str = str(sum_x_xx2)
Difference_str = str(Difference_x_xx2)
Product_str = str(Product_x_xx2) 
Quotient_str = str(Quotient_x_xx2)

#print
print("Sum:"+ sum_str)
print("Difference:"+Difference_str)
print("Product:"+Product_str)
print("Quotient:"+Quotient_str)