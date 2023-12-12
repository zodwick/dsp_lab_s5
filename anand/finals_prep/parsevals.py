import numpy as np

x= np.array(input("x").split(",")  , dtype=int)

X=np.fft.fft(x)
lhs= sum(abs(x*x))

rhs = (1/len(x))*sum(abs(X*X))

print("lhs",lhs)
print("rhs",rhs)