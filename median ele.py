
b=[]
m=int(input("enter the limit :"))
for j in range(0,m):
	m=int(input("enter the element:"))
	b.append(m)
print("The list is",b)
b.sort()
print("Sorted elements are :",b)
t=m//2
if (m%2==0):
    print("This list have no middle elements")
else:                                                                                             
    print(" middle elements is ",b[t]) 
