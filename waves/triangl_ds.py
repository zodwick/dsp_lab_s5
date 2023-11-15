import numpy as np
import matplotlib.pyplot as p
t=np.arange(-10,10,1)
T=int(input("enter the width"))
t_lower = -(T/2)
t_upper = T/2
x=list(np.zeros(len(t),dtype=int))
y=[]
j=0
for i in range(len(t)):
    if (0>=t[i]>t_lower):
        j+=1
        y.append(j)
    elif(t_upper>=t[i]>0):
        j-=1
        y.append(j)
    else:
        y.append(0)
p.stem(t,y)
p.xticks(np.arange(-10,10,1))
p.show()

#missinte 
# a = np.arange(6)
# b = np.arange(4, -1, -1)
# x = np.concatenate([a, b])
# p.stem(x)
# p.xticks(np.arange(11))
# p.show()