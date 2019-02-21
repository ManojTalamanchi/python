m=int(input(""))
m1 = 1
m2 = 1
count = 0
n=[]
if m == 1:
    n.append(m1)
    print(n)
else:
    while count < m:
        n.append(m1)
        mth = m1 + m2
        m1 = m2
        m2 = mth
        count += 1
print(" ".join(str(x) for x in n))
