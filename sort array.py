m=int(input())
sum=0
num=m
while(num>0):
	a=num%8
	sum=sum*18+a
	num=num/8
print(sum)
