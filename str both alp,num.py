s=input()
b,m=0,0
for j in s:
    if(j.isnumeric()):
        m=m+1
    elif(j.isalpha()):
        b=b+1
    else:
        continue
if(b>0 and m>0):
    print("Yes")
else:
    print("No")
