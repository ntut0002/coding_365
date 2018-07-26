import math 
#input
number01 , number02 , number03 , number04 , number05 = map(int,(input()).split())

#math
N  = 5 
#精確到小數點後第二位(註，之後的小數捨去)

#平均數 μ=Σ(Xi)/N
μ = (number01 + number02 + number03 + number04 + number05 ) / N 
#變異數 Σ(Xi-μ)^2/N
V = ( ( number01 - μ )**2 + ( number02 - μ )**2 + ( number03 - μ )**2 + ( number04 - μ )**2 + ( number05 - μ )**2 ) / N 
#標準差(Σ(Xi-μ)^2/N)^(0.5)
σ = V **0.5

#trans
μ_ = math.floor (μ*100) / 100
V_ = math.floor (V*100) / 100  
σ_ = math.floor (σ*100) / 100

#print
print ('%.2f'% μ_)
print ('%.2f'% V_)
print ('%.2f'% σ_)