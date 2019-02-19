m=int(input())
if(m>60):
    hour=m//60
    mins=m%60
    print(hour,mins)
else:
    print("0",m)
