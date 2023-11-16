x=np.array(input("enter x:").split(",")).astype(int)
h=np.array(input("enter h:").split(",")).astype(int)
print(overlap_add(x,h))