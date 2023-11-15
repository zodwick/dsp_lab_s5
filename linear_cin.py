import numpy as np
x=np.array(input("enter values for x:").split(",")).astype(int)
h=np.array(input("enter values for y:").split(",")).astype(int)
total=len(x)+len(h)-1
y=np.zeros(total)
if len(x)<len(h):
    (x,h)=(h,x)
if len(x)!=len(h):
    z=np.zeros(len(x)-len(h),dtype=int)
    h=np.concatenate((h,z))
for n in range(total):
    sum=0
    for k in range(len(x)):
        i=n-k
        if (i<0) or (i>len(x)-1):
            sum+=0
        else:
            sum+=x[k]*h[i]
    y[i]=sum
print(y)